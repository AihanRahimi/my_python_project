#input information from usesr
x = input('name:'),int(input('nomre1:')),int(input('nomre2:')),int(input('nomre3:'))

#change x to list x 
y = list(x)

#make a dict of list x
z={'name':x[0],'dars1':x[1],'dars2':x[2],'dars3':x[3]}

#if for dars 1
if z['dars1'] < 10:
    print('fail')
else:
    print('pass')

#if for dars 2       
if z['dars2'] < 10:
    print('fail')
else:
    print('pass')

#if for dars 3
if z['dars3'] < 10:
    print('fail')
else:                 
    print('pass')
avg = (z['dars1']+z['dars2']+z['dars3'])/3
print(y[0],"'s avg=",avg)