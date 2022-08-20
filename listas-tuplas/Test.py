from conta_corrente import ContaCorrente
from conta_salario import ContaSalario
from operator import attrgetter

lucas = ContaCorrente(1)
lucas.deposita(1500)

joao = ContaCorrente(2)
joao.deposita(800)

contas = [lucas, joao]
# print(contas)

for conta in contas: print(conta)

# Tupla
# lucas = ["Lucas", 30, 1990]

conta_salario_um = ContaSalario(55)
conta_salario_dois = ContaSalario(55)

print(conta_salario_um)
print(conta_salario_dois)
print(conta_salario_um.__eq__(conta_salario_dois))

# Builtins
numeros = [1, 5, 20, 40, 100, 85, 56, 33]

print(list(range(len(numeros))))

for indice, numero in enumerate(numeros):
    print(indice, " => ", numero)

# Ordenação
print(sorted(numeros))
print(list(reversed(numeros)))
print(sorted(numeros, reverse=True))

for conta in sorted(contas):
    print(conta)

# functools total_ordering
print(lucas < joao)