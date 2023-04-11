import matplotlib.pyplot as plst
import mpld3

marcas = ["Nike","adidas", "Puma","New Balance", "Gucci"]
vendas = [100,500,200,100,50]

plst.pie(vendas,labels=marcas)
mpld3.show()