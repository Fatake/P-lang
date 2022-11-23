import ply.lex as lex
import sys
import re
import codecs
import os

# Diccionario de palabras reservadas
reserved = {
    'Main':'PMAIN',
    'entero':'ENTERO',
    'var':'VAR',
    'si':'SI',
    'sino':'SINO', 
    'para':'PARA',
    'en':'EN',
    'importa':'IMPORTA',
    'modulo':'MODULO',
    'define':'DEFINE',
    'retorna':'RETORNA'
}

tokens = [
    'ID',# identificador
    'NUMERO', # 123
    'SUMA', # +
    'RESTA', # -
    'MUTIPLICA', # *
    'DIVIDE', # /
    'ASIGNA', # =
    'DIFERENCIA', # !=
    'MENORQUE', # <
    'MAYORQUE', # >
    'MENOIGUAL', # <=
    'MAYOIGUA', # >=
    'IGUALDAD', # ==
    'LPARENT', # (
    'RPARENT', # )
    'LCORCHE', # {
    'RCORCHE', # }
    'LBRACKET', # [
    'RBRACKET', # ]
    'COMA', # ,
    'ENDSENTENCE', # ;
    'CHARACTER', # a
    'CARACTERES' # asdAd
] + list(reserved.values())

t_ignore = '\r'

# Identificador
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')
    return t

# Tokes de Operador
t_SUMA             = r'\+'
t_RESTA            = r'-'
t_MUTIPLICA        = r'\*'
t_DIVIDE           = r'/'
t_MENORQUE         = r'<'
t_MAYORQUE         = r'>'
t_MENOIGUAL        = r'<='
t_MAYOIGUA         = r'>='
t_IGUALDAD         = r'=='
t_DIFERENCIA       = r'!='
t_ASIGNA           = r'='

# Tokes de Delimitación
t_LPARENT          = r'\('
t_RPARENT          = r'\)'
t_LBRACKET         = r'\['
t_RBRACKET         = r'\]'
t_LCORCHE          = r'\{'
t_RCORCHE          = r'\}'
t_COMA             = r','
t_ENDSENTENCE          = r';'

# Enteros
t_NUMERO = r'\d+([uU]|[lL]|[uU][lL]|[lL][uU])?'

# Caracteres
t_CARACTERES = r'\"([^\\\n]|(\\.))*?\"'

# Character constant 'c' or L'c'
t_CHARACTER = r'(L)?\'([^\\\n]|(\\.))*?\''

def t_SPACE(t):
    r'\ '
    pass

# Comentario  en linea // comentario
def t_COMMENTINLINE(t):
    r'//.*'
    pass
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
# Comentarios /* Some */
def t_COMMENT(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    return t

# Si un token es invalido
def t_error(t):
    print("Caracter no reconocido -> %s" % t.value[0])
    t.lexer.skip(1)

def readFile(file):
    if not os.path.exists(file):
        print("[!] No se encontro archivo")
        sys.exit(1)

    fp = codecs.open(file,"r","utf-8")
    cadena = fp.read()
    fp.close()
    return cadena

def analisisLex(cadena):
    analizador = lex.lex()
    analizador.input(cadena)
    tokensAnalizados = []
    while True:
        tok = analizador.token()
        if not tok : 
            break
        print(tok)
        tokensAnalizados.append(tok)
    return tokensAnalizados

def main(file):
    print("<-------------------------->")
    print(f"[i] Tokens del lenguaje \n{tokens}")
    print("<-------------------------->")

    print(f"\n[i] analizando: {file}")

    cadena = readFile(file)
    analisisLex(cadena)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("[!] uso ./AnalizadorLex.py file")
        sys.exit(1)

    main(sys.argv[1])