from typing_extensions import runtime
from qiskit import QuantumCircuit
from qiskit.circuit import instruction
import os
def name_index(name,index):
    return name+'['+str(index)+']'

def overlap(a,b):
    for i in a:
        for j in b:
            if i==j:
                return True
    return False
def mp_cm_Transpiler(target,root='.'):
    circ = QuantumCircuit.from_qasm_file(root+'\\'+target)
    with open('test_runtime\\'+target,'w') as f:
        f.write('qreg q[20],a[20],b[20],cin[20],reg[20];\n')
        for i in range(3):
            circ=circ.decompose()
        last = []
        count=0
        lastIsCNOT = ''
        for item in circ.data:
            gate = item[0]
            qubits = item[1]
            newqubits= [name_index(qubit.register.name,qubit.index) for qubit in qubits]
            para = ','.join([str(i) for i in gate.params])
            if para!='':
                para+=','
            inst = gate.qasm().split('(')[0]+'(' +  para + ','.join(newqubits)+');'
            
            if gate.qasm()=='cx': 
                if lastIsCNOT!='' and overlap(last,newqubits) and last!=[]:       
                    count+=1
                    f.write('choice([0,1]){\n0:'+ inst+'\n1: barrier('+','.join(newqubits)+');}\n')
                    lastIsCNOT=''
                else:
                    lastIsCNOT = inst
                    f.write(inst + '\n')
                    last = newqubits
            else:
                lastIsCNOT = ''
                f.write(inst + '\n')
    print(target+' ',count)

def cmTranspiler(target,root='.'):
    circ = QuantumCircuit.from_qasm_file(root+'\\'+target)
    with open('test_runtime\\'+target,'w') as f:
        f.write('qreg q[20],a[20],b[20],cin[20],reg[20];\n')
        for i in range(3):
            circ=circ.decompose()
        last = []
        count=0
        for item in circ.data:
            gate = item[0]
            qubits = item[1]
            newqubits= [name_index(qubit.register.name,qubit.index) for qubit in qubits]
            para = ','.join([str(i) for i in gate.params])
            if para!='':
                para+=','
            inst = gate.qasm().split('(')[0]+'(' +  para + ','.join(newqubits)+');'
            
            if gate.qasm()=='cx':        
                flag= True
                for i in newqubits:
                    for j in last:
                        if i==j:
                            flag=False
                            break
                if flag and last!=[]:
                    count+=1
                    f.write('choice([0,1]){\n0:'+ inst+'\n1: barrier('+','.join(newqubits)+');}\n')
                else:
                    f.write(inst + '\n')
                last = newqubits
            else:
                f.write(inst + '\n')
    print(target+' ',count)

g=os.walk(r"runtime")
#cmTranspiler('multiplier_n15.qasm','runtime')
for file in g:
    filelist=file[2]
    for target in filelist:
        cmTranspiler(target,'runtime')