from operator import itemgetter

nome = []
nota = []
i = 1
while i <=5:
    nome.append(str(input("Digite o seu nome")))
    nota.append(int(input("Digite a sua nota")))
    i+=1

d = dict(zip(nome, nota))

ranking = sorted(d.items(),key=itemgetter(1),reverse=True)

print(f'A maior nota foi {ranking[0][1]} e foi do/a {ranking[0][0]}')

