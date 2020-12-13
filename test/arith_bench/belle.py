""" belle.py - Synthetic Cirq implementation.
=== Reference ===
Part of the SQUARE benchmark set: https://arxiv.org/abs/2004.08539
"""
# Cirq file synthesized by rand_bench_cirq.py
# qubits: 128 ancilla: 8 gates: 8 levels: 4 degrees: 3
import random
import cirq
from cirq.ops import raw_types
# Call list: 1;2,3,4;5,6;7;8,9,10;11,12,13;14,15,16;17;18,19;20,21,22;23;24,25
# Function 25 with degree 0
# nq: 4, na: 5, ng: 1
class Func25(cirq.Gate):
	def __init__(self, num_qubits, is_inverse=False):
		self._num_qubits = num_qubits
		self.is_inverse = is_inverse
	def num_qubits(self):
		return self._num_qubits
	def __pow__(self, power):
		if power == -1:
			return Func25(self._num_qubits, is_inverse=True)
		else:
			return NotImplemented
	def _decompose_(self, qubits):
		anc = qubits[4:] # ancilla
		res = [qubits[2], qubits[3], qubits[0]]
		# Leaf function
		if not self.is_inverse: 
			# Compute 
			yield cirq.TOFFOLI( qubits[1], anc[1], qubits[2] )
			# Store 
			# Note: this version does not store results.
		else: 
			# Uncompute 
			yield cirq.TOFFOLI( qubits[1], anc[1], qubits[2] )
# Function 24 with degree 0
# nq: 5, na: 2, ng: 6
class Func24(cirq.Gate):
	def __init__(self, num_qubits, is_inverse=False):
		self._num_qubits = num_qubits
		self.is_inverse = is_inverse
	def num_qubits(self):
		return self._num_qubits
	def __pow__(self, power):
		if power == -1:
			return Func24(self._num_qubits, is_inverse=True)
		else:
			return NotImplemented
	def _decompose_(self, qubits):
		anc = qubits[5:] # ancilla
		res = [qubits[3], qubits[4]]
		# Leaf function
		if not self.is_inverse: 
			# Compute 
			yield cirq.TOFFOLI( qubits[1], anc[0], qubits[4] )
			yield cirq.TOFFOLI( qubits[1], qubits[2], anc[1] )
			yield cirq.CNOT( qubits[0], qubits[1] )
			yield cirq.CNOT( qubits[1], qubits[2] )
			yield cirq.TOFFOLI( anc[0], qubits[3], anc[1] )
			yield cirq.TOFFOLI( anc[0], qubits[1], qubits[0] )
			# Store 
			# Note: this version does not store results.
		else: 
			# Uncompute 
			yield cirq.TOFFOLI( anc[0], qubits[1], qubits[0] )
			yield cirq.TOFFOLI( anc[0], qubits[3], anc[1] )
			yield cirq.CNOT( qubits[1], qubits[2] )
			yield cirq.CNOT( qubits[0], qubits[1] )
			yield cirq.TOFFOLI( qubits[1], qubits[2], anc[1] )
			yield cirq.TOFFOLI( qubits[1], anc[0], qubits[4] )
# Function 23 with degree 0
# nq: 23, na: 6, ng: 4
class Func23(cirq.Gate):
	def __init__(self, num_qubits, is_inverse=False):
		self._num_qubits = num_qubits
		self.is_inverse = is_inverse
	def num_qubits(self):
		return self._num_qubits
	def __pow__(self, power):
		if power == -1:
			return Func23(self._num_qubits, is_inverse=True)
		else:
			return NotImplemented
	def _decompose_(self, qubits):
		anc = qubits[23:] # ancilla
		res = [qubits[13], qubits[15], qubits[17], qubits[16], qubits[1], qubits[2], qubits[9], qubits[19], qubits[20], qubits[21], qubits[11], qubits[7], qubits[12], qubits[18], qubits[22], qubits[4], qubits[0], qubits[10]]
		# Leaf function
		if not self.is_inverse: 
			# Compute 
			yield cirq.CNOT( qubits[16], anc[1] )
			yield cirq.CNOT( qubits[13], qubits[6] )
			yield cirq.TOFFOLI( qubits[9], qubits[13], qubits[11] )
			yield cirq.CNOT( anc[1], qubits[8] )
			# Store 
			# Note: this version does not store results.
		else: 
			# Uncompute 
			yield cirq.CNOT( anc[1], qubits[8] )
			yield cirq.TOFFOLI( qubits[9], qubits[13], qubits[11] )
			yield cirq.CNOT( qubits[13], qubits[6] )
			yield cirq.CNOT( qubits[16], anc[1] )
# Function 22 with degree 0
# nq: 7, na: 2, ng: 8
class Func22(cirq.Gate):
	def __init__(self, num_qubits, is_inverse=False):
		self._num_qubits = num_qubits
		self.is_inverse = is_inverse
	def num_qubits(self):
		return self._num_qubits
	def __pow__(self, power):
		if power == -1:
			return Func22(self._num_qubits, is_inverse=True)
		else:
			return NotImplemented
	def _decompose_(self, qubits):
		anc = qubits[7:] # ancilla
		res = [qubits[4], qubits[2], qubits[0], qubits[5], qubits[1]]
		# Leaf function
		if not self.is_inverse: 
			# Compute 
			yield cirq.CNOT( qubits[6], qubits[4] )
			yield cirq.TOFFOLI( qubits[6], anc[1], qubits[4] )
			yield cirq.TOFFOLI( anc[1], qubits[2], qubits[6] )
			yield cirq.CNOT( qubits[3], anc[0] )
			yield cirq.CNOT( anc[0], qubits[4] )
			yield cirq.CNOT( qubits[2], qubits[5] )
			yield cirq.CNOT( qubits[6], qubits[5] )
			yield cirq.TOFFOLI( qubits[5], qubits[2], qubits[1] )
			# Store 
			# Note: this version does not store results.
		else: 
			# Uncompute 
			yield cirq.TOFFOLI( qubits[5], qubits[2], qubits[1] )
			yield cirq.CNOT( qubits[6], qubits[5] )
			yield cirq.CNOT( qubits[2], qubits[5] )
			yield cirq.CNOT( anc[0], qubits[4] )
			yield cirq.CNOT( qubits[3], anc[0] )
			yield cirq.TOFFOLI( anc[1], qubits[2], qubits[6] )
			yield cirq.TOFFOLI( qubits[6], anc[1], qubits[4] )
			yield cirq.CNOT( qubits[6], qubits[4] )
# Function 21 with degree 0
# nq: 8, na: 8, ng: 1
class Func21(cirq.Gate):
	def __init__(self, num_qubits, is_inverse=False):
		self._num_qubits = num_qubits
		self.is_inverse = is_inverse
	def num_qubits(self):
		return self._num_qubits
	def __pow__(self, power):
		if power == -1:
			return Func21(self._num_qubits, is_inverse=True)
		else:
			return NotImplemented
	def _decompose_(self, qubits):
		anc = qubits[8:] # ancilla
		res = [qubits[4]]
		# Leaf function
		if not self.is_inverse: 
			# Compute 
			yield cirq.TOFFOLI( anc[3], qubits[7], qubits[5] )
			# Store 
			# Note: this version does not store results.
		else: 
			# Uncompute 
			yield cirq.TOFFOLI( anc[3], qubits[7], qubits[5] )
