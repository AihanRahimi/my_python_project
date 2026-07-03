a = float(input('a: '))
b = float(input('b: '))
op = input('op: ')
if op == '+':
    c = a+b 
    print('%f %s %f=%s'%(a,op,b,c))
elif op == '-':
    c = a-b 
    print('%f %s %f=%s'%(a,op,b,c))  
elif op == '*':
    c = a*b 
    print('%f %s %f=%s'%(a,op,b,c))  
elif op == '/':
    c = a/b 
    print('%f %s %f=%s'%(a,op,b,c))     
else:
    print('error from op')       

