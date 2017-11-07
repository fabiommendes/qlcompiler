from .compiler import Compiler
import ox

class JsCompiler(Compiler):

    """
    Javascript compiler.
    """
    # Lexer

    tokens_list = [
        'NUMBERS',
        'STRINGS',
        'BOOLEAN',
        'OPERATORS',
        'COND_IF',
        'COND_ELIF',
        'COND_ELSE',
        'LOOP_FOR',
        'LOOP_WHILE',
        'COLON',
        'BO_EQUAL',
        'BO_BIGGER',
        'BO_BIGGER_EQUAL',
        'BO_LOWER',
        'BO_LOWER_EQUAL',
        'LO_NOT',
        'LO_AND',
        'LO_OR',
        'VARIABLE',
        'RW_IN',
        'RW_IS',
        'RW_RANGE'
    ]

    def js_lexer:
        lexer = ox.make_lexer([
            ('NUMBERS', r'[+-]?\d+(?:\.\d+)'),
            ('STRINGS', r'^([\'|\"]{1})+(?:(\w+|\W+|\d+|\D+|\s+|\S+|))+([\'|\"]{1})$'),
            ('BOOLEAN', r'(\ATrue)|(\AFalse)'),
            ('OPERATORS', r'[+\-*/%\|\&]'),
            ('COND_IF', r'^\s*if'),
            ('COND_ELIF', r'^\s*elif'),
            ('COND_ELSE', r'^\s*else'),
            ('LOOP_FOR', r'^\s*for'),
            ('LOOP_WHILE', r'^\s*while'),
            ('COLON', r':$'),
            ('BO_EQUAL', r'=='),
            ('BO_BIGGER', r'>'),
            ('BO_BIGGER_EQUAL', r'>='),
            ('BO_LOWER', r'<'),
            ('BO_LOWER_EQUAL', r'<='),
            ('LO_NOT', r'(not)'),
            ('LO_AND', r'(and)'),
            ('LO_OR', r'(or)'),
            ('VARIABLE', r'([a-zA-Z]|_)\w+'),
            ('RW_IN', r'(in)'),
            ('RW_IS', r'(is)'),
            ('RW_RANGE', r'(range)')
        ])

        return lexer
      


def compile(ql, **kwargs):
    """
    Compiles quick lambda object to Javascript.
    """

    compiler = JsCompiler(ql)
    return compiler.compile(**kwargs)
