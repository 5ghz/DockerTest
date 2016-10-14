#!/usr/bin/env python
import sys
import compiler
#str='12+2/3*3-6'
str='2/3*3'
ast= compiler.parse( str )
print(ast)
