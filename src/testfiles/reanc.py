def do(num,name='anc'):
    a=[name+'[' + str(i) + ']' for i in range(num)]
    return ','.join(a)


import sys
n=sys.argv[1]
print(do(int(n),'anc2'))