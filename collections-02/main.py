from collections import Counter

idades = [18, 25, 35, 40, 50]
idades_dois = [18, 23, 39, 40, 55]

dados = Counter(idades)
print(dados)

idades_manipulacao = idades.copy()
idades_manipulacao.extend(idades_dois)
removendo_repetidos = set(idades_manipulacao)
print(len(removendo_repetidos))
print(removendo_repetidos)

idades = {18, 25, 35, 40, 50}
idades_dois = {18, 23, 39, 40, 55}

print(idades - idades_dois)
print(idades in idades_dois)
print(idades | idades_dois)
print(idades & idades_dois)

frozen_set = frozenset(idades)
print(type(frozen_set))

dados = {
    "nome": "Lucas",
    "idade": 23
}

print(dados)
print(dados["nome"])


for chave in dados.keys():
    print(chave)

for usuario in dados.items():
    print(usuario)

print(dados.get("nome"))

texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed at augue pharetra, malesuada magna sed, eleifend dui. Nulla a diam gravida, tincidunt tellus maximus, elementum lorem. Praesent feugiat sit amet mi at volutpat. Nulla facilisi. Pellentesque pretium mi lorem, non pulvinar mi varius vitae. Etiam vestibulum malesuada mauris, et porttitor felis efficitur quis. Maecenas lectus leo, tempor ullamcorper ante non, aliquam facilisis libero. Suspendisse ullamcorper et mauris at imperdiet."
counter = Counter(texto.replace(" ", ""))
prop = [(letra , frequencia / len(texto)) for letra, frequencia in counter.items()]
prop = Counter(dict(prop))
for caractere, proporcao in prop.most_common(10):
    print("{} => {:.2f}%".format(caractere, proporcao * 100))

