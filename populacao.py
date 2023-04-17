import matplotlib.pyplot as plst
import mpld3


cidades = ["São Paulo","Guarulhos","Campinas","São Bernardo do Campo","São José dos Campos","Santo André","Riberão Preto","Osasco","Sorocaba","Mauá","São José dos Rio Preto","Mongi das Cruzes","Santos"]
habitantes = [12396372, 1404694,1223237,849874,737310,723889,720116,701428,695328,481725,469173,455587,433991]
plst.pie(habitantes,labels=cidades)
plst.savefig("/usr/share/nginx/html/grafico.png")
plst.show()

html ="""
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gráfico de Python</title>
    <link rel="shortcut icon" href="https://cdn-icons-png.flaticon.com/512/2257/2257295.png">
    <style>
        body{
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
        }
        .navegador{
            background-color: red;
            width: 100%;
            height: 100%;
            padding: 1px;
        }
        h1{
            text-align: center;
            color: white;
            font-size: 25px;
            font-family: Arial;
        }
        .img{
            text-align:center;
        }
    </style>
</head>
<body>
    <header class="navegador">
        <h1>Gráfico em Python</h1>
    </header>
     <img class="img" src=grafico.png>
</body>
</html>
   
"""
f = open('/usr/share/nginx/html/grafico.html', 'w')
f.write(html)
f.close()