# Function 20 with degree 0
# nq: 20, na: 5, ng: 5
class Func20(cirq.Gate):
	def __init__(self, num_qubits, is_inverse=False):
		self._num_qubits = num_qubits
		self.is_inverse = is_inverse
	def num_qubits(self):
		return self._num_qubits
	def __pow__(self, power):
		if power == -1:
			return Func20(self._num_qubits, is_inverse=True)
		else:
			return NotImplemented
	def _decompose_(self, qubits):
		anc = qubits[20:] # ancilla
		res = [qubits[9], qubits[19], qubits[1], qubits[8]]
		# Leaf function
		if not self.is_inverse: 
			# Compute 
			yield cirq.CNOT( anc[1], qubits[18] )
			yield cirq.CNOT( qubits[12], qubits[18] )
			yield cirq.TOFFOLI( qubits[9], qubits[7], qubits[18] )
			yield cirq.CNOT( qubits[8], qubits[14] )
			yield cirq.CNOT( qubits[16], qubits[7] )
			# Store 
			# Note: this version does not store results.
		else: 
			# Uncompute 
			yield cirq.CNOT( qubits[16], qubits[7] )
			yield cirq.CNOT( qubits[8], qubits[14] )
			yield cirq.TOFFOLI( qubits[9], qubits[7], qubits[18] )
			yield cirq.CNOT( qubits[12], qubits[18] )
			yield cirq.CNOT( anc[1], qubits[18] )
# Function 19 with degree 0
# nq: 30, na: 2, ng: 5
class Func19(cirq.Gate):
	def __init__(self, num_qubits, is_inverse=False):
		self._num_qubits = num_qubits
		self.is_inverse = is_inverse
	def num_qubits(self):
		return self._num_qubits
	def __pow__(self, power):
		if power == -1:
			return Func19(self._num_qubits, is_inverse=True)
		else:
			return NotImplemented
	def _decompose_(self, qubits):
		anc = qubits[30:] # ancilla
		res = [qubits[0], qubits[8], qubits[6], qubits[15], qubits[7], qubits[20], qubits[2], qubits[4], qubits[12], qubits[9], qubits[1], qubits[23], qubits[14], qubits[19], qubits[26], qubits[25]]
		# Leaf function
		if not self.is_inverse: 
			# Compute 
			yield cirq.TOFFOLI( anc[0], qubits[1], qubits[16] )
			yield cirq.TOFFOLI( qubits[1], qubits[29], anc[0] )
			yield cirq.TOFFOLI( qubits[27], qubits[8], qubits[14] )
			yield cirq.TOFFOLI( qubits[13], qubits[7], qubits[29] )
			yield cirq.TOFFOLI( qubits[1], qubits[15], qubits[20] )
			# Store 
			# Note: this version does not store results.
		else: 
			# Uncompute 
			yield cirq.TOFFOLI( qubits[1], qubits[15], qubits[20] )
			yield cirq.TOFFOLI( qubits[13], qubits[7], qubits[29] )
			yield cirq.TOFFOLI( qubits[27], qubits[8], qubits[14] )
			yield cirq.TOFFOLI( qubits[1], qubits[29], anc[0] )
			yield cirq.TOFFOLI( anc[0], qubits[1], qubits[16] )
# Function 18 with degree 0
# nq: 10, na: 5, ng: 6
class Func18(cirq.Gate):
	def __init__(self, num_qubits, is_inverse=False):
		self._num_qubits = num_qubits
		self.is_inverse = is_inverse
	def num_qubits(self):
		return self._num_qubits
	def __pow__(self, power):
		if power == -1:
			return Func18(self._num_qubits, is_inverse=True)
		else:
			return NotImplemented
	def _decompose_(self, qubits):
		anc = qubits[10:] # ancilla
		res = [qubits[9], qubits[1], qubits[6], qubits[3]]
		# Leaf function
		if not self.is_inverse: 
			# Compute 
			yield cirq.CNOT( qubits[6], anc[1] )
			yield cirq.CNOT( qubits[6], anc[2] )
			yield cirq.CNOT( anc[1], qubits[7] )
			yield cirq.TOFFOLI( qubits[8], qubits[2], qubits[0] )
			yield cirq.CNOT( qubits[7], qubits[6] )
			yield cirq.CNOT( qubits[3], qubits[2] )
			# Store 
			# Note: this version does not store results.
		else: 
			# Uncompute 
			yield cirq.CNOT( qubits[3], qubits[2] )
			yield cirq.CNOT( qubits[7], qubits[6] )
			yield cirq.TOFFOLI( qubits[8], qubits[2], qubits[0] )
			yield cirq.CNOT( anc[1], qubits[7] )
			yield cirq.CNOT( qubits[6], anc[2] )
			yield cirq.CNOT( qubits[6], anc[1] )
# Function 17 with degree 0
# nq: 16, na: 4, ng: 2
class Func17(cirq.Gate):
	def __init__(self, num_qubits, is_inverse=False):
		self._num_qubits = num_qubits
		self.is_inverse = is_inverse
	def num_qubits(self):
		return self._num_qubits
	def __pow__(self, power):
		if power == -1:
			return Func17(self._num_qubits, is_inverse=True)
		else:
			return NotImplemented
	def _decompose_(self, qubits):
		anc = qubits[16:] # ancilla
		res = [qubits[11], qubits[4], qubits[8], qubits[3], qubits[14], qubits[13], qubits[0], qubits[1]]
		# Leaf function
		if not self.is_inverse: 
			# Compute 
			yield cirq.TOFFOLI( anc[1], qubits[4], qubits[2] )
			yield cirq.TOFFOLI( qubits[4], qubits[14], qubits[2] )
			# Store 
			# Note: this version does not store results.
		else: 
			# Uncompute 
			yield cirq.TOFFOLI( qubits[4], qubits[14], qubits[2] )
			yield cirq.TOFFOLI( anc[1], qubits[4], qubits[2] )
# Function 16 with degree 0
# nq: 47, na: 3, ng: 1
class Func16(cirq.Gate):
	def __init__(self, num_qubits, is_inverse=False):
		self._num_qubits = num_qubits
		self.is_inverse = is_inverse
	def num_qubits(self):
		return self._num_qubits
	def __pow__(self, power):
		if power == -1:
			return Func16(self._num_qubits, is_inverse=True)
		else:
			return NotImplemented
	def _decompose_(self, qubits):
		anc = qubits[47:] # ancilla
		res = [qubits[38], qubits[1], qubits[14], qubits[33], qubits[22], qubits[8], qubits[32], qubits[23], qubits[42], qubits[35], qubits[43], qubits[45]]
		# Leaf function
		if not self.is_inverse: 
			# Compute 
			yield cirq.TOFFOLI( qubits[45], qubits[8], qubits[46] )
			# Store 
			# Note: this version does not store results.
		else: 
			# Uncompute 
			yield cirq.TOFFOLI( qubits[45], qubits[8], qubits[46] )
# Function 15 with degree 0
# nq: 55, na: 7, ng: 4
class Func15(cirq.Gate):
	def __init__(self, num_qubits, is_inverse=False):
		self._num_qubits = num_qubits
		self.is_inverse = is_inverse
	def num_qubits(self):
		return self._num_qubits
	def __pow__(self, power):
		if power == -1:
			return Func15(self._num_qubits, is_inverse=True)
		else:
			return NotImplemented
	def _decompose_(self, qubits):
		anc = qubits[55:] # ancilla
		res = [qubits[1], qubits[39], qubits[26], qubits[5]]
		# Leaf function
		if not self.is_inverse: 
			# Compute 
			yield cirq.TOFFOLI( qubits[42], qubits[18], qubits[37] )
			yield cirq.CNOT( anc[1], qubits[4] )
			yield cirq.CNOT( qubits[37], qubits[11] )
			yield cirq.CNOT( qubits[24], qubits[8] )
			# Store 
			# Note: this version does not store results.
		else: 
			# Uncompute 
			yield cirq.CNOT( qubits[24], qubits[8] )
			yield cirq.CNOT( qubits[37], qubits[11] )
			yield cirq.CNOT( anc[1], qubits[4] )
			yield cirq.TOFFOLI( qubits[42], qubits[18], qubits[37] )
