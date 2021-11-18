# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

# List of token names.   This is always required
reserved = {
    'choice': 'CHOICE',
    'case': 'CASE',
    'qreg': 'QREG',
    'creg': 'CREG',
    'fcho': 'FCHO',
    'lcho': 'LCHO',
    #'measure': 'MEASURE',
    'pass': 'PASS',
    'default': 'DEFAULT',
    'OPENQASM' : 'QASM',
    'include' : 'Include',
}

''''''
tokens = [
    'Integer',
    'Float',
    'Plus',
    'Minus',
    'Times',
    'Divide',
    'Mod',
    'LParen',
    'RParen',
    'LBracket',
    'RBracket',
    'LBrace',
    'RBrace',
    'ID',
    'Comma',
    'SemiColon',
    'Assign',
    'Colon',
    'DQuotation',
    'DeciPoint'
]
tokens += reserved.values()

# Regular expression rules for simple tokens
t_Plus = r'\+'
t_Minus = r'-'
t_Times = r'\*'
t_Divide = r'/'
t_Mod = r'%'
t_LParen = r'\('
t_RParen = r'\)'
t_LBracket = r'\['
t_RBracket = r'\]'
t_Comma = r'\,'
t_SemiColon = r';'
t_Assign = r'='
t_Colon = r':'
t_DQuotation = r'\"'
t_DeciPoint = r'.'
# A regular expression rule with some action code


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t


def t_Float(t):
    r'([0-9]+\.[0-9]*|[0-9]*\.[0-9]+)([eE][-+]?[0-9]+)?'
    # t.value = float(t.value)
    return t


def t_Integer(t):
    r'[1-9]+[0-9]*|0'
    # t.value = int(t.value)
    return t

# Define a rule so we can track line numbers


def t_LBrace(t):
    r'{'
    return t


def t_RBrace(t):
    r'}'
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    # return t


def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'
t_ignore_COMMENT = r'[\#//].*'

# Error handling rule


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


print('lex start')
lexer = lex.lex()
print('lex end')
if __name__ == "__main__":
    # Build the lexer

    # Test it out
    data = '''
    gate 1 1.2 1.232

    '''

    # Give the lexer some input
    lexer.input(data)

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break      # No more input
        print(tok)
