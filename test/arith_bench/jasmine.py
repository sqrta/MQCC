""" jasmine.py - Synthetic Cirq implementation.
=== Reference ===
Part of the SQUARE benchmark set: https://arxiv.org/abs/2004.08539
"""
# Cirq file synthesized by rand_bench_cirq.py
# qubits: 16 ancilla: 16 gates: 32 levels: 2 degrees: 4
import random
import cirq
from cirq.ops import raw_types
# Call list: 1;2,3,4;5,6
# Function 6 with degree 0
# nq: 2, na: 12, ng: 15
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
		res = [qubits[0]]
		# Leaf function
		if not self.is_inverse: 
			# Compute 
			yield cirq.TOFFOLI( anc[6], anc[7], anc[4] )
			yield cirq.CNOT( anc[4], anc[2] )
			yield cirq.CNOT( anc[5], anc[2] )
			yield cirq.CNOT( anc[8], anc[1] )
			yield cirq.CNOT( anc[2], anc[6] )
			yield cirq.TOFFOLI( anc[2], anc[1], anc[11] )
			yield cirq.CNOT( anc[3], anc[7] )
			yield cirq.CNOT( anc[0], anc[3] )
			yield cirq.TOFFOLI( anc[4], anc[10], anc[5] )
			yield cirq.TOFFOLI( anc[8], anc[1], anc[6] )
			yield cirq.TOFFOLI( anc[3], qubits[0], anc[2] )
			yield cirq.TOFFOLI( anc[5], anc[10], anc[7] )
			yield cirq.CNOT( anc[5], qubits[0] )
			yield cirq.CNOT( qubits[1], anc[7] )
			yield cirq.TOFFOLI( anc[6], anc[8], qubits[0] )
			# Store 
			# Note: this version does not store results.
		else: 
			# Uncompute 
			yield cirq.TOFFOLI( anc[6], anc[8], qubits[0] )
			yield cirq.CNOT( qubits[1], anc[7] )
			yield cirq.CNOT( anc[5], qubits[0] )
			yield cirq.TOFFOLI( anc[5], anc[10], anc[7] )
			yield cirq.TOFFOLI( anc[3], qubits[0], anc[2] )
			yield cirq.TOFFOLI( anc[8], anc[1], anc[6] )
			yield cirq.TOFFOLI( anc[4], anc[10], anc[5] )
			yield cirq.CNOT( anc[0], anc[3] )
			yield cirq.CNOT( anc[3], anc[7] )
			yield cirq.TOFFOLI( anc[2], anc[1], anc[11] )
			yield cirq.CNOT( anc[2], anc[6] )
			yield cirq.CNOT( anc[8], anc[1] )
			yield cirq.CNOT( anc[5], anc[2] )
			yield cirq.CNOT( anc[4], anc[2] )
			yield cirq.TOFFOLI( anc[6], anc[7], anc[4] )
