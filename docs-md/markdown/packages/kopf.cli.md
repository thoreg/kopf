# kopf.cli module

### *class* kopf.cli.CLIControls(ready_flag=None, stop_flag=None, vault=None, registry=None, settings=None, loop=None)

Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

KopfRunner controls, which are impossible to pass via CLI.

* **Parameters:**
  * **ready_flag** (*Future* *|* *Event* *|* *Future* *|* [*Event*](https://docs.python.org/3/library/threading.html#threading.Event) *|* *None*) – 
  * **stop_flag** (*Future* *|* *Event* *|* *Future* *|* [*Event*](https://docs.python.org/3/library/threading.html#threading.Event) *|* *None*) – 
  * **vault** (*Vault* *|* *None*) – 
  * **registry** ([*OperatorRegistry*](kopf.md#kopf.OperatorRegistry) *|* *None*) – 
  * **settings** ([*OperatorSettings*](kopf.md#kopf.OperatorSettings) *|* *None*) – 
  * **loop** (*AbstractEventLoop* *|* *None*) – 

#### ready_flag*: [`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[`Future`, `Event`, `Future`, [`Event`](https://docs.python.org/3/library/threading.html#threading.Event), [`None`](https://docs.python.org/3/library/constants.html#None)]* *= None*

#### stop_flag*: [`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[`Future`, `Event`, `Future`, [`Event`](https://docs.python.org/3/library/threading.html#threading.Event), [`None`](https://docs.python.org/3/library/constants.html#None)]* *= None*

#### vault*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[`Vault`]* *= None*

#### registry*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`OperatorRegistry`](kopf.md#kopf.OperatorRegistry)]* *= None*

#### settings*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`OperatorSettings`](kopf.md#kopf.OperatorSettings)]* *= None*

#### loop*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[`AbstractEventLoop`]* *= None*

### *class* kopf.cli.LogFormatParamType

Bases: `Choice`

#### convert(value, param, ctx)

Convert the value to the correct type. This is not called if
the value is `None` (the missing value).

This must accept string values from the command line, as well as
values that are already the correct type. It may also convert
other compatible types.

The `param` and `ctx` arguments may be `None` in certain
situations, such as when converting prompt input.

If the value cannot be converted, call `fail()` with a
descriptive message.

* **Parameters:**
  * **value** ([`Any`](https://docs.python.org/3/library/typing.html#typing.Any)) – The value to convert.
  * **param** ([`Any`](https://docs.python.org/3/library/typing.html#typing.Any)) – The parameter that is using this type to convert
    its value. May be `None`.
  * **ctx** ([`Any`](https://docs.python.org/3/library/typing.html#typing.Any)) – The current context that arrived at this value. May
    be `None`.
* **Return type:**
  [`LogFormat`](kopf.md#kopf.LogFormat)

### kopf.cli.logging_options(fn)

A decorator to configure logging in all commands the same way.

* **Return type:**
  [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)]
* **Parameters:**
  **fn** ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*]*) –
