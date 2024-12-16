print("CUIDADES DEL ECUADOR")
tupla = ("A","B","C","CH","D","E","F","G","H","I","J","K","L","LL","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z")
print(tupla)
print("Selecciona una letra")
letra_acierto = ("A")
letra = str(input("""
Adivina la letra y acierta !!!
Ingresa una letra entre A y Z: """))
for i in ("A","L","A","U","S","I"):
            while letra != letra_acierto:
                letra = str(input("Ingresa otra letra:"))