# Function 14 with degree 0
# nq: 18, na: 7, ng: 2
class Func14(cirq.Gate):
	def __init__(self, num_qubits, is_inverse=False):
		self._num_qubits = num_qubits
		self.is_inverse = is_inverse
	def num_qubits(self):
		return self._num_qubits
	def __pow__(self, power):
		if power == -1:
			return Func14(self._num_qubits, is_inverse=True)
		else:
			return NotImplemented
	def _decompose_(self, qubits):
		anc = qubits[18:] # ancilla
		res = [qubits[13], qubits[9], qubits[3], qubits[7], qubits[4], qubits[17]]
		# Leaf function
		if not self.is_inverse: 
			# Compute 
			yield cirq.CNOT( qubits[15], qubits[3] )
			yield cirq.CNOT( anc[2], qubits[2] )
			# Store 
			# Note: this version does not store results.
		else: 
			# Uncompute 
			yield cirq.CNOT( anc[2], qubits[2] )
			yield cirq.CNOT( qubits[15], qubits[3] )
# Function 13 with degree 0
# nq: 12, na: 8, ng: 1
class Func13(cirq.Gate):
	def __init__(self, num_qubits, is_inverse=False):
		self._num_qubits = num_qubits
		self.is_inverse = is_inverse
	def num_qubits(self):
		return self._num_qubits
	def __pow__(self, power):
		if power == -1:
			return Func13(self._num_qubits, is_inverse=True)
		else:
			return NotImplemented
	def _decompose_(self, qubits):
		anc = qubits[12:] # ancilla
		res = [qubits[7], qubits[4], qubits[0], qubits[9], qubits[2]]
		# Leaf function
		if not self.is_inverse: 
			# Compute 
			yield cirq.CNOT( anc[3], qubits[5] )
			# Store 
			# Note: this version does not store results.
		else: 
			# Uncompute 
			yield cirq.CNOT( anc[3], qubits[5] )
# Function 12 with degree 0
# nq: 4, na: 3, ng: 8
class Func12(cirq.Gate):
	def __init__(self, num_qubits, is_inverse=False):
		self._num_qubits = num_qubits
		self.is_inverse = is_inverse
	def num_qubits(self):
		return self._num_qubits
	def __pow__(self, power):
		if power == -1:
			return Func12(self._num_qubits, is_inverse=True)
		else:
			return NotImplemented
	def _decompose_(self, qubits):
		anc = qubits[4:] # ancilla
		res = [qubits[1], qubits[3], qubits[2]]
		# Leaf function
		if not self.is_inverse: 
			# Compute 
			yield cirq.TOFFOLI( qubits[3], anc[1], anc[0] )
			yield cirq.CNOT( anc[1], anc[2] )
			yield cirq.TOFFOLI( qubits[0], anc[2], qubits[3] )
			yield cirq.TOFFOLI( qubits[3], anc[0], qubits[1] )
			yield cirq.TOFFOLI( qubits[1], qubits[0], anc[2] )
			yield cirq.CNOT( qubits[3], qubits[2] )
			yield cirq.CNOT( qubits[3], qubits[2] )
			yield cirq.CNOT( qubits[3], anc[0] )
			# Store 
			# Note: this version does not store results.
		else: 
			# Uncompute 
			yield cirq.CNOT( qubits[3], anc[0] )
			yield cirq.CNOT( qubits[3], qubits[2] )
			yield cirq.CNOT( qubits[3], qubits[2] )
			yield cirq.TOFFOLI( qubits[1], qubits[0], anc[2] )
			yield cirq.TOFFOLI( qubits[3], anc[0], qubits[1] )
			yield cirq.TOFFOLI( qubits[0], anc[2], qubits[3] )
			yield cirq.CNOT( anc[1], anc[2] )
			yield cirq.TOFFOLI( qubits[3], anc[1], anc[0] )
# Function 11 with degree 2
# nq: 2, na: 6, ng: 6
class Func11(cirq.Gate):
	def __init__(self, num_qubits, is_inverse=False):
		self._num_qubits = num_qubits
		self.is_inverse = is_inverse
	def num_qubits(self):
		return self._num_qubits
	def __pow__(self, power):
		if power == -1:
			return Func11(self._num_qubits, is_inverse=True)
		else:
			return NotImplemented
	def _decompose_(self, qubits):
		anc = qubits[2:] # ancilla
		res = [qubits[1], qubits[0]]
		# Non-leaf function
		func24 = Func24(7, is_inverse=self.is_inverse)
		func24R = Func24(7, is_inverse=(not self.is_inverse))
		nq0 = [anc[3], anc[1], qubits[1], anc[0], anc[2], anc[6], anc[7]]
		func25 = Func25(9, is_inverse=self.is_inverse)
		func25R = Func25(9, is_inverse=(not self.is_inverse))
		nq1 = [anc[5], qubits[0], anc[4], anc[2], anc[8], anc[9], anc[10], anc[11], anc[12]]
		if not self.is_inverse: 
			# Compute 
			yield cirq.TOFFOLI( qubits[1], qubits[0], anc[3] )
			yield cirq.TOFFOLI( anc[1], anc[0], anc[3] )
			yield cirq.TOFFOLI( anc[4], anc[0], anc[3] )
			yield func24(*nq0)
			yield cirq.CNOT( qubits[1], anc[1] )
			yield cirq.TOFFOLI( anc[0], anc[1], anc[2] )
			yield func25(*nq1)
			yield cirq.CNOT( anc[5], anc[4] )
			# Store 
			# Note: this version does not store results.
		else: 
			yield cirq.CNOT( anc[5], anc[4] )
			yield func25R(*nq1)
			yield cirq.TOFFOLI( anc[0], anc[1], anc[2] )
			yield cirq.CNOT( qubits[1], anc[1] )
			yield func24R(*nq0)
			yield cirq.TOFFOLI( anc[4], anc[0], anc[3] )
			yield cirq.TOFFOLI( anc[1], anc[0], anc[3] )
			yield cirq.TOFFOLI( qubits[1], qubits[0], anc[3] )
