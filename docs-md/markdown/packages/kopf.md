# kopf package

The main Kopf module for all the exported functions & classes.

### kopf.register(fn, \*, id=None, param=None, errors=None, timeout=None, retries=None, backoff=None, labels=None, annotations=None, when=None)

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
  * **errors** ([*ErrorsMode*](#kopf.ErrorsMode) *|* *None*) – 
  * **timeout** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **retries** ([*int*](https://docs.python.org/3/library/functions.html#int) *|* *None*) – 
  * **backoff** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **labels** ([*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]**]* *|* *None*) – 
  * **annotations** ([*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]**]* *|* *None*) – 
  * **when** ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]* *|* *None*) – 

### *async* kopf.execute(\*, fns=None, handlers=None, registry=None, lifecycle=None, cause=None)

Execute the handlers in an isolated lifecycle.

This function is just a public wrapper for execute with multiple
ways to specify the handlers: either as the raw functions, or as the
pre-created handlers, or as a registry (as used in the object handling).

If no explicit functions or handlers or registry are passed,
the sub-handlers of the current handler are assumed, as accumulated
in the per-handler registry with `@kopf.subhandler`.

If the call to this method for the sub-handlers is not done explicitly
in the handler, it is done implicitly after the handler is exited.
One way or another, it is executed for the sub-handlers.

* **Return type:**
  [`None`](https://docs.python.org/3/library/constants.html#None)
* **Parameters:**
  * **fns** ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable)*[*[*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*object*](https://docs.python.org/3/library/functions.html#object) *|* *None* *|* [*Coroutine*](https://docs.python.org/3/library/typing.html#typing.Coroutine)*[**None**,* *None**,* [*object*](https://docs.python.org/3/library/functions.html#object) *|* *None**]**]**]* *|* *None*) – 
  * **handlers** ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable)*[**ChangingHandler**]* *|* *None*) – 
  * **registry** (*ChangingRegistry* *|* *None*) – 
  * **lifecycle** (*LifeCycleFn* *|* *None*) – 
  * **cause** (*Cause* *|* *None*) – 

