import nltk
from nltk import CFG

grammar = CFG.fromstring("""
S -> SN SV
SN -> Det N
SV -> V | V N
Det -> 'el'
N -> 'perro' | 'gato' | 'huesos'
V -> 'duerme' | 'come'
""")

grammar.start()
grammar.productions()

cad = ['el','perro','come','huesos']
parser = nltk.ChartParser(grammar)

for tree in parser.parse(cad):
    print(tree)

tree.draw()