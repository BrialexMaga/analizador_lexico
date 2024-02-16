from ply.lex import lex

tokens = (
    'IDENTIFICADOR',
    'ENTERO',
    'REAL',
    'CADENA',
    'TIPO',
    'OPSUMA',
    'OPMUL',
    'OPRELAC',
    'OPOR',
    'OPAND',
    'OPNOT',
    'OPIGUALDAD',
    'PUNTOCOMA',
    'COMA',
    'PARENTESISIZQ',
    'PARENTESISDER',
    'LLAVEIZQ',
    'LLAVEDER',
    'ASIGNACION',
    'IF',
    'WHILE',
    'RETURN',
    'ELSE',
    'SIGNODINERO'
)

# Expresiones regulares para los tokens
t_IDENTIFICADOR = r'[a-zA-Z_][a-zA-Z_0-9]*'
t_ENTERO = r'\d+'
t_REAL = r'\d+\.\d+'
t_CADENA = r'\".*\"'
t_TIPO = r'int|float|void'
t_OPSUMA = r'\+|-'
t_OPMUL = r'\*|/'
t_OPRELAC = r'<|>|<=|>=|==|!='
t_OPOR = r'\|\|'
t_OPAND = r'&&'
t_OPNOT = r'!'
t_OPIGUALDAD = r'==|!='
t_PUNTOCOMA = r';'
t_COMA = r','
t_PARENTESISIZQ = r'\('
t_PARENTESISDER = r'\)'
t_LLAVEIZQ = r'\{'
t_LLAVEDER = r'\}'
t_ASIGNACION = r'='
t_IF = r'if'
t_WHILE = r'while'
t_RETURN = r'return'
t_ELSE = r'else'
t_SIGNODINERO = r'\$'

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Expresión regular para manejar errores
def t_error(t):
    print(f'Caracter no reconocido: {t.value[0]}')
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comments(t):
    r'/\*(.|\n)*?\*/'
    # No return value. Token discarded

def t_comments_oneline(t):
    r'//.*\n'
    # No return value. Token discarded

lexer = lex()

# Test it out
data = """
/* Esto es un comentario */
// Esto es otro comentario
3 + 4 * 10
  + -20 *2
"""

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)



'''
from enum import Enum

class Alfabeto(Enum):
    IDENTIFICADOR = 0
    ENTERO = 1
    REAL = 2
    CADENA = 3
    TIPO = 4 # int, float, void
    OPSUMA = 5 # +, -
    OPMUL = 6 # *, /
    OPRELAC = 7 # <, >, <=, >=, ==, !=
    OPOR = 8 # ||
    OPAND = 9 # &&
    OPNOT = 10 # !
    OPIGUALDAD = 11 # ==, !=
    PUNTOCOMA = 12 # ;
    COMA = 13 # ,
    PARENTESISIZQ = 14 # (
    PARENTESISDER = 15 # )
    LLAVEIZQ = 16 # {
    LLAVEDER = 17 # }
    ASIGNACION = 18 # =
    IF = 19
    WHILE = 20
    RETURN = 21
    ELSE = 22
    SIGNODINERO = 23 # $
    DESCONOCIDO = 24
    FIN = 25

    def isdigit(s):
        return s.isdigit()

    def isidentifier(s):
        s = str(s)
        if not s[0].isalpha():
            return False
        for char in s[1:]:
            if not (char.isalpha() or char.isdigit()):
                return False
        
        return True


    @staticmethod
    def get_token(word):
        word = str(word)

        if not word:
            return Alfabeto.IDENTIFICADOR
        elif not word:
            return Alfabeto.ENTERO
        elif word.replace('.', '', 1).isdigit():
            return Alfabeto.REAL
        elif word in ['int', 'float', 'void']:
            return Alfabeto.TIPO
        elif word in ['+', '-']:
            return Alfabeto.OPSUMA
        elif word in ['*', '/']:
            return Alfabeto.OPMUL
        elif word in ['<', '>', '<=', '>=', '==', '!=']:
            return Alfabeto.OPRELAC
        elif word == '||':
            return Alfabeto.OPOR
        elif word == '&&':
            return Alfabeto.OPAND
        elif word == '!':
            return Alfabeto.OPNOT
        elif word in ['==', '!=']:
            return Alfabeto.OPIGUALDAD
        elif word == ';':
            return Alfabeto.PUNTOCOMA
        elif word == ',':
            return Alfabeto.COMA
        elif word == '(':
            return Alfabeto.PARENTESISIZQ
        elif word == ')':
            return Alfabeto.PARENTESISDER
        elif word == '{':
            return Alfabeto.LLAVEIZQ
        elif word == '}':
            return Alfabeto.LLAVEDER
        elif word == '=':
            return Alfabeto.ASIGNACION
        elif word == 'if':
            return Alfabeto.IF
        elif word == 'while':
            return Alfabeto.WHILE
        elif word == 'return':
            return Alfabeto.RETURN
        elif word == 'else':
            return Alfabeto.ELSE
        elif word == '$':
            return Alfabeto.SIGNODINERO
        else:
            return Alfabeto.DESCONOCIDO
'''