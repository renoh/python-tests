def validaCpf(cpf,d1=0,d2=0,i=0):
    while i<10:
        d1,d2,i=(d1+(int(cpf[i])*(11-i-1)))%11 if i<9 else d1,(d2+(int(cpf[i])*(11-i)))%11,i+1
    return (int(cpf[9])==(11-d1 if d1>1 else 0)) and (int(cpf[10])==(11-d2 if d2>1 else 0))



import numpy

def calcula_digito(cpf):
  return (sum(numpy.prod(numpy.array([range(len(cpf)+1, 1, -1), cpf]), axis = 0))*10)%11%10

def validaCpf2(cpf):
  cpfN = [int(x) for x in cpf]
  return calcula_digito(cpfN[:-2]) == int(cpfN[-2]) and (calcula_digito(cpfN[:-1]) == int(cpfN[-1]))


def calcula_digito3(cpf):
  return (sum([(x*y) for (x,y) in zip(range(len(cpf)+1,1,-1),cpf)])*10)%11%10

def validaCpf3(cpf):
  cpfN = [int(x) for x in cpf]
  return calcula_digito3(cpfN[:-2]) == (cpfN[-2]) and (calcula_digito3(cpfN[:-1]) == (cpfN[-1]))

#digito RG
print calcula_digito3([int (x) for x in (reversed('34084844'))])


print 1
print validaCpf2('67383130804')
print validaCpf2('35062136873')
print validaCpf2('12345678901')

print 2
print validaCpf('67383130804')
print validaCpf('35062136873')
print validaCpf('12345678901')

print 3
print validaCpf3('67383130804')
print validaCpf3('35062136873')
print validaCpf3('12345678901')

import timeit
print timeit.timeit("validaCpf('67383130804')", setup="from __main__ import validaCpf", number=100000)
print timeit.timeit("validaCpf2('67383130804')", setup="from __main__ import validaCpf2", number=100000)
print timeit.timeit("validaCpf3('67383130804')", setup="from __main__ import validaCpf3", number=100000)