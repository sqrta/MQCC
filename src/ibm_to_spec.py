import csv
import pandas as pd

name = "ibmq_rochester.csv"
content = pd.read_csv(name)
column = ['Qubit', 'Single-qubit U2 error rate', 'CNOT error rate']
content = content[column]
content.to_csv('hdwspec', index=False)
