""" little_belle.py - Synthetic Cirq implementation.
=== Reference ===
Part of the SQUARE benchmark set: https://arxiv.org/abs/2004.08539
"""
# Cirq file synthesized by rand_bench_cirq.py
# qubits: 2 ancilla: 1 gates: 2 levels: 3 degrees: 2
import random
import cirq
from cirq.ops import raw_types
# Call list: 1;2;3;
# Function 3 with degree 0
# nq: 2, na: 1, ng: 2
class Func3(cirq.Gate):
	def __init__(self, num_qubits, is_inverse=False):
		self._num_qubits = num_qubits
		self.is_inverse = is_inverse
	def num_qubits(self):
		return self._num_qubits
	def __pow__(self, power):
		if power == -1:
			return Func3(self._num_qubits, is_inverse=True)
		else:
			return NotImplemented
	def _decompose_(self, qubits):
		anc = qubits[2:] # ancilla
		res = [qubits[1]]
		# Leaf function
		if not self.is_inverse: 
			# Compute 
			yield cirq.CNOT( qubits[0], anc[0] )
			yield cirq.CNOT( qubits[1], anc[0] )
			# Store 
			# Note: this version does not store results.
		else: 
			# Uncompute 
			yield cirq.CNOT( qubits[1], anc[0] )
			yield cirq.CNOT( qubits[0], anc[0] )
# Function 2 with degree 1
# nq: 2, na: 1, ng: 2
class Func2(cirq.Gate):
	def __init__(self, num_qubits, is_inverse=False):
		self._num_qubits = num_qubits
		self.is_inverse = is_inverse
	def num_qubits(self):
		return self._num_qubits
	def __pow__(self, power):
		if power == -1:
			return Func2(self._num_qubits, is_inverse=True)
		else:
			return NotImplemented
	def _decompose_(self, qubits):
		anc = qubits[2:] # ancilla
		res = [qubits[1], qubits[0]]
		# Non-leaf function
		func3 = Func3(3, is_inverse=self.is_inverse)
		func3R = Func3(3, is_inverse=(not self.is_inverse))
		nq0 = [qubits[1], anc[0], anc[1]]
		if not self.is_inverse: 
			# Compute 
			yield cirq.CNOT( qubits[1], qubits[0] )
			yield cirq.CNOT( qubits[0], qubits[1] )
			yield func3(*nq0)
			# Store 
			# Note: this version does not store results.
		else: 
			yield func3R(*nq0)
			yield cirq.CNOT( qubits[0], qubits[1] )
			yield cirq.CNOT( qubits[1], qubits[0] )
# Function 1 with degree 1
# nq: 2, na: 1, ng: 2
class Func1(cirq.Gate):
	def __init__(self, num_qubits, is_inverse=False):
		self._num_qubits = num_qubits
		self.is_inverse = is_inverse
	def num_qubits(self):
		return self._num_qubits
	def __pow__(self, power):
		if power == -1:
			return Func1(self._num_qubits, is_inverse=True)
		else:
			return NotImplemented
	def _decompose_(self, qubits):
		anc = qubits[2:] # ancilla
		res = [qubits[1]]
		# Non-leaf function
		func2 = Func2(4, is_inverse=self.is_inverse)
		func2R = Func2(4, is_inverse=(not self.is_inverse))
		nq0 = [anc[0], qubits[0], anc[1], anc[2]]
		if not self.is_inverse: 
			# Compute 
			yield func2(*nq0)
			yield cirq.TOFFOLI( qubits[1], qubits[0], anc[0] )
			yield cirq.CNOT( qubits[0], qubits[1] )
			# Store 
			# Note: this version does not store results.
		else: 
			yield cirq.CNOT( qubits[0], qubits[1] )
			yield cirq.TOFFOLI( qubits[1], qubits[0], anc[0] )
			yield func2R(*nq0)
# main function
def main():
	num_in = 2
	num_anc = 3
	c = cirq.Circuit()
	in_qubits = [cirq.GridQubit(i,0) for i in range(num_in)]
	anc_qubits = [cirq.GridQubit(num_in+i,0) for i in range(num_anc)]
	all_qubits = in_qubits + anc_qubits
	# Intialize random inputs
	c.append([cirq.X(in_qubits[1])])
	# Start computation
	func1 = Func1(5, is_inverse=False)
	circ = func1(*all_qubits)
	func1R = Func1(5, is_inverse=True)
	circR = func1R(*all_qubits)
	c.append([circ])
	c.append([circR])
	c.append([cirq.measure(*in_qubits, key='result')])
	print("Circuit:")
	print(c)
	if num_in + num_anc > 32:
		print("Done. Skipping simulation for circuit size > 32.")
	else:
		simulator = cirq.Simulator()
		result = simulator.run(c, repetitions=1)
		print("Results:")
		print(result)

if __name__ == '__main__':
	main()
