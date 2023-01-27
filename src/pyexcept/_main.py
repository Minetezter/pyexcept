import os
import json

__all__ = ['DecodeError', 'CompileError', 'BlockageError', 'EncodeError', 'HTTPError', 'IOError', 'WebConnectionError', 'RefuseError', 'RunError', 'TranslationError', 'RunError', 'FormatError', 'base', 'raiser', 'newException', 'HostResolveError']

def READ_LINE(file, nline):
  i = 1
  for line in open(file, 'r'):
    if i == nline:
      return line
    
    i = i + 1

###########################################################

def DecodeError(*message):
    """Raise this Exception by using the code 'raise exceptions.DecodeError(...)'. This will create an error message like 'DecodeError: [your text here]'."""
    exec(f'''
class JSONDecodeError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

JSONDecodeError({json.dumps(' '.join(message))})
    ''')
    
    fs = open("_.py", 'x')
    fs.write('''
class JSONDecodeError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
''')
    
    fs.close()
    
    import _
    
    _exception = _.JSONDecodeError(' '.join(message))
    
    del _
    os.remove("_.py")
    
    return _exception

###########################################################

def CompileError(*message):
    """Raise this Exception by using the code 'raise exceptions.CompileError(...)'. This will create an error message like 'CompileError: [your text here]'."""
    exec(f'''
class CompileError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

CompileError({json.dumps(' '.join(message))})
    ''')
    
    fs = open("_.py", 'x')
    fs.write('''
class CompileError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
''')
    
    fs.close()
    
    import _
    
    _exception = _.CompileError(' '.join(message))
    
    del _
    os.remove("_.py")
    
    return _exception

###########################################################

def IOError(*message):
    """Raise this Exception by using the code 'raise exceptions.IOError(...)'. This will create an error message like 'IOError: [your text here]'."""
    exec(f'''
class InputOutputError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

InputOutputError({json.dumps(' '.join(message))})
    ''')
    
    fs = open("_.py", 'x')
    fs.write('''
class InputOutputError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
''')
    
    fs.close()
    
    import _
    
    _exception = _.InputOutputError(' '.join(message))
    
    del _
    os.remove("_.py")
    
    return _exception

###########################################################

def RunError(*message):
    """Raise this Exception by using the code 'raise exceptions.RunError(...)'. This will create an error message like 'RunError: [your text here]'."""
    exec(f'''
class RunError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

RunError({json.dumps(' '.join(message))})
    ''')
    
    fs = open("_.py", 'x')
    fs.write('''
class RunError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
''')
    
    fs.close()
    
    import _
    
    _exception = _.RunError(' '.join(message))
    
    del _
    os.remove("_.py")
    
    return _exception

###########################################################

def WebConnectionError(*message):
    """Raise this Exception by using the code 'raise exceptions.WebConnectionError(...)'. This will create an error message like 'WebConnectionError: [your text here]'."""
    exec(f'''
class WebConnectionError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

WebConnectionError({json.dumps(' '.join(message))})
    ''')
    
    fs = open("_.py", 'x')
    fs.write('''
class WebConnectionError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
''')
    
    fs.close()
    
    import _
    
    _exception = _.WebConnectionError(' '.join(message))
    
    del _
    os.remove("_.py")
    
    return _exception

###########################################################

def RefuseError(*message):
    """Raise this Exception by using the code 'raise exceptions.RefuseError(...)'. This will create an error message like 'RefuseError: [your text here]'."""
    exec(f'''
class RefuseError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

RefuseError({json.dumps(' '.join(message))})
    ''')
    
    fs = open("_.py", 'x')
    fs.write('''
class RefuseError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
''')
    
    fs.close()
    
    import _
    
    _exception = _.RefuseError(' '.join(message))
    
    del _
    os.remove("_.py")
    
    return _exception

###########################################################

def BlockageError(*message):
    """Raise this Exception by using the code 'raise exceptions.BlockageError(...)'. This will create an error message like 'BlockageError: [your text here]'."""
    exec(f'''
class BockageError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

BockageError({json.dumps(' '.join(message))})
    ''')
    
    fs = open("_.py", 'x')
    fs.write('''
class BockageError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
''')
    
    fs.close()
    
    import _
    
    _exception = _.BockageError(' '.join(message))
    
    del _
    os.remove("_.py")
    
    return _exception

###########################################################

