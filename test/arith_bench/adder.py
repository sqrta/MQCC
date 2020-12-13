""" adder.py - Cirq implementation of the adder function.


=== Reference ===
In place: a,b -> a+b,b from https://arxiv.org/abs/1202.6614

Part of the SQUARE benchmark set: https://arxiv.org/abs/2004.08539

=== Note ===
This implementation performs uncomputation.

"""


import random
import cirq

from cirq.ops import raw_types

class CMaj(cirq.Gate):
    """
    """
    def __init__(self, num_qubits, is_inverse=False):
        assert(num_qubits == 4)
        self._num_qubits = num_qubits
        self.is_inverse = is_inverse
    
    def num_qubits(self):
        return self._num_qubits

    def __pow__(self, power):
        if power == -1:
            return CMaj(self._num_qubits, is_inverse=True)
        else:
            return NotImplemented
        
    def _decompose_(self, qubits):
        [ctrl, x,y,z] = qubits
        if self.is_inverse:
            yield cirq.TOFFOLI(x, y, z)
            yield cirq.CNOT(z, x)
            yield cirq.TOFFOLI(ctrl, x, y)
        else:
            yield cirq.TOFFOLI(ctrl, z, y) 
            yield cirq.CNOT(z, x)
            yield cirq.TOFFOLI(x, y, z)
 



def cucarroAdder(qubits, N, num_anc, j, with_inverse=False):
    ctrl = qubits[0]
    a = qubits[1:N+1]
    b = qubits[N+2:]
    cmaj = CMaj(4)

    anc = [cirq.GridQubit(i+j*num_anc+len(qubits),0) for i in range(num_anc)]
    cin = anc[0]
    cout = anc[1]
    for i in range(N):
        if (i==0):
            x = cin
            y = a[0]
            z = b[0]
        else:
            x = b[i-1]
            y = a[i]
            z = b[i]
        yield cmaj(*[ctrl,x,y,z])
    if with_inverse:
        # Copy
        yield cirq.TOFFOLI(ctrl, b[N-1], cout)
        yield cirq.TOFFOLI(ctrl, cout, qubits[N+1])
        # Uncompute
        for i in range(N-1, -1, -1):
            if (i==0):
                x = cin
                y = a[0]
                z = b[0]
            else:
                x = b[i-1]
                y = a[i]
                z = b[i]
            yield cirq.inverse(cmaj(*[ctrl,x,y,z]))
            
        

def main():
    n_iter = 1
    N = 4
    # 1 bit for control, N bits for input a, 1 bit for carry, N bits for input b
    num_in = 2*N+2 
    num_anc = 2 # per iter
    #num_qubit = num_in + num_out + num_anc

    # Initialize qubits and circuit
    c = cirq.Circuit()

    cntr = 0
    for j in range(n_iter):
        in_qubits = [cirq.GridQubit(i,0) for i in range(num_in)]
        #out_qubits = [cirq.GridQubit(i+num_in,0) for i in range(num_out)]
        a = in_qubits[1:N+1]
        b = in_qubits[N+2:]

        c.append([cirq.X(in_qubits[0])]) # turn on ctrl bit
        # Pick a random input
        rand_bits = [random.randint(0,1) for i in range(2*N)]
        for r in range(N):
            if rand_bits[r] == 1:
                c.append([cirq.X(a[r])])
            if rand_bits[N+r] == 1:
                c.append([cirq.X(b[r])])

        #anc_qubits = [cirq.GridQubit(i+j*num_anc+num_in,0) for i in range(num_anc)]
        #all_qubits = in_qubits + anc_qubits
        circ = cucarroAdder(in_qubits, N, num_anc, j, with_inverse=True) 
        print(len(cirq.decompose(circ)))
        return
        c.append([circ])
        res = a+[in_qubits[N+1]]
        c.append([cirq.measure(*res, key='result')])
    
    print("Circuit:")
    print(c)
    simulator = cirq.Simulator()
    result = simulator.run(c, repetitions=1)
    print("Results:")
    print(result)
    


if __name__ == '__main__':
    main()
