#Referências: https://www.youtube.com/watch?v=o7iCDj3Atms
#https://www.youtube.com/watch?v=mkkQMO9dQxI

def zera(linha1, exesub):
  final = []
  for i in range(len(linha1)):
    final.append(0)
  for i in range(len(linha1)):
    x = linha1[i] - exesub[i]
    final[i]=x
  return final
  
def ExE(linha1, linha):
    exe = []
    for i in range(len(linha1)):
      exe.append(0)
    for i in range(len(linha1)):
        x = linha1[i] * linha
        exe[i]= x
    return exe
  
def pivotamento(m):
  for i in range(0,len(m) - 1):
    for j in range(i + 1,len(m)):
      if m[j][i] == 0:
        for k in range(i,len(m)):
          if m[k][i] != 0:
            m[i],m[k] = m[k],m[i]
      if m[i][i] != 0:
        expected = m[j][i] / m[i][i]
        exe = ExE(m[i], expected)
        linha = m[j]
        m[j] = zera(exe, linha)
      
  return m

def triangular(m):
  b = [] #separa respostas em vetor B para melhor entendimento
  for i in range(0,len(m)):
    b.append(m[i][len(m)])
  A = m #separa incognitas em matriz A para melhor entendimento
  for i in range(0,len(m)):
    A[i].pop()
  resultados = []
  for i in range(len(m)):
    resultados.append(0)
  for y in range(len(m)-1,-1,-1):
    x = b[y]
    xj = len(A)-1
    for k in range(len(m)-1,y,-1):#-somatoria
      x -= A[y][k]*resultados[k] 
      xj -= 1
    x/= A[y][y] #divide por aii
    resultados[xj]=x
  return resultados

def printM(m):
  for i in range(len(m)):
    for j in range(len(m[i])):
      print(m[i][j],end = "   ")
    print('\n')
    
def gauss(m):
  printM(m)
  print('\n')
  m = pivotamento(m)
  printM(pivotamento(m))
  resultados = triangular(m)
  print(resultados)
  
def testePivot(): #testes
  print('testes pivotamento')
  m = [[1.0, -1.0, 2.0, -1.0, -8.0], [2.0, -2.0, 3.0, -3.0, -20.0], [1.0, 1.0, 1.0, 0.0, -2.0], [1.0, -1.0, 4.0, 3.0, 4.0]]
  printM(pivotamento(m))
  print('\n')
  newm = [[1.0, -1.0, 2.0, -1.0, -6.0], [2.0, -4.0, 3.0, -3.0, -28.0], [1.0, 1.0, 1.0, 0.0, -2.0], [1.0, -1.0, 2.0, 3.0, 2.0]]
  printM(pivotamento(newm))
  
def testeTriang(): #testes
  print('testes triangular')
  m = [[1.0, -1.0, 2.0, -1.0, -8.0], [0.0, 2.0, -1.0, 1.0, 6.0], [0.0, 0.0, 1.0, 1.0, 4.0], [0.0, 0.0, 0.0, -2.0, -4.0]]
  print(triangular(m))
  newm = [[1.0, 1.0, 1.0, 1.0], [0.0, -1.0, -3.0, -2.0], [0.0, 0.0, 1.0, 1.0]]
  print(triangular(newm))

def testeGauss():#testes
  print('testes gauss')
  m = [[1.0, -1.0, 2.0, -1.0, -8.0], [2.0, -2.0, 3.0, -3.0, -20.0], [1.0, 1.0, 1.0, 0.0, -2.0], [1.0, -1.0, 4.0, 3.0, 4.0]]
  gauss(m)
  print('\n\n')
  newm = [[1.0, -1.0, 2.0, -1.0, -6.0], [2.0, -4.0, 3.0, -3.0, -28.0], [1.0, 1.0, 1.0, 0.0, -2.0], [1.0, -1.0, 2.0, 3.0, 2.0]]
  gauss(newm)

#gauss(m)
print('\n')
testeTriang()
print('\n')
testePivot()
print('\n')
testeGauss()
print('Exercícios')
a = [[1.0,-1.0,3.0,2.0],[1.0,-3.0,1.0,-1.0],[1.0,1.0,0.0,3.0]]
print('a\n')
gauss(a)

b = [[2.0,-1.5,3.0,1.0],[-1,0.0,2.0,3.0],[4.0,-4.5,5.0,1.0]]
print('b\n')
gauss(b)

c = [[2.0,0.0,0.0,0.0,3.0],[1,1.5,0.0,0.0,4.5],[0.0,-3.0,0.5,0.0,-6.6],[2.0,-2.0,1.0,1.0,0.8]]
print('c\n')
gauss(c)

d = [[1.0,1.0,0.0,1.0,2.0],[2.0,1.0,-1.0,1.0,1.0],[4.0,-1.0,-2.0,2.0,0.0],[3.0,-1.0,-1.0,2.0,-3.0]]
print('d\n')
gauss(d)
