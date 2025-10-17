nombres = ["Ana", "Luis", "Maria","Miguel","Juan","Eduardo","Sayma","Saul","Luka Modrich"]
with open("nombres.txt", "w") as archivo:
    for n in nombres:
        archivo.write(n + "\n")
