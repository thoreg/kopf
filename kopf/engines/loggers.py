"""
A connection between object logger and background k8s-event poster.

Everything logged to the object logger (except for debug information)
is also posted as the k8s-event -- in the background: `kopf.engines.posting`.

This eliminates the need to log & post the same messages, which complicates
the operators' code, and can lead to information loss or mismatch
(e.g. when logging call is added, but posting is forgotten).
"""
import asyncio
import copy
import logging
from typing import Any, MutableMapping, Optional, Tuple

from kopf.engines import posting
from kopf.structs import bodies, configuration


class ObjectPrefixingFormatter(logging.Formatter):
    """ An utility to prefix the per-object log messages. """

    def format(self, record: logging.LogRecord) -> str:
        if hasattr(record, 'k8s_ref'):
            ref = getattr(record, 'k8s_ref')
            namespace = ref.get('namespace', '')
            name = ref.get('name', '')
            prefix = f"[{namespace}/{name}]" if namespace else f"[{name}]"
            record = copy.copy(record)  # shallow
            record.msg = f"{prefix} {record.msg}"
        return super().format(record)


class K8sPoster(logging.Handler):
    """
    A handler to post all log messages as K8s events.
    """

    def createLock(self) -> None:
        # Save some time on unneeded locks. Events are posted in the background.
        # We only put events to the queue, which is already lock-protected.
        self.lock = None

    def filter(self, record: logging.LogRecord) -> bool:
        # Only those which have a k8s object referred (see: `ObjectLogger`).
        # Otherwise, we have nothing to post, and nothing to do.
        settings: Optional[configuration.OperatorSettings]
        settings = getattr(record, 'settings', None)
        level_ok = settings is not None and record.levelno >= settings.posting.level
        enabled = settings is not None and settings.posting.enabled
        has_ref = hasattr(record, 'k8s_ref')
        skipped = hasattr(record, 'k8s_skip') and getattr(record, 'k8s_skip')
        return enabled and level_ok and has_ref and not skipped and super().filter(record)

    def emit(self, record: logging.LogRecord) -> None:
        # Same try-except as in e.g. `logging.StreamHandler`.
        try:
            ref = getattr(record, 'k8s_ref')
            type = (
                "Debug" if record.levelno <= logging.DEBUG else
                "Normal" if record.levelno <= logging.INFO else
                "Warning" if record.levelno <= logging.WARNING else
                "Error" if record.levelno <= logging.ERROR else
                "Fatal" if record.levelno <= logging.FATAL else
                logging.getLevelName(record.levelno).capitalize())
            reason = 'Logging'
            message = self.format(record)
            posting.enqueue(
                ref=ref,
                type=type,
                reason=reason,
                message=message)
        except Exception:
            self.handleError(record)


class ObjectLogger(logging.LoggerAdapter):
    """
    A logger/adapter to carry the object identifiers for formatting.

    The identifiers are then used both for formatting the per-object messages
    in `ObjectPrefixingFormatter`, and when posting the per-object k8s-events.

    Constructed in event handling of each individual object.

    The internal structure is made the same as an object reference in K8s API,
    but can change over time to anything needed for our internal purposes.
    However, as little information should be carried as possible,
    and the information should be protected against the object modification
    (e.g. in case of background posting via the queue; see `K8sPoster`).
    """

    def __init__(self, *, body: bodies.Body, settings: configuration.OperatorSettings) -> None:
        super().__init__(logger, dict(
            settings=settings,
            k8s_skip=False,
            k8s_ref=dict(
                apiVersion=body.get('apiVersion'),
                kind=body.get('kind'),
                name=body.get('metadata', {}).get('name'),
                uid=body.get('metadata', {}).get('uid'),
                namespace=body.get('metadata', {}).get('namespace'),
            ),
        ))

    def process(
            self,
            msg: str,
            kwargs: MutableMapping[str, Any],
    ) -> Tuple[str, MutableMapping[str, Any]]:
        # Native logging overwrites the message's extra with the adapter's extra.
        # We merge them, so that both message's & adapter's extras are available.
        kwargs["extra"] = dict(self.extra, **kwargs.get('extra', {}))
        return msg, kwargs


class LocalObjectLogger(ObjectLogger):
    """
    Same as `ObjectLogger`, but does not post the messages as k8s-events.

    Used in the resource-watching handlers to log the handler's invocation
    successes/failures without overloading K8s with excessively many k8s-events.

    This class is used internally only and is not exposed publicly in any way.
    """

    def log(self, *args: Any, **kwargs: Any) -> None:
        kwargs['extra'] = dict(kwargs.pop('extra', {}), k8s_skip=True)
        return super().log(*args, **kwargs)


logger = logging.getLogger('kopf.objects')
logger.addHandler(K8sPoster())

format = '[%(asctime)s] %(name)-20.20s [%(levelname)-8.8s] %(message)s'


def configure(
        debug: Optional[bool] = None,
        verbose: Optional[bool] = None,
        quiet: Optional[bool] = None,
) -> None:
    log_level = 'DEBUG' if debug or verbose else 'WARNING' if quiet else 'INFO'

    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = ObjectPrefixingFormatter(format)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(log_level)

    # Prevent the low-level logging unless in the debug mode. Keep only the operator's messages.
    # For no-propagation loggers, add a dummy null handler to prevent printing the messages.
    for name in ['asyncio']:
        logger = logging.getLogger(name)
        logger.propagate = bool(debug)
        if not debug:
            logger.handlers[:] = [logging.NullHandler()]

    loop = asyncio.get_event_loop()
    loop.set_debug(bool(debug))
