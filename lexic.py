import ply.lex as lex
import string as st


reserved = {
    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE',
    'while' : 'WHILE',
    'int':'INT', 'real':'REAL', 'boolean':'BOOLEAN',
    'print':'PRINT',
    'return':'RETURN', 'function':'FUNCTION',
    'write':'WRITE', 'read':'READ',
    'for':'FOR',
    
    'programa_SOL':'PROGRAMA_SOL', 'sequencia':'SEQUENCIA', 'tempo':'TEMPO', 'fases_EPIC':'FASES_EPIC',
    'Explore':'EXPLORE', 'Interact':'INTERACT', 'Present':'PRESENT', 'Critique':'CRITIQUE',
    'navegar':'NAVEGAR', 'browser':'BROWSER',
    'visualizar_pdf':'VISUALIZAR_PDF', 'visualizar_video':'VISUALIZAR_VIDEO', 'videoconferencia':'VIDEOCONFERENCIA',
    'whatsapp_web':'WHATSAPP_WEB', 'email':'EMAIL',

    'begin':'BEGIN','end':'END',

    "30_min":"30MIN", "1_hora":"1HORA", "1_dia":"1DIA",
    "2_dias":"2DIAS", "sem_limite":"NO_LIMIT",

    "false":"FALSE", "true":"TRUE", "empty":"EMPTY",
}


# List of token names.   This is always required
tokens = [
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'DS_POINT_COMMA',
    'DS_COMMA',
    'DS_POINT',
    'DS_OCOCH',
    'DS_CCOCH',
    'DS_OKEY',
    'DS_CKEY',
    'RO_EQUAL',
    'RO_THAN_MORE',
    'RO_THAN_LESS',
    'RO_THAN_MORE_OR_EQUAL',
    'RO_THAN_LESS_OR_EQUAL',
    'RO_DIFF',
    'ALPHA',
] + list(reserved.values())

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_DS_POINT_COMMA = r'\;'
t_DS_COMMA = r'\,'
t_DS_POINT = r'\.'
t_DS_OCOCH = r'\['
t_DS_CCOCH = r'\]'
t_DS_OKEY = r'\{'
t_DS_CKEY = r'\}'
t_RO_EQUAL = r"\=\="
t_RO_THAN_MORE = r"\>"
t_RO_THAN_LESS = r"\<"
t_RO_THAN_MORE_OR_EQUAL = r"\>\="
t_RO_THAN_LESS_OR_EQUAL = r"\<\="
t_RO_DIFF = r"\!"

# t_A = r'\a'
# t_B = r'\a'
# t_C = r'\a'
# t_D = r'\a'
# t_E = r'\a'
# t_F = r'\a'
# t_G = r'\a'
# t_H = r'\a'
# t_I = r'\a'
# t_J = r'\a'
# t_K = r'\a'
# t_L = r'\a'
# t_M = r'\a'
# t_N = r'\a'
# t_O = r'\a'
# t_P = r'\a'
# t_Q = r'\a'
# t_R = r'\a'
# t_S = r'\a'
# t_T = r'\a'
# t_U = r'\a'
# t_A = r'\a'
# t_A = r'\a'
# t_A = r'\a'
# t_A = r'\a'

t_PROGRAMA_SOL = r'programa_SOL'
t_INT = r'int'
t_REAL = r'real'
t_BOOLEAN = r'boolean'
t_PRINT = r'print'
t_RETURN = r'return'
t_FUNCTION = r'function'
t_WRITE = r'write'
t_READ = r'read'
t_FOR = r'for'
t_FASES_EPIC = r'fases_EPIC'
t_TEMPO = r'tempo'
t_SEQUENCIA = r'sequencia'
t_EXPLORE = r'Explore'
t_CRITIQUE = r'Critique'
t_INTERACT = r'Interact'
t_PRESENT = r'Present'
t_NAVEGAR = r'navegar'
t_BROWSER = r'browser'
t_VISUALIZAR_VIDEO = r'visualizar_video'
t_VISUALIZAR_PDF = r'visualizar_pdf'
t_VIDEOCONFERENCIA = r'videoconferencia'
t_EMAIL = r'email'
t_WHATSAPP_WEB = r'whatsapp_web'
t_END = r'end'
t_BEGIN = r'begin'
t_30MIN = r"30_min"
t_1HORA = r"1_hora"
t_1DIA = r"1_dia"
t_2DIAS = r"2_dias"
t_NO_LIMIT = r"sem_limite"
t_EMPTY = r"empty"
t_FALSE = r"false"
t_TRUE = r"true"


# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t


def t_ALPHA(t):
    r'st.ascii_letters}'
    t.value = int(t.value)
    return t.value


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'
t_ignore_COMMENT = r'\/\/.*'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


datas = []
acc0 = 0
data = "0"
while (data!=''):
    data = input(f"{acc0}: ")
    if (data!=''):
        datas.append(data)
        acc0+=1
# print(datas," acc0=",acc0)
data_joineds = str("")
for i in datas:
    data_joineds = data_joineds+i

    # print(data_joineds)


# Build the lexer
lexer = lex.lex()
lexer.input(data_joineds)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)
# print(help(lexer))