# Function 5 with degree 0
# nq: 5, na: 3, ng: 19
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
		anc = qubits[5:] # ancilla
		res = [qubits[0]]
		# Leaf function
		if not self.is_inverse: 
			# Compute 
			yield cirq.TOFFOLI( anc[1], qubits[1], anc[0] )
			yield cirq.CNOT( qubits[4], anc[0] )
			yield cirq.CNOT( qubits[4], anc[1] )
			yield cirq.TOFFOLI( anc[0], qubits[0], anc[2] )
			yield cirq.CNOT( anc[1], qubits[4] )
			yield cirq.CNOT( qubits[3], anc[1] )
			yield cirq.CNOT( anc[0], qubits[0] )
			yield cirq.CNOT( qubits[1], qubits[4] )
			yield cirq.TOFFOLI( anc[2], qubits[3], qubits[2] )
			yield cirq.CNOT( qubits[3], anc[2] )
			yield cirq.CNOT( anc[0], anc[2] )
			yield cirq.CNOT( anc[2], qubits[2] )
			yield cirq.CNOT( qubits[4], qubits[1] )
			yield cirq.CNOT( anc[0], qubits[2] )
			yield cirq.CNOT( qubits[2], qubits[3] )
			yield cirq.TOFFOLI( qubits[0], qubits[1], qubits[3] )
			yield cirq.CNOT( anc[1], qubits[3] )
			yield cirq.CNOT( anc[0], qubits[1] )
			yield cirq.CNOT( qubits[1], anc[2] )
			# Store 
			# Note: this version does not store results.
		else: 
			# Uncompute 
			yield cirq.CNOT( qubits[1], anc[2] )
			yield cirq.CNOT( anc[0], qubits[1] )
			yield cirq.CNOT( anc[1], qubits[3] )
			yield cirq.TOFFOLI( qubits[0], qubits[1], qubits[3] )
			yield cirq.CNOT( qubits[2], qubits[3] )
			yield cirq.CNOT( anc[0], qubits[2] )
			yield cirq.CNOT( qubits[4], qubits[1] )
			yield cirq.CNOT( anc[2], qubits[2] )
			yield cirq.CNOT( anc[0], anc[2] )
			yield cirq.CNOT( qubits[3], anc[2] )
			yield cirq.TOFFOLI( anc[2], qubits[3], qubits[2] )
			yield cirq.CNOT( qubits[1], qubits[4] )
			yield cirq.CNOT( anc[0], qubits[0] )
			yield cirq.CNOT( qubits[3], anc[1] )
			yield cirq.CNOT( anc[1], qubits[4] )
			yield cirq.TOFFOLI( anc[0], qubits[0], anc[2] )
			yield cirq.CNOT( qubits[4], anc[1] )
			yield cirq.CNOT( qubits[4], anc[0] )
			yield cirq.TOFFOLI( anc[1], qubits[1], anc[0] )
# Function 4 with degree 0
# nq: 16, na: 14, ng: 12
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
		anc = qubits[16:] # ancilla
		res = [qubits[6], qubits[13], qubits[15], qubits[2], qubits[11], qubits[9], qubits[8], qubits[7]]
		# Leaf function
		if not self.is_inverse: 
			# Compute 
			yield cirq.TOFFOLI( anc[5], qubits[7], qubits[3] )
			yield cirq.TOFFOLI( anc[2], anc[9], qubits[8] )
			yield cirq.TOFFOLI( qubits[6], qubits[15], qubits[1] )
			yield cirq.CNOT( anc[11], qubits[2] )
			yield cirq.TOFFOLI( anc[5], qubits[10], anc[9] )
			yield cirq.TOFFOLI( qubits[7], qubits[13], qubits[3] )
			yield cirq.TOFFOLI( qubits[10], anc[13], qubits[9] )
			yield cirq.CNOT( qubits[13], anc[11] )
			yield cirq.CNOT( qubits[10], qubits[11] )
			yield cirq.TOFFOLI( qubits[9], anc[12], anc[1] )
			yield cirq.CNOT( anc[3], qubits[5] )
			yield cirq.CNOT( qubits[2], qubits[14] )
			# Store 
			# Note: this version does not store results.
		else: 
			# Uncompute 
			yield cirq.CNOT( qubits[2], qubits[14] )
			yield cirq.CNOT( anc[3], qubits[5] )
			yield cirq.TOFFOLI( qubits[9], anc[12], anc[1] )
			yield cirq.CNOT( qubits[10], qubits[11] )
			yield cirq.CNOT( qubits[13], anc[11] )
			yield cirq.TOFFOLI( qubits[10], anc[13], qubits[9] )
			yield cirq.TOFFOLI( qubits[7], qubits[13], qubits[3] )
			yield cirq.TOFFOLI( anc[5], qubits[10], anc[9] )
			yield cirq.CNOT( anc[11], qubits[2] )
			yield cirq.TOFFOLI( qubits[6], qubits[15], qubits[1] )
			yield cirq.TOFFOLI( anc[2], anc[9], qubits[8] )
			yield cirq.TOFFOLI( anc[5], qubits[7], qubits[3] )
