
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASIGNA CARACTERES CHARACTER COMA DEFINE DIFERENCIA DIVIDE EN ENDSENTENCE ENTERO ID IGUALDAD IMPORTA LBRACKET LCORCHE LPARENT MAYOIGUA MAYORQUE MENOIGUAL MENORQUE MODULO MUTIPLICA NUMERO PARA PMAIN RBRACKET RCORCHE RESTA RETORNA RPARENT SI SINO SUMA VARprogram : modulo librerias funcionmainmodulo : MODULO ID ENDSENTENCEfuncionmain : DEFINE PMAIN LPARENT RPARENT LCORCHE instrucciones RCORCHElibrerias : IMPORTA ID ENDSENTENCE libreriaslibrerias : emptyinstrucciones : declaraciones instrucciones : ciclos instrucciones : condicionales instrucciones : expresiones ENDSENTENCEinstrucciones : instruccionesinstrucciones : emptydeclaraciones : VAR ID ENDSENTENCEdeclaraciones : VAR ID ASIGNA expresiones ENDSENTENCEcondicionales : SI LPARENT expresiones RPARENT LCORCHE instrucciones RCORCHE sinocondicionsinocondicion : SINO LCORCHE instrucciones RCORCHEsinocondicion : emptyciclos : PARA LPARENT ID COMA ID RPARENT EN LPARENT condicionfor RPARENT LCORCHE instrucciones RCORCHEcondicionfor : expresiones expresiones : expresiones SUMA terminosexpresiones : expresiones IGUALDAD terminosexpresiones : expresiones RESTA terminosexpresiones : terminosterminos : terminos MUTIPLICA factorterminos : terminos DIVIDE factorterminos : factorfactor : NUMEROfactor : IDfactor : LPARENT expresiones RPARENTempty :'
    
