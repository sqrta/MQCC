""" little_jasmine.py - Synthetic Cirq implementation.
=== Reference ===
Part of the SQUARE benchmark set: https://arxiv.org/abs/2004.08539
"""
# Cirq file synthesized by rand_bench_cirq.py
# qubits: 2 ancilla: 1 gates: 4 levels: 2 degrees: 4
import random
import cirq
from cirq.ops import raw_types
# Call list: 1;2,3,4;5,6
# Function 6 with degree 0
# nq: 2, na: 1, ng: 4
class Func6(cirq.Gate):
	def __init__(self, num_qubits, is_inverse=False):
		self._num_qubits = num_qubits
		self.is_inverse = is_inverse
	def num_qubits(self):
		return self._num_qubits
	def __pow__(self, power):
		if power == -1:
			return Func6(self._num_qubits, is_inverse=True)
		else:
			return NotImplemented
	def _decompose_(self, qubits):
		anc = qubits[2:] # ancilla
		res = [qubits[0], qubits[1]]
		# Leaf function
		if not self.is_inverse: 
			# Compute 
			yield cirq.CNOT( qubits[1], anc[0] )
			yield cirq.CNOT( qubits[1], anc[0] )
			yield cirq.CNOT( anc[0], qubits[0] )
			yield cirq.CNOT( qubits[1], anc[0] )
			# Store 
			# Note: this version does not store results.
		else: 
			# Uncompute 
			yield cirq.CNOT( qubits[1], anc[0] )
			yield cirq.CNOT( anc[0], qubits[0] )
			yield cirq.CNOT( qubits[1], anc[0] )
			yield cirq.CNOT( qubits[1], anc[0] )
# Function 5 with degree 0
# nq: 2, na: 1, ng: 3
class Func5(cirq.Gate):
	def __init__(self, num_qubits, is_inverse=False):
		self._num_qubits = num_qubits
		self.is_inverse = is_inverse
	def num_qubits(self):
		return self._num_qubits
	def __pow__(self, power):
		if power == -1:
			return Func5(self._num_qubits, is_inverse=True)
		else:
			return NotImplemented
	def _decompose_(self, qubits):
		anc = qubits[2:] # ancilla
		res = [qubits[0], qubits[1]]
		# Leaf function
		if not self.is_inverse: 
			# Compute 
			yield cirq.TOFFOLI( anc[0], qubits[1], qubits[0] )
			yield cirq.TOFFOLI( qubits[1], qubits[0], anc[0] )
			yield cirq.TOFFOLI( qubits[0], qubits[1], anc[0] )
			# Store 
			# Note: this version does not store results.
		else: 
			# Uncompute 
			yield cirq.TOFFOLI( qubits[0], qubits[1], anc[0] )
			yield cirq.TOFFOLI( qubits[1], qubits[0], anc[0] )
			yield cirq.TOFFOLI( anc[0], qubits[1], qubits[0] )
# Function 4 with degree 0
# nq: 2, na: 1, ng: 1
class Func4(cirq.Gate):
	def __init__(self, num_qubits, is_inverse=False):
		self._num_qubits = num_qubits
		self.is_inverse = is_inverse
	def num_qubits(self):
		return self._num_qubits
	def __pow__(self, power):
		if power == -1:
			return Func4(self._num_qubits, is_inverse=True)
		else:
			return NotImplemented
	def _decompose_(self, qubits):
		anc = qubits[2:] # ancilla
		res = [qubits[0]]
		# Leaf function
		if not self.is_inverse: 
			# Compute 
			yield cirq.TOFFOLI( anc[0], qubits[0], qubits[1] )
			# Store 
			# Note: this version does not store results.
		else: 
			# Uncompute 
			yield cirq.TOFFOLI( anc[0], qubits[0], qubits[1] )
