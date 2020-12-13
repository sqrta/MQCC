""" rand_bench_cirq.py - Script for generating Cirq implementation of synthetic
    functions.

=== Usage ===
Usage: rand_bench_cirq.py -o <output file> -q <qubits> -a <ancilla> -g <gates> -L <levels> -d <degree> -s <seed, optional>

=== Reference ===
Part of the SQUARE benchmark set: https://arxiv.org/abs/2004.08539

=== Note ===
This implementation performs uncomputation.

"""


import random
import cirq

from cirq.ops import raw_types


import os, sys, getopt, math, random

SEED = 15859211
# call graph degree: number of distinct callees in a function
DEFAULT_MAX_DEGREE = 3
TL = 0 # tab level

builtR = []

def tab():
    global TL
    TL += 1

def untab():
    global TL
    TL -= 1

def writeline(outf, line_str):
    outf.write("\t"*TL + line_str + "\n")

def strsum(s):
    res = "["
    for (i,e) in enumerate(s):
        res += e
        if i < len(s)-1:
            res += ", "
    res += "]"
    return res

def sample_gates(ng, nq, na):
    # returns the operands
    res = []
    for ig in range(ng):
        # Sample a random gate (CNOT or Toffoli)
        num_op = random.randint(2,3)
        ops = random.sample(range(nq+na), num_op)
        res.append(ops)
    return res
   
    buff += "\t"*TL +  + "\n"
    buff_r += "\t"*TL +  + "\n"

def get_nanc(all_calls):
    # all_calls[i]: (i, callees, [nq,na,ng, len(parent)])
    ncall = len(all_calls)
    all_nancs = [0 for _ in range(ncall)] # ignore 0th
    parent = [0 for _ in range(ncall)] # ignore 0th
    for (i,callee,_) in all_calls:
        for c in callee:
            parent[c] = i
    ancestors = [[] for _ in range(ncall)]
    for i in range(1,ncall):
        idx = i
        p = parent[idx]
        while not p==0:
            ancestors[i].append(p)
            idx = p
            p = parent[idx]
    
    for (i,c,n) in all_calls[1:]:
        all_nancs[i] += n[1] # num ancilla of current
        for p in ancestors[i]:
            all_nancs[p] += n[1] # add to all ancestors
    return all_nancs
        

