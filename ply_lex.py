import ply.lex as lex


tokens = (
    'EOF',
	'NEWLINE',
	'NUMBER',
	'IDENT',
	'STRING',
	# Keywords.
	'LABEL',
	'GOTO' ,
	'PRINT',
	'INPUT',
	'LET',
	'IF' ,
	'THEN',
	'ENDIF',
	'WHILE',
	'REPEAT' ,
	'ENDWHILE',
	# Operators.
    'EQ' ,
	'PLUS',
	'MINUS',
	'ASTERISK',
	'SLASH',
	'EQEQ' ,
	'NOTEQ',
	'LT' ,
	'LTEQ',
	'GT' ,
	'GTEQ',
)

# Palavras reservadas
reserved = {
    'LABEL' : 'LABEL',
	'GOTO'  : 'GOTO',
	'PRINT' : 'PRINT',
	'INPUT' : 'INPUT',
	'LET' : 'LET',
	'IF'  : 'IF',
	'THEN' : 'THEN',
	'ENDIF' : 'ENDIF',
	'WHILE' : 'WHILE',
	'REPEAT'  : 'REPEAT',
	'ENDWHILE' : 'ENDWHILE',
}


# Tokens simples que não precisam de nenhuma ação
t_EQ = r'\='
t_PLUS = r'\+'
t_MINUS = r'-'
t_ASTERISK = r'\*'
t_SLASH = r'\/'
t_EQEQ = r'\=\='
t_NOTEQ = r'\!\='
t_LT = r'\<'
t_LTEQ = r'\<\='
t_GT = r'\>'
t_GTEQ = r'\>\='

t_EOF = r'\0'



# Token que precisa de alguma ação
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_STRING(t):
    r'("[^"]*")|(\'[^\']*\')'
    t.values= str(t.value)
    return t

def t_IDENT(t):
    r'\w+'        
    if t.value in reserved:        
        pass
    else:
        t.values = str(t.value)
    return t




# Contabiliza nova linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Descarta comentário
t_ignore_COMMENT = r'\#.*'
# ignora espaço e tab
t_ignore  = ' \t'

data = '''
#comentario
LABEL
variavel =  "isso eh pra  ser uma string"
21 / 4 * 10
   + -20 *2
 '''

lexer = lex.lex()
lexer.input(data)

while True:
     tok = lexer.token()
     if not tok: 
         break      # No more input
     print(tok)
