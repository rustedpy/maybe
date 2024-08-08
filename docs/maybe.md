<!-- markdownlint-disable -->

<a href="https://github.com/rustedpy/maybe/blob/main/src/maybe/maybe.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `maybe`




**Global Variables**
---------------
- **SomeNothing**

---

<a href="https://github.com/rustedpy/maybe/blob/main/src/maybe/maybe.py#L283"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `is_some`

```python
is_some(maybe: 'Maybe[T]') → TypeGuard[Some[T]]
```

A typeguard to check if a maybe is a `Some`. 

Usage: 

```plain
     >>> r: Maybe[int, str] = get_a_maybe()
     >>> if is_some(r):
     ...     r   # r is of type Some[int]
     ... elif is_nothing(r):
     ...     r   # r is of type Nothing[str]
``` 


---

<a href="https://github.com/rustedpy/maybe/blob/main/src/maybe/maybe.py#L299"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `is_nothing`

```python
is_nothing(maybe: 'Maybe[T]') → TypeGuard[Nothing]
```

A typeguard to check if a maybe is a `Nothing`. 

Usage: 

```plain
     >>> r: Maybe[int, str] = get_a_maybe()
     >>> if is_some(r):
     ...     r   # r is of type Some[int]
     ... elif is_nothing(r):
     ...     r   # r is of type Nothing[str]
``` 


---

<a href="https://github.com/rustedpy/maybe/blob/main/src/maybe/maybe.py#L30"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Some`
An object that indicates some inner value is present 

<a href="https://github.com/rustedpy/maybe/blob/main/src/maybe/maybe.py#L38"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(value: 'T') → None
```






---

#### <kbd>property</kbd> some_value

Return the inner value. 



---

<a href="https://github.com/rustedpy/maybe/blob/main/src/maybe/maybe.py#L123"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `and_then`

```python
and_then(op: 'Callable[[T], Maybe[U]]') → Maybe[U]
```

There is a contained value, so return the maybe of `op` with the original value passed in 

---

<a href="https://github.com/rustedpy/maybe/blob/main/src/maybe/maybe.py#L72"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `expect`

```python
expect(_message: 'str') → T
```

Return the value. 

---

<a href="https://github.com/rustedpy/maybe/blob/main/src/maybe/maybe.py#L56"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `is_nothing`

```python
is_nothing() → Literal[False]
```





---

<a href="https://github.com/rustedpy/maybe/blob/main/src/maybe/maybe.py#L53"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `is_some`

```python
is_some() → Literal[True]
```





---

<a href="https://github.com/rustedpy/maybe/blob/main/src/maybe/maybe.py#L102"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `map`

```python
map(op: 'Callable[[T], U]') → Some[U]
```

There is a contained value, so return `Some` with original value mapped to a new value using the passed in function. 

---

<a href="https://github.com/rustedpy/maybe/blob/main/src/maybe/maybe.py#L109"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `map_or`

```python
map_or(_default: 'object', op: 'Callable[[T], U]') → U
```

There is a contained value, so return the original value mapped to a new value using the passed in function. 

---

<a href="https://github.com/rustedpy/maybe/blob/main/src/maybe/maybe.py#L116"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `map_or_else`

```python
map_or_else(_default_op: 'object', op: 'Callable[[T], U]') → U
```

There is a contained value, so return original value mapped to a new value using the passed in `op` function. 

---

<a href="https://github.com/rustedpy/maybe/blob/main/src/maybe/maybe.py#L130"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `or_else`

```python
or_else(_op: 'object') → Some[T]
```

There is a contained value, so return `Some` with the original value 

---

<a href="https://github.com/rustedpy/maybe/blob/main/src/maybe/maybe.py#L59"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `some`

```python
some() → T
```

Return the value. 

---

<a href="https://github.com/rustedpy/maybe/blob/main/src/maybe/maybe.py#L78"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `unwrap`

```python
unwrap() → T
```

Return the value. 

---

<a href="https://github.com/rustedpy/maybe/blob/main/src/maybe/maybe.py#L84"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `unwrap_or`

```python
unwrap_or(_default: 'U') → T
```

Return the value. 

---

