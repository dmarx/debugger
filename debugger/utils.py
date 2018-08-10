from pygments.lexers import Python3Lexer as Py3Lexer
from pygments.token import Token

lexer = Py3Lexer(ensurenl=False)

def remove_comments(code_text):
    toks = list(lexer.get_tokens(text=code_text))
    return ''.join([text for kind, text in toks if not kind in Token.Comment])