# Function 10 with degree 1
# nq: 31, na: 5, ng: 4
class Func10(cirq.Gate):
	def __init__(self, num_qubits, is_inverse=False):
		self._num_qubits = num_qubits
		self.is_inverse = is_inverse
	def num_qubits(self):
		return self._num_qubits
	def __pow__(self, power):
		if power == -1:
			return Func10(self._num_qubits, is_inverse=True)
		else:
			return NotImplemented
	def _decompose_(self, qubits):
		anc = qubits[31:] # ancilla
		res = [qubits[11], qubits[7], qubits[27], qubits[0], qubits[29], qubits[10]]
		# Non-leaf function
		func23 = Func23(29, is_inverse=self.is_inverse)
		func23R = Func23(29, is_inverse=(not self.is_inverse))
		nq0 = [qubits[1], qubits[17], qubits[30], qubits[15], anc[3], qubits[28], qubits[0], qubits[16], qubits[4], qubits[7], qubits[9], qubits[12], qubits[21], qubits[11], qubits[2], qubits[22], qubits[8], qubits[23], qubits[18], qubits[3], qubits[20], anc[4], anc[1], anc[5], anc[6], anc[7], anc[8], anc[9], anc[10]]
		if not self.is_inverse: 
			# Compute 
			yield cirq.CNOT( qubits[3], qubits[10] )
			yield cirq.CNOT( qubits[17], anc[0] )
			yield func23(*nq0)
			yield cirq.TOFFOLI( qubits[1], qubits[8], qubits[10] )
			yield cirq.TOFFOLI( qubits[1], qubits[4], qubits[8] )
			# Store 
			# Note: this version does not store results.
		else: 
			yield cirq.TOFFOLI( qubits[1], qubits[4], qubits[8] )
			yield cirq.TOFFOLI( qubits[1], qubits[8], qubits[10] )
			yield func23R(*nq0)
			yield cirq.CNOT( qubits[17], anc[0] )
			yield cirq.CNOT( qubits[3], qubits[10] )
# Function 9 with degree 3
# nq: 19, na: 8, ng: 6
class Func9(cirq.Gate):
	def __init__(self, num_qubits, is_inverse=False):
		self._num_qubits = num_qubits
		self.is_inverse = is_inverse
	def num_qubits(self):
		return self._num_qubits
	def __pow__(self, power):
		if power == -1:
			return Func9(self._num_qubits, is_inverse=True)
		else:
			return NotImplemented
	def _decompose_(self, qubits):
		anc = qubits[19:] # ancilla
		res = [qubits[7], qubits[8], qubits[10], qubits[13], qubits[18], qubits[12], qubits[4], qubits[17], qubits[1], qubits[0], qubits[14], qubits[16], qubits[9], qubits[15], qubits[6], qubits[11], qubits[2], qubits[5]]
		# Non-leaf function
		func20 = Func20(25, is_inverse=self.is_inverse)
		func20R = Func20(25, is_inverse=(not self.is_inverse))
		nq0 = [anc[2], qubits[14], qubits[18], anc[1], qubits[7], qubits[15], qubits[17], qubits[12], qubits[2], qubits[0], qubits[3], anc[5], qubits[1], qubits[11], anc[3], qubits[16], qubits[8], qubits[4], qubits[13], qubits[10], anc[8], anc[9], anc[10], anc[11], anc[12]]
		func21 = Func21(16, is_inverse=self.is_inverse)
		func21R = Func21(16, is_inverse=(not self.is_inverse))
		nq1 = [qubits[0], qubits[6], qubits[15], qubits[7], qubits[12], qubits[2], qubits[18], qubits[5], anc[13], anc[14], anc[15], anc[16], anc[17], anc[18], anc[19], anc[20]]
		func22 = Func22(9, is_inverse=self.is_inverse)
		func22R = Func22(9, is_inverse=(not self.is_inverse))
		nq2 = [qubits[3], qubits[5], anc[5], qubits[13], qubits[1], qubits[16], qubits[6], anc[21], anc[22]]
		if not self.is_inverse: 
			# Compute 
			yield cirq.TOFFOLI( anc[6], qubits[10], qubits[5] )
			yield cirq.CNOT( qubits[8], qubits[2] )
			yield func22(*nq2)
			yield func21(*nq1)
			yield func20(*nq0)
			yield cirq.TOFFOLI( qubits[9], anc[5], qubits[5] )
			yield cirq.CNOT( anc[0], qubits[8] )
			yield cirq.TOFFOLI( qubits[14], anc[4], qubits[5] )
			yield cirq.CNOT( anc[2], anc[4] )
			# Store 
			# Note: this version does not store results.
		else: 
			yield cirq.CNOT( anc[2], anc[4] )
			yield cirq.TOFFOLI( qubits[14], anc[4], qubits[5] )
			yield cirq.CNOT( anc[0], qubits[8] )
			yield cirq.TOFFOLI( qubits[9], anc[5], qubits[5] )
			yield func20R(*nq0)
			yield func21R(*nq1)
			yield func22R(*nq2)
			yield cirq.CNOT( qubits[8], qubits[2] )
			yield cirq.TOFFOLI( anc[6], qubits[10], qubits[5] )
# Function 8 with degree 2
# nq: 63, na: 3, ng: 6
class Func8(cirq.Gate):
	def __init__(self, num_qubits, is_inverse=False):
		self._num_qubits = num_qubits
		self.is_inverse = is_inverse
	def num_qubits(self):
		return self._num_qubits
	def __pow__(self, power):
		if power == -1:
			return Func8(self._num_qubits, is_inverse=True)
		else:
			return NotImplemented
	def _decompose_(self, qubits):
		anc = qubits[63:] # ancilla
		res = [qubits[40], qubits[18], qubits[5], qubits[48], qubits[17], qubits[20], qubits[10], qubits[9], qubits[58], qubits[57], qubits[62], qubits[19], qubits[61], qubits[2], qubits[26], qubits[51], qubits[30], qubits[6], qubits[60], qubits[24], qubits[43], qubits[22], qubits[21], qubits[23], qubits[37], qubits[59], qubits[41], qubits[56], qubits[34], qubits[25], qubits[8], qubits[11], qubits[49], qubits[13], qubits[15], qubits[50], qubits[36], qubits[38], qubits[33], qubits[35]]
		# Non-leaf function
		func18 = Func18(15, is_inverse=self.is_inverse)
		func18R = Func18(15, is_inverse=(not self.is_inverse))
		nq0 = [qubits[59], qubits[5], qubits[32], anc[2], qubits[50], qubits[11], qubits[62], qubits[14], qubits[56], qubits[30], anc[3], anc[4], anc[5], anc[6], anc[7]]
		func19 = Func19(32, is_inverse=self.is_inverse)
		func19R = Func19(32, is_inverse=(not self.is_inverse))
		nq1 = [qubits[41], qubits[24], qubits[35], qubits[30], qubits[52], anc[0], qubits[57], qubits[13], qubits[12], qubits[49], anc[1], qubits[62], qubits[23], qubits[29], qubits[51], qubits[56], qubits[61], qubits[31], qubits[1], qubits[28], qubits[15], qubits[38], qubits[0], qubits[2], qubits[54], qubits[55], qubits[9], qubits[50], qubits[7], qubits[6], anc[8], anc[9]]
		if not self.is_inverse: 
			# Compute 
			yield cirq.TOFFOLI( qubits[14], qubits[28], qubits[17] )
			yield cirq.TOFFOLI( qubits[14], qubits[1], qubits[59] )
			yield cirq.CNOT( qubits[52], qubits[19] )
			yield cirq.TOFFOLI( qubits[9], qubits[38], qubits[22] )
			yield cirq.TOFFOLI( anc[1], qubits[21], qubits[28] )
			yield func19(*nq1)
			yield cirq.CNOT( qubits[45], qubits[22] )
			yield func18(*nq0)
			# Store 
			# Note: this version does not store results.
		else: 
			yield func18R(*nq0)
			yield cirq.CNOT( qubits[45], qubits[22] )
			yield func19R(*nq1)
			yield cirq.TOFFOLI( anc[1], qubits[21], qubits[28] )
			yield cirq.TOFFOLI( qubits[9], qubits[38], qubits[22] )
			yield cirq.CNOT( qubits[52], qubits[19] )
			yield cirq.TOFFOLI( qubits[14], qubits[1], qubits[59] )
			yield cirq.TOFFOLI( qubits[14], qubits[28], qubits[17] )
