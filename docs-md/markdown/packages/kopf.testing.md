# kopf.testing module

Helper tools to test the Kopf-based operators.

This module is a part of the framework’s public interface.

### *class* kopf.testing.KopfRunner(\*args, reraise=True, timeout=None, registry=None, settings=None, \*\*kwargs)

Bases: `_AbstractKopfRunner`

A context manager to run a Kopf-based operator in parallel with the tests.

Usage:

```default
from kopf.testing import KopfRunner

with KopfRunner(['run', '-A', '--verbose', 'examples/01-minimal/example.py']) as runner:
    # do something while the operator is running.
    time.sleep(3)

assert runner.exit_code == 0
assert runner.exception is None
assert 'And here we are!' in runner.stdout
```

All the args & kwargs are passed directly to Click’s invocation method.
See: `click.testing.CliRunner`.
All properties proxy directly to Click’s `click.testing.Result` object
when it is available (i.e. after the context manager exits).

CLI commands have to be invoked in parallel threads, never in processes:

First, with multiprocessing, they are unable to pickle and pass
exceptions (specifically, their traceback objects)
from a child thread (Kopf’s CLI) to the parent thread (pytest).

Second, mocking works within one process (all threads),
but not across processes — the mock’s calls (counts, arrgs) are lost.

* **Parameters:**
  * **args** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any)) – 
  * **reraise** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **timeout** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **registry** ([*OperatorRegistry*](kopf.md#kopf.OperatorRegistry) *|* *None*) – 
  * **settings** ([*OperatorSettings*](kopf.md#kopf.OperatorSettings) *|* *None*) – 
  * **kwargs** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any)) – 

#### *property* future*: Future*

#### *property* output*: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### *property* stdout*: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### *property* stdout_bytes*: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes)*

#### *property* stderr*: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### *property* stderr_bytes*: [bytes](https://docs.python.org/3/library/stdtypes.html#bytes)*

#### *property* exit_code*: [int](https://docs.python.org/3/library/functions.html#int)*

#### *property* exception*: [BaseException](https://docs.python.org/3/library/exceptions.html#BaseException)*

#### *property* exc_info*: [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple)[[Type](https://docs.python.org/3/library/typing.html#typing.Type)[[BaseException](https://docs.python.org/3/library/exceptions.html#BaseException)], [BaseException](https://docs.python.org/3/library/exceptions.html#BaseException), [TracebackType](https://docs.python.org/3/library/types.html#types.TracebackType)]*
