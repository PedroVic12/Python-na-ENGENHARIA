# Portanto, n_termos = 50
a1 = 1
razao = 1
n_derrubadas = 50

#Lista de Arvores derrubadas
derrubadas = []
x = 1

while x < (n_derrubadas+1): # precisa disso pq no python o indice começa no 0
    an = a1 + (x-1)*razao
    derrubadas.append(an)
    x = x + 1
print(f"A sequencia de arvores derrubadas é \n{derrubadas}")


y = 0
plantadas = []

while y < (n_derrubadas):
    p = 2*(derrubadas[y]) - 1
    plantadas.append(p)
    y = y + 1
print(f"A sequencia de arvores PLantadas é {plantadas} ")

#Quantidade total (soma dos termos)

soma_termos_plantadas = 0
z = 0
while z < n_derrubadas:
    soma_termos_plantadas = soma_termos_plantadas + plantadas[z]
    z = z+1
print(f'\n Quantidade total de arvores = {soma_termos_plantadas}')



#Entrada de dados
PA = []
a1 = 1
razao = 2
n_termos_plantadas = (2*n_derrubadas) - 1


# Motando a estrutura pra formar a lista
n = 1
while n < (n_termos_plantadas+1):
    proximo_termo = a1 + (n-1)*razao
    PA.append(proximo_termo)
    n = n + 1

#Soma dos termos:
soma_termos2 = 0
i = 0
    
while i < n_termos_plantadas:
    soma_termos2 = soma_termos2 + PA[i]
    i = i + 1
      

print(f'A sequencia: \n{PA} ')
print(f'\n A soma dos termos da PA é: {soma_termos2} ')        