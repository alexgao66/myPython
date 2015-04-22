print('------basic------')
print ('hello world!')
myStr = 'abc'
print(myStr)
a, b, c, d, e = 1, 'b', True, 3.14, 4+3j
print(type(a),type(b),type(c),type(d),type(e))

print('\n------number------')
print('2/4:',2/4)
print('2//4:',2//4)
print('2 ** 5:', 2 ** 5)

print('\n------str------')
s = 'Yes,he\'s'
print(s,type(s),len(s))
print('c:\a\b')
print(r'c:\a\b')
print('str'+'ing','alex'*2)
p = 'Python'
print(p[0],p[5])
print(p[-6],p[-1])
print(p[0:1])
print(p[-6:-5])
print(p[2:])
print(p[-4:])

print('\n------list------')
a = ['She','is','my','lover']
print(a)
print(a + ['He','is','my','boy'])
a[3] = 'wife';
print(a)
print(a[2:3])
print(a[2:])
a[2:] = []
print(a)