def HostResolveError(*message):
    """Raise this Exception by using the code 'raise exceptions.HostResolveError(...)'. This will create an error message like 'HostResolveError: [your text here]'."""
    exec(f'''
class HostResolveError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

HostResolveError({json.dumps(' '.join(message))})
    ''')
    
    fs = open("_.py", 'x')
    fs.write('''
class HostResolveError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
''')
    
    fs.close()
    
    import _
    
    _exception = _.HostResolveError(' '.join(message))
    
    del _
    os.remove("_.py")
    
    return _exception

###########################################################

def HTTPError(*message):
    """Raise this Exception by using the code 'raise exceptions.HTTPError(...)'. This will create an error message like 'HTTPError: [your text here]'."""
    exec(f'''
class HTTPError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

HTTPError({json.dumps(' '.join(message))})
    ''')
    
    fs = open("_.py", 'x')
    fs.write('''
class HTTPError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
''')
    
    fs.close()
    
    import _
    
    _exception = _.HTTPError(' '.join(message))
    
    del _
    os.remove("_.py")
    
    return _exception

###########################################################

def EncodeError(*message):
    """Raise this Exception by using the code 'raise exceptions.EncodeError(...)'. This will create an error message like 'EncodeError: [your text here]'."""
    exec(f'''
class EncodeError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

EncodeError({json.dumps(' '.join(message))})
    ''')
    
    fs = open("_.py", 'x')
    fs.write('''
class EncodeError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
''')
    
    fs.close()
    
    import _
    
    _exception = _.EncodeError(' '.join(message))
    
    del _
    os.remove("_.py")
    
    return _exception

###########################################################

def PermissionError(*message):
    """Raise this Exception by using the code 'raise exceptions.PermissionError(...)'. This will create an error message like 'PermissionError: [your text here]'."""
    exec(f'''
class PermissionError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

PermissionError({json.dumps(' '.join(message))})
    ''')
    
    fs = open("_.py", 'x')
    fs.write('''
class PermissionError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
''')
    
    fs.close()
    
    import _
    
    _exception = _.PermissionError(' '.join(message))
    
    del _
    os.remove("_.py")
    
    return _exception

###########################################################

def TranslationError(*message):
    """Raise this Exception by using the code 'raise exceptions.TranslateError(...)'. This will create an error message like 'TranslateError: [your text here]'."""
    exec(f'''
class TranslationError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

TranslationError({json.dumps(' '.join(message))})
    ''')
    
    fs = open("_.py", 'x')
    fs.write('''
class TranslationError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
''')
    
    fs.close()
    
    import _
    
    _exception = _.TranslationError(' '.join(message))
    
    del _
    os.remove("_.py")
    
    return _exception

###########################################################

def FormatError(*message):
    """Raise this Exception by using the code 'raise exceptions.FormatError(...)'. This will create an error message like 'FormatError: [your text here]'."""
    exec(f'''
class TranslationError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

TranslationError({json.dumps(' '.join(message))})
    ''')
    
    fs = open("_.py", 'x')
    fs.write('''
class TranslationError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
''')
    
    fs.close()
    
    import _
    
    _exception = _.TranslationError(' '.join(message))
    
    del _
    os.remove("_.py")
    
    return _exception

###########################################################

def newException(errortype, messages):
    """Creates a new type of Exception, along with a custom error. Highly recommended!!!"""
    exec("""class """ + str(errortype) + """(Exception):
    def __init__(self, *args):
      if args:
        self.message = args[0]
      else:
        self.message = None
  
    def __str__(self):
      if self.message:
        return '''""" + str(errortype) + """'''.format(self.message)
      else:
        return '''""" + str(messages) + """'''""")
    
    fs = open("_.py", 'x')
    fs.write("""class """ + str(errortype) + """(Exception):
    def __init__(self, *args):
      if args:
        self.message = args[0]
      else:
        self.message = None
  
    def __str__(self):
      if self.message:
        return '''""" + str(errortype) + """'''.format(self.message)
      else:
        return '''""" + str(messages) + """'''""")
    
    fs.close()
    
    import _
    
    _exception = eval(f"_.{errortype}()")
    
    del _
    os.remove("_.py")
    
    return _exception

###########################################################

def raiser(errtype, message, line=0, file=""):
    """Raises the given error.
    Create full errors That include the filename and line."""
    if line != 0: 
        lines = READ_LINE(file, line)
        if "\n" in lines:
            err = newException("_", f'\n  File "{os.getcwd()}/{file}", line {line}, in <module>\n    {lines}{errtype}: {message}')
        else:
            err = newException("_", f'\n  File "{os.getcwd()}/{file}", line {line}, in <module>\n    {lines}\n{errtype}: {message}')
    else:
        err = str(message)
    
    raise err

###########################################################

def base(exception, message):
    "Raises normal exceptions derived from BaseException."
    return exception(message)



