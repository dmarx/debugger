# To do:


import inspect
#import logging #Do I really wanna use logging for this? Logging is actually turning into sort of a PITA
from collections import Counter
import datetime as dt
import re
import warnings
import pprint
import sys

from debugger.utils import remove_comments
from debugger.exceptions import NonStandardDebugHelperName

# Again... do I really want to use logging here?
# It's a simple way to get the timestamp and I like that the messages show as colored (in jupyter),
# but otherwise it's sort of a pain. Does all sorts of weird shit with white space.

#logging.basicConfig(
#    format="[%(asctime)s] %(message)s",
#    level=logging.INFO,
#    stream=sys.stdout
#)

class DebugHelper(object):
    def __init__(self, parent_logger_name='DebugHelper'):
        self.scope_calls = Counter()
        #self.logger = logging.getLogger(parent_logger_name)
        #self.logger.setLevel(logging.INFO)

        init_call = self._calling_context(2)
        init_name = re.findall('(\w+)\s?=\s?DebugHelper\\(', init_call)
        if not init_name:
            init_name = re.findall('(\w+)\s?=\s?debugger.DebugHelper\\(', init_call)
        if not init_name:
            raise NonStandardDebugHelperName
        self._init_name = init_name[0].strip()
    def _pformat(self, v):
        """pretty print formatting for multi-line outputs"""
        v = pprint.pformat(v)
        if '\n' in v:
            v = '\n' + v
        return v
    @staticmethod
    def _ts():
        return str(dt.datetime.now())
    def _msg(self, msg_str):
        ts = self._ts()
        #bgnd = "\u001b[45m"
        code = 223 # 224 is the same color jupyter uses for stderr.
        bgnd = u"\u001b[48;5;" + str(code) + "m "
        reset = "\u001b[0m"
        print("{}[{}] {} {}".format(bgnd, ts, msg_str, reset))
        #self.logger.info(msg)
    def msg(self, *args, **kwargs):
        """Workhorse"""
        scope = self._calling_scope()
        self.scope_calls[scope] += 1
        n = self.scope_calls[scope]
        msg_str = '[{}] {}'.format(scope, n)
        #self.logger.info(msg_str)
        self._msg(msg_str)

        parts = []
        if args:
            parts.extend(self._make_argstr(args))
        if kwargs:
            for k,v in kwargs.items():
                parts.append('... {}: {}'.format(k, self._pformat(v)))
        for i, msg_str in enumerate(parts):
            if i == (len(parts)-1):
                msg_str += '\n'
            #self.logger.info(msg_str)
            self._msg(msg_str)
        #print()
    def _calling_context(self, i):
        context = inspect.stack()[i].code_context[0].strip()
        return remove_comments(context)
    def _calling_scope(self):
        scope = self._calling_context(4)
        if scope == 'exec(code_obj, self.user_global_ns, self.user_ns)':
            scope = '__main__'
        return scope
    def _msg_argnames(self):
        src_call = self._calling_context(4)
        call_pat = '{}.msg('.format(self._init_name)
        _, args1 = src_call.split(call_pat)
        args2 = args1.strip()[:-1] # assumes no comments on line
        args = args2.split(',')
        argnames = []
        for a in args:
            if a:
                if (a[0]==a[-1]) and (a[0] in ('"', "'")):
                    argnames.append(None)
                elif '=' not in a:
                    argnames.append(a)
        return argnames
    def _make_argstr(self, args):
        argnames = self._msg_argnames()
        argstrs = []
        for argname, arg in zip(argnames, args):
            if argname:
                argstrs.append('...{}: {}'.format(argname, self._pformat(arg)))
            else:
                argstrs.append('...{}'.format(arg))
        argstrs[0] = '... ' + argstrs[0][3:]
        return argstrs

if __name__ == '__main__':

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
