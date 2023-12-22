from ply import lex, yacc

tokens = (
    'SUMA', 'RESTA', 'MULTIPLICACION', 'DIVISION','INT', 'FLOAT', 'CHAR', 'DOUBLE', 'BOOLEAN', 'LONG',
    'STRING', 'IF', 'ELSE', 'WHILE', 'DO', 'FOR', 'RETURN', 'COMA', 'PRINT', 'MAIN', 'VOID',
    'PARENTESIS_IZQ', 'PARENTESIS_DER', 'CORCHETE_IZQ', 'CORCHETE_DER',
    'ASIGNACION', 'MENOR_IGUAL', 'MAYOR_IGUAL', 'IGUAL', 'DISTINTO','MENOR', 'MAYOR',
    'AND', 'OR', 'NOT',
    'ID', 'NUMERO', 'CADENA',
    'PUNTO_Y_COMA', 'LLAVE_IZQ', 'LLAVE_DER',
)

reservado ={'if': 'IF','else': 'ELSE', 'while': 'WHILE','main':'MAIN',
           'do': 'DO','for': 'FOR', 'return': 'RETURN','break':'BREAK'}
t_PRINT= r'<<'
t_COMA = r','
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_PARENTESIS_IZQ = r'\('
t_PARENTESIS_DER = r'\)'
t_LLAVE_IZQ = r'\{'
t_LLAVE_DER = r'\}'
t_CORCHETE_IZQ = r'\['
t_CORCHETE_DER = r'\]'
t_ASIGNACION = r'='
t_MENOR = r'<'
t_MAYOR = r'>'
t_MENOR_IGUAL = r'<='
t_MAYOR_IGUAL = r'>='
t_IGUAL = r'=='
t_DISTINTO = r'!='
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_NUMERO = r'\d+'
t_CADENA = r'\"([^\\\n]|(\\.))*?\"'
t_PUNTO_Y_COMA = r';'

t_ignore = ' \t\n'

def t_MAIN(t):
    r'main'
    return t

def t_VOID(t):
    r'void'
    return t

def t_INT(t):
    r'int'
    return t

def t_FLOAT(t):
    r'float'
    return t

def t_CHAR(t):
    r'char'
    return t

def t_DOUBLE(t):
    r'double'
    return t

def t_BOOLEAN(t):
    r'boolean'
    return t

def t_STRING(t):
    r'string'
    return t

def t_LONG(t):
    r'long'
    return t


def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_DO(t):
    r'do'
    return t

def t_FOR(t):
    r'for'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reservado.get(t.value, 'ID')  
    return t

def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

precedence = (
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULTIPLICACION', 'DIVISION'),
)

def p_program(p):
    '''program : function_declaration program
               | main_function
    '''
    
def p_main_function(p):
    '''main_function : INT MAIN PARENTESIS_IZQ PARENTESIS_DER LLAVE_IZQ function_body LLAVE_DER'''


def p_function_declaration(p):
    '''function_declaration : variable ID PARENTESIS_IZQ argument_list PARENTESIS_DER LLAVE_IZQ function_body LLAVE_DER'''


def p_function_body(p):
    '''function_body : statement_list
        | vacio
    '''

def p_statement_list(p):
    '''statement_list : statement
        | statement_list statement
    '''

def p_statement(p):
    '''statement : assignment_statement 
        | expression_statement
        | if
        | while
        | do_while
        | for
        | return
        | function_call PUNTO_Y_COMA
    '''
def p_if_statement(p):
    '''if : IF PARENTESIS_IZQ expression PARENTESIS_DER LLAVE_IZQ statement_list LLAVE_DER
        | IF PARENTESIS_IZQ expression PARENTESIS_DER LLAVE_IZQ statement_list LLAVE_DER ELSE LLAVE_IZQ statement_list LLAVE_DER
    '''

def p_while_statement(p):
    '''while : WHILE PARENTESIS_IZQ expression PARENTESIS_DER LLAVE_IZQ statement_list LLAVE_DER'''

def p_do_while_statement(p):
    '''do_while : DO LLAVE_IZQ statement_list LLAVE_DER WHILE PARENTESIS_IZQ expression PARENTESIS_DER PUNTO_Y_COMA'''

def p_for_statement(p):
    '''for : FOR PARENTESIS_IZQ variable ID ASIGNACION expression PUNTO_Y_COMA expression PUNTO_Y_COMA expression PARENTESIS_DER LLAVE_IZQ statement_list LLAVE_DER'''

def p_return_statement(p):
    '''return : RETURN expression PUNTO_Y_COMA'''

def p_function_call(p):
    '''function_call : ID PARENTESIS_IZQ argument_list PARENTESIS_DER'''

def p_argument_list(p):
    '''argument_list : expression
        | expression COMA argument_list
        | variable expression
        | variable expression COMA argument_list
    '''

def p_assignment_statement(p):
    '''assignment_statement : variable ID ASIGNACION expression PUNTO_Y_COMA
        | variable ID CORCHETE_IZQ expression CORCHETE_DER ASIGNACION expression PUNTO_Y_COMA
        | ID ASIGNACION expression PUNTO_Y_COMA
    '''

def p_variable(p):
    '''variable : INT
        | FLOAT 
        | CHAR 
        | DOUBLE 
        | BOOLEAN 
        | LONG 
        | STRING 
        | VOID
    '''

def p_expression_statement(p):
    '''expression_statement : expression PUNTO_Y_COMA'''

def p_expression(p):
    '''expression : expression SUMA expression
        | expression RESTA expression
        | expression MULTIPLICACION expression
        | expression DIVISION expression
        | expression MENOR_IGUAL expression
        | expression MAYOR_IGUAL expression
        | expression IGUAL expression
        | expression DISTINTO expression
        | expression AND expression
        | expression OR expression
        | NOT expression
        | PARENTESIS_IZQ expression PARENTESIS_DER
        | LLAVE_IZQ expression LLAVE_DER  
        | NUMERO
        | CADENA
        | expression PRINT expression 
        | expression MENOR expression 
        | expression MAYOR expression
        | ID
    '''

def p_vacio(p):
    '''vacio : '''
    pass

def p_error(p):
    print("ENTRADA:\n")
    print(entrada_aux)
    print("Error de sintaxis (La sintaxis no es valida)", p)
    global accion
    accion = True 

def analizador(entrada):
    global entrada_aux
    entrada_aux = entrada 
    parser.parse(entrada, lexer=lexer)
    if not accion:
        print("ENTRADA:\n")
        print(entrada)
        print("\nLa entrada es sintácticamente válida")


parser = yacc.yacc()
accion=False

def leer(codigo_fuente):

    with open(codigo_fuente, 'r') as file:
        entrada = file.read()
    analizador(entrada)

codigo = 'ejemplo1.j'
leer(codigo)
print("\n\n")
codigo1 = 'ejemplo2.j'
leer(codigo1)
print("\n\n")
codigo2 = 'ejemplo3.j'
leer(codigo2)