# Function 7 with degree 1
# nq: 77, na: 2, ng: 4
class Func7(cirq.Gate):
	def __init__(self, num_qubits, is_inverse=False):
		self._num_qubits = num_qubits
		self.is_inverse = is_inverse
	def num_qubits(self):
		return self._num_qubits
	def __pow__(self, power):
		if power == -1:
			return Func7(self._num_qubits, is_inverse=True)
		else:
			return NotImplemented
	def _decompose_(self, qubits):
		anc = qubits[77:] # ancilla
		res = [qubits[26], qubits[54], qubits[39], qubits[63], qubits[69], qubits[67], qubits[45], qubits[21], qubits[28], qubits[51], qubits[72], qubits[41], qubits[14], qubits[44], qubits[68], qubits[2], qubits[25], qubits[57], qubits[13], qubits[22], qubits[4], qubits[59], qubits[52], qubits[29], qubits[5], qubits[47], qubits[34], qubits[18], qubits[9], qubits[30], qubits[33], qubits[19], qubits[11], qubits[0], qubits[32], qubits[24], qubits[61], qubits[62], qubits[55], qubits[38], qubits[64], qubits[58], qubits[49], qubits[35], qubits[50], qubits[27], qubits[40], qubits[74], qubits[3], qubits[53], qubits[7], qubits[76], qubits[36], qubits[46], qubits[71]]
		# Non-leaf function
		func17 = Func17(20, is_inverse=self.is_inverse)
		func17R = Func17(20, is_inverse=(not self.is_inverse))
		nq0 = [qubits[66], qubits[52], qubits[70], qubits[61], qubits[2], qubits[31], qubits[20], anc[0], qubits[72], qubits[39], qubits[56], qubits[51], qubits[25], qubits[64], qubits[27], qubits[18], anc[2], anc[3], anc[4], anc[5]]
		if not self.is_inverse: 
			# Compute 
			yield func17(*nq0)
			yield cirq.CNOT( qubits[44], qubits[55] )
			yield cirq.TOFFOLI( qubits[4], qubits[14], qubits[34] )
			yield cirq.CNOT( qubits[18], qubits[10] )
			yield cirq.TOFFOLI( qubits[3], qubits[7], qubits[72] )
			# Store 
			# Note: this version does not store results.
		else: 
			yield cirq.TOFFOLI( qubits[3], qubits[7], qubits[72] )
			yield cirq.CNOT( qubits[18], qubits[10] )
			yield cirq.TOFFOLI( qubits[4], qubits[14], qubits[34] )
			yield cirq.CNOT( qubits[44], qubits[55] )
			yield func17R(*nq0)
# Function 6 with degree 3
# nq: 58, na: 8, ng: 5
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
		anc = qubits[58:] # ancilla
		res = [qubits[54], qubits[1], qubits[11], qubits[48], qubits[44]]
		# Non-leaf function
		func14 = Func14(25, is_inverse=self.is_inverse)
		func14R = Func14(25, is_inverse=(not self.is_inverse))
		nq0 = [qubits[14], qubits[22], qubits[41], qubits[15], qubits[34], qubits[1], anc[3], qubits[16], qubits[30], qubits[29], qubits[11], qubits[46], qubits[49], qubits[56], qubits[39], qubits[52], qubits[25], anc[7], anc[8], anc[9], anc[10], anc[11], anc[12], anc[13], anc[14]]
		func15 = Func15(62, is_inverse=self.is_inverse)
		func15R = Func15(62, is_inverse=(not self.is_inverse))
		nq1 = [qubits[43], qubits[20], qubits[18], qubits[3], qubits[4], qubits[33], qubits[12], qubits[24], qubits[31], qubits[49], qubits[9], anc[5], qubits[29], qubits[15], qubits[11], qubits[35], qubits[13], qubits[52], qubits[37], qubits[54], qubits[17], anc[1], anc[7], qubits[30], anc[2], anc[6], qubits[2], anc[0], qubits[50], qubits[7], qubits[51], qubits[0], qubits[56], qubits[26], qubits[39], qubits[40], qubits[19], qubits[25], qubits[27], qubits[8], qubits[1], qubits[47], qubits[53], qubits[57], qubits[36], qubits[46], anc[4], qubits[44], qubits[48], qubits[10], anc[3], qubits[45], qubits[34], qubits[38], qubits[5], anc[15], anc[16], anc[17], anc[18], anc[19], anc[20], anc[21]]
		func16 = Func16(50, is_inverse=self.is_inverse)
		func16R = Func16(50, is_inverse=(not self.is_inverse))
		nq2 = [anc[4], qubits[12], qubits[24], qubits[37], qubits[46], qubits[29], qubits[56], qubits[45], qubits[25], qubits[27], qubits[0], qubits[40], qubits[48], qubits[47], anc[6], qubits[31], qubits[49], qubits[15], qubits[41], qubits[30], qubits[19], qubits[4], qubits[50], qubits[16], qubits[17], qubits[28], anc[7], qubits[13], qubits[1], qubits[14], anc[0], qubits[51], qubits[20], qubits[44], qubits[52], qubits[7], anc[5], qubits[33], qubits[26], qubits[3], qubits[18], qubits[55], qubits[6], qubits[36], anc[3], qubits[43], qubits[38], anc[22], anc[23], anc[24]]
		if not self.is_inverse: 
			# Compute 
			yield cirq.TOFFOLI( qubits[44], qubits[24], qubits[37] )
			yield func16(*nq2)
			yield cirq.CNOT( anc[4], qubits[29] )
			yield cirq.TOFFOLI( qubits[16], qubits[1], qubits[10] )
			yield cirq.CNOT( qubits[11], qubits[8] )
			yield cirq.CNOT( anc[2], qubits[57] )
			yield func14(*nq0)
			yield func15(*nq1)
			# Store 
			# Note: this version does not store results.
		else: 
			yield func15R(*nq1)
			yield func14R(*nq0)
			yield cirq.CNOT( anc[2], qubits[57] )
			yield cirq.CNOT( qubits[11], qubits[8] )
			yield cirq.TOFFOLI( qubits[16], qubits[1], qubits[10] )
			yield cirq.CNOT( anc[4], qubits[29] )
			yield func16R(*nq2)
			yield cirq.TOFFOLI( qubits[44], qubits[24], qubits[37] )
# Function 5 with degree 3
# nq: 10, na: 2, ng: 6
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
		anc = qubits[10:] # ancilla
		res = [qubits[6], qubits[3], qubits[4], qubits[9], qubits[8], qubits[0], qubits[1], qubits[2], qubits[7], qubits[5]]
		# Non-leaf function
		func11 = Func11(15, is_inverse=self.is_inverse)
		func11R = Func11(15, is_inverse=(not self.is_inverse))
		nq0 = [qubits[0], qubits[4], anc[2], anc[3], anc[4], anc[5], anc[6], anc[7], anc[8], anc[9], anc[10], anc[11], anc[12], anc[13], anc[14]]
		func12 = Func12(7, is_inverse=self.is_inverse)
		func12R = Func12(7, is_inverse=(not self.is_inverse))
		nq1 = [anc[0], qubits[2], anc[1], qubits[7], anc[15], anc[16], anc[17]]
		func13 = Func13(20, is_inverse=self.is_inverse)
		func13R = Func13(20, is_inverse=(not self.is_inverse))
		nq2 = [qubits[0], qubits[2], qubits[3], qubits[7], qubits[9], qubits[1], anc[0], qubits[4], qubits[6], qubits[8], anc[1], qubits[5], anc[18], anc[19], anc[20], anc[21], anc[22], anc[23], anc[24], anc[25]]
		if not self.is_inverse: 
			# Compute 
			yield func12(*nq1)
			yield func11(*nq0)
			yield cirq.TOFFOLI( qubits[2], anc[1], qubits[6] )
			yield cirq.CNOT( qubits[1], qubits[3] )
			yield cirq.CNOT( qubits[9], qubits[2] )
			yield cirq.TOFFOLI( qubits[2], qubits[4], anc[1] )
			yield func13(*nq2)
			yield cirq.CNOT( qubits[8], qubits[7] )
			yield cirq.CNOT( anc[1], qubits[0] )
			# Store 
			# Note: this version does not store results.
		else: 
			yield cirq.CNOT( anc[1], qubits[0] )
			yield cirq.CNOT( qubits[8], qubits[7] )
			yield func13R(*nq2)
			yield cirq.TOFFOLI( qubits[2], qubits[4], anc[1] )
			yield cirq.CNOT( qubits[9], qubits[2] )
			yield cirq.CNOT( qubits[1], qubits[3] )
			yield cirq.TOFFOLI( qubits[2], anc[1], qubits[6] )
			yield func11R(*nq0)
			yield func12R(*nq1)