def build_fun(i, all_calls, all_nancs, outf):
    # all_calls[i]: (i, callees, [nq,na,ng])
    callees = all_calls[i][1]
    nq = all_calls[i][2][0]
    na = all_calls[i][2][1] # num ancilla of func i itself
    nanc = all_nancs[i] # num ancilla of func i and its children
    ng = all_calls[i][2][2]
    parent_degree = all_calls[i][2][3]
    buff = ""
    buff_r = ""
    # Write a function with branching degree b
    buff += "\t"*TL + "# Function " + str(i) + " with degree " + str(len(callees)) + "\n"
    buff_r += "\t"*TL + "# Function " + str(i) + " with degree " + str(len(callees)) + "\n"
    buff += "\t"*TL + "# nq: " + str(nq) + ", na: " + str(na) + ", ng: " + str(ng) + "\n"
    buff_r += "\t"*TL + "# nq: " + str(nq) + ", na: " + str(na) + ", ng: " + str(ng) + "\n"
    buff += "\t"*TL + "class Func" + str(i) + "(cirq.Gate):" + "\n"

    tab()
    all_ops = sample_gates(ng, nq, na)
    interqs = [x for ops in all_ops for x in ops if x < nq] # TODO? remove duplicates
    buff += "\t"*TL + "def __init__(self, num_qubits, is_inverse=False):\n"
    tab()
    buff += "\t"*TL + "self._num_qubits = num_qubits\n"
    buff += "\t"*TL + "self.is_inverse = is_inverse\n"
    untab()
    buff += "\t"*TL + "def num_qubits(self):\n"
    tab()
    buff += "\t"*TL + "return self._num_qubits\n"
    untab()
    buff += "\t"*TL + "def __pow__(self, power):\n"
    tab()
    buff += "\t"*TL + "if power == -1:\n"
    tab()
    buff += "\t"*TL + "return Func" + str(i)+ "(self._num_qubits, is_inverse=True)\n"
    untab()
    buff += "\t"*TL + "else:\n"
    tab()
    buff += "\t"*TL + "return NotImplemented\n"
    untab()
    untab()
    buff += "\t"*TL + "def _decompose_(self, qubits):\n"
    tab()
    # Assign qubits for computation in current function
    buff += "\t"*TL + "anc = qubits["+str(nq)+":] # ancilla" + "\n"
    num_out = random.randint(1, nq)
    outs = random.sample(range(nq), num_out)
    buff += "\t"*TL + "res = " + strsum(["qubits[%d]"%qo for qo in outs]) + "\n"

    # Assign qubits for callees
    callees_nq = []
    for j in range(len(callees)):
        # need to sample the same number of qubits that callee needs
        num_q = all_calls[callees[j]][2][0]
        callees_nq.append(num_q)
    # Start computations
    all_ins = []
    all_ins_r = []
    for ops in all_ops:
        if (len(ops) == 2):
            op0 = "qubits["+str(ops[0])+"]" if (ops[0]<nq) else "anc["+str(ops[0]-nq)+"]"
            op1 = "qubits["+str(ops[1])+"]" if (ops[1]<nq) else "anc["+str(ops[1]-nq)+"]"
            all_ins.append("cirq.CNOT( " + op0 + ", " + op1 + " )")
            all_ins_r.append("cirq.CNOT( " + op0 + ", " + op1 + " )")
        else:
            op0 = "qubits["+str(ops[0])+"]" if (ops[0]<nq) else "anc["+str(ops[0]-nq)+"]"
            op1 = "qubits["+str(ops[1])+"]" if (ops[1]<nq) else "anc["+str(ops[1]-nq)+"]"
            op2 = "qubits["+str(ops[2])+"]" if (ops[2]<nq) else "anc["+str(ops[2]-nq)+"]"
            all_ins.append("cirq.TOFFOLI( " + op0 + ", " + op1 + ", " + op2 + " )")
            all_ins_r.append("cirq.TOFFOLI( " + op0 + ", " + op1 + ", " + op2 + " )")

    if (len(callees) == 0):
        buff += "\t"*TL + "# Leaf function" + "\n"
        # Now ready to allocate the ancilla
        buff += "\t"*TL + "if not self.is_inverse: \n"
        tab()
        buff += "\t"*TL + "# Compute \n"
        for ins in all_ins:
            buff += "\t"*TL + "yield " + ins + "\n"
        buff += "\t"*TL + "# Store \n"
        
        temp_bits = random.sample(range(nq+na), num_out) 
        for j in range(num_out):
            if (temp_bits[j]<nq):
                # need to be different from outs
                if (temp_bits[j] == outs[j]):
                    temp_op = "anc["+str(random.randint(0,na-1))+"]"
                else:
                    temp_op = "qubits["+str(temp_bits[j])+"]" 
            else:
                temp_op = "anc["+str(temp_bits[j]-nq)+"]"
            # Note: Uncomment next line if want to store to random qubits
            #buff += "\t"*TL + "yield cirq.CNOT( " + temp_op + ", res[" + str(j) + "] )" + "\n"
        buff += "\t"*TL + "# Note: this version does not store results.\n"
        untab()
        buff += "\t"*TL + "else: \n"
        tab()
        buff += "\t"*TL + "# Uncompute \n"

        for ins in reversed(all_ins):
            buff += "\t"*TL + "yield " + ins + "\n"
        untab()

    else:
        buff += "\t"*TL + "# Non-leaf function" + "\n"
        # Interleaving function calls among gates
        a_cnt = 0
        for (j, c) in enumerate(callees):
            num_q = callees_nq[j]
            num_a = all_nancs[c]
            buff += "\t"*TL + "func"+str(c)+" = Func"+str(c)+"("+str(num_q+num_a)+", is_inverse=self.is_inverse)\n"
            buff += "\t"*TL + "func"+str(c)+"R = Func"+str(c)+"("+str(num_q+num_a)+", is_inverse=(not self.is_inverse))\n"
            callee_q = random.sample(range(nq+na), num_q)
            buff += "\t"*TL + "nq"+str(j)+" = ["
            for (k,cq) in enumerate(callee_q):
                cq_op = "qubits["+str(cq)+"]" if (cq<nq) else "anc["+str(cq-nq)+"]"
                buff += cq_op
                if k < len(callee_q)-1:
                    buff += ", "
            for a in range(num_a):
                buff += ", anc["+str(na+a_cnt+a)+"]"
            a_cnt += num_a
            buff += "]\n"
            all_ins.append("func" + str(c) + "(*nq"+str(j)+")")
            all_ins_r.append("func" + str(c) + "R(*nq"+str(j)+")")
        indices = list(range(len(all_ins)))
        random.shuffle(indices)
        shuffle_ins = [all_ins[i] for i in indices]
        shuffle_ins_r = [all_ins_r[i] for i in indices]
        buff += "\t"*TL + "if not self.is_inverse: \n"
        tab()
        buff += "\t"*TL + "# Compute \n"
        # Now ready to allocate the ancilla
        # In-place reverse if building reverse version of function
        shuffle_ins_r.reverse()
        for ins in shuffle_ins:
            buff += "\t"*TL + "yield " + ins + "\n"
        buff += "\t"*TL + "# Store \n"
        temp_bits = random.sample(range(nq+na), num_out) 
        for j in range(num_out):
            if (temp_bits[j]<nq):
                # need to be different from outs
                if (temp_bits[j] == outs[j]):
                    temp_op = "anc["+str(random.randint(0,na-1))+"]"
                else:
                    temp_op = "qubits["+str(temp_bits[j])+"]" 
            else:
                temp_op = "anc["+str(temp_bits[j]-nq)+"]"
            # Note: Uncomment next line if want to store to random qubits
            #buff += "\t"*TL + "yield cirq.CNOT( " + temp_op + ", res[" + str(j) + "] );" + "\n"
        buff += "\t"*TL + "# Note: this version does not store results.\n"
        untab()
        buff += "\t"*TL + "else: \n"
        tab()
        for ins in shuffle_ins_r:
            buff += "\t"*TL + "yield " + ins + "\n"

        untab()
    untab()
    untab()

    outf.write(buff)