# Function 3 with degree 0
# nq: 12, na: 3, ng: 27
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
		anc = qubits[12:] # ancilla
		res = [qubits[5], qubits[8], qubits[11], qubits[9], qubits[2], qubits[1], qubits[4], qubits[10], qubits[7], qubits[0], qubits[6]]
		# Leaf function
		if not self.is_inverse: 
			# Compute 
			yield cirq.TOFFOLI( anc[1], qubits[6], qubits[10] )
			yield cirq.TOFFOLI( qubits[7], qubits[8], qubits[9] )
			yield cirq.TOFFOLI( qubits[11], qubits[2], qubits[0] )
			yield cirq.CNOT( anc[2], qubits[6] )
			yield cirq.TOFFOLI( qubits[1], qubits[7], anc[2] )
			yield cirq.CNOT( anc[2], qubits[6] )
			yield cirq.CNOT( anc[1], anc[0] )
			yield cirq.TOFFOLI( qubits[4], qubits[6], qubits[5] )
			yield cirq.CNOT( anc[0], qubits[4] )
			yield cirq.TOFFOLI( qubits[7], qubits[8], anc[1] )
			yield cirq.CNOT( qubits[1], anc[0] )
			yield cirq.TOFFOLI( anc[1], qubits[4], qubits[2] )
			yield cirq.TOFFOLI( qubits[7], qubits[1], qubits[11] )
			yield cirq.CNOT( qubits[4], qubits[0] )
			yield cirq.TOFFOLI( qubits[8], anc[2], qubits[6] )
			yield cirq.CNOT( qubits[10], qubits[6] )
			yield cirq.TOFFOLI( qubits[2], qubits[8], qubits[7] )
			yield cirq.CNOT( qubits[7], qubits[5] )
			yield cirq.CNOT( qubits[6], qubits[4] )
			yield cirq.TOFFOLI( qubits[6], qubits[11], qubits[8] )
			yield cirq.TOFFOLI( qubits[8], qubits[9], anc[0] )
			yield cirq.TOFFOLI( qubits[8], qubits[9], anc[1] )
			yield cirq.CNOT( anc[0], qubits[3] )
			yield cirq.CNOT( qubits[7], qubits[0] )
			yield cirq.TOFFOLI( qubits[9], anc[0], qubits[4] )
			yield cirq.CNOT( qubits[11], qubits[2] )
			yield cirq.TOFFOLI( qubits[2], qubits[6], qubits[9] )
			# Store 
			# Note: this version does not store results.
		else: 
			# Uncompute 
			yield cirq.TOFFOLI( qubits[2], qubits[6], qubits[9] )
			yield cirq.CNOT( qubits[11], qubits[2] )
			yield cirq.TOFFOLI( qubits[9], anc[0], qubits[4] )
			yield cirq.CNOT( qubits[7], qubits[0] )
			yield cirq.CNOT( anc[0], qubits[3] )
			yield cirq.TOFFOLI( qubits[8], qubits[9], anc[1] )
			yield cirq.TOFFOLI( qubits[8], qubits[9], anc[0] )
			yield cirq.TOFFOLI( qubits[6], qubits[11], qubits[8] )
			yield cirq.CNOT( qubits[6], qubits[4] )
			yield cirq.CNOT( qubits[7], qubits[5] )
			yield cirq.TOFFOLI( qubits[2], qubits[8], qubits[7] )
			yield cirq.CNOT( qubits[10], qubits[6] )
			yield cirq.TOFFOLI( qubits[8], anc[2], qubits[6] )
			yield cirq.CNOT( qubits[4], qubits[0] )
			yield cirq.TOFFOLI( qubits[7], qubits[1], qubits[11] )
			yield cirq.TOFFOLI( anc[1], qubits[4], qubits[2] )
			yield cirq.CNOT( qubits[1], anc[0] )
			yield cirq.TOFFOLI( qubits[7], qubits[8], anc[1] )
			yield cirq.CNOT( anc[0], qubits[4] )
			yield cirq.TOFFOLI( qubits[4], qubits[6], qubits[5] )
			yield cirq.CNOT( anc[1], anc[0] )
			yield cirq.CNOT( anc[2], qubits[6] )
			yield cirq.TOFFOLI( qubits[1], qubits[7], anc[2] )
			yield cirq.CNOT( anc[2], qubits[6] )
			yield cirq.TOFFOLI( qubits[11], qubits[2], qubits[0] )
			yield cirq.TOFFOLI( qubits[7], qubits[8], qubits[9] )
			yield cirq.TOFFOLI( anc[1], qubits[6], qubits[10] )
