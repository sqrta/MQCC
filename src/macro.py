import sys

def macroProcess(name):
    with open(name, 'r') as r:
        content = r.readlines()
        i = 0
        macroList = []
        text = ''
        while True:
            if i>=len(content):
                break
            item = content[i]
            if 'module' in item:
                defnition = item.split('module ', 1)[1]
                pair = defnition.split('{', 1)
                macroHead = pair[0]
                macroTail = pair[1]
                flag = 1
                while flag > 0:
                    i += 1
                    gateContent = content[i]
                    flag += gateContent.count('{') - gateContent.count('}')
                    macroTail += gateContent
                macroTail=macroTail.rstrip()
                macroTail.replace('//*\n','')
                macroTail=macroTail.rstrip('}').replace('\n','\\\n__NL__')
                dgpair = macroHead.split('(')
                dgHead = dgpair[0]+'dg(' + dgpair[1]
                macroList.append((macroHead,macroTail))
                macroList.append((dgHead, macroTail))
                i+=1
            else:
                text+=content[i]
                i+=1
        return text,macroList

def genMacro(source, target):
    text, macroList = macroProcess(source)
    with open(target,'w') as w:
        for item in macroList:
            w.write('#define ' + item[0] + ' ' + item[1] +'\n')
        w.write(text)

if __name__ == '__main__':
    source = sys.argv[1] 
    genMacro(source,'out.c')
    
