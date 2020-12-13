import pandas as pd
import numpy as np

def getNoiseMap(name):
    content = pd.read_csv(name)
    length=len(content)
    noiseMap = np.zeros((length,length))
    single=content['Single-qubit U2 error rate']
    cnot=content['CNOT error rate']
    for i in range(length):
        noiseMap[i,i]=single[i]
        cnotE = cnot[i]
        Elist = cnotE.split(',')
        for item in Elist:
            pair = item.split(':')
            error = float(pair[1])
            qubits=pair[0].split('_')
            target = int(qubits[1])
            noiseMap[i,target]= error
            noiseMap[target,i]=error


    return noiseMap


if __name__ =='__main__':
    b=getNoiseMap('hdwspec')
    print(b[:6,:6])
