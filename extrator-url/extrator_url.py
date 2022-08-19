import re


class ExtratorUrl:

    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.__valida_url()

    def sanitiza_url(self, url):
        return url.strip() if type(url) == str else ""

    def __valida_url(self):
        verifica_dominio = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        if not self.url or not verifica_dominio.match(self.url):
            raise ValueError("URL é inválida!")


    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        return self.url[:indice_interrogacao]

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        return self.url[indice_interrogacao + 1:]

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)

        if indice_e_comercial == -1:
            return self.get_url_parametros()[indice_valor:]

        return self.get_url_parametros()[indice_valor:indice_e_comercial]

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.__class__.__name__