# Function 4 with degree 3
# nq: 68, na: 6, ng: 1
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
		anc = qubits[68:] # ancilla
		res = [qubits[36], qubits[42], qubits[54], qubits[29], qubits[18], qubits[31], qubits[43], qubits[5], qubits[65], qubits[61], qubits[7], qubits[64], qubits[27], qubits[32], qubits[40], qubits[48], qubits[1], qubits[51], qubits[10], qubits[21], qubits[24], qubits[2], qubits[46], qubits[67], qubits[63], qubits[49], qubits[8], qubits[44], qubits[6], qubits[34], qubits[62], qubits[14], qubits[47], qubits[17], qubits[39], qubits[20], qubits[37], qubits[3], qubits[4], qubits[57], qubits[59], qubits[28], qubits[0], qubits[56], qubits[15], qubits[33], qubits[25], qubits[16], qubits[66], qubits[9], qubits[45], qubits[35], qubits[23], qubits[50], qubits[12], qubits[58], qubits[38], qubits[13], qubits[41], qubits[52], qubits[26], qubits[53], qubits[11], qubits[55], qubits[60], qubits[30], qubits[22]]
		# Non-leaf function
		func8 = Func8(73, is_inverse=self.is_inverse)
		func8R = Func8(73, is_inverse=(not self.is_inverse))
		nq0 = [qubits[66], qubits[43], qubits[45], qubits[1], qubits[0], qubits[52], qubits[29], qubits[30], qubits[57], qubits[24], qubits[36], qubits[16], qubits[11], qubits[60], anc[5], qubits[8], qubits[62], anc[2], qubits[35], qubits[4], qubits[51], qubits[26], anc[3], qubits[17], qubits[56], qubits[5], qubits[34], qubits[55], qubits[19], qubits[54], anc[4], qubits[44], qubits[7], qubits[28], qubits[41], qubits[53], qubits[42], qubits[37], qubits[61], qubits[47], qubits[9], qubits[50], qubits[18], qubits[58], qubits[63], qubits[10], qubits[20], qubits[12], qubits[3], anc[1], qubits[21], qubits[15], qubits[67], qubits[2], qubits[32], qubits[48], qubits[46], qubits[23], qubits[38], qubits[31], qubits[25], qubits[49], qubits[64], anc[6], anc[7], anc[8], anc[9], anc[10], anc[11], anc[12], anc[13], anc[14], anc[15]]
		func9 = Func9(42, is_inverse=self.is_inverse)
		func9R = Func9(42, is_inverse=(not self.is_inverse))
		nq1 = [qubits[56], qubits[62], qubits[39], qubits[4], qubits[60], qubits[41], qubits[51], qubits[5], qubits[67], qubits[27], qubits[3], qubits[25], qubits[9], qubits[31], qubits[11], anc[3], qubits[53], qubits[33], qubits[36], anc[16], anc[17], anc[18], anc[19], anc[20], anc[21], anc[22], anc[23], anc[24], anc[25], anc[26], anc[27], anc[28], anc[29], anc[30], anc[31], anc[32], anc[33], anc[34], anc[35], anc[36], anc[37], anc[38]]
		func10 = Func10(42, is_inverse=self.is_inverse)
		func10R = Func10(42, is_inverse=(not self.is_inverse))
		nq2 = [qubits[8], qubits[33], qubits[56], qubits[25], qubits[41], qubits[48], qubits[11], qubits[30], qubits[34], qubits[10], qubits[55], qubits[42], qubits[6], qubits[20], qubits[28], qubits[54], qubits[26], qubits[64], qubits[47], anc[3], qubits[19], qubits[61], qubits[43], qubits[2], qubits[4], anc[5], qubits[21], qubits[52], qubits[0], qubits[51], qubits[9], anc[39], anc[40], anc[41], anc[42], anc[43], anc[44], anc[45], anc[46], anc[47], anc[48], anc[49]]
		if not self.is_inverse: 
			# Compute 
			yield func10(*nq2)
			yield func9(*nq1)
			yield cirq.CNOT( anc[2], qubits[49] )
			yield func8(*nq0)
			# Store 
			# Note: this version does not store results.
		else: 
			yield func8R(*nq0)
			yield cirq.CNOT( anc[2], qubits[49] )
			yield func9R(*nq1)
			yield func10R(*nq2)
# Function 3 with degree 1
# nq: 107, na: 4, ng: 2
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
		anc = qubits[107:] # ancilla
		res = [qubits[80], qubits[59], qubits[85], qubits[105], qubits[89], qubits[60]]
		# Non-leaf function
		func7 = Func7(83, is_inverse=self.is_inverse)
		func7R = Func7(83, is_inverse=(not self.is_inverse))
		nq0 = [qubits[15], qubits[28], qubits[100], qubits[62], qubits[45], qubits[39], qubits[42], qubits[59], qubits[99], qubits[106], qubits[0], qubits[27], qubits[32], qubits[84], qubits[23], qubits[18], qubits[61], qubits[85], qubits[103], qubits[74], qubits[58], anc[2], qubits[101], qubits[8], qubits[87], qubits[16], qubits[29], qubits[91], qubits[78], qubits[104], qubits[69], qubits[81], qubits[6], qubits[26], qubits[20], qubits[79], qubits[4], qubits[24], qubits[57], qubits[51], qubits[14], anc[3], qubits[2], qubits[48], qubits[68], qubits[21], anc[0], qubits[54], qubits[86], qubits[19], qubits[102], qubits[34], qubits[60], qubits[95], qubits[73], qubits[1], qubits[17], qubits[43], qubits[33], qubits[49], anc[1], qubits[44], qubits[82], qubits[37], qubits[98], qubits[72], qubits[56], qubits[30], qubits[47], qubits[25], qubits[105], qubits[35], qubits[70], qubits[63], qubits[40], qubits[89], qubits[50], anc[4], anc[5], anc[6], anc[7], anc[8], anc[9]]
		if not self.is_inverse: 
			# Compute 
			yield cirq.CNOT( qubits[26], qubits[11] )
			yield func7(*nq0)
			yield cirq.TOFFOLI( anc[1], qubits[19], qubits[48] )
			# Store 
			# Note: this version does not store results.
		else: 
			yield cirq.TOFFOLI( anc[1], qubits[19], qubits[48] )
			yield func7R(*nq0)
			yield cirq.CNOT( qubits[26], qubits[11] )
