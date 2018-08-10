import datetime as dt
import pprint

from pygments.lexers import Python3Lexer as Py3Lexer
from pygments.token import Token

lexer = Py3Lexer(ensurenl=False)

def remove_comments(code_text):
    toks = list(lexer.get_tokens(text=code_text))
    return ''.join([text for kind, text in toks if not kind in Token.Comment])

def timestamp():
    return str(dt.datetime.now())

def pformatml(v):
    """pretty print formatting for multi-line outputs"""
    v = pprint.pformat(v)
    if '\n' in v:
        v = '\n' + v
    return v

def colorize(instr, code = 223):
    # 224 is the same color jupyter uses for stderr.
    bgnd = u"\u001b[48;5;" + str(code) + "m "
    reset = "\u001b[0m"
    return bgnd + instr + reset