def build_main(callees, all_calls, all_nancs, outf, nq, na, ng):
    if (len(callees) == 0):
        print ("Error. main function should have at least one callees.")
        sys.exit()

    writeline(outf, "# main function")
    writeline(outf, "def main():")
    tab()
    # allocating qubits
    writeline(outf, "num_in = " + str (nq))
    nanc = sum([ac[2][1] for ac in all_calls[1:]])
    writeline(outf, "num_anc = " + str (nanc))
    writeline(outf, "c = cirq.Circuit()")
    writeline(outf, "in_qubits = [cirq.GridQubit(i,0) for i in range(num_in)]")
    writeline(outf, "anc_qubits = [cirq.GridQubit(num_in+i,0) for i in range(num_anc)]")
    writeline(outf, "all_qubits = in_qubits + anc_qubits")

    writeline(outf, "# Intialize random inputs")
    all_bits = range(nq)
    num_ones = random.randint(0, nq)
    bits = random.sample(all_bits, num_ones)
    for b in bits:
        writeline(outf, "c.append([cirq.X(in_qubits[" + str(b) + "])])")
    writeline(outf, "# Start computation")
    if (len(callees) == 1):
        for c in callees:
            writeline(outf, "func" + str(c) + " = Func"+str(c)+"(" + str(nq+nanc) + ", is_inverse=False)")
            writeline(outf, "circ = func" + str(c) + "(*all_qubits)")
            writeline(outf, "func" + str(c) + "R = Func"+str(c)+"(" + str(nq+nanc) + ", is_inverse=True)")
            writeline(outf, "circR = func" + str(c) + "R(*all_qubits)")
            writeline(outf, "c.append([circ])")
            writeline(outf, "c.append([circR])")

    else:
        callees_nq = []
        all_ins = []
        for j in range(len(callees)):
            # need to sample the same number of qubits that callee needs
            num_q = all_calls[callees[j]][2][0]
            callees_nq.append(num_q)
        a_cnt = 0
        for (j, c) in enumerate(callees):
            num_q = callees_nq[j]
            num_a = all_nancs[c]
            callee_q = random.sample(range(nq), num_q)
            nq_str = "nq"+str(j)+"=["
            for (k,cq) in enumerate(callee_q):
                cq_op = "in_qubits["+str(cq)+"]" 
                nq_str += cq_op
                if (k<len(callee_q)-1):
                    nq_str += ", "
            for a in range(num_a):
                nq_str += ", anc_qubits["+str(a_cnt+a)+"]" 
            a_cnt += num_a
            nq_str += "]"
            writeline(outf, nq_str)
            all_ins.append("func"+str(c)+" = Func"+str(c)+"("+str(num_q+num_a)+", is_inverse=False")
            all_ins.append("circ"+str(j)+" = func"+str(c)+"(*nq"+str(j)+")")
            all_ins.append("c.append([circ"+str(j)+"])")
            all_ins.append("func"+str(c)+"R = Func"+str(c)+"("+str(num_q+num_a)+", is_inverse=True")
            all_ins.append("circ"+str(j)+"R = func"+str(c)+"R(*nq"+str(j)+")")
            all_ins.append("c.append([circ"+str(j)+"R])")
        for ins in all_ins:
            writeline(outf, ins)

    writeline(outf, "c.append([cirq.measure(*in_qubits, key=\'result\')])")
    writeline(outf, "print(\"Circuit:\")")
    writeline(outf, "print(c)")
    
    writeline(outf, "if num_in + num_anc > 32:")
    tab()
    writeline(outf, "print(\"Done. Skipping simulation for circuit size > 32.\")")
    untab()
    writeline(outf, "else:")
    tab()
    writeline(outf, "simulator = cirq.Simulator()")
    writeline(outf, "result = simulator.run(c, repetitions=1)")
    writeline(outf, "print(\"Results:\")")
    writeline(outf, "print(result)")
    untab()

    untab()
    writeline(outf, "")