# Function 3 with degree 0
# nq: 2, na: 1, ng: 4
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
			yield cirq.TOFFOLI( qubits[0], anc[0], qubits[1] )
			yield cirq.CNOT( anc[0], qubits[1] )
			yield cirq.TOFFOLI( qubits[1], qubits[0], anc[0] )
			yield cirq.TOFFOLI( anc[0], qubits[0], qubits[1] )
			# Store 
			# Note: this version does not store results.
		else: 
			# Uncompute 
			yield cirq.TOFFOLI( anc[0], qubits[0], qubits[1] )
			yield cirq.TOFFOLI( qubits[1], qubits[0], anc[0] )
			yield cirq.CNOT( anc[0], qubits[1] )
			yield cirq.TOFFOLI( qubits[0], anc[0], qubits[1] )
# Function 2 with degree 2
# nq: 2, na: 1, ng: 4
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
		res = [qubits[0], qubits[1]]
		# Non-leaf function
		func5 = Func5(3, is_inverse=self.is_inverse)
		func5R = Func5(3, is_inverse=(not self.is_inverse))
		nq0 = [qubits[0], anc[0], anc[1]]
		func6 = Func6(3, is_inverse=self.is_inverse)
		func6R = Func6(3, is_inverse=(not self.is_inverse))
		nq1 = [qubits[1], anc[0], anc[2]]
		if not self.is_inverse: 
			# Compute 
			yield cirq.CNOT( qubits[0], qubits[1] )
			yield cirq.CNOT( qubits[1], qubits[0] )
			yield cirq.TOFFOLI( anc[0], qubits[0], qubits[1] )
			yield func5(*nq0)
			yield cirq.TOFFOLI( qubits[1], anc[0], qubits[0] )
			yield func6(*nq1)
			# Store 
			# Note: this version does not store results.
		else: 
			yield func6R(*nq1)
			yield cirq.TOFFOLI( qubits[1], anc[0], qubits[0] )
			yield func5R(*nq0)
			yield cirq.TOFFOLI( anc[0], qubits[0], qubits[1] )
			yield cirq.CNOT( qubits[1], qubits[0] )
			yield cirq.CNOT( qubits[0], qubits[1] )
# Function 1 with degree 3
# nq: 2, na: 1, ng: 4
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
		func2 = Func2(5, is_inverse=self.is_inverse)
		func2R = Func2(5, is_inverse=(not self.is_inverse))
		nq0 = [qubits[1], qubits[0], anc[1], anc[2], anc[3]]
		func3 = Func3(3, is_inverse=self.is_inverse)
		func3R = Func3(3, is_inverse=(not self.is_inverse))
		nq1 = [qubits[0], qubits[1], anc[4]]
		func4 = Func4(3, is_inverse=self.is_inverse)
		func4R = Func4(3, is_inverse=(not self.is_inverse))
		nq2 = [anc[0], qubits[1], anc[5]]
		if not self.is_inverse: 
			# Compute 
			yield func3(*nq1)
			yield func4(*nq2)
			yield func2(*nq0)
			yield cirq.CNOT( qubits[1], qubits[0] )
			yield cirq.CNOT( qubits[0], anc[0] )
			yield cirq.TOFFOLI( qubits[1], qubits[0], anc[0] )
			yield cirq.CNOT( anc[0], qubits[0] )
			# Store 
			# Note: this version does not store results.
		else: 
			yield cirq.CNOT( anc[0], qubits[0] )
			yield cirq.TOFFOLI( qubits[1], qubits[0], anc[0] )
			yield cirq.CNOT( qubits[0], anc[0] )
			yield cirq.CNOT( qubits[1], qubits[0] )
			yield func2R(*nq0)
			yield func4R(*nq2)
			yield func3R(*nq1)
# main function
def main():
	num_in = 2
	num_anc = 6
	c = cirq.Circuit()
	in_qubits = [cirq.GridQubit(i,0) for i in range(num_in)]
	anc_qubits = [cirq.GridQubit(num_in+i,0) for i in range(num_anc)]
	all_qubits = in_qubits + anc_qubits
	# Intialize random inputs
	c.append([cirq.X(in_qubits[1])])
	c.append([cirq.X(in_qubits[0])])
	# Start computation
	func1 = Func1(8, is_inverse=False)
	circ = func1(*all_qubits)
	func1R = Func1(8, is_inverse=True)
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
