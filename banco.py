import pymysql as mysql
# Estabalecendo a conexão com banco de dados que está no container docker
import matplotlib.pyplot as plt
con = mysql.connect(
    host="127.0.0.1",
    user="root",
    password="senac@123",
    database="projetodb",
    port=6556,
    )

dep = []
vlr = []

cur = con.cursor()
cur.execute("Select * from produto")
resultado = cur.fetchall()
for i in resultado:
    dep.append(i[1])
    vlr.append(i[4])

cur.close

plt.figure().set_figheight(35)
plt.figure().set_figheight(5)
plt.barh(dep,vlr)
plt.xlabel("Departamentos")
plt.ylabel("Valores")
plt.savefig("/usr/share/nginx/html/dep_vlr.png")


grafico = open("/usr/share/nginx/html/dep_vlr.html","w")
pagina = """
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
            back
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
            padding: 10px;
            margin: 10px;
        }
    </style>
</head>
<body>
    <header class="navegador">
        <h1>Gráfico em Python</h1>
    </header>
     <img class="img" src="dep_vlr.png">
</body>
</html>
"""

grafico.write(pagina)
grafico.close()