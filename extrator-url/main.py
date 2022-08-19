from extrator_url import ExtratorUrl
from extrator_cep import ExtratorCep

url = "http://www.bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"

extrator = ExtratorUrl(url)
print(extrator.get_url_base())
print(len(extrator))
print(extrator)

endereco = "rua primeira, numero: 111 - Cidade: Altônia / PR - CEP: 00000-000"

extrator = ExtratorCep(endereco)
print(extrator.extrair_cep())