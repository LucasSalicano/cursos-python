idades = [15, 25, 40, 42, 50]

# Adicionando elemento no começo
idades.insert(0, 22)
print(idades)

# Removendo elemento
if 25 in idades:
    idades.remove(25)
print(idades)

# Adicionando vários elementos
idades.append([30, 25])
for idade in idades:
    if type(idade) == list:
        print("tem uma lista dentro de outra")
        idades.remove(idade)

idades.extend([30, 25])
print(idades)

# Filtrando as idades
idades_maior_vinte = [idade for idade in idades if idade > 20]
print(idades_maior_vinte)