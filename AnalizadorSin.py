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
