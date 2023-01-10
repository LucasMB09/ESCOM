import nltk
from nltk import CFG

g3 = """
O -> SN SV | O Conj O
SN -> Det N | Det N Adj | Det Adj N | NProp | SN SP
SV -> V | V SN | V SP | V SN SP
SP -> Prep SN
Det -> 'el' | 'la' | 'un' | 'una' 
N -> 'niño' | 'niña' | 'manzana' | 'pera' | 'cuchillo'
NProp -> 'Juan' | 'Ana' | 'Perico' 
Adj -> 'bonito' | 'pequeña' | 'verde'
V -> 'come' | 'salta' | 'pela' | 'persigue'
Prep -> 'de' | 'con' | 'desde' | 'a'
Conj -> 'y' | 'pero'
"""

analizador3 = nltk.ChartParser(nltk.CFG.fromstring(g3))
for tree in analizador3.parse("""la manzana salta y el niño come pero el cuchillo 
verde persigue a la pequeña manzana de Ana""".split()):
    print(tree)

tree.draw()