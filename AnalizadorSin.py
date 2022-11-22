import ply.yacc as yacc
from AnalizadorLex import tokens
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
def p_program(p):
    ''' '''
    p[0] = 1


def readFile(file):
    fp = codecs.open(file,"r","utf-8")
    cadena = fp.read()
    fp.close()
    return cadena

def main(file):
    print("<-------------------------->")
    print(f"[i] Tokens del lenguaje \n{tokens}")
    print("<-------------------------->")

    print(f"\n[i] analizando: {file}")

    if not os.path.exists(file):
        print("[!] No se encontro archivo")
        sys.exit(1)

    cadena = readFile(file)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("[!] uso ./AnalizadorSin.py file")
        sys.exit(1)

    main(sys.argv[1])