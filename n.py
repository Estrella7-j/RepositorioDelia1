print ("hecho por Estrella Cano Luna")
print ("calcular fibonacci")
n = int(input("Ingresa un número para calcular F(n): "))


a, b = 0, 1


contador = 1


while contador < n:
    a, b = b, a + b  
    contador += 1    

# Mostrar el resultado
print(f"el resultado es:5 = {a}")
