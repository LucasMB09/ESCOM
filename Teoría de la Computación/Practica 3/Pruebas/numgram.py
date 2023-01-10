import nltk
from nltk import CFG
import re

grammar = CFG.fromstring("""
S -> term
term -> term | term num | term let
num -> 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 
let -> min | mayus
min -> a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z 
mayus -> A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z
""")

grammar.start()
grammar.productions()

cad = ['1','a','A','z']
parser = nltk.ChartParser(grammar)

for tree in parser.parse(cad):
    print(tree)

tree.draw()