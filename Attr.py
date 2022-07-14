
from src.attrExp import Accuracy, Noise, gateNum, AQV, crossTalk, Depth, OpenQASM, Fidelity, QubitCount
from YourObject import *
'''
Noise : Noise object according to IBM Q Rochester
AQV : Active Quantum Volume
crossTalk : Crosstalk according to IBM Q Boeblingen
gateNum : Number of operations used in the program
Depth : circuit depth
'''


ObjectSet = {'Fidelity': (Fidelity, 'max','add'), 'QubitCount': (QubitCount, '<10')}

# ObjectSet = {'Depth': (Depth, 'min'),'cross': (crossTalk, '<3')}
