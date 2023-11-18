# Arguments

<a id="std-kwarg-kwargs"></a>

## Forward compatibility kwargs

`**kwargs` is required in all handlers for the forward compatibility:
the framework can add new keywords in the future, and the existing handlers
should accept them without breaking, even if they do not use them.

It can be named `**_` to prevent the “unused variable” warnings by linters.

<a id="std-kwarg-retry"></a>

<a id="std-kwarg-started"></a>

<a id="std-kwarg-runtime"></a>

## Retrying and timing

Most (but not all) of the handlers – such as resource change detection,
resource daemons and timers, and activity handlers – are capable of retrying
their execution in case of errors (see also: [Error handling](errors.md)).
They provide kwargs regarding the retrying process:

`retry` (`int`) is the sequential number of retry of this handler.
For the first attempt, it is `0`, so it can be used in expressions
like `if not retry: ...`.

`started` ([`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime)) is the start time of the handler,
in case of retries & errors – i.e. of the first attempt.

`runtime` ([`datetime.timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta)) is the duration of the handler run,
in case of retries & errors – i.e. since the first attempt.

<a id="std-kwarg-param"></a>

## Parametrization

`param` (any type, defaults to `None`) is a value passed from the same-named
handler option `param=`. It can be helpful if there are multiple decorators,
possibly with multiple different selectors & filters, for one handler function:

```python
import kopf

@kopf.on.create('KopfExample', param=1000)
@kopf.on.resume('KopfExample', param=100)
@kopf.on.update('KopfExample', param=10, field='spec.field')
@kopf.on.update('KopfExample', param=1, field='spec.items')
def count_updates(param, patch, **_):
    patch.status['counter'] = body.status.get('counter', 0) + param

@kopf.on.update('Child1', param='first', field='status.done', new=True)
@kopf.on.update('Child2', param='second', field='status.done', new=True)
def child_updated(param, patch, **_):
    patch_parent({'status': {param: {'done': True}}})
```

Note that Kopf deduplicates the handlers to execute on one single occasion by
their underlying function and its id, which includes the field name by default.

In this example below with overlapping criteria, if `spec.field` is updated,
the handler will be called twice: one time – for `spec` as a whole,
another time – for `spec.field` in particular;
each time with the proper values of old/new/diff/param kwargs for those fields:

```python
import kopf

@kopf.on.update('KopfExample', param=10, field='spec.field')
@kopf.on.update('KopfExample', param=1, field='spec')
def fn(param, **_):
    pass
```

<a id="std-kwarg-settings"></a>

## Operator configuration

`settings` is passed to activity handlers (but not to resource handlers).

