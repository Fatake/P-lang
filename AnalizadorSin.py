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

def p_program(p):
    'program : MODULO ID ENDSENTENCE librerias DEFINE PMAIN LPARENT RPARENT LCORCHE instrucciones RCORCHE'
    
def p_librerias(p):
    'librerias : IMPORTA ID ENDSENTENCE librerias'

def p_librerias_emp(p):
    'librerias : empty'
    
def p_instrucciones_dec(p):
    'instrucciones : declaraciones '
    
def p_instrucciones_cic(p):
    'instrucciones : ciclos '
    
def p_instrucciones_con(p):
    'instrucciones : condicionales '
    
def p_instrucciones_exp(p):
    'instrucciones : expresiones ENDSENTENCE'
    
def p_instrucciones_ins(p):
    'instrucciones : instrucciones'

def p_instrucciones_emp(p):
    'instrucciones : empty'
 
def p_declaraciones(p):
    'declaraciones : VAR ID ENDSENTENCE'
    
def p_declaraciones_exp(p):
    'declaraciones : VAR ID ASIGNA expresiones ENDSENTENCE'
    
def p_condicionales(p):
    'condicionales : SI LPARENT expresiones RPARENT LCORCHE instrucciones RCORCHE sinocondicion'
    
def p_sinocondicion(p):
    'sinocondicion : SINO LCORCHE instrucciones RCORCHE'

def p_sinocondicion_emp(p):
    'sinocondicion : empty'

def p_ciclos(p):
    'ciclos : PARA LPARENT ID COMA ID RPARENT EN LPARENT condicionfor RPARENT LCORCHE instrucciones RCORCHE'
    
def p_condicionfor_ID(p):
    'condicionfor : ID '

def p_condicionfor_exp(p):
    'condicionfor : expresiones '

def p_expression_plus(p):
    'expresiones : expresiones SUMA terminos'
    p[0] = p[1] + p[3]

def p_expression_equal(p):
    'expresiones : expresiones IGUALDAD terminos'
    p[0] = p[1] 

def p_expression_minus(p):
    'expresiones : expresiones RESTA terminos'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expresiones : terminos'
    p[0] = p[1]

def p_term_times(p):
    'terminos : terminos MUTIPLICA factor'
    p[0] = p[1] * p[3]

def p_term_div(p):
    'terminos : terminos DIVIDE factor'
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'terminos : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMERO'
    p[0] = p[1]

def p_factor_ID(p):
    'factor : ID'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPARENT expresiones RPARENT'
    p[0] = p[2]
    
def p_empy(p):
    'empty :'
    pass

# Error rule for syntax errors
def p_error(p):
    print(f"[!] Syntax error in line: {str(p.lineno)}")

def analizadorSin(cadena):
    # Build the parser
    parser = yacc.yacc()
    while True:
        result = parser.parse(cadena)
        print(result)

def main():
    if len(sys.argv) != 2:
        print("[!] uso ./AnalizadorSin.py file")
        sys.exit(1)

    cadena = readFile(sys.argv[1])
    tokensAnalizados = analisisLex(cadena)
    analizadorSin(cadena)

if __name__ == "__main__":
    main()