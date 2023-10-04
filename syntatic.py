import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from lexic_2 import tokens

import webbrowser

# Define the parser start symbol
start = 'programa_SOL'

print("tokens=",tokens)
# print("tokens=",tokens)

def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

# Define new production rules for programa_SOL and navegador
def p_programa_SOL(p):
    'programa_SOL : PROGRAMA_SOL LOOP NUMBER NAVEGAR NO_LIMIT'
    p[0] = p[1]  # You can define the behavior for programa_SOL here
    print(f"Programa SOL {p[3]}")
    chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open('http://www.google.com', new=2)  # Opens Google Chrome
    print("Google Chrome opened.")


def p_command_navegar(p):
    'programa_SOL : NAVEGAR'
    chrome_path = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open('http://www.google.com', new=2)  # Opens Google Chrome
    print("Google Chrome opened.")


# def p_expression_explore(p):
#    'expression : EXPLORE'
#    p[0] = p[1]

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = input('Enter input: ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)