# Function 2 with degree 2
# nq: 5, na: 16, ng: 28
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
		anc = qubits[5:] # ancilla
		res = [qubits[3]]
		# Non-leaf function
		func5 = Func5(8, is_inverse=self.is_inverse)
		func5R = Func5(8, is_inverse=(not self.is_inverse))
		nq0 = [qubits[4], anc[9], qubits[2], anc[2], anc[6], anc[16], anc[17], anc[18]]
		func6 = Func6(14, is_inverse=self.is_inverse)
		func6R = Func6(14, is_inverse=(not self.is_inverse))
		nq1 = [anc[4], anc[11], anc[19], anc[20], anc[21], anc[22], anc[23], anc[24], anc[25], anc[26], anc[27], anc[28], anc[29], anc[30]]
		if not self.is_inverse: 
			# Compute 
			yield func6(*nq1)
			yield cirq.CNOT( anc[10], anc[1] )
			yield cirq.TOFFOLI( anc[13], qubits[0], anc[9] )
			yield cirq.TOFFOLI( qubits[1], anc[15], anc[13] )
			yield cirq.CNOT( anc[2], anc[15] )
			yield cirq.TOFFOLI( anc[0], anc[7], anc[15] )
			yield cirq.TOFFOLI( anc[13], anc[4], anc[14] )
			yield cirq.TOFFOLI( qubits[1], anc[3], anc[11] )
			yield cirq.TOFFOLI( anc[9], anc[14], qubits[4] )
			yield cirq.CNOT( anc[14], qubits[3] )
			yield func5(*nq0)
			yield cirq.CNOT( qubits[3], anc[9] )
			yield cirq.CNOT( anc[10], anc[2] )
			yield cirq.TOFFOLI( anc[12], anc[14], qubits[4] )
			yield cirq.TOFFOLI( anc[4], anc[12], anc[0] )
			yield cirq.CNOT( anc[9], anc[3] )
			yield cirq.TOFFOLI( qubits[2], anc[2], anc[1] )
			yield cirq.TOFFOLI( qubits[1], anc[2], qubits[4] )
			yield cirq.TOFFOLI( anc[9], anc[10], anc[2] )
			yield cirq.TOFFOLI( qubits[0], anc[3], anc[11] )
			yield cirq.CNOT( anc[10], anc[9] )
			yield cirq.CNOT( qubits[3], anc[4] )
			yield cirq.CNOT( qubits[4], anc[7] )
			yield cirq.TOFFOLI( anc[10], qubits[0], anc[3] )
			yield cirq.CNOT( anc[13], anc[0] )
			yield cirq.CNOT( anc[13], qubits[2] )
			yield cirq.TOFFOLI( anc[8], anc[2], anc[3] )
			yield cirq.TOFFOLI( qubits[1], qubits[2], anc[9] )
			yield cirq.TOFFOLI( anc[6], anc[8], qubits[4] )
			yield cirq.TOFFOLI( anc[0], anc[13], anc[4] )
			# Store 
			# Note: this version does not store results.
		else: 
			yield cirq.TOFFOLI( anc[0], anc[13], anc[4] )
			yield cirq.TOFFOLI( anc[6], anc[8], qubits[4] )
			yield cirq.TOFFOLI( qubits[1], qubits[2], anc[9] )
			yield cirq.TOFFOLI( anc[8], anc[2], anc[3] )
			yield cirq.CNOT( anc[13], qubits[2] )
			yield cirq.CNOT( anc[13], anc[0] )
			yield cirq.TOFFOLI( anc[10], qubits[0], anc[3] )
			yield cirq.CNOT( qubits[4], anc[7] )
			yield cirq.CNOT( qubits[3], anc[4] )
			yield cirq.CNOT( anc[10], anc[9] )
			yield cirq.TOFFOLI( qubits[0], anc[3], anc[11] )
			yield cirq.TOFFOLI( anc[9], anc[10], anc[2] )
			yield cirq.TOFFOLI( qubits[1], anc[2], qubits[4] )
			yield cirq.TOFFOLI( qubits[2], anc[2], anc[1] )
			yield cirq.CNOT( anc[9], anc[3] )
			yield cirq.TOFFOLI( anc[4], anc[12], anc[0] )
			yield cirq.TOFFOLI( anc[12], anc[14], qubits[4] )
			yield cirq.CNOT( anc[10], anc[2] )
			yield cirq.CNOT( qubits[3], anc[9] )
			yield func5R(*nq0)
			yield cirq.CNOT( anc[14], qubits[3] )
			yield cirq.TOFFOLI( anc[9], anc[14], qubits[4] )
			yield cirq.TOFFOLI( qubits[1], anc[3], anc[11] )
			yield cirq.TOFFOLI( anc[13], anc[4], anc[14] )
			yield cirq.TOFFOLI( anc[0], anc[7], anc[15] )
			yield cirq.CNOT( anc[2], anc[15] )
			yield cirq.TOFFOLI( qubits[1], anc[15], anc[13] )
			yield cirq.TOFFOLI( anc[13], qubits[0], anc[9] )
			yield cirq.CNOT( anc[10], anc[1] )
			yield func6R(*nq1)
