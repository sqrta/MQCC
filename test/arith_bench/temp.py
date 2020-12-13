# Cirq file synthesized by rand_bench_cirq.py
# qubits: 3 ancilla: 3 gates: 3 levels: 2 degrees: 3
import random
import cirq
from cirq.ops import raw_types
# Call list: 1;2,3,4;5,6
# Function 6 with degree 0
# nq: 3, na: 2, ng: 3
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
		anc = qubits[3:] # ancilla
		res = [qubits[0], qubits[1], qubits[2]]
		# Leaf function
		if not self.is_inverse: 
			# Compute 
			yield cirq.CNOT( qubits[1], qubits[0] )
			yield cirq.TOFFOLI( qubits[0], qubits[2], anc[0] )
			yield cirq.CNOT( qubits[2], anc[0] )
			# Store 
		else: 
			# Uncompute 
			yield cirq.CNOT( qubits[2], anc[0] )
			yield cirq.TOFFOLI( qubits[0], qubits[2], anc[0] )
			yield cirq.CNOT( qubits[1], qubits[0] )
# Function 5 with degree 0
# nq: 3, na: 3, ng: 1
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
		anc = qubits[3:] # ancilla
		res = [qubits[1], qubits[2], qubits[0]]
		# Leaf function
		if not self.is_inverse: 
			# Compute 
			yield cirq.CNOT( qubits[0], qubits[2] )
			# Store 
		else: 
			# Uncompute 
			yield cirq.CNOT( qubits[0], qubits[2] )
# Function 4 with degree 0
# nq: 2, na: 2, ng: 3
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
		res = [qubits[1]]
		# Leaf function
		if not self.is_inverse: 
			# Compute 
			yield cirq.CNOT( qubits[1], anc[1] )
			yield cirq.TOFFOLI( anc[1], qubits[1], anc[0] )
			yield cirq.CNOT( anc[1], qubits[1] )
			# Store 
		else: 
			# Uncompute 
			yield cirq.CNOT( anc[1], qubits[1] )
			yield cirq.TOFFOLI( anc[1], qubits[1], anc[0] )
			yield cirq.CNOT( qubits[1], anc[1] )
# Function 3 with degree 0
# nq: 2, na: 1, ng: 1
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
		res = [qubits[0]]
		# Leaf function
		if not self.is_inverse: 
			# Compute 
			yield cirq.TOFFOLI( anc[0], qubits[0], qubits[1] )
			# Store 
		else: 
			# Uncompute 
			yield cirq.TOFFOLI( anc[0], qubits[0], qubits[1] )
# Function 2 with degree 2
# nq: 3, na: 1, ng: 2
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
		anc = qubits[3:] # ancilla
		res = [qubits[0], qubits[2]]
		# Non-leaf function
		func5 = Func5(6, is_inverse=self.is_inverse)
		func5R = Func5(6, is_inverse=(not self.is_inverse))
		nq0 = [qubits[2], anc[0], qubits[0], anc[1], anc[2], anc[3]]
		func6 = Func6(5, is_inverse=self.is_inverse)
		func6R = Func6(5, is_inverse=(not self.is_inverse))
		nq1 = [qubits[2], anc[0], qubits[1], anc[4], anc[5]]
		if not self.is_inverse: 
			# Compute 
			yield cirq.CNOT( qubits[1], anc[0] )
			yield func6(*nq1)
			yield cirq.CNOT( qubits[0], qubits[2] )
			yield func5(*nq0)
			# Store 
		else: 
			yield func5R(*nq0)
			yield cirq.CNOT( qubits[0], qubits[2] )
			yield func6R(*nq1)
			yield cirq.CNOT( qubits[1], anc[0] )
# Function 1 with degree 3
# nq: 3, na: 3, ng: 3
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
		anc = qubits[3:] # ancilla
		res = [qubits[2], qubits[0]]
		# Non-leaf function
		func2 = Func2(9, is_inverse=self.is_inverse)
		func2R = Func2(9, is_inverse=(not self.is_inverse))
		nq0 = [anc[2], qubits[1], anc[0], anc[3], anc[4], anc[5], anc[6], anc[7], anc[8]]
		func3 = Func3(3, is_inverse=self.is_inverse)
		func3R = Func3(3, is_inverse=(not self.is_inverse))
		nq1 = [anc[1], qubits[1], anc[9]]
		func4 = Func4(4, is_inverse=self.is_inverse)
		func4R = Func4(4, is_inverse=(not self.is_inverse))
		nq2 = [qubits[2], qubits[1], anc[10], anc[11]]
		if not self.is_inverse: 
			# Compute 
			yield func3(*nq1)
			yield cirq.TOFFOLI( qubits[0], anc[2], anc[1] )
			yield cirq.CNOT( qubits[0], anc[1] )
			yield cirq.TOFFOLI( anc[2], anc[0], anc[1] )
			yield func2(*nq0)
			yield func4(*nq2)
			# Store 
		else: 
			yield func4R(*nq2)
			yield func2R(*nq0)
			yield cirq.TOFFOLI( anc[2], anc[0], anc[1] )
			yield cirq.CNOT( qubits[0], anc[1] )
			yield cirq.TOFFOLI( qubits[0], anc[2], anc[1] )
			yield func3R(*nq1)
# main function
def main():
	num_in = 3
	num_anc = 12
	c = cirq.Circuit()
	in_qubits = [cirq.GridQubit(i,0) for i in range(num_in)]
	anc_qubits = [cirq.GridQubit(num_in+i,0) for i in range(num_anc)]
	all_qubits = in_qubits + anc_qubits
	# Intialize random inputs
	c.append([cirq.X(in_qubits[2])])
	c.append([cirq.X(in_qubits[0])])
	# Start computation
	func1 = Func1(15, is_inverse=False)
	circ = func1(*all_qubits)
	func1R = Func1(15, is_inverse=True)
	circR = func1R(*all_qubits)
	c.append([circ])
	c.append([circR])
	c.append([cirq.measure(*in_qubits, key='result')])
	print("Circuit:")
	print(c)
	simulator = cirq.Simulator()
	result = simulator.run(c, repetitions=1)
	print("Results:")
	print(result)

if __name__ == '__main__':
	main()
