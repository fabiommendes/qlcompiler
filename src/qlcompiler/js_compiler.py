from .compiler import Compiler
import ox

class JsCompiler(Compiler):
    """
    Javascript compiler.
    """

    tokens_list = ['NUMBERS', 'STRINGS', 'BOOLEAN', 'OPERATORS']

    def js_lexer:
        lexer = ox.make_lexer([
            ('NUMBERS', r'[+-]?\d+(?:\.\d+)'),
            ('STRINGS', r'^([\'|\"]{1})+(?:(\w+|\W+|\d+|\D+|\s+|\S+|))+([\'|\"]{1})$'),
            ('BOOLEAN', r'(\Atrue)|(\Afalse)'),
            ('OPERATORS', r'[+\-*/%\|\&]'),
        ])
        return lexer


def compile(ql, **kwargs):
    """
    Compiles quick lambda object to Javascript.
    """

    compiler = JsCompiler(ql)
    return compiler.compile(**kwargs)
