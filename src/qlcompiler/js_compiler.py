from .compiler import Compiler
import ox

class JsCompiler(Compiler):
    """
    Javascript compiler.
    """

    # Tokens

    tokens_list = ['NUMBERS', 'STRINGS', 'BOOLEAN', 'OPERATORS', 'FUNCTIONS', 'CONDITIONALS']

    def js_lexer:
        lexer = ox.make_lexer([
            ('NUMBERS', r'[+-]?\d+(?:\.\d+)'),
            ('STRINGS', r'^([\'|\"]{1})+(?:(\w+|\W+|\d+|\D+|\s+|\S+|))+([\'|\"]{1})$'),
            ('BOOLEAN', r'(\Atrue)|(\Afalse)'),
            ('OPERATORS', r'[+\-*/%\|\&]'),
        ])
        return lexer

    # Parser

    def js_parser(tokens):
        parser = ox.make_parser([
            ('term : term OP atom', binop),
            ('term : atom', lambda x: x), 
            ('atom : NUMBER', float), 
        ], tokens)
        
        return parser

    # Parser Operations

    




def compile(ql, **kwargs):
    """
    Compiles quick lambda object to Javascript.
    """

    compiler = JsCompiler(ql)
    return compiler.compile(**kwargs)
