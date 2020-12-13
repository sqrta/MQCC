with open('preout1', 'r') as f:
    content = f.read()
    content=content.replace('__NL__', '\n')

with open('preout','w') as w:
    w.write(content)