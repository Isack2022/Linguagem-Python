import matplotlib.pyplot as plt
sabores = ["Muçarela","Calabresa","Portuguesa","Calamusa","Frango Catupiry","Maguerita"]
consumo = [30,35,19,25,10,2]

# plt.bar(sabores,consumo)
plt.pie(consumo,labels=sabores)
plt.show()