### kopf.daemon(\_\_group_or_groupversion_or_name=None, \_\_version_or_name=None, \_\_name=None, \*, group=None, version=None, kind=None, plural=None, singular=None, shortcut=None, category=None, id=None, param=None, errors=None, timeout=None, retries=None, backoff=None, initial_delay=None, cancellation_backoff=None, cancellation_timeout=None, cancellation_polling=None, labels=None, annotations=None, when=None, field=None, value=None, registry=None)

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
  * **errors** ([*ErrorsMode*](#kopf.ErrorsMode) *|* *None*) – 
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
  * **registry** ([*OperatorRegistry*](#kopf.OperatorRegistry) *|* *None*) – 

### kopf.timer(\_\_group_or_groupversion_or_name=None, \_\_version_or_name=None, \_\_name=None, \*, group=None, version=None, kind=None, plural=None, singular=None, shortcut=None, category=None, id=None, param=None, errors=None, timeout=None, retries=None, backoff=None, interval=None, initial_delay=None, sharp=None, idle=None, labels=None, annotations=None, when=None, field=None, value=None, registry=None)

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
  * **errors** ([*ErrorsMode*](#kopf.ErrorsMode) *|* *None*) – 
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
  * **registry** ([*OperatorRegistry*](#kopf.OperatorRegistry) *|* *None*) – 

### kopf.index(\_\_group_or_groupversion_or_name=None, \_\_version_or_name=None, \_\_name=None, \*, group=None, version=None, kind=None, plural=None, singular=None, shortcut=None, category=None, id=None, param=None, errors=None, timeout=None, retries=None, backoff=None, labels=None, annotations=None, when=None, field=None, value=None, registry=None)

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
  * **errors** ([*ErrorsMode*](#kopf.ErrorsMode) *|* *None*) – 
  * **timeout** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **retries** ([*int*](https://docs.python.org/3/library/functions.html#int) *|* *None*) – 
  * **backoff** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
  * **labels** ([*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]**]* *|* *None*) – 
  * **annotations** ([*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]**]* *|* *None*) – 
  * **when** ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]* *|* *None*) – 
  * **field** (*None* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* *...**]* *|* [*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) – 
  * **value** (*None* *|* [*Any*](https://docs.python.org/3/library/typing.html#typing.Any) *|* *MetaFilterToken* *|* [*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable)*[**[**...**]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool)*]*) – 
  * **registry** ([*OperatorRegistry*](#kopf.OperatorRegistry) *|* *None*) – 

### kopf.configure(debug=None, verbose=None, quiet=None, log_format=LogFormat.FULL, log_prefix=False, log_refkey=None)

* **Return type:**
  [`None`](https://docs.python.org/3/library/constants.html#None)
* **Parameters:**
  * **debug** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **verbose** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **quiet** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **log_format** ([*LogFormat*](#kopf.LogFormat)) – 
  * **log_prefix** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **log_refkey** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 

### *class* kopf.LogFormat(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Bases: [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

Log formats, as specified on CLI.

#### PLAIN *= '%(message)s'*

#### FULL *= '[%(asctime)s] %(name)-20.20s [%(levelname)-8.8s] %(message)s'*

#### JSON *= 1*

### kopf.login_via_pykube(\*, logger, \*\*\_)

* **Return type:**
  [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ConnectionInfo`](#kopf.ConnectionInfo)]
* **Parameters:**
  * **logger** ([*Logger*](https://docs.python.org/3/library/logging.html#logging.Logger) *|* [*LoggerAdapter*](https://docs.python.org/3/library/logging.html#logging.LoggerAdapter)) – 
  * **\_** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any)) – 

### kopf.login_via_client(\*, logger, \*\*\_)

* **Return type:**
  [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ConnectionInfo`](#kopf.ConnectionInfo)]
* **Parameters:**
  * **logger** ([*Logger*](https://docs.python.org/3/library/logging.html#logging.Logger) *|* [*LoggerAdapter*](https://docs.python.org/3/library/logging.html#logging.LoggerAdapter)) – 
  * **\_** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any)) – 

### kopf.login_with_kubeconfig(\*\*\_)

A minimalistic login handler that can get raw data from a kubeconfig file.

Authentication capabilities can be limited to keep the code short & simple.
No parsing or sophisticated multi-step token retrieval is performed.

This login function is intended to make Kopf runnable in trivial cases
when neither pykube-ng nor the official client library are installed.

* **Return type:**
  [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ConnectionInfo`](#kopf.ConnectionInfo)]
* **Parameters:**
  **\_** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any)) – 

### kopf.login_with_service_account(\*\*\_)

A minimalistic login handler that can get raw data from a service account.

Authentication capabilities can be limited to keep the code short & simple.
No parsing or sophisticated multi-step token retrieval is performed.

This login function is intended to make Kopf runnable in trivial cases
when neither pykube-ng nor the official client library are installed.

* **Return type:**
  [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ConnectionInfo`](#kopf.ConnectionInfo)]
* **Parameters:**
  **\_** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any)) – 

### *exception* kopf.LoginError

Bases: [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception)

Raised when the operator cannot login to the API.

### *class* kopf.ConnectionInfo(server, ca_path=None, ca_data=None, insecure=None, username=None, password=None, scheme=None, token=None, certificate_path=None, certificate_data=None, private_key_path=None, private_key_data=None, default_namespace=None, priority=0, expiration=None)

Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

A single endpoint with specific credentials and connection flags to use.

* **Parameters:**
  * **server** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **ca_path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **ca_data** ([*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes) *|* *None*) – 
  * **insecure** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **username** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **password** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **scheme** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **token** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **certificate_path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **certificate_data** ([*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes) *|* *None*) – 
  * **private_key_path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **private_key_data** ([*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes) *|* *None*) – 
  * **default_namespace** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **priority** ([*int*](https://docs.python.org/3/library/functions.html#int)) – 
  * **expiration** ([*datetime*](https://docs.python.org/3/library/datetime.html#datetime.datetime) *|* *None*) – 

#### server*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### ca_path*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### ca_data*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes)]* *= None*

#### insecure*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

#### username*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### password*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### scheme*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### token*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### certificate_path*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### certificate_data*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes)]* *= None*

#### private_key_path*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### private_key_data*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes)]* *= None*

#### default_namespace*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### priority*: [`int`](https://docs.python.org/3/library/functions.html#int)* *= 0*

#### expiration*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime)]* *= None*

### kopf.event(objs, \*, type, reason, message='')

* **Return type:**
  [`None`](https://docs.python.org/3/library/constants.html#None)
* **Parameters:**
  * **objs** ([*Body*](#kopf.Body) *|* [*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable)*[*[*Body*](#kopf.Body)*]*) – 
  * **type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **reason** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **message** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 

### kopf.info(objs, \*, reason, message='')

* **Return type:**
  [`None`](https://docs.python.org/3/library/constants.html#None)
* **Parameters:**
  * **objs** ([*Body*](#kopf.Body) *|* [*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable)*[*[*Body*](#kopf.Body)*]*) – 
  * **reason** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **message** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 

### kopf.warn(objs, \*, reason, message='')

* **Return type:**
  [`None`](https://docs.python.org/3/library/constants.html#None)
* **Parameters:**
  * **objs** ([*Body*](#kopf.Body) *|* [*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable)*[*[*Body*](#kopf.Body)*]*) – 
  * **reason** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **message** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 

### kopf.exception(objs, \*, reason='', message='', exc=None)

* **Return type:**
  [`None`](https://docs.python.org/3/library/constants.html#None)
* **Parameters:**
  * **objs** ([*Body*](#kopf.Body) *|* [*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable)*[*[*Body*](#kopf.Body)*]*) – 
  * **reason** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **message** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **exc** ([*BaseException*](https://docs.python.org/3/library/exceptions.html#BaseException) *|* *None*) – 

### *async* kopf.spawn_tasks(\*, lifecycle=None, indexers=None, registry=None, settings=None, memories=None, insights=None, identity=None, standalone=None, priority=None, peering_name=None, liveness_endpoint=None, clusterwide=False, namespaces=(), namespace=None, stop_flag=None, ready_flag=None, vault=None, memo=None, \_command=None)

Spawn all the tasks needed to run the operator.

The tasks are properly inter-connected with the synchronisation primitives.

* **Return type:**
  [`Collection`](https://docs.python.org/3/library/typing.html#typing.Collection)[`Task`]
* **Parameters:**
  * **lifecycle** (*LifeCycleFn* *|* *None*) – 
  * **indexers** (*OperatorIndexers* *|* *None*) – 
  * **registry** ([*OperatorRegistry*](#kopf.OperatorRegistry) *|* *None*) – 
  * **settings** ([*OperatorSettings*](#kopf.OperatorSettings) *|* *None*) – 
  * **memories** (*ResourceMemories* *|* *None*) – 
  * **insights** (*Insights* *|* *None*) – 
  * **identity** (*Identity* *|* *None*) – 
  * **standalone** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **priority** ([*int*](https://docs.python.org/3/library/functions.html#int) *|* *None*) – 
  * **peering_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **liveness_endpoint** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **clusterwide** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **namespaces** ([*Collection*](https://docs.python.org/3/library/typing.html#typing.Collection)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*Pattern*](https://docs.python.org/3/library/typing.html#typing.Pattern)*]*) – 
  * **namespace** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*Pattern*](https://docs.python.org/3/library/typing.html#typing.Pattern) *|* *None*) – 
  * **stop_flag** (*Future* *|* *Event* *|* *Future* *|* [*Event*](https://docs.python.org/3/library/threading.html#threading.Event) *|* *None*) – 
  * **ready_flag** (*Future* *|* *Event* *|* *Future* *|* [*Event*](https://docs.python.org/3/library/threading.html#threading.Event) *|* *None*) – 
  * **vault** (*Vault* *|* *None*) – 
  * **memo** ([*object*](https://docs.python.org/3/library/functions.html#object) *|* *None*) – 
  * **\_command** ([*Coroutine*](https://docs.python.org/3/library/typing.html#typing.Coroutine)*[**None**,* *None**,* *None**]* *|* *None*) – 

### *async* kopf.run_tasks(root_tasks, \*, ignored=frozenset({}))

Orchestrate the tasks and terminate them gracefully when needed.

The root tasks are expected to run forever. Their number is limited. Once
any of them exits, the whole operator and all other root tasks should exit.

The root tasks, in turn, can spawn multiple sub-tasks of various purposes.
They can be awaited, monitored, or fired-and-forgot.

The hung tasks are those that were spawned during the operator runtime,
and were not cancelled/exited on the root tasks termination. They are given
some extra time to finish, after which they are forcely terminated too.
:rtype: [`None`](https://docs.python.org/3/library/constants.html#None)

#### NOTE
Due to implementation details, every task created after the operator’s
startup is assumed to be a task or a sub-task of the operator.
In the end, all tasks are forcely cancelled. Even if those tasks were
created by other means. There is no way to trace who spawned what.
Only the tasks that existed before the operator startup are ignored
(for example, those that spawned the operator itself).

* **Parameters:**
  * **root_tasks** ([*Collection*](https://docs.python.org/3/library/typing.html#typing.Collection)*[**Task**]*) – 
  * **ignored** ([*Collection*](https://docs.python.org/3/library/typing.html#typing.Collection)*[**Task**]*) – 
* **Return type:**
  None

### *async* kopf.operator(\*, lifecycle=None, indexers=None, registry=None, settings=None, memories=None, insights=None, identity=None, standalone=None, priority=None, peering_name=None, liveness_endpoint=None, clusterwide=False, namespaces=(), namespace=None, stop_flag=None, ready_flag=None, vault=None, memo=None, \_command=None)

Run the whole operator asynchronously.

This function should be used to run an operator in an asyncio event-loop
if the operator is orchestrated explicitly and manually.

It is efficiently spawn_tasks + run_tasks with some safety.

* **Return type:**
  [`None`](https://docs.python.org/3/library/constants.html#None)
* **Parameters:**
  * **lifecycle** (*LifeCycleFn* *|* *None*) – 
  * **indexers** (*OperatorIndexers* *|* *None*) – 
  * **registry** ([*OperatorRegistry*](#kopf.OperatorRegistry) *|* *None*) – 
  * **settings** ([*OperatorSettings*](#kopf.OperatorSettings) *|* *None*) – 
  * **memories** (*ResourceMemories* *|* *None*) – 
  * **insights** (*Insights* *|* *None*) – 
  * **identity** (*Identity* *|* *None*) – 
  * **standalone** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **priority** ([*int*](https://docs.python.org/3/library/functions.html#int) *|* *None*) – 
  * **peering_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **liveness_endpoint** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **clusterwide** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **namespaces** ([*Collection*](https://docs.python.org/3/library/typing.html#typing.Collection)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*Pattern*](https://docs.python.org/3/library/typing.html#typing.Pattern)*]*) – 
  * **namespace** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*Pattern*](https://docs.python.org/3/library/typing.html#typing.Pattern) *|* *None*) – 
  * **stop_flag** (*Future* *|* *Event* *|* *Future* *|* [*Event*](https://docs.python.org/3/library/threading.html#threading.Event) *|* *None*) – 
  * **ready_flag** (*Future* *|* *Event* *|* *Future* *|* [*Event*](https://docs.python.org/3/library/threading.html#threading.Event) *|* *None*) – 
  * **vault** (*Vault* *|* *None*) – 
  * **memo** ([*object*](https://docs.python.org/3/library/functions.html#object) *|* *None*) – 
  * **\_command** ([*Coroutine*](https://docs.python.org/3/library/typing.html#typing.Coroutine)*[**None**,* *None**,* *None**]* *|* *None*) – 

### kopf.run(\*, loop=None, lifecycle=None, indexers=None, registry=None, settings=None, memories=None, insights=None, identity=None, standalone=None, priority=None, peering_name=None, liveness_endpoint=None, clusterwide=False, namespaces=(), namespace=None, stop_flag=None, ready_flag=None, vault=None, memo=None, \_command=None)

Run the whole operator synchronously.

If the loop is not specified, the operator runs in the event loop
of the current \_context_ (by asyncio’s default, the current thread).
See: [https://docs.python.org/3/library/asyncio-policy.html](https://docs.python.org/3/library/asyncio-policy.html) for details.

Alternatively, use asyncio.run(kopf.operator(…)) with the same options.
It will take care of a new event loop’s creation and finalization for this
call. See: [`asyncio.run()`](https://docs.python.org/3/library/asyncio-runner.html#asyncio.run).

* **Return type:**
  [`None`](https://docs.python.org/3/library/constants.html#None)
* **Parameters:**
  * **loop** (*AbstractEventLoop* *|* *None*) – 
  * **lifecycle** (*LifeCycleFn* *|* *None*) – 
  * **indexers** (*OperatorIndexers* *|* *None*) – 
  * **registry** ([*OperatorRegistry*](#kopf.OperatorRegistry) *|* *None*) – 
  * **settings** ([*OperatorSettings*](#kopf.OperatorSettings) *|* *None*) – 
  * **memories** (*ResourceMemories* *|* *None*) – 
  * **insights** (*Insights* *|* *None*) – 
  * **identity** (*Identity* *|* *None*) – 
  * **standalone** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **priority** ([*int*](https://docs.python.org/3/library/functions.html#int) *|* *None*) – 
  * **peering_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **liveness_endpoint** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **clusterwide** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **namespaces** ([*Collection*](https://docs.python.org/3/library/typing.html#typing.Collection)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*Pattern*](https://docs.python.org/3/library/typing.html#typing.Pattern)*]*) – 
  * **namespace** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*Pattern*](https://docs.python.org/3/library/typing.html#typing.Pattern) *|* *None*) – 
  * **stop_flag** (*Future* *|* *Event* *|* *Future* *|* [*Event*](https://docs.python.org/3/library/threading.html#threading.Event) *|* *None*) – 
  * **ready_flag** (*Future* *|* *Event* *|* *Future* *|* [*Event*](https://docs.python.org/3/library/threading.html#threading.Event) *|* *None*) – 
  * **vault** (*Vault* *|* *None*) – 
  * **memo** ([*object*](https://docs.python.org/3/library/functions.html#object) *|* *None*) – 
  * **\_command** ([*Coroutine*](https://docs.python.org/3/library/typing.html#typing.Coroutine)*[**None**,* *None**,* *None**]* *|* *None*) – 

### kopf.adopt(objs, owner=None, \*, forced=False, strict=False, nested=None)

The children should be in the same namespace, named after their parent, and owned by it.

* **Return type:**
  [`None`](https://docs.python.org/3/library/constants.html#None)
* **Parameters:**
  * **objs** ([*MutableMapping*](https://docs.python.org/3/library/typing.html#typing.MutableMapping)*[*[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*,* [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*]* *|* *\_dummy* *|* *KubernetesModel* *|* [*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable)*[*[*MutableMapping*](https://docs.python.org/3/library/typing.html#typing.MutableMapping)*[*[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*,* [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*]* *|* *\_dummy* *|* *KubernetesModel**]*) – 
  * **owner** ([*Body*](#kopf.Body) *|* *None*) – 
  * **forced** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **strict** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **nested** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable)*[**None* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* *...**]* *|* [*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]**]* *|* *None*) – 

### kopf.label(objs, labels=\_UNSET.token, \*, forced=False, nested=None, force=None)

Apply the labels to the object(s).

* **Return type:**
  [`None`](https://docs.python.org/3/library/constants.html#None)
* **Parameters:**
  * **objs** ([*MutableMapping*](https://docs.python.org/3/library/typing.html#typing.MutableMapping)*[*[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*,* [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*]* *|* *\_dummy* *|* *KubernetesModel* *|* [*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable)*[*[*MutableMapping*](https://docs.python.org/3/library/typing.html#typing.MutableMapping)*[*[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*,* [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*]* *|* *\_dummy* *|* *KubernetesModel**]*) – 
  * **labels** ([*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* *None* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str)*]* *|* *\_UNSET*) – 
  * **forced** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **nested** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable)*[**None* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* *...**]* *|* [*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]**]* *|* *None*) – 
  * **force** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 

### kopf.not_(fn)

* **Return type:**
  [`TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar)(`_FnT`, [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis), [`bool`](https://docs.python.org/3/library/functions.html#bool)], [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis), [`bool`](https://docs.python.org/3/library/functions.html#bool)])
* **Parameters:**
  **fn** (*\_FnT*) – 

### kopf.all_(fns)

* **Return type:**
  [`TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar)(`_FnT`, [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis), [`bool`](https://docs.python.org/3/library/functions.html#bool)], [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis), [`bool`](https://docs.python.org/3/library/functions.html#bool)])
* **Parameters:**
  **fns** ([*Collection*](https://docs.python.org/3/library/typing.html#typing.Collection)*[**\_FnT**]*) – 

### kopf.any_(fns)

* **Return type:**
  [`TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar)(`_FnT`, [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis), [`bool`](https://docs.python.org/3/library/functions.html#bool)], [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis), [`bool`](https://docs.python.org/3/library/functions.html#bool)])
* **Parameters:**
  **fns** ([*Collection*](https://docs.python.org/3/library/typing.html#typing.Collection)*[**\_FnT**]*) – 

### kopf.none_(fns)

* **Return type:**
  [`TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar)(`_FnT`, [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis), [`bool`](https://docs.python.org/3/library/functions.html#bool)], [`Callable`](https://docs.python.org/3/library/typing.html#typing.Callable)[[`...`](https://docs.python.org/3/library/constants.html#Ellipsis), [`bool`](https://docs.python.org/3/library/functions.html#bool)])
* **Parameters:**
  **fns** ([*Collection*](https://docs.python.org/3/library/typing.html#typing.Collection)*[**\_FnT**]*) – 

### kopf.get_default_lifecycle()

* **Return type:**
  `LifeCycleFn`

### kopf.set_default_lifecycle(lifecycle)

* **Return type:**
  [`None`](https://docs.python.org/3/library/constants.html#None)
* **Parameters:**
  **lifecycle** (*LifeCycleFn* *|* *None*) – 

### kopf.build_object_reference(body)

Construct an object reference for the events.

Keep in mind that some fields can be absent: e.g. `namespace`
for cluster resources, or e.g. `apiVersion` for `kind: Node`, etc.

* **Return type:**
  [`ObjectReference`](#kopf.ObjectReference)
* **Parameters:**
  **body** ([*Body*](#kopf.Body)) – 

### kopf.build_owner_reference(body, \*, controller=True, block_owner_deletion=True)

Construct an owner reference object for the parent-children relationships.

The structure needed to link the children objects to the current object as a parent.
See [https://kubernetes.io/docs/concepts/workloads/controllers/garbage-collection/](https://kubernetes.io/docs/concepts/workloads/controllers/garbage-collection/)

Keep in mind that some fields can be absent: e.g. `namespace`
for cluster resources, or e.g. `apiVersion` for `kind: Node`, etc.

* **Return type:**
  [`OwnerReference`](#kopf.OwnerReference)
* **Parameters:**
  * **body** ([*Body*](#kopf.Body)) – 
  * **controller** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **block_owner_deletion** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 

### kopf.append_owner_reference(objs, owner=None, \*, controller=True, block_owner_deletion=True)

Append an owner reference to the resource(s), if it is not yet there.

Note: the owned objects are usually not the one being processed,
so the whole body can be modified, no patches are needed.

* **Return type:**
  [`None`](https://docs.python.org/3/library/constants.html#None)
* **Parameters:**
  * **objs** ([*MutableMapping*](https://docs.python.org/3/library/typing.html#typing.MutableMapping)*[*[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*,* [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*]* *|* *\_dummy* *|* *KubernetesModel* *|* [*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable)*[*[*MutableMapping*](https://docs.python.org/3/library/typing.html#typing.MutableMapping)*[*[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*,* [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*]* *|* *\_dummy* *|* *KubernetesModel**]*) – 
  * **owner** ([*Body*](#kopf.Body) *|* *None*) – 
  * **controller** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **block_owner_deletion** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 

### kopf.remove_owner_reference(objs, owner=None)

Remove an owner reference to the resource(s), if it is there.

Note: the owned objects are usually not the one being processed,
so the whole body can be modified, no patches are needed.

* **Return type:**
  [`None`](https://docs.python.org/3/library/constants.html#None)
* **Parameters:**
  * **objs** ([*MutableMapping*](https://docs.python.org/3/library/typing.html#typing.MutableMapping)*[*[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*,* [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*]* *|* *\_dummy* *|* *KubernetesModel* *|* [*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable)*[*[*MutableMapping*](https://docs.python.org/3/library/typing.html#typing.MutableMapping)*[*[*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*,* [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*]* *|* *\_dummy* *|* *KubernetesModel**]*) – 
  * **owner** ([*Body*](#kopf.Body) *|* *None*) – 

### *class* kopf.ErrorsMode(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Bases: [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

How arbitrary (non-temporary/non-permanent) exceptions are treated.

#### IGNORED *= 1*

#### TEMPORARY *= 2*

#### PERMANENT *= 3*

### *exception* kopf.AdmissionError(message='', code=500)

Bases: [`PermanentError`](#kopf.PermanentError)

Raised by admission handlers when an API operation under check is bad.

An admission error behaves the same as kopf.PermanentError, but provides
admission-specific payload for the response: a message & a numeric code.

This error type is preferred when selecting only one error to report back
to apiservers as the admission review result – in case multiple handlers
are called in one admission request, i.e. when the webhook endpoints
are not mapped to the handler ids (e.g. when configured manually).

* **Parameters:**
  * **message** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **code** ([*int*](https://docs.python.org/3/library/functions.html#int) *|* *None*) – 
* **Return type:**
  None

### *class* kopf.WebhookClientConfigService

Bases: `TypedDict`

#### namespace*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

#### name*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

#### path*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

#### port*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]*

### *class* kopf.WebhookClientConfig

Bases: `TypedDict`

A config of clients (apiservers) to access the webhooks’ server (operators).

This dictionary is put into managed webhook configurations “as is”.
The fields & type annotations are only for hinting.

Kopf additionally modifies the url and the service’s path to inject
handler ids as the last path component. This must be taken into account
by custom webhook servers.

#### caBundle*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

#### url*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

#### service*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`WebhookClientConfigService`](#kopf.WebhookClientConfigService)]*

### *class* kopf.UserInfo

Bases: `TypedDict`

#### username*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### uid*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### groups*: [`List`](https://docs.python.org/3/library/typing.html#typing.List)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

### *class* kopf.WebhookFn(\*args, \*\*kwargs)

Bases: `Protocol`

A framework-provided function to call when an admission request is received.

The framework provides the actual function. Custom webhook servers must
accept the function, invoke it accordingly on admission requests, wait
for the admission response, serialise it and send it back. They do not
implement this function. This protocol only declares the exact signature.

### *class* kopf.WebhookServer(\*, addr=None, port=None, path=None, host=None, cadata=None, cafile=None, cadump=None, context=None, insecure=False, certfile=None, pkeyfile=None, password=None, extra_sans=(), verify_mode=None, verify_cafile=None, verify_capath=None, verify_cadata=None)

Bases: `WebhookContextManager`

A local HTTP/HTTPS endpoint.

Currently, the server is based on `aiohttp`, but the implementation
can change in the future without warning.

This server is also used by specialised tunnels when they need
a local endpoint to be tunneled.

* `addr`, `port` is where to listen for connections
  (defaults to `localhost` and `9443`).
* `path` is the root path for a webhook server
  (defaults to no root path).
* `host` is an optional override of the hostname for webhook URLs;
  if not specified, the `addr` will be used.

Kubernetes requires HTTPS, so HTTPS is the default mode of the server.
This webhook server supports SSL both for the server certificates
and for client certificates (e.g., for authentication) at the same time:

* `cadata`, `cafile` is the CA bundle to be passed as a “client config”
  to the webhook configuration objects, to be used by clients/apiservers
  when talking to the webhook server; it is not used in the server itself.
* `cadump` is a path to save the resulting CA bundle to be used
  by clients, i.e. apiservers; it can be passed to `curl --cacert ...`;
  if `cafile` is provided, it contains the same content.
* `certfile`, `pkeyfile` define the server’s endpoint certificate;
  if not specified, a self-signed certificate and CA will be generated
  for both `addr` & `host` as SANs (but only `host` for CommonName).
* `password` is either for decrypting the provided `pkeyfile`,
  or for encrypting and decrypting the generated private key.
* `extra_sans` are put into the self-signed certificate as SANs (DNS/IP)
  in addition to the host & addr (in case some other endpoints exist).
* `verify_mode`, `verify_cafile`, `verify_capath`, `verify_cadata`
  will be loaded into the SSL context for verifying the client certificates
  when provided and if provided by the clients, i.e. apiservers or curl;
  (ssl.SSLContext.verify_mode, ssl.SSLContext.load_verify_locations).
* `insecure` flag disables HTTPS and runs an HTTP webhook server.
  This is used in ngrok for a local endpoint, but can be used for debugging
  or when the certificate-generating dependencies/extras are not installed.

* **Parameters:**
  * **addr** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **port** ([*int*](https://docs.python.org/3/library/functions.html#int) *|* *None*) – 
  * **path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **host** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **cadata** ([*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes) *|* *None*) – 
  * **cafile** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike) *|* *None*) – 
  * **cadump** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike) *|* *None*) – 
  * **context** ([*SSLContext*](https://docs.python.org/3/library/ssl.html#ssl.SSLContext) *|* *None*) – 
  * **insecure** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **certfile** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike) *|* *None*) – 
  * **pkeyfile** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike) *|* *None*) – 
  * **password** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **extra_sans** ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) – 
  * **verify_mode** ([*VerifyMode*](https://docs.python.org/3/library/ssl.html#ssl.VerifyMode) *|* *None*) – 
  * **verify_cafile** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike) *|* *None*) – 
  * **verify_capath** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike) *|* *None*) – 
  * **verify_cadata** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes) *|* *None*) – 

#### DEFAULT_HOST*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

#### addr*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

#### port*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]*

#### path*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

#### host*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

#### cadata*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes)]*

#### cafile*: [`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike), [`None`](https://docs.python.org/3/library/constants.html#None)]*

#### cadump*: [`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike), [`None`](https://docs.python.org/3/library/constants.html#None)]*

#### context*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext)]*

#### insecure*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

#### certfile*: [`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike), [`None`](https://docs.python.org/3/library/constants.html#None)]*

#### pkeyfile*: [`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike), [`None`](https://docs.python.org/3/library/constants.html#None)]*

#### password*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

#### extra_sans*: [`Iterable`](https://docs.python.org/3/library/typing.html#typing.Iterable)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

#### verify_mode*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`VerifyMode`](https://docs.python.org/3/library/ssl.html#ssl.VerifyMode)]*

#### verify_cafile*: [`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike), [`None`](https://docs.python.org/3/library/constants.html#None)]*

#### verify_capath*: [`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike), [`None`](https://docs.python.org/3/library/constants.html#None)]*

#### verify_cadata*: [`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes), [`None`](https://docs.python.org/3/library/constants.html#None)]*

#### *static* build_certificate(hostnames, password=None)

Build a self-signed certificate with SANs (subject alternative names).

Returns a tuple of the certificate and its private key (PEM-formatted).

The certificate is “minimally sufficient”, without much of the extra
information on the subject besides its common and alternative names.
However, IP addresses are properly recognised and normalised for better
compatibility with strict SSL clients (like apiservers of Kubernetes).
The first non-IP hostname becomes the certificate’s common name –
by convention, non-configurable. If no hostnames are found, the first
IP address is used as a fallback. Magic IPs like 0.0.0.0 are excluded.

`certbuilder` is used as an implementation because it is lightweight:
2.9 MB vs. 8.7 MB for cryptography. Still, it is too heavy to include
as a normal runtime dependency (for 8.8 MB of Kopf itself), so it is
only available as the `kopf[dev]` extra for development-mode dependencies.
This can change in the future if self-signed certificates become used
at runtime (e.g. in production/staging environments or other real clusters).

* **Return type:**
  [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes), [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes)]
* **Parameters:**
  * **hostnames** ([*Collection*](https://docs.python.org/3/library/typing.html#typing.Collection)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) – 
  * **password** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 

### *class* kopf.WebhookK3dServer(\*, addr=None, port=None, path=None, host=None, cadata=None, cafile=None, cadump=None, context=None, insecure=False, certfile=None, pkeyfile=None, password=None, extra_sans=(), verify_mode=None, verify_cafile=None, verify_capath=None, verify_cadata=None)

Bases: [`WebhookServer`](#kopf.WebhookServer)

A tunnel from inside of K3d/K3s to its host where the operator is running.

With this tunnel, a developer can develop the webhooks when fully offline,
since all the traffic is local and never leaves the host machine.

The forwarding is maintained by K3d itself. This tunnel only replaces
the endpoints for the Kubernetes webhook and injects an SSL certificate
with proper CN/SANs — to match Kubernetes’s SSL validity expectations.

* **Parameters:**
  * **addr** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **port** ([*int*](https://docs.python.org/3/library/functions.html#int) *|* *None*) – 
  * **path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **host** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **cadata** ([*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes) *|* *None*) – 
  * **cafile** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike) *|* *None*) – 
  * **cadump** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike) *|* *None*) – 
  * **context** ([*SSLContext*](https://docs.python.org/3/library/ssl.html#ssl.SSLContext) *|* *None*) – 
  * **insecure** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **certfile** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike) *|* *None*) – 
  * **pkeyfile** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike) *|* *None*) – 
  * **password** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **extra_sans** ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) – 
  * **verify_mode** ([*VerifyMode*](https://docs.python.org/3/library/ssl.html#ssl.VerifyMode) *|* *None*) – 
  * **verify_cafile** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike) *|* *None*) – 
  * **verify_capath** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike) *|* *None*) – 
  * **verify_cadata** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes) *|* *None*) – 

#### DEFAULT_HOST*: Optional[str]* *= 'host.k3d.internal'*

### *class* kopf.WebhookMinikubeServer(\*, addr=None, port=None, path=None, host=None, cadata=None, cafile=None, cadump=None, context=None, insecure=False, certfile=None, pkeyfile=None, password=None, extra_sans=(), verify_mode=None, verify_cafile=None, verify_capath=None, verify_cadata=None)

Bases: [`WebhookServer`](#kopf.WebhookServer)

A tunnel from inside of Minikube to its host where the operator is running.

With this tunnel, a developer can develop the webhooks when fully offline,
since all the traffic is local and never leaves the host machine.

The forwarding is maintained by Minikube itself. This tunnel only replaces
the endpoints for the Kubernetes webhook and injects an SSL certificate
with proper CN/SANs — to match Kubernetes’s SSL validity expectations.

* **Parameters:**
  * **addr** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **port** ([*int*](https://docs.python.org/3/library/functions.html#int) *|* *None*) – 
  * **path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **host** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **cadata** ([*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes) *|* *None*) – 
  * **cafile** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike) *|* *None*) – 
  * **cadump** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike) *|* *None*) – 
  * **context** ([*SSLContext*](https://docs.python.org/3/library/ssl.html#ssl.SSLContext) *|* *None*) – 
  * **insecure** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **certfile** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike) *|* *None*) – 
  * **pkeyfile** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike) *|* *None*) – 
  * **password** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **extra_sans** ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) – 
  * **verify_mode** ([*VerifyMode*](https://docs.python.org/3/library/ssl.html#ssl.VerifyMode) *|* *None*) – 
  * **verify_cafile** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike) *|* *None*) – 
  * **verify_capath** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike) *|* *None*) – 
  * **verify_cadata** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes) *|* *None*) – 

#### DEFAULT_HOST*: Optional[str]* *= 'host.minikube.internal'*

### *class* kopf.WebhookNgrokTunnel(\*, addr=None, port=None, path=None, token=None, region=None, binary=None)

Bases: `WebhookContextManager`

Tunnel admission webhook request via an external tunnel: [ngrok](https://ngrok.com/).

`addr`, `port`, and `path` have the same meaning as in
kopf.WebhookServer: where to listen for connections locally.
Ngrok then tunnels this endpoint remotely with.

Mind that the ngrok webhook tunnel runs the local webhook server
in an insecure (HTTP) mode. For secure (HTTPS) mode, a paid subscription
and properly issued certificates are needed. This goes beyond Kopf’s scope.
If needed, implement your own ngrok tunnel.

Besides, ngrok tunnel does not report any CA to the webhook client configs.
It is expected that the default trust chain is sufficient for ngrok’s certs.

`token` can be used for paid subscriptions, which lifts some limitations.
Otherwise, the free plan has a limit of 40 requests per minute
(this should be enough for local development).

`binary`, if set, will use the specified `ngrok` binary path;
otherwise, `pyngrok` downloads the binary at runtime (not recommended).

#### WARNING
The public URL is not properly protected and a malicious user
can send requests to a locally running operator. If the handlers
only process the data and make no side effects, this should be fine.

Despite ngrok provides basic auth (“username:password”),
Kubernetes does not permit this information in the URLs.

Ngrok partially “protects” the URLS by assigning them random hostnames.
Additionally, you can add random paths. However, this is not “security”,
only a bit of safety for a short time (enough for development runs).

* **Parameters:**
  * **addr** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **port** ([*int*](https://docs.python.org/3/library/functions.html#int) *|* *None*) – 
  * **path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **token** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **region** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **binary** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike) *|* *None*) – 

#### addr*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

#### port*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]*

#### path*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

#### token*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

#### region*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

#### binary*: [`Union`](https://docs.python.org/3/library/typing.html#typing.Union)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike), [`None`](https://docs.python.org/3/library/constants.html#None)]*

### *class* kopf.WebhookAutoServer(\*, addr=None, port=None, path=None, host=None, cadata=None, cafile=None, cadump=None, context=None, insecure=False, certfile=None, pkeyfile=None, password=None, extra_sans=(), verify_mode=None, verify_cafile=None, verify_capath=None, verify_cadata=None)

Bases: `ClusterDetector`, [`WebhookServer`](#kopf.WebhookServer)

A locally listening webserver which attempts to guess its proper hostname.

The choice is happening between supported webhook servers only
(K3d/K3d and Minikube at the moment). In all other cases,
a regular local server is started without hostname overrides.

If automatic tunneling is possible, consider WebhookAutoTunnel instead.

* **Parameters:**
  * **addr** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **port** ([*int*](https://docs.python.org/3/library/functions.html#int) *|* *None*) – 
  * **path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **host** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **cadata** ([*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes) *|* *None*) – 
  * **cafile** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike) *|* *None*) – 
  * **cadump** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike) *|* *None*) – 
  * **context** ([*SSLContext*](https://docs.python.org/3/library/ssl.html#ssl.SSLContext) *|* *None*) – 
  * **insecure** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **certfile** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike) *|* *None*) – 
  * **pkeyfile** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike) *|* *None*) – 
  * **password** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **extra_sans** ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) – 
  * **verify_mode** ([*VerifyMode*](https://docs.python.org/3/library/ssl.html#ssl.VerifyMode) *|* *None*) – 
  * **verify_cafile** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike) *|* *None*) – 
  * **verify_capath** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*PathLike*](https://docs.python.org/3/library/os.html#os.PathLike) *|* *None*) – 
  * **verify_cadata** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*bytes*](https://docs.python.org/3/library/stdtypes.html#bytes) *|* *None*) – 

### *class* kopf.WebhookAutoTunnel(\*, addr=None, port=None, path=None)

Bases: `ClusterDetector`, `WebhookContextManager`

The same as WebhookAutoServer, but with possible tunneling.

Generally, tunneling gives more possibilities to run in any environment,
but it must not happen without a permission from the developers,
and is not possible if running in a completely isolated/local/CI/CD cluster.
Therefore, developers should activated automatic setup explicitly.

If automatic tunneling is prohibited or impossible, use WebhookAutoServer.

#### NOTE
Automatic server/tunnel detection is highly limited in configuration
and provides only the most common options of all servers & tunners:
specifically, listening `addr:port/path`.
All other options are specific to their servers/tunnels
and the auto-guessing logic cannot use/accept/pass them.

* **Parameters:**
  * **addr** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **port** ([*int*](https://docs.python.org/3/library/functions.html#int) *|* *None*) – 
  * **path** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 

#### addr*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

#### port*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]*

#### path*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

### *exception* kopf.PermanentError

Bases: [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception)

A fatal handler error, the retries are useless.

### *exception* kopf.TemporaryError(\_TemporaryError_\_msg=None, delay=60)

Bases: [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception)

A potentially recoverable error, should be retried.

* **Parameters:**
  * **\_TemporaryError_\_msg** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **delay** ([*float*](https://docs.python.org/3/library/functions.html#float) *|* *None*) – 
* **Return type:**
  None

### *exception* kopf.HandlerTimeoutError

Bases: [`PermanentError`](#kopf.PermanentError)

An error for the handler’s timeout (if set).

### *exception* kopf.HandlerRetriesError

Bases: [`PermanentError`](#kopf.PermanentError)

An error for the handler’s retries exceeded (if set).

### *class* kopf.OperatorRegistry

Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

A global registry is used for handling of multiple resources & activities.

It is usually populated by the `@kopf.on...` decorators, but can also
be explicitly created and used in the embedded operators.

### kopf.get_default_registry()

Get the default registry to be used by the decorators and the reactor
unless the explicit registry is provided to them.

* **Return type:**
  [`OperatorRegistry`](#kopf.OperatorRegistry)

### kopf.set_default_registry(registry)

Set the default registry to be used by the decorators and the reactor
unless the explicit registry is provided to them.

* **Return type:**
  [`None`](https://docs.python.org/3/library/constants.html#None)
* **Parameters:**
  **registry** ([*OperatorRegistry*](#kopf.OperatorRegistry)) – 

### *class* kopf.OperatorSettings(process=<factory>, posting=<factory>, peering=<factory>, watching=<factory>, batching=<factory>, scanning=<factory>, admission=<factory>, execution=<factory>, background=<factory>, networking=<factory>, persistence=<factory>)

Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

* **Parameters:**
  * **process** (*ProcessSettings*) – 
  * **posting** (*PostingSettings*) – 
  * **peering** (*PeeringSettings*) – 
  * **watching** (*WatchingSettings*) – 
  * **batching** (*BatchingSettings*) – 
  * **scanning** (*ScanningSettings*) – 
  * **admission** (*AdmissionSettings*) – 
  * **execution** (*ExecutionSettings*) – 
  * **background** (*BackgroundSettings*) – 
  * **networking** (*NetworkingSettings*) – 
  * **persistence** (*PersistenceSettings*) – 

#### process*: `ProcessSettings`*

#### posting*: `PostingSettings`*

#### peering*: `PeeringSettings`*

#### watching*: `WatchingSettings`*

#### batching*: `BatchingSettings`*

#### scanning*: `ScanningSettings`*

#### admission*: `AdmissionSettings`*

#### execution*: `ExecutionSettings`*

#### background*: `BackgroundSettings`*

#### networking*: `NetworkingSettings`*

#### persistence*: `PersistenceSettings`*

### *class* kopf.DiffBaseStorage

Bases: `StorageKeyMarkingConvention`, `StorageStanzaCleaner`

Store the base essence for diff calculations, i.e. last handled state.

The “essence” is a snapshot of meaningful fields, which must be tracked
to identify the actual changes on the object (or absence of such).

Used in the handling routines to check if there were significant changes
(i.e. not the internal and system changes, like the uids, links, etc),
and to get the exact per-field diffs for the specific handler functions.

Conceptually similar to how `kubectl apply` stores the applied state
on any object, and then uses that for the patch calculation:
[https://kubernetes.io/docs/concepts/overview/object-management-kubectl/declarative-config/](https://kubernetes.io/docs/concepts/overview/object-management-kubectl/declarative-config/)

#### build(\*, body, extra_fields=None)

Extract only the relevant fields for the state comparisons.

The framework ignores all the system fields (mostly from metadata)
and the status senza completely. Except for some well-known and useful
metadata, such as labels and annotations (except for sure garbage).

A special set of fields can be provided even if they are supposed
to be removed. This is used, for example, for handlers which react
to changes in the specific fields in the status stanza,
while the rest of the status stanza is removed.

It is generally not a good idea to override this method in custom
stores, unless a different definition of an object’s essence is needed.

* **Return type:**
  [`BodyEssence`](#kopf.BodyEssence)
* **Parameters:**
  * **body** ([*Body*](#kopf.Body)) – 
  * **extra_fields** ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable)*[**None* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* *...**]* *|* [*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]**]* *|* *None*) – 

#### *abstract* fetch(\*, body)

* **Return type:**
  [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BodyEssence`](#kopf.BodyEssence)]
* **Parameters:**
  **body** ([*Body*](#kopf.Body)) – 

#### *abstract* store(\*, body, patch, essence)

* **Return type:**
  [`None`](https://docs.python.org/3/library/constants.html#None)
* **Parameters:**
  * **body** ([*Body*](#kopf.Body)) – 
  * **patch** ([*Patch*](#kopf.Patch)) – 
  * **essence** ([*BodyEssence*](#kopf.BodyEssence)) – 

### *class* kopf.AnnotationsDiffBaseStorage(\*, prefix='kopf.zalando.org', key='last-handled-configuration', v1=True)

Bases: `StorageKeyFormingConvention`, [`DiffBaseStorage`](#kopf.DiffBaseStorage)

* **Parameters:**
  * **prefix** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **v1** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 

#### build(\*, body, extra_fields=None)

Extract only the relevant fields for the state comparisons.

The framework ignores all the system fields (mostly from metadata)
and the status senza completely. Except for some well-known and useful
metadata, such as labels and annotations (except for sure garbage).

A special set of fields can be provided even if they are supposed
to be removed. This is used, for example, for handlers which react
to changes in the specific fields in the status stanza,
while the rest of the status stanza is removed.

It is generally not a good idea to override this method in custom
stores, unless a different definition of an object’s essence is needed.

* **Return type:**
  [`BodyEssence`](#kopf.BodyEssence)
* **Parameters:**
  * **body** ([*Body*](#kopf.Body)) – 
  * **extra_fields** ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable)*[**None* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* *...**]* *|* [*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]**]* *|* *None*) – 

#### fetch(\*, body)

* **Return type:**
  [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BodyEssence`](#kopf.BodyEssence)]
* **Parameters:**
  **body** ([*Body*](#kopf.Body)) – 

#### store(\*, body, patch, essence)

* **Return type:**
  [`None`](https://docs.python.org/3/library/constants.html#None)
* **Parameters:**
  * **body** ([*Body*](#kopf.Body)) – 
  * **patch** ([*Patch*](#kopf.Patch)) – 
  * **essence** ([*BodyEssence*](#kopf.BodyEssence)) – 

### *class* kopf.StatusDiffBaseStorage(\*, name='kopf', field='status.{name}.last-handled-configuration')

Bases: [`DiffBaseStorage`](#kopf.DiffBaseStorage)

* **Parameters:**
  * **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **field** (*None* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* *...**]* *|* [*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) – 

#### *property* field*: [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple)[[str](https://docs.python.org/3/library/stdtypes.html#str), ...]*

#### build(\*, body, extra_fields=None)

Extract only the relevant fields for the state comparisons.

The framework ignores all the system fields (mostly from metadata)
and the status senza completely. Except for some well-known and useful
metadata, such as labels and annotations (except for sure garbage).

A special set of fields can be provided even if they are supposed
to be removed. This is used, for example, for handlers which react
to changes in the specific fields in the status stanza,
while the rest of the status stanza is removed.

It is generally not a good idea to override this method in custom
stores, unless a different definition of an object’s essence is needed.

* **Return type:**
  [`BodyEssence`](#kopf.BodyEssence)
* **Parameters:**
  * **body** ([*Body*](#kopf.Body)) – 
  * **extra_fields** ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable)*[**None* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* *...**]* *|* [*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]**]* *|* *None*) – 

#### fetch(\*, body)

* **Return type:**
  [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BodyEssence`](#kopf.BodyEssence)]
* **Parameters:**
  **body** ([*Body*](#kopf.Body)) – 

#### store(\*, body, patch, essence)

* **Return type:**
  [`None`](https://docs.python.org/3/library/constants.html#None)
* **Parameters:**
  * **body** ([*Body*](#kopf.Body)) – 
  * **patch** ([*Patch*](#kopf.Patch)) – 
  * **essence** ([*BodyEssence*](#kopf.BodyEssence)) – 

### *class* kopf.MultiDiffBaseStorage(storages)

Bases: [`DiffBaseStorage`](#kopf.DiffBaseStorage)

* **Parameters:**
  **storages** ([*Collection*](https://docs.python.org/3/library/typing.html#typing.Collection)*[*[*DiffBaseStorage*](#kopf.DiffBaseStorage)*]*) – 

#### build(\*, body, extra_fields=None)

Extract only the relevant fields for the state comparisons.

The framework ignores all the system fields (mostly from metadata)
and the status senza completely. Except for some well-known and useful
metadata, such as labels and annotations (except for sure garbage).

A special set of fields can be provided even if they are supposed
to be removed. This is used, for example, for handlers which react
to changes in the specific fields in the status stanza,
while the rest of the status stanza is removed.

It is generally not a good idea to override this method in custom
stores, unless a different definition of an object’s essence is needed.

* **Return type:**
  [`BodyEssence`](#kopf.BodyEssence)
* **Parameters:**
  * **body** ([*Body*](#kopf.Body)) – 
  * **extra_fields** ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable)*[**None* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* *...**]* *|* [*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]**]* *|* *None*) – 

#### fetch(\*, body)

* **Return type:**
  [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`BodyEssence`](#kopf.BodyEssence)]
* **Parameters:**
  **body** ([*Body*](#kopf.Body)) – 

#### store(\*, body, patch, essence)

* **Return type:**
  [`None`](https://docs.python.org/3/library/constants.html#None)
* **Parameters:**
  * **body** ([*Body*](#kopf.Body)) – 
  * **patch** ([*Patch*](#kopf.Patch)) – 
  * **essence** ([*BodyEssence*](#kopf.BodyEssence)) – 

### *class* kopf.ProgressRecord

Bases: `TypedDict`

A single record stored for persistence of a single handler.

#### started*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

#### stopped*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

#### delayed*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

#### purpose*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

#### retries*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`int`](https://docs.python.org/3/library/functions.html#int)]*

#### success*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]*

#### failure*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]*

#### message*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

#### subrefs*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`Collection`](https://docs.python.org/3/library/typing.html#typing.Collection)[[`NewType`](https://docs.python.org/3/library/typing.html#typing.NewType)(`HandlerId`, [`str`](https://docs.python.org/3/library/stdtypes.html#str))]]*

### *class* kopf.ProgressStorage

Bases: `StorageStanzaCleaner`

Base class and an interface for all persistent states.

The state is persisted strict per-handler, not for all handlers at once:
to support overlapping operators (assuming different handler ids) storing
their state on the same fields of the resource (e.g. `state.kopf`).

This also ensures that no extra logic for state merges will be needed:
the handler states are atomic (i.e. state fields are not used separately)
but independent: i.e. handlers should be persisted on their own, unrelated
to other handlers; i.e. never combined to other atomic structures.

If combining is still needed with performance optimization in mind (e.g.
for relational/transactional databases), the keys can be cached in memory
for short time, and `flush()` can be overridden to actually store them.

#### *abstract* fetch(\*, key, body)

* **Return type:**
  [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ProgressRecord`](#kopf.ProgressRecord)]
* **Parameters:**
  * **key** (*HandlerId*) – 
  * **body** ([*Body*](#kopf.Body)) – 

#### *abstract* store(\*, key, record, body, patch)

* **Return type:**
  [`None`](https://docs.python.org/3/library/constants.html#None)
* **Parameters:**
  * **key** (*HandlerId*) – 
  * **record** ([*ProgressRecord*](#kopf.ProgressRecord)) – 
  * **body** ([*Body*](#kopf.Body)) – 
  * **patch** ([*Patch*](#kopf.Patch)) – 

#### *abstract* purge(\*, key, body, patch)

* **Return type:**
  [`None`](https://docs.python.org/3/library/constants.html#None)
* **Parameters:**
  * **key** (*HandlerId*) – 
  * **body** ([*Body*](#kopf.Body)) – 
  * **patch** ([*Patch*](#kopf.Patch)) – 

#### *abstract* touch(\*, body, patch, value)

* **Return type:**
  [`None`](https://docs.python.org/3/library/constants.html#None)
* **Parameters:**
  * **body** ([*Body*](#kopf.Body)) – 
  * **patch** ([*Patch*](#kopf.Patch)) – 
  * **value** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 

#### *abstract* clear(\*, essence)

* **Return type:**
  [`BodyEssence`](#kopf.BodyEssence)
* **Parameters:**
  **essence** ([*BodyEssence*](#kopf.BodyEssence)) – 

#### flush()

* **Return type:**
  [`None`](https://docs.python.org/3/library/constants.html#None)

### *class* kopf.AnnotationsProgressStorage(\*, prefix='kopf.zalando.org', verbose=False, touch_key='touch-dummy', v1=True)

Bases: `StorageKeyFormingConvention`, `StorageKeyMarkingConvention`, [`ProgressStorage`](#kopf.ProgressStorage)

State storage in `.metadata.annotations` with JSON-serialised content.

An example without a prefix:

<!-- code-block: yaml

metadata:
  annotations:
    create_fn_1: '{"started": "2020-02-14T16:58:25.396364", "stopped":
                   "2020-02-14T16:58:25.401844", "retries": 1, "success": true}'
    create_fn_2: '{"started": "2020-02-14T16:58:25.396421", "retries": 0}'
spec: ...
status: ... -->

An example with a prefix:

<!-- code-block: yaml

metadata:
  annotations:
    kopf.zalando.org/create_fn_1: '{"started": "2020-02-14T16:58:25.396364", "stopped":
                            "2020-02-14T16:58:25.401844", "retries": 1, "success": true}'
    kopf.zalando.org/create_fn_2: '{"started": "2020-02-14T16:58:25.396421", "retries": 0}'
spec: ...
status: ... -->

For the annotations’ naming conventions, hashing, and V1 & V2 differences,
see `AnnotationsNamingMixin`.

* **Parameters:**
  * **prefix** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **verbose** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **touch_key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **v1** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 

#### fetch(\*, key, body)

* **Return type:**
  [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ProgressRecord`](#kopf.ProgressRecord)]
* **Parameters:**
  * **key** (*HandlerId*) – 
  * **body** ([*Body*](#kopf.Body)) – 

#### store(\*, key, record, body, patch)

* **Return type:**
  [`None`](https://docs.python.org/3/library/constants.html#None)
* **Parameters:**
  * **key** (*HandlerId*) – 
  * **record** ([*ProgressRecord*](#kopf.ProgressRecord)) – 
  * **body** ([*Body*](#kopf.Body)) – 
  * **patch** ([*Patch*](#kopf.Patch)) – 

#### purge(\*, key, body, patch)

* **Return type:**
  [`None`](https://docs.python.org/3/library/constants.html#None)
* **Parameters:**
  * **key** (*HandlerId*) – 
  * **body** ([*Body*](#kopf.Body)) – 
  * **patch** ([*Patch*](#kopf.Patch)) – 

#### touch(\*, body, patch, value)

* **Return type:**
  [`None`](https://docs.python.org/3/library/constants.html#None)
* **Parameters:**
  * **body** ([*Body*](#kopf.Body)) – 
  * **patch** ([*Patch*](#kopf.Patch)) – 
  * **value** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 

#### clear(\*, essence)

* **Return type:**
  [`BodyEssence`](#kopf.BodyEssence)
* **Parameters:**
  **essence** ([*BodyEssence*](#kopf.BodyEssence)) – 

### *class* kopf.StatusProgressStorage(\*, name='kopf', field='status.{name}.progress', touch_field='status.{name}.dummy')

Bases: [`ProgressStorage`](#kopf.ProgressStorage)

State storage in `.status` stanza with deep structure.

The structure is this:

<!-- code-block: yaml

metadata: ...
spec: ...
status: ...
    kopf:
        progress:
            handler1:
                started: 2018-12-31T23:59:59,999999
                stopped: 2018-01-01T12:34:56,789000
                success: true
            handler2:
                started: 2018-12-31T23:59:59,999999
                stopped: 2018-01-01T12:34:56,789000
                failure: true
                message: "Error message."
            handler3:
                started: 2018-12-31T23:59:59,999999
                retries: 30
            handler3/sub1:
                started: 2018-12-31T23:59:59,999999
                delayed: 2018-01-01T12:34:56,789000
                retries: 10
                message: "Not ready yet."
            handler3/sub2:
                started: 2018-12-31T23:59:59,999999 -->
* **Parameters:**
  * **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **field** (*None* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* *...**]* *|* [*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) – 
  * **touch_field** (*None* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* *...**]* *|* [*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) – 

#### *property* field*: [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple)[[str](https://docs.python.org/3/library/stdtypes.html#str), ...]*

#### *property* touch_field*: [Tuple](https://docs.python.org/3/library/typing.html#typing.Tuple)[[str](https://docs.python.org/3/library/stdtypes.html#str), ...]*

#### fetch(\*, key, body)

* **Return type:**
  [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ProgressRecord`](#kopf.ProgressRecord)]
* **Parameters:**
  * **key** (*HandlerId*) – 
  * **body** ([*Body*](#kopf.Body)) – 

#### store(\*, key, record, body, patch)

* **Return type:**
  [`None`](https://docs.python.org/3/library/constants.html#None)
* **Parameters:**
  * **key** (*HandlerId*) – 
  * **record** ([*ProgressRecord*](#kopf.ProgressRecord)) – 
  * **body** ([*Body*](#kopf.Body)) – 
  * **patch** ([*Patch*](#kopf.Patch)) – 

#### purge(\*, key, body, patch)

* **Return type:**
  [`None`](https://docs.python.org/3/library/constants.html#None)
* **Parameters:**
  * **key** (*HandlerId*) – 
  * **body** ([*Body*](#kopf.Body)) – 
  * **patch** ([*Patch*](#kopf.Patch)) – 

#### touch(\*, body, patch, value)

* **Return type:**
  [`None`](https://docs.python.org/3/library/constants.html#None)
* **Parameters:**
  * **body** ([*Body*](#kopf.Body)) – 
  * **patch** ([*Patch*](#kopf.Patch)) – 
  * **value** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 

#### clear(\*, essence)

* **Return type:**
  [`BodyEssence`](#kopf.BodyEssence)
* **Parameters:**
  **essence** ([*BodyEssence*](#kopf.BodyEssence)) – 

### *class* kopf.MultiProgressStorage(storages)

Bases: [`ProgressStorage`](#kopf.ProgressStorage)

* **Parameters:**
  **storages** ([*Collection*](https://docs.python.org/3/library/typing.html#typing.Collection)*[*[*ProgressStorage*](#kopf.ProgressStorage)*]*) – 

#### fetch(\*, key, body)

* **Return type:**
  [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`ProgressRecord`](#kopf.ProgressRecord)]
* **Parameters:**
  * **key** (*HandlerId*) – 
  * **body** ([*Body*](#kopf.Body)) – 

#### store(\*, key, record, body, patch)

* **Return type:**
  [`None`](https://docs.python.org/3/library/constants.html#None)
* **Parameters:**
  * **key** (*HandlerId*) – 
  * **record** ([*ProgressRecord*](#kopf.ProgressRecord)) – 
  * **body** ([*Body*](#kopf.Body)) – 
  * **patch** ([*Patch*](#kopf.Patch)) – 

#### purge(\*, key, body, patch)

* **Return type:**
  [`None`](https://docs.python.org/3/library/constants.html#None)
* **Parameters:**
  * **key** (*HandlerId*) – 
  * **body** ([*Body*](#kopf.Body)) – 
  * **patch** ([*Patch*](#kopf.Patch)) – 

#### touch(\*, body, patch, value)

* **Return type:**
  [`None`](https://docs.python.org/3/library/constants.html#None)
* **Parameters:**
  * **body** ([*Body*](#kopf.Body)) – 
  * **patch** ([*Patch*](#kopf.Patch)) – 
  * **value** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 

#### clear(\*, essence)

* **Return type:**
  [`BodyEssence`](#kopf.BodyEssence)
* **Parameters:**
  **essence** ([*BodyEssence*](#kopf.BodyEssence)) – 

### *class* kopf.SmartProgressStorage(\*, name='kopf', field='status.{name}.progress', touch_key='touch-dummy', touch_field='status.{name}.dummy', prefix='kopf.zalando.org', v1=True, verbose=False)

Bases: [`MultiProgressStorage`](#kopf.MultiProgressStorage)

* **Parameters:**
  * **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **field** (*None* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* *...**]* *|* [*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) – 
  * **touch_key** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **touch_field** (*None* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* [*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* *...**]* *|* [*List*](https://docs.python.org/3/library/typing.html#typing.List)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) – 
  * **prefix** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **v1** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **verbose** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 

### *class* kopf.RawEvent

Bases: `TypedDict`

#### type*: [`Literal`](https://docs.python.org/3/library/typing.html#typing.Literal)[`None`, `'ADDED'`, `'MODIFIED'`, `'DELETED'`]*

#### object*: [`RawBody`](#kopf.RawBody)*

### *class* kopf.RawBody

Bases: `TypedDict`

#### apiVersion*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### kind*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### metadata*: `RawMeta`*

#### spec*: [`Mapping`](https://docs.python.org/3/library/typing.html#typing.Mapping)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)]*

#### status*: [`Mapping`](https://docs.python.org/3/library/typing.html#typing.Mapping)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)]*

### *class* kopf.Status(\_Status_\_src)

Bases: `MappingView`[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)]

* **Parameters:**
  **\_Status_\_src** ([*Body*](#kopf.Body)) – 

### *class* kopf.Spec(\_Spec_\_src)

Bases: `MappingView`[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)]

* **Parameters:**
  **\_Spec_\_src** ([*Body*](#kopf.Body)) – 

### *class* kopf.Meta(\_Meta_\_src)

Bases: `MappingView`[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)]

* **Parameters:**
  **\_Meta_\_src** ([*Body*](#kopf.Body)) – 

#### *property* labels*: [Mapping](https://docs.python.org/3/library/typing.html#typing.Mapping)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)]*

#### *property* annotations*: [Mapping](https://docs.python.org/3/library/typing.html#typing.Mapping)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str)]*

#### *property* uid*: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

#### *property* name*: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

#### *property* namespace*: NamespaceName | [None](https://docs.python.org/3/library/constants.html#None)*

#### *property* creation_timestamp*: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

#### *property* deletion_timestamp*: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

### *class* kopf.Body(\_Body_\_src)

Bases: `ReplaceableMappingView`[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)]

* **Parameters:**
  **\_Body_\_src** ([*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*]*) – 

#### *property* metadata*: [Meta](#kopf.Meta)*

#### *property* meta*: [Meta](#kopf.Meta)*

#### *property* spec*: [Spec](#kopf.Spec)*

#### *property* status*: [Status](#kopf.Status)*

### *class* kopf.BodyEssence

Bases: `TypedDict`

#### metadata*: `MetaEssence`*

#### spec*: [`Mapping`](https://docs.python.org/3/library/typing.html#typing.Mapping)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)]*

#### status*: [`Mapping`](https://docs.python.org/3/library/typing.html#typing.Mapping)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)]*

### *class* kopf.ObjectReference

Bases: `TypedDict`

#### apiVersion*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### kind*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### namespace*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]*

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### uid*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

### *class* kopf.OwnerReference

Bases: `TypedDict`

#### controller*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

#### blockOwnerDeletion*: [`bool`](https://docs.python.org/3/library/functions.html#bool)*

#### apiVersion*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### kind*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### name*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

#### uid*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

### *class* kopf.Memo

Bases: [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`Any`](https://docs.python.org/3/library/typing.html#typing.Any), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)]

A container to hold arbitrary keys-values assigned by operator developers.

It is used in the [`memo`](../kwargs.md#std-kwarg-memo) kwarg to all resource handlers, isolated
per individual resource object (not the resource kind).

The values can be accessed either as dictionary keys (the memo is a `dict`
under the hood) or as object attributes (except for methods of `dict`).

See more in [In-memory containers](../memos.md).

```pycon
>>> memo = Memo()
```

```pycon
>>> memo.f1 = 100
>>> memo['f1']
... 100
```

```pycon
>>> memo['f2'] = 200
>>> memo.f2
... 200
```

```pycon
>>> set(memo.keys())
... {'f1', 'f2'}
```

### *class* kopf.Index

Bases: [`Mapping`](https://docs.python.org/3/library/typing.html#typing.Mapping)[`_K`, [`Store`](#kopf.Store)[`_V`]], [`Generic`](https://docs.python.org/3/library/typing.html#typing.Generic)[`_K`, `_V`]

A mapping of index keys to collections of values indexed under those keys.

A single index is identified by a handler id and is populated by values
usually from a single indexing function (the `@kopf.index()` decorator).

#### NOTE
This class is only an abstract interface of an index.
The actual implementation is in .indexing.Index.

<!-- seealso:
:doc:`/indexing`. -->

### *class* kopf.Store

Bases: [`Collection`](https://docs.python.org/3/library/typing.html#typing.Collection)[`_V`], [`Generic`](https://docs.python.org/3/library/typing.html#typing.Generic)[`_V`]

A collection of all values under a single unique index key.

Multiple objects can yield the same keys, so all their values
are accumulated into collections. When an object is deleted
or stops matching the filters, all associated values are discarded.

The order of values is not guaranteed.

The values are not deduplicated, so duplicates are possible if multiple
objects return the same values from their indexing functions.

#### NOTE
This class is only an abstract interface of an indexed store.
The actual implementation is in .indexing.Store.

<!-- seealso:
:doc:`/indexing`. -->

### *class* kopf.ObjectLogger(\*, body, settings)

Bases: [`LoggerAdapter`](https://docs.python.org/3/library/logging.html#logging.LoggerAdapter)

A logger/adapter to carry the object identifiers for formatting.

The identifiers are then used both for formatting the per-object messages
in ObjectPrefixingFormatter, and when posting the per-object k8s-events.

Constructed in event handling of each individual object.

The internal structure is made the same as an object reference in K8s API,
but can change over time to anything needed for our internal purposes.
However, as little information should be carried as possible,
and the information should be protected against the object modification
(e.g. in case of background posting via the queue; see K8sPoster).

* **Parameters:**
  * **body** ([*Body*](#kopf.Body)) – 
  * **settings** ([*OperatorSettings*](#kopf.OperatorSettings)) – 

#### process(msg, kwargs)

Process the logging message and keyword arguments passed in to
a logging call to insert contextual information. You can either
manipulate the message itself, the keyword args or both. Return
the message and kwargs modified (or not) to suit your needs.

Normally, you’ll only need to override this one method in a
LoggerAdapter subclass for your specific needs.

* **Return type:**
  [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`MutableMapping`](https://docs.python.org/3/library/typing.html#typing.MutableMapping)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)]]
* **Parameters:**
  * **msg** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **kwargs** ([*MutableMapping*](https://docs.python.org/3/library/typing.html#typing.MutableMapping)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*]*) – 

### *class* kopf.LocalObjectLogger(\*, body, settings)

Bases: [`ObjectLogger`](#kopf.ObjectLogger)

The same as ObjectLogger, but does not post the messages as k8s-events.

Used in the resource-watching handlers to log the handler’s invocation
successes/failures without overloading K8s with excessively many k8s-events.

This class is used internally only and is not exposed publicly in any way.

* **Parameters:**
  * **body** ([*Body*](#kopf.Body)) – 
  * **settings** ([*OperatorSettings*](#kopf.OperatorSettings)) – 

#### log(\*args, \*\*kwargs)

Delegate a log call to the underlying logger, after adding
contextual information from this adapter instance.

* **Return type:**
  [`None`](https://docs.python.org/3/library/constants.html#None)
* **Parameters:**
  * **args** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any)) – 
  * **kwargs** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any)) – 

### *class* kopf.Diff(\_Diff_\_items)

Bases: [`Sequence`](https://docs.python.org/3/library/typing.html#typing.Sequence)[[`DiffItem`](#kopf.DiffItem)]

* **Parameters:**
  **\_Diff_\_items** ([*Iterable*](https://docs.python.org/3/library/typing.html#typing.Iterable)*[*[*DiffItem*](#kopf.DiffItem)*]*) – 

### *class* kopf.DiffItem(operation, field, old, new)

Bases: [`NamedTuple`](https://docs.python.org/3/library/typing.html#typing.NamedTuple)

* **Parameters:**
  * **operation** ([*DiffOperation*](#kopf.DiffOperation)) – 
  * **field** ([*Tuple*](https://docs.python.org/3/library/typing.html#typing.Tuple)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* *...**]*) – 
  * **old** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any)) – 
  * **new** ([*Any*](https://docs.python.org/3/library/typing.html#typing.Any)) – 

#### operation*: [`DiffOperation`](#kopf.DiffOperation)*

Alias for field number 0

#### field*: [`Tuple`](https://docs.python.org/3/library/typing.html#typing.Tuple)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`...`](https://docs.python.org/3/library/constants.html#Ellipsis)]*

Alias for field number 1

#### old*: [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)*

Alias for field number 2

#### new*: [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)*

Alias for field number 3

#### *property* op*: [DiffOperation](#kopf.DiffOperation)*

### *class* kopf.DiffOperation(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

#### ADD *= 'add'*

#### CHANGE *= 'change'*

#### REMOVE *= 'remove'*

### *class* kopf.Reason(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Bases: [`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum)

#### CREATE *= 'create'*

#### UPDATE *= 'update'*

#### DELETE *= 'delete'*

#### RESUME *= 'resume'*

#### NOOP *= 'noop'*

#### FREE *= 'free'*

#### GONE *= 'gone'*

### *class* kopf.Patch(\_Patch_\_src=None, body=None)

Bases: [`Dict`](https://docs.python.org/3/library/typing.html#typing.Dict)[[`str`](https://docs.python.org/3/library/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)]

* **Parameters:**
  * **\_Patch_\_src** ([*MutableMapping*](https://docs.python.org/3/library/typing.html#typing.MutableMapping)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* [*Any*](https://docs.python.org/3/library/typing.html#typing.Any)*]* *|* *None*) – 
  * **body** ([*RawBody*](#kopf.RawBody) *|* *None*) – 

#### *property* metadata*: MetaPatch*

#### *property* meta*: MetaPatch*

#### *property* spec*: SpecPatch*

#### *property* status*: StatusPatch*

#### as_json_patch()

* **Return type:**
  [`List`](https://docs.python.org/3/library/typing.html#typing.List)[`JSONPatchItem`]

### *class* kopf.DaemonStoppingReason(value, names=None, \*, module=None, qualname=None, type=None, start=1, boundary=None)

Bases: [`Flag`](https://docs.python.org/3/library/enum.html#enum.Flag)

A reason or reasons of daemon being terminated.

Daemons are signalled to exit usually for two reasons: the operator itself
is exiting or restarting, so all daemons of all resources must stop;
or the individual resource was deleted, but the operator continues running.

No matter the reason, the daemons must exit, so one and only one stop-flag
is used. Some daemons can check the reason of exiting if it is important.

There can be multiple reasons combined (in rare cases, all of them).

#### DONE *= 1*

#### FILTERS_MISMATCH *= 2*

#### RESOURCE_DELETED *= 4*

#### OPERATOR_PAUSING *= 8*

#### OPERATOR_EXITING *= 16*

#### DAEMON_SIGNALLED *= 32*

#### DAEMON_CANCELLED *= 64*

#### DAEMON_ABANDONED *= 128*

### *class* kopf.Resource(group, version, plural, kind=None, singular=None, shortcuts=frozenset({}), categories=frozenset({}), subresources=frozenset({}), namespaced=None, preferred=True, verbs=frozenset({}))

Bases: [`object`](https://docs.python.org/3/library/functions.html#object)

A reference to a very specific custom or built-in resource kind.

It is used to form the K8s API URLs. Generally, K8s API only needs
an API group, an API version, and a plural name of the resource.
All other names are remembered to match against resource selectors,
for logging, and for informational purposes.

* **Parameters:**
  * **group** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **version** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **plural** ([*str*](https://docs.python.org/3/library/stdtypes.html#str)) – 
  * **kind** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **singular** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **shortcuts** ([*FrozenSet*](https://docs.python.org/3/library/typing.html#typing.FrozenSet)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) – 
  * **categories** ([*FrozenSet*](https://docs.python.org/3/library/typing.html#typing.FrozenSet)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) – 
  * **subresources** ([*FrozenSet*](https://docs.python.org/3/library/typing.html#typing.FrozenSet)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) – 
  * **namespaced** ([*bool*](https://docs.python.org/3/library/functions.html#bool) *|* *None*) – 
  * **preferred** ([*bool*](https://docs.python.org/3/library/functions.html#bool)) – 
  * **verbs** ([*FrozenSet*](https://docs.python.org/3/library/typing.html#typing.FrozenSet)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*]*) – 

#### group*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The resource’s API group; e.g. `"kopf.dev"`, `"apps"`, `"batch"`.
For Core v1 API resources, an empty string: `""`.

#### version*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The resource’s API version; e.g. `"v1"`, `"v1beta1"`, etc.

#### plural*: [`str`](https://docs.python.org/3/library/stdtypes.html#str)*

The resource’s plural name; e.g. `"pods"`, `"kopfexamples"`.
It is used as an API endpoint, together with API group & version.

#### kind*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

The resource’s kind (as in YAML files); e.g. `"Pod"`, `"KopfExample"`.

#### singular*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= None*

The resource’s singular name; e.g. `"pod"`, `"kopfexample"`.

#### shortcuts*: [`FrozenSet`](https://docs.python.org/3/library/typing.html#typing.FrozenSet)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= frozenset({})*

The resource’s short names; e.g. `{"po"}`, `{"kex", "kexes"}`.

#### categories*: [`FrozenSet`](https://docs.python.org/3/library/typing.html#typing.FrozenSet)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= frozenset({})*

The resource’s categories, to which the resource belongs; e.g. `{"all"}`.

#### subresources*: [`FrozenSet`](https://docs.python.org/3/library/typing.html#typing.FrozenSet)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= frozenset({})*

The resource’s subresources, if defined; e.g. `{"status", "scale"}`.

#### namespaced*: [`Optional`](https://docs.python.org/3/library/typing.html#typing.Optional)[[`bool`](https://docs.python.org/3/library/functions.html#bool)]* *= None*

Whether the resource is namespaced (`True`) or cluster-scoped (`False`).

#### preferred*: [`bool`](https://docs.python.org/3/library/functions.html#bool)* *= True*

Whether the resource belong to a “preferred” API version.
Only “preferred” resources are served when the version is not specified.

#### verbs*: [`FrozenSet`](https://docs.python.org/3/library/typing.html#typing.FrozenSet)[[`str`](https://docs.python.org/3/library/stdtypes.html#str)]* *= frozenset({})*

All available verbs for the resource, as supported by K8s API;
e.g., `{"list", "watch", "create", "update", "delete", "patch"}`.
Note that it is not the same as all verbs permitted by RBAC.

#### get_url(\*, server=None, namespace=None, name=None, subresource=None, params=None)

Build a URL to be used with K8s API.

If the namespace is not set, a cluster-wide URL is returned.
For cluster-scoped resources, the namespace is ignored.

If the name is not set, the URL for the resource list is returned.
Otherwise (if set), the URL for the individual resource is returned.

If subresource is set, that subresource’s URL is returned,
regardless of whether such a subresource is known or not.

Params go to the query parameters (`?param1=value1&param2=value2...`).

* **Return type:**
  [`str`](https://docs.python.org/3/library/stdtypes.html#str)
* **Parameters:**
  * **server** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **namespace** (*NamespaceName* *|* *None*) – 
  * **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **subresource** ([*str*](https://docs.python.org/3/library/stdtypes.html#str) *|* *None*) – 
  * **params** ([*Mapping*](https://docs.python.org/3/library/typing.html#typing.Mapping)*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str)*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str)*]* *|* *None*) – 

## Submodules

* [kopf.cli module](kopf.cli.md)
  * [`CLIControls`](kopf.cli.md#kopf.cli.CLIControls)
    * [`CLIControls.ready_flag`](kopf.cli.md#kopf.cli.CLIControls.ready_flag)
    * [`CLIControls.stop_flag`](kopf.cli.md#kopf.cli.CLIControls.stop_flag)
    * [`CLIControls.vault`](kopf.cli.md#kopf.cli.CLIControls.vault)
    * [`CLIControls.registry`](kopf.cli.md#kopf.cli.CLIControls.registry)
    * [`CLIControls.settings`](kopf.cli.md#kopf.cli.CLIControls.settings)
    * [`CLIControls.loop`](kopf.cli.md#kopf.cli.CLIControls.loop)
  * [`LogFormatParamType`](kopf.cli.md#kopf.cli.LogFormatParamType)
    * [`LogFormatParamType.convert()`](kopf.cli.md#kopf.cli.LogFormatParamType.convert)
  * [`logging_options()`](kopf.cli.md#kopf.cli.logging_options)
* [kopf.on module](kopf.on.md)
  * [`startup()`](kopf.on.md#kopf.on.startup)
  * [`cleanup()`](kopf.on.md#kopf.on.cleanup)
  * [`login()`](kopf.on.md#kopf.on.login)
  * [`probe()`](kopf.on.md#kopf.on.probe)
  * [`validate()`](kopf.on.md#kopf.on.validate)
  * [`mutate()`](kopf.on.md#kopf.on.mutate)
  * [`resume()`](kopf.on.md#kopf.on.resume)
  * [`create()`](kopf.on.md#kopf.on.create)
  * [`update()`](kopf.on.md#kopf.on.update)
  * [`delete()`](kopf.on.md#kopf.on.delete)
  * [`field()`](kopf.on.md#kopf.on.field)
  * [`index()`](kopf.on.md#kopf.on.index)
  * [`event()`](kopf.on.md#kopf.on.event)
  * [`daemon()`](kopf.on.md#kopf.on.daemon)
  * [`timer()`](kopf.on.md#kopf.on.timer)
  * [`subhandler()`](kopf.on.md#kopf.on.subhandler)
  * [`register()`](kopf.on.md#kopf.on.register)
* [kopf.testing module](kopf.testing.md)
  * [`KopfRunner`](kopf.testing.md#kopf.testing.KopfRunner)
    * [`KopfRunner.future`](kopf.testing.md#kopf.testing.KopfRunner.future)
    * [`KopfRunner.output`](kopf.testing.md#kopf.testing.KopfRunner.output)
    * [`KopfRunner.stdout`](kopf.testing.md#kopf.testing.KopfRunner.stdout)
    * [`KopfRunner.stdout_bytes`](kopf.testing.md#kopf.testing.KopfRunner.stdout_bytes)
    * [`KopfRunner.stderr`](kopf.testing.md#kopf.testing.KopfRunner.stderr)
    * [`KopfRunner.stderr_bytes`](kopf.testing.md#kopf.testing.KopfRunner.stderr_bytes)
    * [`KopfRunner.exit_code`](kopf.testing.md#kopf.testing.KopfRunner.exit_code)
    * [`KopfRunner.exception`](kopf.testing.md#kopf.testing.KopfRunner.exception)
    * [`KopfRunner.exc_info`](kopf.testing.md#kopf.testing.KopfRunner.exc_info)
