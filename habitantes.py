import matplotlib.pyplot as plt
import mpld3 

cidades = ["São Paulo","Guarulhos","Campinas","São Bernardo do Campo","São José dos Campos","Santo André","Riberão Preto","Osasco","Sorocaba","Mauá","São José dos Rio Preto","Mongi das Cruzes","Santos"]
habitantes = [12396372, 1404694,1223237,849874,737310,723889,720116,701428,695328,481725,469173,455587,433991]
plt.barh(cidades,habitantes)
mpld3.show  