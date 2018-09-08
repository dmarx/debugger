# Debugger

...probably gonna change the name to "sprinkles".
* homage to "icecream"
* Sprinkle print statements in your code

... Is there a way to use icecream with sprinkles? That would be both convenient and hilarious.

## Motivation

Inspired by the [icecream](https://github.com/gruns/icecream), this tool aims to solve a similar problem: improving debugging-via-print-statement. This library addresses icecream's biggest weakness: python is an interactive language, but icecream can only be used in scripts. This is because icecream mainly operates via sourcecode inspection. Which is great, but if you're working in an ipython session or a jupyter notebook, this isn't very helpful.

Similar to icecream, this library makes liberal usage of the `inspect` module, but it doesn't actually do any introspection of source code. Instead, this tool peeks into the call stack to figure out where and what was calling it.

## Features

* Automatically generates a timestamp for all messages
* Determines and reports the calling function/method
* Tracks and reports the number of messages emitted by a particular calling scope
* Simple printing for arbitrary number of variables whose values you'd like to inspect, paired with the variable name
* Automatic pretty printing for large outputs
* Automatic output colorization

## Usage

```
from debugger import DebugHelper

dbgr = DebugHelper()

def foo(a,b, *args, **kwargs):
    dbgr.msg()
    dbgr.msg(a,b)
    dbgr.msg("our args", args)
    dbgr.msg("our kwargs", kwargs)
    dbgr.msg()

def bar(*args, **kwargs):
    dbgr.msg(args)
    dbgr.msg(kwargs)
    dbgr.msg("calling foobar()")
    foobar(*args, **kwargs)
    dbgr.msg("exited foobar()")

bar('left', 'right', par=[0,3,5])
```

```
 [2018-08-14 02:40:54.403393] [bar('left', 'right', par=[0,3,5])] 1
 [2018-08-14 02:40:54.412746] ... args: ('left', 'right')

 [2018-08-14 02:40:54.419271] [bar('left', 'right', par=[0,3,5])] 2
 [2018-08-14 02:40:54.431777] ... kwargs: {'par': [0, 3, 5]}

 [2018-08-14 02:40:54.440045] [bar('left', 'right', par=[0,3,5])] 3
 [2018-08-14 02:40:54.448042] ... calling foobar()

 [2018-08-14 02:40:54.459262] [foobar(*args, **kwargs)] 1
 [2018-08-14 02:40:54.472212] [foobar(*args, **kwargs)] 2
 [2018-08-14 02:40:54.489089] ... a: 'left'
 [2018-08-14 02:40:54.489089] ...b: 'right'

 [2018-08-14 02:40:54.507275] [foobar(*args, **kwargs)] 3
 [2018-08-14 02:40:54.525061] ... our args
 [2018-08-14 02:40:54.525061] ... args: ()

 [2018-08-14 02:40:54.544017] [foobar(*args, **kwargs)] 4
 [2018-08-14 02:40:54.561380] ... our kwargs
 [2018-08-14 02:40:54.561380] ... kwargs: {'par': [0, 3, 5]}

 [2018-08-14 02:40:54.578566] [foobar(*args, **kwargs)] 5
 [2018-08-14 02:40:54.592380] [bar('left', 'right', par=[0,3,5])] 4
 [2018-08-14 02:40:54.605746] ... exited foobar()
```
