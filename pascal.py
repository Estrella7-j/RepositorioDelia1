print ("hecho por:Estrella Cano Luna y Sarahi Prada Lara")
filas = int(input("Ingrese el número de filas del Triángulo de Pascal: "))

triangulo = []

for n in range(filas):
    
    fila = [1] * (n + 1)
    
    for k in range(1, n):
        fila[k] = triangulo[n - 1][k - 1] + triangulo[n - 1][k]
    
    triangulo.append(fila)

for fila in triangulo:
    print(" ".join(map(str, fila)).center(len(triangulo[-1]) * 3))
