from cpf import Cpf
from cnpj import Cnpj
import pandas as pd
import docbr as dbr
import seaborn as sns
import matplotlib.pyplot as plt
import re
from telefonebr import Telefonebr
from datetime import datetime
from cep import Cep

cpf = "722.574.800-90"
valida_cpf = Cpf(cpf)
valida_cpf.validate()

cnpj = "55.986.474/0001-46"
valida_cnpj = Cnpj(cnpj)
valida_cnpj.validate()

list_cnpj = {'cnpj': ['12345678000158', '12345678000298', '55.986.474/0001-46',  '55.986.474/0001-46']} # dicionario
print(type(list_cnpj))
df = pd.DataFrame(list_cnpj)
df["cnpj_valid"] = dbr.validate(df["cnpj"], doctype="cnpj")
print(df.head())


''' 
plot seaborn
sns.set_theme(style="darkgrid")
plot = sns.countplot(data=df, x="cnpj_valid")
plt.show()
'''

texto = re.compile("[0-9]{1}[a-z]{1}[0-9]{1}")
email = re.compile("\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}")

if email.search("testex@teste.com.br"):
    print("valid")
else:
    print("not valid")

telefone = "+124100000-0005"

valida_telefone = Telefonebr(telefone)
valida_telefone.validate()

print(datetime.today())
print(datetime.today().month)
print(datetime.today().strftime("%d/%m/%Y"))

# CEP
cep = Cep("07550001")
print(cep.consultar())