# Function 2 with degree 2
# nq: 83, na: 7, ng: 3
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
		anc = qubits[83:] # ancilla
		res = [qubits[67], qubits[57], qubits[31], qubits[48], qubits[72], qubits[52], qubits[54], qubits[46], qubits[1], qubits[76], qubits[4], qubits[77], qubits[35], qubits[37], qubits[22], qubits[78], qubits[7], qubits[36], qubits[27], qubits[30], qubits[33], qubits[41], qubits[50], qubits[28], qubits[71], qubits[0], qubits[82], qubits[58], qubits[3], qubits[20], qubits[17], qubits[34], qubits[12], qubits[79], qubits[26], qubits[63], qubits[13], qubits[5], qubits[51], qubits[75], qubits[49], qubits[38], qubits[68], qubits[74], qubits[9], qubits[29], qubits[80], qubits[70], qubits[65], qubits[60], qubits[69], qubits[10], qubits[43], qubits[25], qubits[6], qubits[73], qubits[45], qubits[39], qubits[53], qubits[15]]
		# Non-leaf function
		func5 = Func5(36, is_inverse=self.is_inverse)
		func5R = Func5(36, is_inverse=(not self.is_inverse))
		nq0 = [qubits[50], qubits[79], qubits[22], qubits[38], qubits[24], anc[2], qubits[3], qubits[76], qubits[16], qubits[61], anc[7], anc[8], anc[9], anc[10], anc[11], anc[12], anc[13], anc[14], anc[15], anc[16], anc[17], anc[18], anc[19], anc[20], anc[21], anc[22], anc[23], anc[24], anc[25], anc[26], anc[27], anc[28], anc[29], anc[30], anc[31], anc[32]]
		func6 = Func6(83, is_inverse=self.is_inverse)
		func6R = Func6(83, is_inverse=(not self.is_inverse))
		nq1 = [anc[2], qubits[43], qubits[5], qubits[42], qubits[45], qubits[16], qubits[27], qubits[72], qubits[73], qubits[30], qubits[34], qubits[25], qubits[51], qubits[17], qubits[66], qubits[0], qubits[81], qubits[77], qubits[50], qubits[44], qubits[65], qubits[56], qubits[67], qubits[22], qubits[21], qubits[11], qubits[9], qubits[3], qubits[75], qubits[7], qubits[24], qubits[2], qubits[82], qubits[79], anc[3], qubits[47], qubits[8], qubits[23], qubits[13], anc[0], qubits[71], qubits[49], qubits[48], qubits[1], qubits[18], qubits[4], qubits[69], qubits[28], qubits[31], qubits[63], qubits[78], qubits[38], qubits[57], qubits[76], qubits[68], anc[6], qubits[58], qubits[39], anc[33], anc[34], anc[35], anc[36], anc[37], anc[38], anc[39], anc[40], anc[41], anc[42], anc[43], anc[44], anc[45], anc[46], anc[47], anc[48], anc[49], anc[50], anc[51], anc[52], anc[53], anc[54], anc[55], anc[56], anc[57]]
		if not self.is_inverse: 
			# Compute 
			yield func6(*nq1)
			yield cirq.CNOT( qubits[57], qubits[77] )
			yield cirq.CNOT( qubits[11], anc[1] )
			yield cirq.CNOT( qubits[64], qubits[44] )
			yield func5(*nq0)
			# Store 
			# Note: this version does not store results.
		else: 
			yield func5R(*nq0)
			yield cirq.CNOT( qubits[64], qubits[44] )
			yield cirq.CNOT( qubits[11], anc[1] )
			yield cirq.CNOT( qubits[57], qubits[77] )
			yield func6R(*nq1)
