
from src.attrExp import Accuracy, Noise, gateNum, AQV, crossTalk, Depth, OpenQASM
from YourObject import *
'''
Noise : Noise object according to IBM Q Rochester
AQV : Active Quantum Volume
crossTalk : Crosstalk according to IBM Q Boeblingen
gateNum : Number of operations used in the program
Depth : circuit depth
'''


#ObjectSet = {'Depth': (Depth, 'min','add'), 'Noise': (Noise, '<0.15', 'add')}
ObjectSet = {'Depth': (Depth, 'min'),'cross': (crossTalk, '<3')}
# TODO backendSet = {'OpenQASM' : (OpenQASM, 'output/tmp.qasm')}