import ply.lex as lex

# Reserved words
reserved = {
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'while': 'WHILE',
    'int': 'INT',
    'real': 'REAL',
    'boolean': 'BOOLEAN',
    'print': 'PRINT',
    'return': 'RETURN',
    'function': 'FUNCTION',
    'write': 'WRITE',
    'read': 'READ',
    'for': 'FOR',
    'programa_SOL': 'PROGRAMA_SOL',
    'sequencia': 'SEQUENCIA',
    'tempo': 'TEMPO',
    'fases_EPIC': 'FASES_EPIC',
    'Explore': 'EXPLORE',
    'Interact': 'INTERACT',
    'Present': 'PRESENT',
    'Critique': 'CRITIQUE',
    'navegar': 'NAVEGAR',
    'browser': 'BROWSER',
    'visualizar_pdf': 'VISUALIZAR_PDF',
    'visualizar_video': 'VISUALIZAR_VIDEO',
    'videoconferencia': 'VIDEOCONFERENCIA',
    'whatsapp_web': 'WHATSAPP_WEB',
    'email': 'EMAIL',
    'begin': 'BEGIN',
    'end': 'END',
    '30_min': '30MIN',
    '1_hora': '1HORA',
    '1_dia': '1DIA',
    '2_dias': '2DIAS',
    'sem_limite': 'NO_LIMIT',
    'false': 'FALSE',
    'true': 'TRUE',
    'empty': 'EMPTY',
    'link_pdf': 'LINK_PDF',
    'link_video': 'LINK_VIDEO',
    'link_videoconferencia': 'LINK_VIDEOCONFERENCIA',
    'link_whatsapp_web': 'LINK_WHATSAPP_WEB',
    'link_email': 'LINK_EMAIL',
    'navegador': 'NAVEGADOR',
}

# List of token names
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
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_DS_POINT_COMMA = r'\;'
t_DS_COMMA = r'\,'
t_DS_POINT = r'\.'
t_DS_OCOCH = r'\['
t_DS_CCOCH = r'\]'
t_DS_OKEY = r'\{'
t_DS_CKEY = r'\}'
t_RO_EQUAL = r'\=\='
t_RO_THAN_MORE = r'\>'
t_RO_THAN_LESS = r'\<'
t_RO_THAN_MORE_OR_EQUAL = r'\>\='
t_RO_THAN_LESS_OR_EQUAL = r'\<\='
t_RO_DIFF = r'\!'

# A regular expression rule for numbers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# A regular expression rule for alphabetic identifiers
def t_ALPHA(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ALPHA')  # Check for reserved words
    return t

# Define a rule to track line numbers when a newline character is encountered
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Test input data
datas = []
acc0 = 0
data = "0"
while data != '':
    data = input(f"{acc0}: ")
    if data != '':
        datas.append(data)
        acc0 += 1

# Join input lines into a single string
datas2 = []
for i in datas:
    datas2.append(i+"\n")
# print(datas2)
data_joineds = str("")
data_joineds = data_joineds.join(datas2)
# print(data_joineds)

# Build the lexer
lexer = lex.lex()
lexer.input(data_joineds)

# Tokenize and print the tokens
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)