def printStructure(call_lists):
    print("[rand_bench_cirq.py] Program structure:")
    for (i,calls) in enumerate(call_lists):
        call_str = ",".join([str(c) for c in calls])
        print("\tFun " + str(i) + ": " + call_str)

def rand_synth(outname, outf, nq, na, ng, nl, nd):
    writeline(outf, "\"\"\" "+outname+" - Synthetic Cirq implementation.")
    writeline(outf, "=== Reference ===")
    writeline(outf, "Part of the SQUARE benchmark set: https://arxiv.org/abs/2004.08539")
    writeline(outf, "\"\"\"")
    writeline(outf, "# Cirq file synthesized by rand_bench_cirq.py")
    writeline(outf, "# qubits: " + str(nq) + " ancilla: " + str(na) + " gates: " + str(ng) + " levels: " + str(nl) + " degrees: "+ str(nd))
    writeline(outf, "import random")
    writeline(outf, "import cirq")
    writeline(outf, "from cirq.ops import raw_types")
    # Build a tree-like program with depth nl, and random branching
    # First create the random branching array A[l] is the branching 

    random.seed(SEED)
    print("[rand_bench_cirq.py] Random seed used: " + str(SEED))

    if (nl == 1):
        call_lists = [[i for i in range(1,nd+1)]]
    else:
        branch = [random.randint(0,nd) for li in range(nd**nl)]
        if branch[0]==0:
            branch[0]+=1
        cuts = [1]
        start = 0
        end = 1
        for b in branch:
            if end >= len(branch):
                break
            temp = 0
            for i in range(start,end):
                temp += branch[i]
            cuts.append(cuts[-1]+temp)
            start = end
            end = end + temp
        acc = 1
        ll = 0
        call_lists = []
        for (i, b) in enumerate(branch):
            call_lists.append([j for j in range(acc, acc+b)])
            acc += b
            if i in cuts:
                ll += 1 
            if ll >= nl:
                break
        
    print(call_lists)
        
    printStructure(call_lists)
    writeline(outf, "# Call list: " + (";".join([",".join([str(c) for c in calls]) for calls in call_lists])))
    num_funs = 0
    for calls in call_lists:
        num_funs += len(calls)
    all_calls = [(0,[],[]) for _ in range(num_funs+1)]
    all_calls[0] = (0, call_lists[0], (nq, 0, 0, 0)) # for main
    for (i, calls) in enumerate(call_lists):
        for c in calls:
            callees = call_lists[c] if (c < len(call_lists)) else []
            if (i == 0):
                if (len(calls) == 1):
                    subq = nq
                    suba = na
                    subg = ng
                else:
                    subq = random.randint(2, nq)
                    suba = random.randint(1, na)
                    subg = random.randint(1, ng)
                    
            else:
                subq = random.randint(2,min(nq, all_calls[i][2][0]+all_calls[i][2][1])) # fewer than nq+na of parent
                suba = random.randint(1, na) # ancs dont have to be fewer 
                subg = random.randint(1, ng) # gates dont have to be fewer 
            all_calls[c] = (c, callees, [subq, suba, subg, len(calls)])
            
    all_nancs = get_nanc(all_calls)
    builtR = [0 for _ in range(len(all_calls))]
    for (c, _, _) in reversed(all_calls[1:]):
        build_fun(c, all_calls, all_nancs, outf)

    # Lastly, build main
    build_main(call_lists[0], all_calls, all_nancs, outf, nq, na, ng)
    
    writeline(outf, "if __name__ == \'__main__\':")
    tab()
    writeline(outf, "main()")
    untab()

    print("[rand_bench_cirq.py] Sythetic benchmark written to: " + outf.name)