It is an object with a predefined nested structure of containers with values,
which defines the operator’s behaviour. See: [`kopf.OperatorSettings`](packages/kopf.md#kopf.OperatorSettings).

It can be modified if needed (usually in the startup handlers). Every operator
(if there are more than one in the same process) has its config.

See also: [Configuration](configuration.md).

## Resource-related kwargs

<a id="std-kwarg-resource"></a>

<a id="std-kwarg-body"></a>

<a id="std-kwarg-spec"></a>

<a id="std-kwarg-meta"></a>

<a id="std-kwarg-status"></a>

<a id="std-kwarg-uid"></a>

<a id="std-kwarg-name"></a>

<a id="std-kwarg-namespace"></a>

<a id="std-kwarg-labels"></a>

<a id="std-kwarg-annotations"></a>

### Body parts

`resource` ([`kopf.Resource`](packages/kopf.md#kopf.Resource)) is the actual resource being served
as retrieved from the cluster during the initial discovery.
Please note that it is not necessary the same selector as used in the decorator,
as one selector can match multiple actual resources.

`body` is the handled object’s body, a read-only mapping (dict).
It might look like this as an example:

```python
{
    'apiVersion': 'kopf.dev/v1',
    'kind': 'KopfExample',
    'metadata': {
        'name': 'kopf-example-1',
        'namespace': 'default',
        'uid': '1234-5678-...',
    },
    'spec': {
        'field': 'value',
    },
    'status': {
        ...
    },
}
```

`spec`, `meta`, `status` are aliases for relevant stanzas, and are
live-views into `body['spec']`, `body['metadata']`, `body['status']`.

`namespace`, `name`, `uid` can be used to identify the object being
handled, and are aliases for the respective fields in `body['metadata']`.
If the values are not present for any reason (e.g. namespaced for cluster-scoped
objects), the fields are `None` – unlike accessing the same fields by key,
when a `KeyError` is raised.

`labels` and `annotations` are equivalents of `body['metadata']['labels']`
and `body['metadata']['annotations']` if they exist. If not, these two behave
as empty dicts.

<a id="std-kwarg-logger"></a>

### Logging

`logger` is a per-object logger, with the messages prefixed with the object’s
namespace/name.

Some of the log messages are also sent as Kubernetes events according to the
log-level configuration (default is INFO, WARNINGs, ERRORs).

<a id="std-kwarg-patch"></a>

### Patching

`patch` is a mutable mapping (dict) with the object changes to be applied
after the handler. It is actively used internally by the framework itself,
and is shared to the handlers for convenience \_(since patching happens anyway
in the framework, why make separate API calls for patching?)_.

#### NOTE
Currently, it is just a dictionary, and the changes are applied
as `application/merge-patch+json`: `None` values delete the fields,
other values override, dicts are merged.

In the future, at discretion of this framework, it can be converted
to JSON-patch (a list of add/change/remove operation), while keeping
the same Python mutable mapping protocol and remembering the changes
in the order they were made.

<a id="std-kwarg-memo"></a>

### In-memory container

`memo` is an in-memory container for arbitrary runtime-only keys-values.
The values can be accessed as either object attributes or dictionary keys.

For resource handlers, `memo` is shared by all handlers of the same
individual resource (not of the resource kind, but of the resource object).
For operator handlers, `memo` is shared by all handlers of the same operator
and later used to populate the resources’ `memo` containers.

#### SEE ALSO
[In-memory containers](memos.md) and [`kopf.Memo`](packages/kopf.md#kopf.Memo).

<a id="std-kwarg-indices"></a>

<a id="std-kwarg-indexes"></a>

### In-memory indices

Indices are in-memory overviews of matching resources in the cluster.
They are populated according to `@kopf.index` handlers and their filters.

Each index is exposed in kwargs under its name (function name)
or id (if overridden with `id=`). There is no global structure to access
all indices at once. If needed, use `**kwargs` itself.

Indices are available for all operator-level and all resource-level handlers.
For resource handlers, they are guaranteed to be populated before any handlers
are invoked. For operator handlers, there is no such guarantee.

#### SEE ALSO
[In-memory indexing](indexing.md).

## Resource-watching kwargs

For the resource watching handlers, an extra kwarg is provided:

<a id="std-kwarg-event"></a>

### API event

`event` is a raw JSON-decoded message received from Kubernetes API;
it is a dict with `['type']` & `['object']` keys.

## Resource-changing kwargs

Kopf provides functionality for change detection and triggers the handlers
for those changes (not for every event coming from the Kubernetes API).
A few extra kwargs are provided for these handlers, exposing the changes:

<a id="std-kwarg-reason"></a>

### Causation

`reason` is a type of change detection (creation, update, deletion, resuming).
It is generally reflected in the handler decorator used, but can be useful for
the multi-purpose handlers pointing to the same function
(e.g. for `@kopf.on.create` + `@kopf.on.resume` pairs).

<a id="std-kwarg-old"></a>

<a id="std-kwarg-new"></a>

<a id="std-kwarg-diff"></a>

### Diffing

`old` & `new` are the old & new state of the object or a field within
the detected changes. The new state usually corresponds to [`body`](#std-kwarg-body).

For the whole-object handlers, `new` is an equivalent of [`body`](#std-kwarg-body).
For the field handlers, it is the value of that field specifically.

`diff` is a list of changes of the object between old & new states.

The diff highlights which keys were added, changed, or removed
in the dictionary, with old & new values being selectable,
and generally ignores all other fields that were not changed.

Due to specifics of Kubernetes, `None` is interpreted as absence
of the value/field, not as a value of its own kind. In case of diffs,
it means that the value did not exist before, or will not exist after
the changes (for the old & new value positions respectively):

## Resource daemon kwargs

<a id="std-kwarg-stopped"></a>

### Stop-flag

Daemons also have `stopped`. It is a flag object for sync & async daemons
(mostly, sync) to check if they should stop. See also: `DaemonStopped`.

To check, `.is_set()` method can be called, or the object itself can be used
as a boolean expression: e.g. `while not stopped: ...`.

Its `.wait()` method can be used to replace `time.sleep()`
or `asyncio.sleep()` for faster (instant) termination on resource deletion.

See more: [Daemons](daemons.md).

## Resource admission kwargs

<a id="std-kwarg-dryrun"></a>

### Dry run

Admission handlers, both validating and mutating, must skip any side effects
if `dryrun` is `True`. It is `True` when a dry-run API request is made,
e.g. with `kubectl --dry-run=server ...`.

Regardless of `dryrun`, the handlers must not make any side effects
unless they declare themselves as `side_effects=True`.

See more: [Admission control](admission.md).

<a id="std-kwarg-subresource"></a>

### Subresources

`subresource` (`str|None`) is the name of a subresource being checked.
`None` means that the main body of the resource is being checked.
Otherwise, it is usually `"status"` or `"scale"`; other values are possible.
(The value is never `"*"`, as the star mask is used only for handler filters.)

See more: [Admission control](admission.md).

<a id="std-kwarg-warnings"></a>

### Admission warnings

`warnings` (`list[str]`) is a **mutable** list of string used as warnings.
The admission webhook handlers can populate the list with warnings (strings),
and the webhook servers/tunnels return them to Kubernetes, which shows them
to `kubectl`.

See more: [Admission control](admission.md).

<a id="std-kwarg-userinfo"></a>

### User information

`userinfo` (`Mapping[str, Any]`) is an information about a user that
sends the API request to Kubernetes.

It usually contains the keys `'username'`, `'uid'`, `'groups'`,
but this might change in the future. The information is provided exactly
as Kubernetes sends it in the admission request.

See more: [Admission control](admission.md).

<a id="std-kwarg-headers"></a>

<a id="std-kwarg-sslpeer"></a>

### Request credentials

For rudimentary authentication and authorization, Kopf passes the information
from the admission requests to the admission handlers as is,
without additional interpretation of it.

`headers` (`Mapping[str, str]`) contains all HTTPS request headers,
including `Authorization: Basic ...`, `Authorization: Bearer ...`.

`sslpeer` (`Mapping[str, Any]`) contains the SSL peer information
as returned by `ssl.SSLSocket.getpeercert()`. It is `None` if no proper
SSL client certificate was provided (i.e. by apiservers talking to webhooks),
or if the SSL protocol could not verify the provided certificate with its CA.

#### NOTE
This is an identity of the apiservers that send the admission request,
not of the user or an app that sends the API request to Kubernetes.
For the user’s identity, use [`userinfo`](#std-kwarg-userinfo).

See more: [Admission control](admission.md).
