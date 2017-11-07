from .compiler import Compiler
import ox

class JsCompiler(Compiler):
    """
    Javascript compiler.
    """

<<<<<<< HEAD
    # Lexer
    
    tokens_list = ['NUMBERS', 'STRINGS', 'BOOLEAN', 'OPERATORS', 'CONDITIONALS']
=======
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
>>>>>>> 5d7594d9b93ff5fce3c4f78aac2718e28a06743f

    def js_lexer:
        lexer = ox.make_lexer([
            ('NUMBERS', r'[+-]?\d+(?:\.\d+)'),
            ('STRINGS', r'^([\'|\"]{1})+(?:(\w+|\W+|\d+|\D+|\s+|\S+|))+([\'|\"]{1})$'),
            ('BOOLEAN', r'(\ATrue)|(\AFalse)'),
            ('OPERATORS', r'[+\-*/%\|\&]'),
<<<<<<< HEAD
            ('CONDITIONALS', r'(\Aif)|(\Aelif)|(\Aelse)'),
=======
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
>>>>>>> 5d7594d9b93ff5fce3c4f78aac2718e28a06743f
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
