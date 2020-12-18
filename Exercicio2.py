import math
list1 = []
cont = 0
b = 0
for cont in range (0,10):
  if cont % 2 ==0:
    b = (3**cont + 7*math.factorial(cont))
    list1.append(b)
  else:
    b = (2**cont + 4*math.log(cont))
    list1.append(b)
maior = max(list1)
media = sum(list1)/len(list1)
print (f'O maior valor da lista é {maior} e a média dos valores é {media:.2f}')