# Function 1 with degree 3
# nq: 128, na: 8, ng: 8
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
		anc = qubits[128:] # ancilla
		res = [qubits[88], qubits[84], qubits[27], qubits[72], qubits[70], qubits[39], qubits[96], qubits[58], qubits[47], qubits[105], qubits[87], qubits[125], qubits[64], qubits[122], qubits[77], qubits[117], qubits[118], qubits[102], qubits[16], qubits[126], qubits[86], qubits[85], qubits[11], qubits[35], qubits[44], qubits[32], qubits[9], qubits[12], qubits[2], qubits[94], qubits[61], qubits[43], qubits[45], qubits[54], qubits[112], qubits[93], qubits[50], qubits[3], qubits[15], qubits[121], qubits[103], qubits[21], qubits[13], qubits[113], qubits[6], qubits[14], qubits[62], qubits[22], qubits[53], qubits[119], qubits[76], qubits[71], qubits[108], qubits[99], qubits[36], qubits[59], qubits[82], qubits[56], qubits[95], qubits[116], qubits[1], qubits[97], qubits[17], qubits[100], qubits[51], qubits[10], qubits[81], qubits[110], qubits[49], qubits[101], qubits[48], qubits[109], qubits[38], qubits[68], qubits[127], qubits[107], qubits[57], qubits[7], qubits[98], qubits[69], qubits[41], qubits[67], qubits[37], qubits[104], qubits[73], qubits[123], qubits[28], qubits[31], qubits[111], qubits[4], qubits[89], qubits[115], qubits[66], qubits[0], qubits[30]]
		# Non-leaf function
		func2 = Func2(141, is_inverse=self.is_inverse)
		func2R = Func2(141, is_inverse=(not self.is_inverse))
		nq0 = [qubits[85], qubits[14], qubits[80], qubits[122], qubits[16], qubits[24], qubits[18], qubits[109], qubits[10], qubits[52], qubits[51], qubits[40], qubits[74], qubits[34], qubits[55], qubits[70], qubits[117], qubits[6], qubits[5], anc[0], qubits[64], qubits[47], qubits[126], qubits[106], qubits[11], qubits[124], qubits[110], qubits[97], qubits[101], anc[7], qubits[62], qubits[2], qubits[96], qubits[44], qubits[68], anc[1], qubits[60], qubits[27], qubits[83], qubits[20], qubits[19], qubits[46], qubits[84], qubits[69], qubits[25], qubits[103], qubits[33], qubits[89], qubits[38], qubits[54], qubits[63], qubits[92], qubits[56], qubits[107], qubits[42], qubits[94], qubits[53], anc[6], qubits[15], qubits[90], qubits[71], qubits[113], qubits[49], anc[4], qubits[112], qubits[65], qubits[111], qubits[12], qubits[82], qubits[99], anc[3], qubits[115], qubits[91], qubits[105], qubits[1], qubits[73], qubits[125], qubits[31], qubits[75], qubits[57], qubits[104], qubits[100], qubits[35], anc[8], anc[9], anc[10], anc[11], anc[12], anc[13], anc[14], anc[15], anc[16], anc[17], anc[18], anc[19], anc[20], anc[21], anc[22], anc[23], anc[24], anc[25], anc[26], anc[27], anc[28], anc[29], anc[30], anc[31], anc[32], anc[33], anc[34], anc[35], anc[36], anc[37], anc[38], anc[39], anc[40], anc[41], anc[42], anc[43], anc[44], anc[45], anc[46], anc[47], anc[48], anc[49], anc[50], anc[51], anc[52], anc[53], anc[54], anc[55], anc[56], anc[57], anc[58], anc[59], anc[60], anc[61], anc[62], anc[63], anc[64], anc[65]]
		func3 = Func3(117, is_inverse=self.is_inverse)
		func3R = Func3(117, is_inverse=(not self.is_inverse))
		nq1 = [anc[2], qubits[71], qubits[48], qubits[105], qubits[65], qubits[109], qubits[0], qubits[46], qubits[104], qubits[2], qubits[99], qubits[122], anc[7], qubits[90], qubits[3], qubits[73], qubits[94], qubits[116], qubits[124], anc[6], qubits[110], qubits[8], qubits[92], qubits[9], qubits[4], qubits[21], qubits[31], qubits[37], qubits[16], anc[1], qubits[22], anc[4], qubits[98], qubits[80], qubits[117], qubits[121], qubits[18], qubits[6], qubits[40], qubits[53], qubits[96], qubits[119], qubits[106], qubits[17], qubits[28], qubits[84], qubits[13], qubits[68], qubits[81], qubits[88], qubits[33], qubits[39], qubits[62], qubits[83], qubits[120], qubits[5], qubits[49], qubits[41], qubits[51], qubits[52], qubits[50], qubits[36], anc[0], qubits[63], qubits[34], anc[3], qubits[44], qubits[100], qubits[66], qubits[89], qubits[75], qubits[72], qubits[32], qubits[97], qubits[87], qubits[76], qubits[38], qubits[10], qubits[107], qubits[61], qubits[23], qubits[78], qubits[20], qubits[42], qubits[12], qubits[114], qubits[103], qubits[24], qubits[58], qubits[11], qubits[30], qubits[95], qubits[111], qubits[79], qubits[15], qubits[43], qubits[85], qubits[27], qubits[26], qubits[56], qubits[35], qubits[125], qubits[127], qubits[118], qubits[123], qubits[55], qubits[69], anc[66], anc[67], anc[68], anc[69], anc[70], anc[71], anc[72], anc[73], anc[74], anc[75]]
		func4 = Func4(118, is_inverse=self.is_inverse)
		func4R = Func4(118, is_inverse=(not self.is_inverse))
		nq2 = [qubits[32], anc[4], qubits[74], qubits[122], qubits[84], qubits[96], qubits[41], qubits[68], qubits[0], qubits[17], qubits[28], anc[5], qubits[59], qubits[113], qubits[45], qubits[54], qubits[71], qubits[92], qubits[42], qubits[12], qubits[72], qubits[117], qubits[116], qubits[124], anc[1], qubits[121], qubits[6], qubits[104], qubits[99], qubits[123], qubits[61], qubits[63], qubits[11], qubits[55], qubits[31], qubits[43], qubits[65], qubits[108], qubits[44], qubits[86], qubits[29], qubits[109], qubits[34], qubits[101], qubits[111], qubits[110], qubits[52], anc[3], qubits[120], qubits[103], qubits[4], qubits[26], qubits[27], qubits[53], qubits[35], anc[0], qubits[50], qubits[36], qubits[49], qubits[106], qubits[119], qubits[73], qubits[22], qubits[66], qubits[118], qubits[77], qubits[81], qubits[9], anc[76], anc[77], anc[78], anc[79], anc[80], anc[81], anc[82], anc[83], anc[84], anc[85], anc[86], anc[87], anc[88], anc[89], anc[90], anc[91], anc[92], anc[93], anc[94], anc[95], anc[96], anc[97], anc[98], anc[99], anc[100], anc[101], anc[102], anc[103], anc[104], anc[105], anc[106], anc[107], anc[108], anc[109], anc[110], anc[111], anc[112], anc[113], anc[114], anc[115], anc[116], anc[117], anc[118], anc[119], anc[120], anc[121], anc[122], anc[123], anc[124], anc[125]]
		if not self.is_inverse: 
			# Compute 
			yield cirq.CNOT( qubits[54], qubits[102] )
			yield cirq.CNOT( qubits[83], qubits[67] )
			yield cirq.CNOT( qubits[61], qubits[74] )
			yield func2(*nq0)
			yield cirq.CNOT( qubits[6], qubits[70] )
			yield func3(*nq1)
			yield cirq.CNOT( qubits[81], qubits[82] )
			yield cirq.TOFFOLI( qubits[122], qubits[102], qubits[14] )
			yield cirq.CNOT( qubits[39], qubits[20] )
			yield cirq.TOFFOLI( qubits[11], qubits[96], qubits[23] )
			yield func4(*nq2)
			# Store 
			# Note: this version does not store results.
		else: 
			yield func4R(*nq2)
			yield cirq.TOFFOLI( qubits[11], qubits[96], qubits[23] )
			yield cirq.CNOT( qubits[39], qubits[20] )
			yield cirq.TOFFOLI( qubits[122], qubits[102], qubits[14] )
			yield cirq.CNOT( qubits[81], qubits[82] )
			yield func3R(*nq1)
			yield cirq.CNOT( qubits[6], qubits[70] )
			yield func2R(*nq0)
			yield cirq.CNOT( qubits[61], qubits[74] )
			yield cirq.CNOT( qubits[83], qubits[67] )
			yield cirq.CNOT( qubits[54], qubits[102] )
# main function
def main():
	num_in = 128
	num_anc = 126
	c = cirq.Circuit()
	in_qubits = [cirq.GridQubit(i,0) for i in range(num_in)]
	anc_qubits = [cirq.GridQubit(num_in+i,0) for i in range(num_anc)]
	all_qubits = in_qubits + anc_qubits
	# Intialize random inputs
	c.append([cirq.X(in_qubits[98])])
	c.append([cirq.X(in_qubits[69])])
	c.append([cirq.X(in_qubits[87])])
	c.append([cirq.X(in_qubits[29])])
	c.append([cirq.X(in_qubits[105])])
	c.append([cirq.X(in_qubits[97])])
	c.append([cirq.X(in_qubits[30])])
	c.append([cirq.X(in_qubits[24])])
	c.append([cirq.X(in_qubits[38])])
	c.append([cirq.X(in_qubits[17])])
	c.append([cirq.X(in_qubits[108])])
	c.append([cirq.X(in_qubits[99])])
	c.append([cirq.X(in_qubits[45])])
	c.append([cirq.X(in_qubits[103])])
	c.append([cirq.X(in_qubits[114])])
	c.append([cirq.X(in_qubits[116])])
	c.append([cirq.X(in_qubits[49])])
	c.append([cirq.X(in_qubits[33])])
	c.append([cirq.X(in_qubits[46])])
	c.append([cirq.X(in_qubits[55])])
	c.append([cirq.X(in_qubits[6])])
	c.append([cirq.X(in_qubits[77])])
	c.append([cirq.X(in_qubits[117])])
	c.append([cirq.X(in_qubits[13])])
	c.append([cirq.X(in_qubits[119])])
	c.append([cirq.X(in_qubits[122])])
	c.append([cirq.X(in_qubits[83])])
	c.append([cirq.X(in_qubits[93])])
	c.append([cirq.X(in_qubits[110])])
	c.append([cirq.X(in_qubits[101])])
	c.append([cirq.X(in_qubits[74])])
	c.append([cirq.X(in_qubits[113])])
	c.append([cirq.X(in_qubits[42])])
	c.append([cirq.X(in_qubits[71])])
	c.append([cirq.X(in_qubits[76])])
	c.append([cirq.X(in_qubits[44])])
	c.append([cirq.X(in_qubits[8])])
	c.append([cirq.X(in_qubits[16])])
	c.append([cirq.X(in_qubits[124])])
	c.append([cirq.X(in_qubits[63])])
	# Start computation
	func1 = Func1(254, is_inverse=False)
	circ = func1(*all_qubits)
	func1R = Func1(254, is_inverse=True)
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
