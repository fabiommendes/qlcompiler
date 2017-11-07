 import ox


class JSParser():

    '''
       A Parser to emit js code from python 
    '''

    def js_parser(tokens):
        parser = ox.make_parser([
            ('term : term OP atom', binop),
            ('term : atom', lambda x: x), 
            ('atom : NUMBER', float), 
        ], tokens)
        
        return parser

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
 
    # Binary Operator

    OPERATORS = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
    }

    def binary_operator (first_value, second_value, operator):
        return OPERATORS[operator](first_value, second_value)
   
   
    # Backlog

    def parse_expressions(statements):
        return "Some expression in JS"
