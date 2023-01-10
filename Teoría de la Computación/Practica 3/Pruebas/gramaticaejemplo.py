import nltk
from nltk import CFG

def saltaEspacios(cadena):
    nuevaCad = cadena.replace(' ','')
    tokens = list(nuevaCad)
    return tokens

grammar = CFG.fromstring("""
E -> SN SV ';'
SN -> ID '='
SV -> TERM | SV "+" TERM | SV "-" TERM
TERM -> FACTOR | TERM "*" FACTOR | TERM "/" FACTOR | TERM "%" FACTOR
FACTOR -> DIGITO | ID | "(" SV ")"
ID -> ID LETRA | ID DIGITO | LETRA | DIGITO
DIGITO -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' 
LETRA -> 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z' | 'A' | 'B' | 'C' | 'D' | 'E' | 'F' | 'G' | 'H' | 'I' | 'J' | 'K' | 'L' | 'M' | 'N' | 'O' | 'P' | 'Q' | 'R' | 'S' | 'T' | 'U' | 'V' | 'W' | 'X' | 'Y' | 'Z'

""")

grammar.start()
grammar.productions()

cad = input("Introduce la cadena:")
tokens = saltaEspacios(cad)
print(tokens)
parser = nltk.ChartParser(grammar)

for tree in parser.parse(tokens):
    print(tree)

tree.draw()