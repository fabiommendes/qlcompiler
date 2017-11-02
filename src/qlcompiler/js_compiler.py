from .compiler import Compiler
import ox

class JsCompiler(Compiler):
    """
    Javascript compiler.
    """

    tokens_list = [
        'NUMBER',
        'STRINGS',
        'BOOLEAN',
        'ATRIB_OP',
        'SIMPLE_OP',
        'MUL_OP',
        'BREAKLINE',
        'INDENT',
        ]

    def js_lexer:
        lexer = ox.make_lexer([
            ('NUMBER', r'[+-]?\d+(?:\.\d+)'),
            ('STRING', r'^([\'|\"]{1})+(?:(\w+|\W+|\d+|\D+|\s+|\S+|))+([\'|\"]{1})$'),
            ('BOOLEAN', r'(\ATrue)|(\AFalse)'),
            ('ATRIB_OP', r'[\={1}]'),
            ('SIMPLE_OP', r'[-+]'),
            ('MUL_OP', r'[*/]'),
            ('BREAKLINE', r'[\n\r]'),
            ('INDENT', r'[\t]'),
        ])
        return lexer


def compile(ql, **kwargs):
    """
    Compiles quick lambda object to Javascript.
    """

    compiler = JsCompiler(ql)
    return compiler.compile(**kwargs)