# Function 1 with degree 3
# nq: 16, na: 16, ng: 32
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
		anc = qubits[16:] # ancilla
		res = [qubits[4], qubits[9], qubits[2], qubits[5], qubits[7], qubits[8], qubits[13], qubits[15], qubits[0], qubits[1], qubits[6]]
		# Non-leaf function
		func2 = Func2(36, is_inverse=self.is_inverse)
		func2R = Func2(36, is_inverse=(not self.is_inverse))
		nq0 = [qubits[9], anc[1], anc[15], anc[5], qubits[1], anc[16], anc[17], anc[18], anc[19], anc[20], anc[21], anc[22], anc[23], anc[24], anc[25], anc[26], anc[27], anc[28], anc[29], anc[30], anc[31], anc[32], anc[33], anc[34], anc[35], anc[36], anc[37], anc[38], anc[39], anc[40], anc[41], anc[42], anc[43], anc[44], anc[45], anc[46]]
		func3 = Func3(15, is_inverse=self.is_inverse)
		func3R = Func3(15, is_inverse=(not self.is_inverse))
		nq1 = [qubits[4], anc[15], anc[3], qubits[0], anc[10], anc[2], qubits[1], qubits[5], anc[8], qubits[11], qubits[7], anc[12], anc[47], anc[48], anc[49]]
		func4 = Func4(30, is_inverse=self.is_inverse)
		func4R = Func4(30, is_inverse=(not self.is_inverse))
		nq2 = [qubits[15], qubits[10], qubits[0], qubits[8], anc[5], anc[15], qubits[7], anc[12], anc[13], anc[0], qubits[4], anc[9], qubits[9], qubits[12], qubits[11], qubits[2], anc[50], anc[51], anc[52], anc[53], anc[54], anc[55], anc[56], anc[57], anc[58], anc[59], anc[60], anc[61], anc[62], anc[63]]
		if not self.is_inverse: 
			# Compute 
			yield cirq.TOFFOLI( qubits[5], anc[1], qubits[7] )
			yield cirq.CNOT( qubits[4], qubits[11] )
			yield cirq.CNOT( anc[10], qubits[4] )
			yield func4(*nq2)
			yield cirq.CNOT( anc[14], anc[3] )
			yield cirq.TOFFOLI( anc[15], qubits[4], qubits[2] )
			yield cirq.TOFFOLI( anc[12], anc[0], qubits[0] )
			yield cirq.TOFFOLI( qubits[6], qubits[14], qubits[4] )
			yield cirq.CNOT( anc[12], anc[2] )
			yield cirq.CNOT( qubits[8], anc[6] )
			yield cirq.TOFFOLI( anc[11], qubits[14], anc[9] )
			yield cirq.CNOT( anc[6], qubits[10] )
			yield cirq.TOFFOLI( anc[9], anc[6], qubits[1] )
			yield cirq.CNOT( anc[10], anc[3] )
			yield cirq.TOFFOLI( anc[14], anc[9], qubits[15] )
			yield cirq.CNOT( qubits[8], qubits[2] )
			yield cirq.TOFFOLI( qubits[2], anc[5], anc[11] )
			yield cirq.TOFFOLI( anc[9], qubits[6], qubits[5] )
			yield func2(*nq0)
			yield cirq.CNOT( anc[14], qubits[11] )
			yield cirq.CNOT( qubits[5], qubits[14] )
			yield cirq.TOFFOLI( anc[2], anc[13], qubits[13] )
			yield cirq.CNOT( anc[15], anc[7] )
			yield cirq.TOFFOLI( anc[12], qubits[14], anc[2] )
			yield cirq.CNOT( anc[3], anc[14] )
			yield cirq.TOFFOLI( anc[10], qubits[12], anc[1] )
			yield cirq.CNOT( anc[11], qubits[13] )
			yield cirq.TOFFOLI( anc[8], anc[0], qubits[7] )
			yield cirq.CNOT( anc[10], anc[3] )
			yield func3(*nq1)
			yield cirq.TOFFOLI( anc[2], qubits[4], qubits[13] )
			yield cirq.CNOT( qubits[3], qubits[1] )
			yield cirq.CNOT( qubits[7], anc[8] )
			yield cirq.TOFFOLI( qubits[3], qubits[7], anc[14] )
			yield cirq.CNOT( anc[15], anc[0] )
			# Store 
			# Note: this version does not store results.
		else: 
			yield cirq.CNOT( anc[15], anc[0] )
			yield cirq.TOFFOLI( qubits[3], qubits[7], anc[14] )
			yield cirq.CNOT( qubits[7], anc[8] )
			yield cirq.CNOT( qubits[3], qubits[1] )
			yield cirq.TOFFOLI( anc[2], qubits[4], qubits[13] )
			yield func3R(*nq1)
			yield cirq.CNOT( anc[10], anc[3] )
			yield cirq.TOFFOLI( anc[8], anc[0], qubits[7] )
			yield cirq.CNOT( anc[11], qubits[13] )
			yield cirq.TOFFOLI( anc[10], qubits[12], anc[1] )
			yield cirq.CNOT( anc[3], anc[14] )
			yield cirq.TOFFOLI( anc[12], qubits[14], anc[2] )
			yield cirq.CNOT( anc[15], anc[7] )
			yield cirq.TOFFOLI( anc[2], anc[13], qubits[13] )
			yield cirq.CNOT( qubits[5], qubits[14] )
			yield cirq.CNOT( anc[14], qubits[11] )
			yield func2R(*nq0)
			yield cirq.TOFFOLI( anc[9], qubits[6], qubits[5] )
			yield cirq.TOFFOLI( qubits[2], anc[5], anc[11] )
			yield cirq.CNOT( qubits[8], qubits[2] )
			yield cirq.TOFFOLI( anc[14], anc[9], qubits[15] )
			yield cirq.CNOT( anc[10], anc[3] )
			yield cirq.TOFFOLI( anc[9], anc[6], qubits[1] )
			yield cirq.CNOT( anc[6], qubits[10] )
			yield cirq.TOFFOLI( anc[11], qubits[14], anc[9] )
			yield cirq.CNOT( qubits[8], anc[6] )
			yield cirq.CNOT( anc[12], anc[2] )
			yield cirq.TOFFOLI( qubits[6], qubits[14], qubits[4] )
			yield cirq.TOFFOLI( anc[12], anc[0], qubits[0] )
			yield cirq.TOFFOLI( anc[15], qubits[4], qubits[2] )
			yield cirq.CNOT( anc[14], anc[3] )
			yield func4R(*nq2)
			yield cirq.CNOT( anc[10], qubits[4] )
			yield cirq.CNOT( qubits[4], qubits[11] )
			yield cirq.TOFFOLI( qubits[5], anc[1], qubits[7] )
# main function
def main():
	num_in = 16
	num_anc = 64
	c = cirq.Circuit()
	in_qubits = [cirq.GridQubit(i,0) for i in range(num_in)]
	anc_qubits = [cirq.GridQubit(num_in+i,0) for i in range(num_anc)]
	all_qubits = in_qubits + anc_qubits
	# Intialize random inputs
	c.append([cirq.X(in_qubits[10])])
	c.append([cirq.X(in_qubits[15])])
	c.append([cirq.X(in_qubits[6])])
	c.append([cirq.X(in_qubits[7])])
	c.append([cirq.X(in_qubits[4])])
	c.append([cirq.X(in_qubits[8])])
	c.append([cirq.X(in_qubits[1])])
	c.append([cirq.X(in_qubits[0])])
	# Start computation
	func1 = Func1(80, is_inverse=False)
	circ = func1(*all_qubits)
	func1R = Func1(80, is_inverse=True)
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
