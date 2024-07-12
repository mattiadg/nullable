# Nullable

This is an example code, not an installable library, that shows how we can concatenate operations like 
getting an attribute or indexing, while not crashing the program if None or an Exception shows up somewhere.

## Code
The sample class that allows everything is defined in nullable.py:

```python
class Nullable(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def __getattr__(self, item):
        try:
            return Nullable(self.value.item)
        except AttributeError:
            return Nullable(None)

    def __getitem__(self, item):
        try:
            return Nullable(self.value[item])
        except (TypeError, KeyError):
            return Nullable(None)

    def get(self) -> T | None:
        return self.value
```

## Usage
The use cases are shown in tests.py:

```python
from nullable import Nullable


def test_none():
    assert Nullable(None).get() is None


def test_chain_none_attr():
    assert Nullable(None).x.y.get() is None


def test_chain_none_item():
    assert Nullable(None)["item1"]["item2"].get() is None


def test_good_values():
    elem = Nullable([1, "two", {"three": 3}])
    assert elem.x.get() is None
    assert isinstance(elem[0], Nullable)
    assert elem[0].get() == 1
    assert len(elem[1].get()) == 3
    assert elem[2]["three"].get() == 3
    assert elem[2]["one"].get() is None
```

This can help to simplify coding situations like:
``` python
l = parse_external_data(data)
if l:
    names = [(x.name or "NONAME") if x else "NONAME" for x in l]
```
which becomes
``` python
x = Nullable(parse_external_data(data))
names = [x.name.get() or "NONAME" for x in l]
```
and the simplification is even more apparent if more attributes or indexes have to be concatenated.

## Why not a library?
This code is very simple and short and can be easily copied and adapted to your project without a need for
an additional dependency. It is also more flexible if you have the option to modify the class at your will.