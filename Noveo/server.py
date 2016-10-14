#!/usr/bin/env python
import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from calclex import tokens

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
    p[0] = (p[1]+0.0) / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

def application(environ, start_response):
                body=''
                if environ['REQUEST_METHOD'] == 'POST':
                        try:
                            request_body_size = int(environ.get('CONTENT_LENGTH', 0))
                        except (ValueError):
                            request_body_size = 0

                        request_body = environ['wsgi.input'].read(request_body_size)
                        print(request_body)
                        parser= yacc.yacc(debug=0, write_tables=0)
                        res=str(parser.parse(request_body))
                        print(res)

                start_response("200 Ok",
                 [("Content-Type", "text/xml"),
                  ("Content-Length", str(len(res)))])

                return [res]
