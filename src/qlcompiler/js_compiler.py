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
            ('COND_IF', r'^\s*if'),
            ('COND_ELIF', r'^\s*elif'),
            ('COND_ELSE', r'^\s*else'),
            ('LOOP_FOR', r'^\s*for'),
            ('LOOP_WHILE', r'^\s*while'),
            ('COLON', r'(:{1})$')
        ])
        return lexer


def compile(ql, **kwargs):
    """
    Compiles quick lambda object to Javascript.
    """

    compiler = JsCompiler(ql)
    return compiler.compile(**kwargs)