def main():
    s = -1
    outname= ""
    num_qubits = 0
    num_ancilla= 0 # max per function 
    num_gates = 0
    L = 0
    d = DEFAULT_MAX_DEGREE
    try:
        opt, args = getopt.getopt(sys.argv[1:], "ho:q:a:g:L:d:s:", ["help", "output=", "qubits=", "ancilla=", "gates=", "levels=", "degree=", "seed="])
    except getopt.GetOptError as err:
        print(err)
        print("Usage: rand_bench_cirq.py -o <output file> -q <qubits> -a <ancilla> -g <gates> -L <levels> -d <degree> -s <seed, optional>")
        sys.exit(2)
    for o,a in opt:
        if o in ("-h", "--help"):
            print("Usage: rand_bench_cirq.py -o <output file> -q <qubits> -a <ancilla> -g <gates> -L <levels> -d <degree> -s <seed, optional>")
            sys.exit()
        elif o in ("-o", "--output"):
            outname = a
        elif o in ("-q", "--qubits"):
            num_qubits = int(a)
        elif o in ("-a", "--ancilla"):
            num_ancilla = int(a)
        elif o in ("-g", "--gates"):
            num_gates = int(a)
        elif o in ("-L", "--levels"):
            L = int(a)
        elif o in ("-d", "--degree"):
            d = int(a)
        elif o in ("-s", "--seed"):
            s = int(a)
        else:
            print("Usage: rand_bench_cirq.py -o <output file> -q <qubits> -a <ancilla> -g <gates> -L <levels> -d <degree> -s <seed, optional>")
            sys.exit()
    if (num_qubits > 0 and num_ancilla > 0 and num_gates > 0 and L > 0 and d > 0):
        if (not outname):
            print("Please specify valid output scaffold filename")
        else:
            if (not s == -1):
                global SEED
                SEED = s
            with open(outname, 'w') as outfile:
                rand_synth(outname, outfile, num_qubits, num_ancilla,  num_gates, L, d)
    else:
        print("qubits, gates, or levels needs to be a positive integer.")
        print("Usage: rand_bench_cirq.py -o <output file> -q <qubits> -a <ancilla> -g <gates> -L <levels> -d <degree> -s <seed, optional>")
 
if __name__ == "__main__":
  main()

