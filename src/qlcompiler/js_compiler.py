from .compiler import Compiler
import ox

class JsCompiler(Compiler):
    """
    Javascript compiler.
    """

    # Lexer
    
    tokens_list = ['NUMBERS', 'STRINGS', 'BOOLEAN', 'OPERATORS', 'CONDITIONALS']

    def js_lexer:
        lexer = ox.make_lexer([
            ('NUMBERS', r'[+-]?\d+(?:\.\d+)'),
            ('STRINGS', r'^([\'|\"]{1})+(?:(\w+|\W+|\d+|\D+|\s+|\S+|))+([\'|\"]{1})$'),
            ('BOOLEAN', r'(\ATrue)|(\AFalse)'),
            ('OPERATORS', r'[+\-*/%\|\&]'),
            ('CONDITIONALS', r'(\Aif)|(\Aelif)|(\Aelse)'),
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

    # Parse Operators

    OPERATORS = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
    }

    # Parser Operations

    def parse_booleans(binary): 
        if binary:
            binary = 'true'
        else:
            binary = 'false'
    
        return binary

    def parse_operations(first_value, second_value, operator):

        if operator == '+' || operator == '-' || operator == '*' || operator == '/':
            return binary_operator(first_value, operator, second_value)            
 
    def binary_operator (first_value, second_value, operator):
        return OPERATORS[operator](first_value, second_value)
   
    def parse_expressions(statements):
        return "Some expression in JS"
    


def compile(ql, **kwargs):
    """
    Compiles quick lambda object to Javascript.
    """

    compiler = JsCompiler(ql)
    return compiler.compile(**kwargs)
