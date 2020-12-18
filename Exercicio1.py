x = 1
cont = 0

while x <= 5000000:
  if x%2==0 and x%49==0 and x%37==0:
    cont+=1
    x+=1
  else:
    x=x+1

print(f'A quantidade de números pares, divisiveis por 49 e 37 entre 1 e 5.000.000 é {cont}')