_lr_action_items = {'MODULO':([0,],[3,]),'$end':([1,8,33,],[0,-1,-3,]),'IMPORTA':([2,11,13,],[5,-2,5,]),'DEFINE':([2,4,6,11,13,15,],[-29,9,-5,-2,-29,-4,]),'ID':([3,5,17,18,25,35,36,37,39,40,41,42,48,54,58,63,69,72,],[7,10,26,26,38,26,26,26,49,26,26,26,26,57,26,26,26,26,]),'ENDSENTENCE':([7,10,23,26,29,30,31,38,43,44,45,46,51,52,53,],[11,13,34,-27,-22,-25,-26,47,-28,-19,-20,-21,-23,-24,56,]),'PMAIN':([9,],[12,]),'LPARENT':([12,17,18,27,28,35,36,37,40,41,42,48,58,61,63,69,72,],[14,18,18,39,40,18,18,18,18,18,18,18,18,63,18,18,18,]),'RPARENT':([14,26,29,30,31,32,43,44,45,46,50,51,52,57,67,68,],[16,-27,-22,-25,-26,43,-28,-19,-20,-21,55,-23,-24,59,70,-18,]),'LCORCHE':([16,55,65,70,],[17,58,69,72,]),'VAR':([17,58,69,72,],[25,25,25,25,]),'PARA':([17,58,69,72,],[27,27,27,27,]),'SI':([17,58,69,72,],[28,28,28,28,]),'RCORCHE':([17,19,20,21,22,24,34,47,56,58,60,62,64,66,69,71,72,73,74,75,],[-29,33,-6,-7,-8,-11,-9,-12,-13,-29,62,-29,-14,-16,-29,73,-29,-15,75,-17,]),'NUMERO':([17,18,35,36,37,40,41,42,48,58,63,69,72,],[31,31,31,31,31,31,31,31,31,31,31,31,31,]),'SUMA':([23,26,29,30,31,32,43,44,45,46,50,51,52,53,68,],[35,-27,-22,-25,-26,35,-28,-19,-20,-21,35,-23,-24,35,35,]),'IGUALDAD':([23,26,29,30,31,32,43,44,45,46,50,51,52,53,68,],[36,-27,-22,-25,-26,36,-28,-19,-20,-21,36,-23,-24,36,36,]),'RESTA':([23,26,29,30,31,32,43,44,45,46,50,51,52,53,68,],[37,-27,-22,-25,-26,37,-28,-19,-20,-21,37,-23,-24,37,37,]),'MUTIPLICA':([26,29,30,31,43,44,45,46,51,52,],[-27,41,-25,-26,-28,41,41,41,-23,-24,]),'DIVIDE':([26,29,30,31,43,44,45,46,51,52,],[-27,42,-25,-26,-28,42,42,42,-23,-24,]),'ASIGNA':([38,],[48,]),'COMA':([49,],[54,]),'EN':([59,],[61,]),'SINO':([62,],[65,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'modulo':([0,],[2,]),'librerias':([2,13,],[4,15,]),'empty':([2,13,17,58,62,69,72,],[6,6,24,24,66,24,24,]),'funcionmain':([4,],[8,]),'instrucciones':([17,58,69,72,],[19,60,71,74,]),'declaraciones':([17,58,69,72,],[20,20,20,20,]),'ciclos':([17,58,69,72,],[21,21,21,21,]),'condicionales':([17,58,69,72,],[22,22,22,22,]),'expresiones':([17,18,40,48,58,63,69,72,],[23,32,50,53,23,68,23,23,]),'terminos':([17,18,35,36,37,40,48,58,63,69,72,],[29,29,44,45,46,29,29,29,29,29,29,]),'factor':([17,18,35,36,37,40,41,42,48,58,63,69,72,],[30,30,30,30,30,30,51,52,30,30,30,30,30,]),'sinocondicion':([62,],[64,]),'condicionfor':([63,],[67,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> modulo librerias funcionmain','program',3,'p_program','AnalizadorSin.py',23),
  ('modulo -> MODULO ID ENDSENTENCE','modulo',3,'p_modulo','AnalizadorSin.py',26),
  ('funcionmain -> DEFINE PMAIN LPARENT RPARENT LCORCHE instrucciones RCORCHE','funcionmain',7,'p_funcionmain','AnalizadorSin.py',29),
  ('librerias -> IMPORTA ID ENDSENTENCE librerias','librerias',4,'p_librerias','AnalizadorSin.py',32),
  ('librerias -> empty','librerias',1,'p_librerias_emp','AnalizadorSin.py',35),
  ('instrucciones -> declaraciones','instrucciones',1,'p_instrucciones_dec','AnalizadorSin.py',38),
  ('instrucciones -> ciclos','instrucciones',1,'p_instrucciones_cic','AnalizadorSin.py',41),
  ('instrucciones -> condicionales','instrucciones',1,'p_instrucciones_con','AnalizadorSin.py',44),
  ('instrucciones -> expresiones ENDSENTENCE','instrucciones',2,'p_instrucciones_exp','AnalizadorSin.py',47),
  ('instrucciones -> instrucciones','instrucciones',1,'p_instrucciones_ins','AnalizadorSin.py',50),
  ('instrucciones -> empty','instrucciones',1,'p_instrucciones_emp','AnalizadorSin.py',53),
  ('declaraciones -> VAR ID ENDSENTENCE','declaraciones',3,'p_declaraciones','AnalizadorSin.py',56),
  ('declaraciones -> VAR ID ASIGNA expresiones ENDSENTENCE','declaraciones',5,'p_declaraciones_exp','AnalizadorSin.py',59),
  ('condicionales -> SI LPARENT expresiones RPARENT LCORCHE instrucciones RCORCHE sinocondicion','condicionales',8,'p_condicionales','AnalizadorSin.py',62),
  ('sinocondicion -> SINO LCORCHE instrucciones RCORCHE','sinocondicion',4,'p_sinocondicion','AnalizadorSin.py',65),
  ('sinocondicion -> empty','sinocondicion',1,'p_sinocondicion_emp','AnalizadorSin.py',68),
  ('ciclos -> PARA LPARENT ID COMA ID RPARENT EN LPARENT condicionfor RPARENT LCORCHE instrucciones RCORCHE','ciclos',13,'p_ciclos','AnalizadorSin.py',71),
  ('condicionfor -> expresiones','condicionfor',1,'p_condicionfor_exp','AnalizadorSin.py',74),
  ('expresiones -> expresiones SUMA terminos','expresiones',3,'p_expression_plus','AnalizadorSin.py',77),
  ('expresiones -> expresiones IGUALDAD terminos','expresiones',3,'p_expression_equal','AnalizadorSin.py',81),
  ('expresiones -> expresiones RESTA terminos','expresiones',3,'p_expression_minus','AnalizadorSin.py',85),
  ('expresiones -> terminos','expresiones',1,'p_expression_term','AnalizadorSin.py',89),
  ('terminos -> terminos MUTIPLICA factor','terminos',3,'p_term_times','AnalizadorSin.py',93),
  ('terminos -> terminos DIVIDE factor','terminos',3,'p_term_div','AnalizadorSin.py',97),
  ('terminos -> factor','terminos',1,'p_term_factor','AnalizadorSin.py',101),
  ('factor -> NUMERO','factor',1,'p_factor_num','AnalizadorSin.py',105),
  ('factor -> ID','factor',1,'p_factor_ID','AnalizadorSin.py',109),
  ('factor -> LPARENT expresiones RPARENT','factor',3,'p_factor_expr','AnalizadorSin.py',113),
  ('empty -> <empty>','empty',0,'p_empy','AnalizadorSin.py',117),
]
