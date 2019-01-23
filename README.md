# staticvariable
staticvariable in Python

Staticvariable is defined through process of managing a variable within the globals.

To use staticvariable in python

```python

self.value = staticvariable(class_, variable_name, variable_value)

# Example in a class

class Demo:
    def __init__(self):
        self.value = staticvariable(Demo, "value", [1,2,3])

# self.value gives staticvariable object for class Demo

```

Get Value of static variable

```python

self.value.get_static_value(variable_name)

```

Set Value of staic variable

```python

self.value.set_static_value(variable_name, variable_value)

```

