# kopf.on module

The decorators for the event handlers. Usually used as:

```default
import kopf

@kopf.on.create('kopfexamples')
def creation_handler(**kwargs):
    pass
```

This module is a part of the framework’s public interface.

### kopf.on.startup(\*, id=None, param=None, errors=None, timeout=None, retries=None, backoff=None, registry=None)

* **Return type:**
  [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[[`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis), [`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`object`](https://docs.python.org/3/library/functions.html#object), [`None`](https://docs.python.org/3/library/constants.html#None), [`Coroutine`](https://docs.python.org/3/library/typing.html#typing.Coroutine)[[`None`](https://docs.python.org/3/library/constants.html#None), [`None`](https://docs.python.org/3/library/constants.html#None), [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`object`](https://docs.python.org/3/library/functions.html#object)]]]]], [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis), [`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`object`](https://docs.python.org/3/library/functions.html#object), [`None`](https://docs.python.org/3/library/constants.html#None), [`Coroutine`](https://docs.python.org/3/library/typing.html#typing.Coroutine)[[`None`](https://docs.python.org/3/library/constants.html#None), [`None`](https://docs.python.org/3/library/constants.html#None), [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`object`](https://docs.python.org/3/library/functions.html#object)]]]]]
* **Parameters:**
  * **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **param** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any) *|* *None*) – 
  * **errors** ([*ErrorsMode*](kopf.md#kopf.ErrorsMode) *|* *None*) – 
  * **timeout** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **retries** ([*int*](https://docs.python.org/3/library/functions.html#int) *|* *None*) – 
  * **backoff** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **registry** ([*OperatorRegistry*](kopf.md#kopf.OperatorRegistry) *|* *None*) – 

### kopf.on.cleanup(\*, id=None, param=None, errors=None, timeout=None, retries=None, backoff=None, registry=None)

* **Return type:**
  [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[[`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis), [`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`object`](https://docs.python.org/3/library/functions.html#object), [`None`](https://docs.python.org/3/library/constants.html#None), [`Coroutine`](https://docs.python.org/3/library/typing.html#typing.Coroutine)[[`None`](https://docs.python.org/3/library/constants.html#None), [`None`](https://docs.python.org/3/library/constants.html#None), [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`object`](https://docs.python.org/3/library/functions.html#object)]]]]], [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis), [`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`object`](https://docs.python.org/3/library/functions.html#object), [`None`](https://docs.python.org/3/library/constants.html#None), [`Coroutine`](https://docs.python.org/3/library/typing.html#typing.Coroutine)[[`None`](https://docs.python.org/3/library/constants.html#None), [`None`](https://docs.python.org/3/library/constants.html#None), [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`object`](https://docs.python.org/3/library/functions.html#object)]]]]]
* **Parameters:**
  * **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **param** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any) *|* *None*) – 
  * **errors** ([*ErrorsMode*](kopf.md#kopf.ErrorsMode) *|* *None*) – 
  * **timeout** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **retries** ([*int*](https://docs.python.org/3/library/functions.html#int) *|* *None*) – 
  * **backoff** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **registry** ([*OperatorRegistry*](kopf.md#kopf.OperatorRegistry) *|* *None*) – 

### kopf.on.login(\*, id=None, param=None, errors=None, timeout=None, retries=None, backoff=None, registry=None)

`@kopf.on.login()` handler for custom (re-)authentication.

* **Return type:**
  [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[[`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis), [`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`object`](https://docs.python.org/3/library/functions.html#object), [`None`](https://docs.python.org/3/library/constants.html#None), [`Coroutine`](https://docs.python.org/3/library/typing.html#typing.Coroutine)[[`None`](https://docs.python.org/3/library/constants.html#None), [`None`](https://docs.python.org/3/library/constants.html#None), [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`object`](https://docs.python.org/3/library/functions.html#object)]]]]], [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis), [`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`object`](https://docs.python.org/3/library/functions.html#object), [`None`](https://docs.python.org/3/library/constants.html#None), [`Coroutine`](https://docs.python.org/3/library/typing.html#typing.Coroutine)[[`None`](https://docs.python.org/3/library/constants.html#None), [`None`](https://docs.python.org/3/library/constants.html#None), [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`object`](https://docs.python.org/3/library/functions.html#object)]]]]]
* **Parameters:**
  * **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **param** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any) *|* *None*) – 
  * **errors** ([*ErrorsMode*](kopf.md#kopf.ErrorsMode) *|* *None*) – 
  * **timeout** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **retries** ([*int*](https://docs.python.org/3/library/functions.html#int) *|* *None*) – 
  * **backoff** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **registry** ([*OperatorRegistry*](kopf.md#kopf.OperatorRegistry) *|* *None*) – 

### kopf.on.probe(\*, id=None, param=None, errors=None, timeout=None, retries=None, backoff=None, registry=None)

`@kopf.on.probe()` handler for arbitrary liveness metrics.

* **Return type:**
  [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[[`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis), [`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`object`](https://docs.python.org/3/library/functions.html#object), [`None`](https://docs.python.org/3/library/constants.html#None), [`Coroutine`](https://docs.python.org/3/library/typing.html#typing.Coroutine)[[`None`](https://docs.python.org/3/library/constants.html#None), [`None`](https://docs.python.org/3/library/constants.html#None), [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`object`](https://docs.python.org/3/library/functions.html#object)]]]]], [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis), [`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`object`](https://docs.python.org/3/library/functions.html#object), [`None`](https://docs.python.org/3/library/constants.html#None), [`Coroutine`](https://docs.python.org/3/library/typing.html#typing.Coroutine)[[`None`](https://docs.python.org/3/library/constants.html#None), [`None`](https://docs.python.org/3/library/constants.html#None), [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`object`](https://docs.python.org/3/library/functions.html#object)]]]]]
* **Parameters:**
  * **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **param** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any) *|* *None*) – 
  * **errors** ([*ErrorsMode*](kopf.md#kopf.ErrorsMode) *|* *None*) – 
  * **timeout** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **retries** ([*int*](https://docs.python.org/3/library/functions.html#int) *|* *None*) – 
  * **backoff** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **registry** ([*OperatorRegistry*](kopf.md#kopf.OperatorRegistry) *|* *None*) – 

### kopf.on.validate(\_\_group_or_groupversion_or_name=None, \_\_version_or_name=None, \_\_name=None, \*, group=None, version=None, kind=None, plural=None, singular=None, shortcut=None, category=None, id=None, param=None, operation=None, operations=None, subresource=None, persistent=None, side_effects=None, ignore_failures=None, labels=None, annotations=None, when=None, field=None, value=None, registry=None)

`@kopf.on.validate()` handler for validating admission webhooks.

* **Return type:**
  [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[[`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis), [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Coroutine`](https://docs.python.org/3/library/typing.html#typing.Coroutine)[[`None`](https://docs.python.org/3/library/constants.html#None), [`None`](https://docs.python.org/3/library/constants.html#None), [`None`](https://docs.python.org/3/library/constants.html#None)]]]], [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis), [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Coroutine`](https://docs.python.org/3/library/typing.html#typing.Coroutine)[[`None`](https://docs.python.org/3/library/constants.html#None), [`None`](https://docs.python.org/3/library/constants.html#None), [`None`](https://docs.python.org/3/library/constants.html#None)]]]]
* **Parameters:**
  * **\_\_group_or_groupversion_or_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *Marker* *|* *None*) – 
  * **\_\_version_or_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *Marker* *|* *None*) – 
  * **\_\_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *Marker* *|* *None*) – 
  * **group** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **version** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **kind** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **plural** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **singular** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **shortcut** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **category** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **param** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any) *|* *None*) – 
  * **operation** ([*Literal*](https://docs.python.org/3/library/typing.html#typing.Literal)*[**'CREATE'**,* *'UPDATE'**,* *'DELETE'**,* *'CONNECT'**]* *|* *None*) – 
  * **operations** ([*Collection*](https://docs.python.org/3/library/typing.html#typing.Collection)*[*[*Literal*](https://docs.python.org/3/library/typing.html#typing.Literal)*[**'CREATE'**,* *'UPDATE'**,* *'DELETE'**,* *'CONNECT'**]**]* *|* *None*) – 
  * **subresource** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **persistent** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **side_effects** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **ignore_failures** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **labels** ([*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]**]* *|* *None*) – 
  * **annotations** ([*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]**]* *|* *None*) – 
  * **when** ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]* *|* *None*) – 
  * **field** (*None* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* *...**]* *|* [*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) – 
  * **value** (*None* *|* [*Any*](https://docs.python.org/3/library/typing.html#typing.Any) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]*) – 
  * **registry** ([*OperatorRegistry*](kopf.md#kopf.OperatorRegistry) *|* *None*) – 

### kopf.on.mutate(\_\_group_or_groupversion_or_name=None, \_\_version_or_name=None, \_\_name=None, \*, group=None, version=None, kind=None, plural=None, singular=None, shortcut=None, category=None, id=None, param=None, operation=None, operations=None, subresource=None, persistent=None, side_effects=None, ignore_failures=None, labels=None, annotations=None, when=None, field=None, value=None, registry=None)

`@kopf.on.mutate()` handler for mutating admission webhooks.

* **Return type:**
  [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[[`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis), [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Coroutine`](https://docs.python.org/3/library/typing.html#typing.Coroutine)[[`None`](https://docs.python.org/3/library/constants.html#None), [`None`](https://docs.python.org/3/library/constants.html#None), [`None`](https://docs.python.org/3/library/constants.html#None)]]]], [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis), [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Coroutine`](https://docs.python.org/3/library/typing.html#typing.Coroutine)[[`None`](https://docs.python.org/3/library/constants.html#None), [`None`](https://docs.python.org/3/library/constants.html#None), [`None`](https://docs.python.org/3/library/constants.html#None)]]]]
* **Parameters:**
  * **\_\_group_or_groupversion_or_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *Marker* *|* *None*) – 
  * **\_\_version_or_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *Marker* *|* *None*) – 
  * **\_\_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *Marker* *|* *None*) – 
  * **group** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **version** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **kind** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **plural** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **singular** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **shortcut** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **category** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **param** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any) *|* *None*) – 
  * **operation** ([*Literal*](https://docs.python.org/3/library/typing.html#typing.Literal)*[**'CREATE'**,* *'UPDATE'**,* *'DELETE'**,* *'CONNECT'**]* *|* *None*) – 
  * **operations** ([*Collection*](https://docs.python.org/3/library/typing.html#typing.Collection)*[*[*Literal*](https://docs.python.org/3/library/typing.html#typing.Literal)*[**'CREATE'**,* *'UPDATE'**,* *'DELETE'**,* *'CONNECT'**]**]* *|* *None*) – 
  * **subresource** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **persistent** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **side_effects** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **ignore_failures** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **labels** ([*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]**]* *|* *None*) – 
  * **annotations** ([*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]**]* *|* *None*) – 
  * **when** ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]* *|* *None*) – 
  * **field** (*None* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* *...**]* *|* [*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) – 
  * **value** (*None* *|* [*Any*](https://docs.python.org/3/library/typing.html#typing.Any) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]*) – 
  * **registry** ([*OperatorRegistry*](kopf.md#kopf.OperatorRegistry) *|* *None*) – 

### kopf.on.resume(\_\_group_or_groupversion_or_name=None, \_\_version_or_name=None, \_\_name=None, \*, group=None, version=None, kind=None, plural=None, singular=None, shortcut=None, category=None, id=None, param=None, errors=None, timeout=None, retries=None, backoff=None, deleted=None, labels=None, annotations=None, when=None, field=None, value=None, registry=None)

`@kopf.on.resume()` handler for the object resuming on operator (re)start.

* **Return type:**
  [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[[`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis), [`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`object`](https://docs.python.org/3/library/functions.html#object), [`None`](https://docs.python.org/3/library/constants.html#None), [`Coroutine`](https://docs.python.org/3/library/typing.html#typing.Coroutine)[[`None`](https://docs.python.org/3/library/constants.html#None), [`None`](https://docs.python.org/3/library/constants.html#None), [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`object`](https://docs.python.org/3/library/functions.html#object)]]]]], [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis), [`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`object`](https://docs.python.org/3/library/functions.html#object), [`None`](https://docs.python.org/3/library/constants.html#None), [`Coroutine`](https://docs.python.org/3/library/typing.html#typing.Coroutine)[[`None`](https://docs.python.org/3/library/constants.html#None), [`None`](https://docs.python.org/3/library/constants.html#None), [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`object`](https://docs.python.org/3/library/functions.html#object)]]]]]
* **Parameters:**
  * **\_\_group_or_groupversion_or_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *Marker* *|* *None*) – 
  * **\_\_version_or_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *Marker* *|* *None*) – 
  * **\_\_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *Marker* *|* *None*) – 
  * **group** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **version** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **kind** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **plural** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **singular** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **shortcut** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **category** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **param** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any) *|* *None*) – 
  * **errors** ([*ErrorsMode*](kopf.md#kopf.ErrorsMode) *|* *None*) – 
  * **timeout** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **retries** ([*int*](https://docs.python.org/3/library/functions.html#int) *|* *None*) – 
  * **backoff** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **deleted** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **labels** ([*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]**]* *|* *None*) – 
  * **annotations** ([*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]**]* *|* *None*) – 
  * **when** ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]* *|* *None*) – 
  * **field** (*None* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* *...**]* *|* [*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) – 
  * **value** (*None* *|* [*Any*](https://docs.python.org/3/library/typing.html#typing.Any) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]*) – 
  * **registry** ([*OperatorRegistry*](kopf.md#kopf.OperatorRegistry) *|* *None*) – 

### kopf.on.create(\_\_group_or_groupversion_or_name=None, \_\_version_or_name=None, \_\_name=None, \*, group=None, version=None, kind=None, plural=None, singular=None, shortcut=None, category=None, id=None, param=None, errors=None, timeout=None, retries=None, backoff=None, labels=None, annotations=None, when=None, field=None, value=None, registry=None)

`@kopf.on.create()` handler for the object creation.

* **Return type:**
  [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[[`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis), [`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`object`](https://docs.python.org/3/library/functions.html#object), [`None`](https://docs.python.org/3/library/constants.html#None), [`Coroutine`](https://docs.python.org/3/library/typing.html#typing.Coroutine)[[`None`](https://docs.python.org/3/library/constants.html#None), [`None`](https://docs.python.org/3/library/constants.html#None), [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`object`](https://docs.python.org/3/library/functions.html#object)]]]]], [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis), [`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`object`](https://docs.python.org/3/library/functions.html#object), [`None`](https://docs.python.org/3/library/constants.html#None), [`Coroutine`](https://docs.python.org/3/library/typing.html#typing.Coroutine)[[`None`](https://docs.python.org/3/library/constants.html#None), [`None`](https://docs.python.org/3/library/constants.html#None), [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`object`](https://docs.python.org/3/library/functions.html#object)]]]]]
* **Parameters:**
  * **\_\_group_or_groupversion_or_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *Marker* *|* *None*) – 
  * **\_\_version_or_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *Marker* *|* *None*) – 
  * **\_\_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *Marker* *|* *None*) – 
  * **group** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **version** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **kind** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **plural** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **singular** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **shortcut** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **category** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **param** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any) *|* *None*) – 
  * **errors** ([*ErrorsMode*](kopf.md#kopf.ErrorsMode) *|* *None*) – 
  * **timeout** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **retries** ([*int*](https://docs.python.org/3/library/functions.html#int) *|* *None*) – 
  * **backoff** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **labels** ([*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]**]* *|* *None*) – 
  * **annotations** ([*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]**]* *|* *None*) – 
  * **when** ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]* *|* *None*) – 
  * **field** (*None* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* *...**]* *|* [*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) – 
  * **value** (*None* *|* [*Any*](https://docs.python.org/3/library/typing.html#typing.Any) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]*) – 
  * **registry** ([*OperatorRegistry*](kopf.md#kopf.OperatorRegistry) *|* *None*) – 

### kopf.on.update(\_\_group_or_groupversion_or_name=None, \_\_version_or_name=None, \_\_name=None, \*, group=None, version=None, kind=None, plural=None, singular=None, shortcut=None, category=None, id=None, param=None, errors=None, timeout=None, retries=None, backoff=None, labels=None, annotations=None, when=None, field=None, value=None, old=None, new=None, registry=None)

`@kopf.on.update()` handler for the object update or change.

* **Return type:**
  [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[[`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis), [`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`object`](https://docs.python.org/3/library/functions.html#object), [`None`](https://docs.python.org/3/library/constants.html#None), [`Coroutine`](https://docs.python.org/3/library/typing.html#typing.Coroutine)[[`None`](https://docs.python.org/3/library/constants.html#None), [`None`](https://docs.python.org/3/library/constants.html#None), [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`object`](https://docs.python.org/3/library/functions.html#object)]]]]], [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis), [`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`object`](https://docs.python.org/3/library/functions.html#object), [`None`](https://docs.python.org/3/library/constants.html#None), [`Coroutine`](https://docs.python.org/3/library/typing.html#typing.Coroutine)[[`None`](https://docs.python.org/3/library/constants.html#None), [`None`](https://docs.python.org/3/library/constants.html#None), [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`object`](https://docs.python.org/3/library/functions.html#object)]]]]]
* **Parameters:**
  * **\_\_group_or_groupversion_or_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *Marker* *|* *None*) – 
  * **\_\_version_or_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *Marker* *|* *None*) – 
  * **\_\_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *Marker* *|* *None*) – 
  * **group** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **version** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **kind** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **plural** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **singular** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **shortcut** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **category** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **param** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any) *|* *None*) – 
  * **errors** ([*ErrorsMode*](kopf.md#kopf.ErrorsMode) *|* *None*) – 
  * **timeout** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **retries** ([*int*](https://docs.python.org/3/library/functions.html#int) *|* *None*) – 
  * **backoff** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **labels** ([*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]**]* *|* *None*) – 
  * **annotations** ([*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]**]* *|* *None*) – 
  * **when** ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]* *|* *None*) – 
  * **field** (*None* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* *...**]* *|* [*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) – 
  * **value** (*None* *|* [*Any*](https://docs.python.org/3/library/typing.html#typing.Any) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]*) – 
  * **old** (*None* *|* [*Any*](https://docs.python.org/3/library/typing.html#typing.Any) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]*) – 
  * **new** (*None* *|* [*Any*](https://docs.python.org/3/library/typing.html#typing.Any) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]*) – 
  * **registry** ([*OperatorRegistry*](kopf.md#kopf.OperatorRegistry) *|* *None*) – 

### kopf.on.delete(\_\_group_or_groupversion_or_name=None, \_\_version_or_name=None, \_\_name=None, \*, group=None, version=None, kind=None, plural=None, singular=None, shortcut=None, category=None, id=None, param=None, errors=None, timeout=None, retries=None, backoff=None, optional=None, labels=None, annotations=None, when=None, field=None, value=None, registry=None)

`@kopf.on.delete()` handler for the object deletion.

* **Return type:**
  [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[[`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis), [`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`object`](https://docs.python.org/3/library/functions.html#object), [`None`](https://docs.python.org/3/library/constants.html#None), [`Coroutine`](https://docs.python.org/3/library/typing.html#typing.Coroutine)[[`None`](https://docs.python.org/3/library/constants.html#None), [`None`](https://docs.python.org/3/library/constants.html#None), [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`object`](https://docs.python.org/3/library/functions.html#object)]]]]], [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis), [`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`object`](https://docs.python.org/3/library/functions.html#object), [`None`](https://docs.python.org/3/library/constants.html#None), [`Coroutine`](https://docs.python.org/3/library/typing.html#typing.Coroutine)[[`None`](https://docs.python.org/3/library/constants.html#None), [`None`](https://docs.python.org/3/library/constants.html#None), [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`object`](https://docs.python.org/3/library/functions.html#object)]]]]]
* **Parameters:**
  * **\_\_group_or_groupversion_or_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *Marker* *|* *None*) – 
  * **\_\_version_or_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *Marker* *|* *None*) – 
  * **\_\_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *Marker* *|* *None*) – 
  * **group** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **version** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **kind** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **plural** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **singular** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **shortcut** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **category** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **param** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any) *|* *None*) – 
  * **errors** ([*ErrorsMode*](kopf.md#kopf.ErrorsMode) *|* *None*) – 
  * **timeout** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **retries** ([*int*](https://docs.python.org/3/library/functions.html#int) *|* *None*) – 
  * **backoff** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **optional** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **labels** ([*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]**]* *|* *None*) – 
  * **annotations** ([*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]**]* *|* *None*) – 
  * **when** ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]* *|* *None*) – 
  * **field** (*None* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* *...**]* *|* [*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) – 
  * **value** (*None* *|* [*Any*](https://docs.python.org/3/library/typing.html#typing.Any) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]*) – 
  * **registry** ([*OperatorRegistry*](kopf.md#kopf.OperatorRegistry) *|* *None*) – 

### kopf.on.field(\_\_group_or_groupversion_or_name=None, \_\_version_or_name=None, \_\_name=None, \*, group=None, version=None, kind=None, plural=None, singular=None, shortcut=None, category=None, id=None, param=None, errors=None, timeout=None, retries=None, backoff=None, labels=None, annotations=None, when=None, field, value=None, old=None, new=None, registry=None)

`@kopf.on.field()` handler for the individual field changes.

* **Return type:**
  [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[[`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis), [`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`object`](https://docs.python.org/3/library/functions.html#object), [`None`](https://docs.python.org/3/library/constants.html#None), [`Coroutine`](https://docs.python.org/3/library/typing.html#typing.Coroutine)[[`None`](https://docs.python.org/3/library/constants.html#None), [`None`](https://docs.python.org/3/library/constants.html#None), [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`object`](https://docs.python.org/3/library/functions.html#object)]]]]], [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis), [`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`object`](https://docs.python.org/3/library/functions.html#object), [`None`](https://docs.python.org/3/library/constants.html#None), [`Coroutine`](https://docs.python.org/3/library/typing.html#typing.Coroutine)[[`None`](https://docs.python.org/3/library/constants.html#None), [`None`](https://docs.python.org/3/library/constants.html#None), [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`object`](https://docs.python.org/3/library/functions.html#object)]]]]]
* **Parameters:**
  * **\_\_group_or_groupversion_or_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *Marker* *|* *None*) – 
  * **\_\_version_or_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *Marker* *|* *None*) – 
  * **\_\_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *Marker* *|* *None*) – 
  * **group** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **version** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **kind** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **plural** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **singular** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **shortcut** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **category** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **param** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any) *|* *None*) – 
  * **errors** ([*ErrorsMode*](kopf.md#kopf.ErrorsMode) *|* *None*) – 
  * **timeout** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **retries** ([*int*](https://docs.python.org/3/library/functions.html#int) *|* *None*) – 
  * **backoff** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **labels** ([*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]**]* *|* *None*) – 
  * **annotations** ([*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]**]* *|* *None*) – 
  * **when** ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]* *|* *None*) – 
  * **field** (*None* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* *...**]* *|* [*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) – 
  * **value** (*None* *|* [*Any*](https://docs.python.org/3/library/typing.html#typing.Any) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]*) – 
  * **old** (*None* *|* [*Any*](https://docs.python.org/3/library/typing.html#typing.Any) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]*) – 
  * **new** (*None* *|* [*Any*](https://docs.python.org/3/library/typing.html#typing.Any) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]*) – 
  * **registry** ([*OperatorRegistry*](kopf.md#kopf.OperatorRegistry) *|* *None*) – 

### kopf.on.index(\_\_group_or_groupversion_or_name=None, \_\_version_or_name=None, \_\_name=None, \*, group=None, version=None, kind=None, plural=None, singular=None, shortcut=None, category=None, id=None, param=None, errors=None, timeout=None, retries=None, backoff=None, labels=None, annotations=None, when=None, field=None, value=None, registry=None)

`@kopf.index()` handler for the indexing callbacks.

* **Return type:**
  [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[[`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis), [`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`object`](https://docs.python.org/3/library/functions.html#object), [`None`](https://docs.python.org/3/library/constants.html#None), [`Coroutine`](https://docs.python.org/3/library/typing.html#typing.Coroutine)[[`None`](https://docs.python.org/3/library/constants.html#None), [`None`](https://docs.python.org/3/library/constants.html#None), [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`object`](https://docs.python.org/3/library/functions.html#object)]]]]], [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis), [`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`object`](https://docs.python.org/3/library/functions.html#object), [`None`](https://docs.python.org/3/library/constants.html#None), [`Coroutine`](https://docs.python.org/3/library/typing.html#typing.Coroutine)[[`None`](https://docs.python.org/3/library/constants.html#None), [`None`](https://docs.python.org/3/library/constants.html#None), [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`object`](https://docs.python.org/3/library/functions.html#object)]]]]]
* **Parameters:**
  * **\_\_group_or_groupversion_or_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *Marker* *|* *None*) – 
  * **\_\_version_or_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *Marker* *|* *None*) – 
  * **\_\_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *Marker* *|* *None*) – 
  * **group** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **version** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **kind** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **plural** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **singular** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **shortcut** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **category** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **param** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any) *|* *None*) – 
  * **errors** ([*ErrorsMode*](kopf.md#kopf.ErrorsMode) *|* *None*) – 
  * **timeout** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **retries** ([*int*](https://docs.python.org/3/library/functions.html#int) *|* *None*) – 
  * **backoff** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **labels** ([*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]**]* *|* *None*) – 
  * **annotations** ([*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]**]* *|* *None*) – 
  * **when** ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]* *|* *None*) – 
  * **field** (*None* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* *...**]* *|* [*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) – 
  * **value** (*None* *|* [*Any*](https://docs.python.org/3/library/typing.html#typing.Any) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]*) – 
  * **registry** ([*OperatorRegistry*](kopf.md#kopf.OperatorRegistry) *|* *None*) – 

### kopf.on.event(\_\_group_or_groupversion_or_name=None, \_\_version_or_name=None, \_\_name=None, \*, group=None, version=None, kind=None, plural=None, singular=None, shortcut=None, category=None, id=None, param=None, labels=None, annotations=None, when=None, field=None, value=None, registry=None)

`@kopf.on.event()` handler for the silent spies on the events.

* **Return type:**
  [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[[`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis), [`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`object`](https://docs.python.org/3/library/functions.html#object), [`None`](https://docs.python.org/3/library/constants.html#None), [`Coroutine`](https://docs.python.org/3/library/typing.html#typing.Coroutine)[[`None`](https://docs.python.org/3/library/constants.html#None), [`None`](https://docs.python.org/3/library/constants.html#None), [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`object`](https://docs.python.org/3/library/functions.html#object)]]]]], [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis), [`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`object`](https://docs.python.org/3/library/functions.html#object), [`None`](https://docs.python.org/3/library/constants.html#None), [`Coroutine`](https://docs.python.org/3/library/typing.html#typing.Coroutine)[[`None`](https://docs.python.org/3/library/constants.html#None), [`None`](https://docs.python.org/3/library/constants.html#None), [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`object`](https://docs.python.org/3/library/functions.html#object)]]]]]
* **Parameters:**
  * **\_\_group_or_groupversion_or_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *Marker* *|* *None*) – 
  * **\_\_version_or_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *Marker* *|* *None*) – 
  * **\_\_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *Marker* *|* *None*) – 
  * **group** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **version** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **kind** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **plural** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **singular** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **shortcut** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **category** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **param** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any) *|* *None*) – 
  * **labels** ([*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]**]* *|* *None*) – 
  * **annotations** ([*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]**]* *|* *None*) – 
  * **when** ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]* *|* *None*) – 
  * **field** (*None* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* *...**]* *|* [*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) – 
  * **value** (*None* *|* [*Any*](https://docs.python.org/3/library/typing.html#typing.Any) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]*) – 
  * **registry** ([*OperatorRegistry*](kopf.md#kopf.OperatorRegistry) *|* *None*) – 

### kopf.on.daemon(\_\_group_or_groupversion_or_name=None, \_\_version_or_name=None, \_\_name=None, \*, group=None, version=None, kind=None, plural=None, singular=None, shortcut=None, category=None, id=None, param=None, errors=None, timeout=None, retries=None, backoff=None, initial_delay=None, cancellation_backoff=None, cancellation_timeout=None, cancellation_polling=None, labels=None, annotations=None, when=None, field=None, value=None, registry=None)

`@kopf.daemon()` decorator for the background threads/tasks.

* **Return type:**
  [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[[`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis), [`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`object`](https://docs.python.org/3/library/functions.html#object), [`None`](https://docs.python.org/3/library/constants.html#None), [`Coroutine`](https://docs.python.org/3/library/typing.html#typing.Coroutine)[[`None`](https://docs.python.org/3/library/constants.html#None), [`None`](https://docs.python.org/3/library/constants.html#None), [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`object`](https://docs.python.org/3/library/functions.html#object)]]]]], [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis), [`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`object`](https://docs.python.org/3/library/functions.html#object), [`None`](https://docs.python.org/3/library/constants.html#None), [`Coroutine`](https://docs.python.org/3/library/typing.html#typing.Coroutine)[[`None`](https://docs.python.org/3/library/constants.html#None), [`None`](https://docs.python.org/3/library/constants.html#None), [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`object`](https://docs.python.org/3/library/functions.html#object)]]]]]
* **Parameters:**
  * **\_\_group_or_groupversion_or_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *Marker* *|* *None*) – 
  * **\_\_version_or_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *Marker* *|* *None*) – 
  * **\_\_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *Marker* *|* *None*) – 
  * **group** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **version** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **kind** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **plural** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **singular** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **shortcut** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **category** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **param** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any) *|* *None*) – 
  * **errors** ([*ErrorsMode*](kopf.md#kopf.ErrorsMode) *|* *None*) – 
  * **timeout** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **retries** ([*int*](https://docs.python.org/3/library/functions.html#int) *|* *None*) – 
  * **backoff** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **initial_delay** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **cancellation_backoff** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **cancellation_timeout** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **cancellation_polling** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **labels** ([*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]**]* *|* *None*) – 
  * **annotations** ([*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]**]* *|* *None*) – 
  * **when** ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]* *|* *None*) – 
  * **field** (*None* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* *...**]* *|* [*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) – 
  * **value** (*None* *|* [*Any*](https://docs.python.org/3/library/typing.html#typing.Any) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]*) – 
  * **registry** ([*OperatorRegistry*](kopf.md#kopf.OperatorRegistry) *|* *None*) – 

### kopf.on.timer(\_\_group_or_groupversion_or_name=None, \_\_version_or_name=None, \_\_name=None, \*, group=None, version=None, kind=None, plural=None, singular=None, shortcut=None, category=None, id=None, param=None, errors=None, timeout=None, retries=None, backoff=None, interval=None, initial_delay=None, sharp=None, idle=None, labels=None, annotations=None, when=None, field=None, value=None, registry=None)

`@kopf.timer()` handler for the regular events.

* **Return type:**
  [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[[`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis), [`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`object`](https://docs.python.org/3/library/functions.html#object), [`None`](https://docs.python.org/3/library/constants.html#None), [`Coroutine`](https://docs.python.org/3/library/typing.html#typing.Coroutine)[[`None`](https://docs.python.org/3/library/constants.html#None), [`None`](https://docs.python.org/3/library/constants.html#None), [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`object`](https://docs.python.org/3/library/functions.html#object)]]]]], [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis), [`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`object`](https://docs.python.org/3/library/functions.html#object), [`None`](https://docs.python.org/3/library/constants.html#None), [`Coroutine`](https://docs.python.org/3/library/typing.html#typing.Coroutine)[[`None`](https://docs.python.org/3/library/constants.html#None), [`None`](https://docs.python.org/3/library/constants.html#None), [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`object`](https://docs.python.org/3/library/functions.html#object)]]]]]
* **Parameters:**
  * **\_\_group_or_groupversion_or_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *Marker* *|* *None*) – 
  * **\_\_version_or_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *Marker* *|* *None*) – 
  * **\_\_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *Marker* *|* *None*) – 
  * **group** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **version** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **kind** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **plural** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **singular** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **shortcut** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **category** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **param** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any) *|* *None*) – 
  * **errors** ([*ErrorsMode*](kopf.md#kopf.ErrorsMode) *|* *None*) – 
  * **timeout** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **retries** ([*int*](https://docs.python.org/3/library/functions.html#int) *|* *None*) – 
  * **backoff** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **interval** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **initial_delay** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **sharp** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **idle** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **labels** ([*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]**]* *|* *None*) – 
  * **annotations** ([*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]**]* *|* *None*) – 
  * **when** ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]* *|* *None*) – 
  * **field** (*None* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* *...**]* *|* [*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) – 
  * **value** (*None* *|* [*Any*](https://docs.python.org/3/library/typing.html#typing.Any) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]*) – 
  * **registry** ([*OperatorRegistry*](kopf.md#kopf.OperatorRegistry) *|* *None*) – 

### kopf.on.subhandler(\*, id=None, param=None, errors=None, timeout=None, retries=None, backoff=None, labels=None, annotations=None, when=None, field=None, value=None, old=None, new=None)

`@kopf.subhandler()` decorator for the dynamically generated sub-handlers.

Can be used only inside of the handler function.
It is efficiently a syntax sugar to look like all other handlers:

```default
@kopf.on.create('kopfexamples')
def create(*, spec, **kwargs):

    for task in spec.get('tasks', []):

        @kopf.subhandler(id=f'task_{task}')
        def create_task(*, spec, task=task, **kwargs):
            pass
```

In this example, having spec.tasks set to `[abc, def]`, this will create
the following handlers: `create`, `create/task_abc`, `create/task_def`.

The parent handler is not considered as finished if there are unfinished
sub-handlers left. Since the sub-handlers will be executed in the regular
reactor and lifecycle, with multiple low-level events (one per iteration),
the parent handler will also be executed multiple times, and is expected
to produce the same (or at least predictable) set of sub-handlers.
In addition, keep its logic idempotent (not failing on the repeated calls).

Note: `task=task` is needed to freeze the closure variable, so that every
create function will have its own value, not the latest in the for-cycle.

* **Return type:**
  [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[[`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis), [`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`object`](https://docs.python.org/3/library/functions.html#object), [`None`](https://docs.python.org/3/library/constants.html#None), [`Coroutine`](https://docs.python.org/3/library/typing.html#typing.Coroutine)[[`None`](https://docs.python.org/3/library/constants.html#None), [`None`](https://docs.python.org/3/library/constants.html#None), [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`object`](https://docs.python.org/3/library/functions.html#object)]]]]], [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis), [`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`object`](https://docs.python.org/3/library/functions.html#object), [`None`](https://docs.python.org/3/library/constants.html#None), [`Coroutine`](https://docs.python.org/3/library/typing.html#typing.Coroutine)[[`None`](https://docs.python.org/3/library/constants.html#None), [`None`](https://docs.python.org/3/library/constants.html#None), [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`object`](https://docs.python.org/3/library/functions.html#object)]]]]]
* **Parameters:**
  * **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **param** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any) *|* *None*) – 
  * **errors** ([*ErrorsMode*](kopf.md#kopf.ErrorsMode) *|* *None*) – 
  * **timeout** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **retries** ([*int*](https://docs.python.org/3/library/functions.html#int) *|* *None*) – 
  * **backoff** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **labels** ([*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]**]* *|* *None*) – 
  * **annotations** ([*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]**]* *|* *None*) – 
  * **when** ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]* *|* *None*) – 
  * **field** (*None* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* *...**]* *|* [*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) – 
  * **value** (*None* *|* [*Any*](https://docs.python.org/3/library/typing.html#typing.Any) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]*) – 
  * **old** (*None* *|* [*Any*](https://docs.python.org/3/library/typing.html#typing.Any) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]*) – 
  * **new** (*None* *|* [*Any*](https://docs.python.org/3/library/typing.html#typing.Any) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]*) – 

### kopf.on.register(fn, \*, id=None, param=None, errors=None, timeout=None, retries=None, backoff=None, labels=None, annotations=None, when=None)

Register a function as a sub-handler of the currently executed handler.

Example:

```default
@kopf.on.create('kopfexamples')
def create_it(spec, **kwargs):
    for task in spec.get('tasks', []):

        def create_single_task(task=task, **_):
            pass

        kopf.register(id=task, fn=create_single_task)
```

This is efficiently an equivalent for:

```default
@kopf.on.create('kopfexamples')
def create_it(spec, **kwargs):
    for task in spec.get('tasks', []):

        @kopf.subhandler(id=task)
        def create_single_task(task=task, **_):
            pass
```

* **Return type:**
  [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis), [`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`object`](https://docs.python.org/3/library/functions.html#object), [`None`](https://docs.python.org/3/library/constants.html#None), [`Coroutine`](https://docs.python.org/3/library/typing.html#typing.Coroutine)[[`None`](https://docs.python.org/3/library/constants.html#None), [`None`](https://docs.python.org/3/library/constants.html#None), [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`object`](https://docs.python.org/3/library/functions.html#object)]]]]
* **Parameters:**
  * **fn** ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*object*](https://docs.python.org/3/library/functions.html#object) *|* *None* *|* [*Coroutine*](https://docs.python.org/3/library/typing.html#typing.Coroutine)*[**None**,* *None**,* [*object*](https://docs.python.org/3/library/functions.html#object) *|* *None**]**]*) – 
  * **id** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **param** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any) *|* *None*) – 
  * **errors** ([*ErrorsMode*](kopf.md#kopf.ErrorsMode) *|* *None*) – 
  * **timeout** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **retries** ([*int*](https://docs.python.org/3/library/functions.html#int) *|* *None*) – 
  * **backoff** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **labels** ([*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]**]* *|* *None*) – 
  * **annotations** ([*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]**]* *|* *None*) – 
  * **when** ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]* *|* *None*) –