<a href="https://github.com/rustedpy/maybe/blob/main/src/maybe/maybe.py#L90"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `unwrap_or_else`

```python
unwrap_or_else(op: 'object') → T
```

Return the value. 

---

<a href="https://github.com/rustedpy/maybe/blob/main/src/maybe/maybe.py#L96"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `unwrap_or_raise`

```python
unwrap_or_raise(e: 'object') → T
```

Return the value. 


---

<a href="https://github.com/rustedpy/maybe/blob/main/src/maybe/maybe.py#L137"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Nothing`
An object that indicates no inner value is present 

<a href="https://github.com/rustedpy/maybe/blob/main/src/maybe/maybe.py#L145"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__() → None
```








---

<a href="https://github.com/rustedpy/maybe/blob/main/src/maybe/maybe.py#L230"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `and_then`

```python
and_then(_op: 'object') → Nothing
```

There is no contained value, so return `Nothing` 

---

<a href="https://github.com/rustedpy/maybe/blob/main/src/maybe/maybe.py#L174"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `expect`

```python
expect(message: 'str') → NoReturn
```

Raises an `UnwrapError`. 

---

<a href="https://github.com/rustedpy/maybe/blob/main/src/maybe/maybe.py#L165"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `is_nothing`

```python
is_nothing() → Literal[True]
```





---

<a href="https://github.com/rustedpy/maybe/blob/main/src/maybe/maybe.py#L162"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `is_some`

```python
is_some() → Literal[False]
```





---

<a href="https://github.com/rustedpy/maybe/blob/main/src/maybe/maybe.py#L212"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `map`

```python
map(_op: 'object') → Nothing
```

Return `Nothing` 

---

<a href="https://github.com/rustedpy/maybe/blob/main/src/maybe/maybe.py#L218"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `map_or`

```python
map_or(default: 'U', _op: 'object') → U
```

Return the default value 

---

<a href="https://github.com/rustedpy/maybe/blob/main/src/maybe/maybe.py#L224"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `map_or_else`

```python
map_or_else(default_op: 'Callable[[], U]', op: 'object') → U
```

Return the result of the `default_op` function 

---

<a href="https://github.com/rustedpy/maybe/blob/main/src/maybe/maybe.py#L236"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `or_else`

```python
or_else(op: 'Callable[[], Maybe[T]]') → Maybe[T]
```

There is no contained value, so return the result of `op` 

---

<a href="https://github.com/rustedpy/maybe/blob/main/src/maybe/maybe.py#L168"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `some`

```python
some() → None
```

Return `None`. 

---

<a href="https://github.com/rustedpy/maybe/blob/main/src/maybe/maybe.py#L184"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `unwrap`

```python
unwrap() → NoReturn
```

Raises an `UnwrapError`. 

---

<a href="https://github.com/rustedpy/maybe/blob/main/src/maybe/maybe.py#L194"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `unwrap_or`

```python
unwrap_or(default: 'U') → U
```

Return `default`. 

---

<a href="https://github.com/rustedpy/maybe/blob/main/src/maybe/maybe.py#L200"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `unwrap_or_else`

```python
unwrap_or_else(op: 'Callable[[], T]') → T
```

There is no contained value, so return a new value by calling `op`. 

---

<a href="https://github.com/rustedpy/maybe/blob/main/src/maybe/maybe.py#L206"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `unwrap_or_raise`

```python
unwrap_or_raise(e: 'Type[TBE]') → NoReturn
```

There is no contained value, so raise the exception with the value. 


---

<a href="https://github.com/rustedpy/maybe/blob/main/src/maybe/maybe.py#L259"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `UnwrapError`
Exception raised from ``.unwrap_<...>`` and ``.expect_<...>`` calls. 

The original ``Maybe`` can be accessed via the ``.maybe`` attribute, but this is not intended for regular use, as type information is lost: ``UnwrapError`` doesn't know about ``T``, since it's raised from ``Some()`` or ``Nothing()`` which only knows about either ``T`` or no-value, not both. 

<a href="https://github.com/rustedpy/maybe/blob/main/src/maybe/maybe.py#L271"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(maybe: 'Maybe[object]', message: 'str') → None
```






---

#### <kbd>property</kbd> maybe

Returns the original maybe. 






---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
