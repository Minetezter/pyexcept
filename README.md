# pyexcept

The perfect Python 3 library for creating new exceptions, raising custom errors with custom messages and choosing from a set of 13 unique exceptions!

# pyexcept Built-in Exceptions

pyexcept contains built-in 13 Exceptions that python BaseException does not include built-in.
List:

1)  **BlockageError**
2)  **ComileError**
3)  **EncodeError**
4)  **DecodeError**
5)  **HTTPError**
6)  **HostResolveError**
7)  **IOError**
8)  **PermissionError**
9)  **RefuseError**
10) **RunError**
11) **TranslationError**
12) **WebConnectionError**
13) **FormatError**

__Usage example:__

**INPUT:**
```python
import pyexcept

raise pyexcept.PermissionError("This is an example error")
```

**OUTPUT:**
```
Traceback (most recent call last):
  File "/home/your_name/exampleFile.py", line 3, in <module>
    raise pyexcept.PermissionError("This is an example error")
_.PermissionError: This is an example error
```

# pyexcept Create custom exception

Using the pyexcept module, you can create custom exception names and messages.
__Example:__

**INPUT:**
```python
import pyexcept

raise pyexcept.newException("MyCustomError", "This is a custom error type, not from BaseException")
```

**OUTPUT:**
```
Traceback (most recent call last):
  File "/home/your_name/exampleFile.py", line 3 in <module>
    raise pyexcept.newException("MyCustomError", "This is a custom error type, not from BaseException")
_.MyCustomError: This is a custom error type, not from BaseException
```

# pyexception Raise full error

In pyexcept, you can use the raiser() method to create full errors.
I will tell exceptions to raise an error that says the error happend on line #1 of "exampleFile.py".

__Definition and Usage:__

**INPUT:**
```python
import pyexcept

raise pyexcept.raiser("FullError", "Raise an error", line=1, file="exampleFile.py")
```

**OUTPUT:**
```
Traceback (most recent call last):
  File "/home/your_name/exampleFile.py", line 3 in <module>
    raise pyexcept.newException("MyCustomError", "This is a custom error type, not from BaseException")
_._:
  File "/home/your_name/exampleFile.py", line 1 in <module>
    import pyexcept
FullError: Raise an error
```

# Finally, raise errors from BaseException using exceptions

__Usage:__

**INPUT:**
```python
import pyexcept

raise pyexcept.base(NameError, "This is an example")
```

**OUTPUT:**
```
Traceback (most recent call last):
  File "/home/your_name/exampleFile.py", line 3 in <module>
    raise pyexcept.base(NameError, "This is an example")
NameError: This is an example
```

# Thank you!

Now, please visit my [github](https://github.com) account [here](https://github.com/Minetezter)!
