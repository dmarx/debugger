
err_text_NonStandardDebugHelperName = """
DebugHelper needs to be able to identify itself by name when invoked.
Instantiation call must be one of the following:

    instanceName = DebugHelper(*args, **kwargs)
    instanceName = debugger.DebugHelper(*args, **kwargs)

Aliasing the DebugHelper class is not supported:

    from debugger import DebugHelper as FooBar

    instanceName = FooBar()

Inheritance is not supported:

   class BarBaz(DebugerHelper):
       pass

   instanceName = BarBaz()
"""

class NonStandardDebugHelperName(NotImplementedError):

    def __init__(self, expression, message=err_text_NonStandardDebugHelperName):
        self.expression = expression
        self.message = message
