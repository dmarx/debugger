from debugger import DebugHelper

dbgr = DebugHelper()

class TestClass(object):
    def __init__(self, arg):
        dbgr.msg()
        dbgr.msg('top')
        dbgr.msg(arg)
        b = self.msg(arg)
        dbgr.msg(b)
        self.msg(arg+'bar')
        dbgr.msg()
    def msg(self, foo):
        dbgr.msg()
        dbgr.msg(foo)
        b = '~~{}~~'.format(foo)
        dbgr.msg(b)
        print(b)
        return b

TestClass('foo')
