import ply.yacc as yacc
import ply.lex as lex
from AnalizadorLex import tokens,analisisLex,readFile
import AnalizadorLex
import re
import codecs
import os
import sys

## Cuales analizar por derecha y por izquiereda
precendece = (
    ('right','ASIGNA'), ## Menor Preferencia
    ('left','DIFERENCIA'),
    ('left','MENORQUE','MAYORQUE','MENOIGUAL','MAYOIGUA'),
    ('left','SUMA','RESTA'),
    ('left','MUTIPLICA','DIVIDE'),
    ('left','LPARENT','RPARENT'), ## mayor preferencia
)

## Analisis de producciones
## p -> producction
'''
def p_program(p):
    program = block
    p[0] = program(p[1], "program")

def p_constDecl(p):
    constDecl = const constAssignmentList ; '''
    
def p_constDeclEmpy(p):
    'constDecl :'
    pass

def p_expression_plus(p):
    'expression : expression SUMA term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression RESTA term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term MUTIPLICA factor'
    p[0] = p[1] * p[3]

def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMERO'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPARENT expression RPARENT'
    p[0] = p[2]

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

def analizadorSin(tokensAnalizados):
    # Build the parser
    parser = yacc.yacc()
    while True:
        try:
            s = input('calc > ')
        except EOFError:
            break
        if not s: 
            continue
        result = parser.parse(s)
        print(result)

def main():
    if len(sys.argv) != 2:
        print("[!] uso ./AnalizadorSin.py file")
        sys.exit(1)

    cadena = readFile(sys.argv[1])
    tokensAnalizados = analisisLex(cadena)
    analizadorSin(tokensAnalizados)

if __name__ == "__main__":
    main()