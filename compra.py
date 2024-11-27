print("Hecho por: Sarahi Prado Lara y Estrella Cano Luna")
print("Dada la aplicación básica de un menú (“Maquillaje”) con la estructura while")

maquillaje = {
    "11": {"Producto": "corrector liquido", "Marca": "Maybelline", "Tono": "110,112,115,120", "Gramos": "6.0 g", "Tamaño": "chico", "Consistencia": "Líquida", "Lote": "20X904", "Duracion": "14 horas", "Material": "Hidratante", "Precio": "$270"},
    "22": {"Producto": "rubor en polvo", "Marca": "L'Oréal", "Tono": "Petalo", "Gramos": "4 g", "Tamaño": "chico", "Consistencia": "Crema", "Lote": "b017957", "Duracion": "1 horas", "Material": "Polvo", "Precio": "$78"},
    "33": {"Producto": "labial", "Marca": "Maybellin", "Tono": "125", "Gramos": "50 g", "Tamaño": "mediano", "Consistencia": "Compacta", "Lote": "G949376", "Duracion": "24 horas", "Material": "liquida", "Precio": "$280"},
    "44": {"Producto": "polco compacto", "Marca": "L'Oréal", "Tono": "125 ivory buff", "Gramos": "9 g", "Tamaño": "mediano", "Consistencia": "Polvo", "Lote": "86R141", "Duracion": "24 horas", "Material": "polvo", "Precio": "$180"},
    "55": {"Producto": "Primer", "Marca": "Maybellin", "Tono": "transparente mate", "Gramos": "30 ml", "Tamaño": "chico", "Consistencia": "Polvo", "Lote": "B739904", "Duracion": "12 horas", "Material": "liquida", "Precio": "$147"},
    "66": {"Producto": "Gloss", "Marca": "Maybellin", "Tono": "gummy bear", "Gramos": "5.4 ml", "Tamaño": "chico", "Consistencia": "Líquida", "Lote": "C4T97", "Duracion": "12 horas", "Material": "liquido espeso", "Precio": "$229"},
    "77": {"Producto": "Mascara de pestañas", "Marca": "Maybelline", "Tono": "negro", "Gramos": "6 g", "Tamaño": "mediano", "Consistencia": "Líquida", "Lote": "S197R2", "Duracion": "24 horas", "Material": "polvo", "Precio": "$131"},
    "88": {"Producto": "Crema de cejas", "Marca": "BISSU", "Tono": "Chocolate", "Gramos": "5 g", "Tamaño": "chico", "Consistencia": "Crema", "Lote": "764R7", "Duracion": "7 horas", "Material": "polvo", "Precio": "$70"},
    "99": {"Producto": "Iluminador", "Marca": "BISSU", "Tono": "Capricornio", "Gramos": "6 g", "Tamaño": "chico", "Consistencia": "Polvo", "Lote": "47T5G8", "Duracion": "14 horas", "Material": "liquido", "Precio": "$180"},
    "1010": {"Producto": "Delienador", "Marca": "Maybellin", "Tono": "Negro", "Gramos": "7 g", "Tamaño": "chico", "Consistencia": "Polvo", "Lote": "J012", "Duracion": "6 horas", "Material": "liquido", "Precio": "$324"}
}

# Contraseña inicial
CONTRASEÑA = "estrellita"

# Validar contraseña con while
while True:
    intento = input("Introduce la contraseña: ")
    if intento == CONTRASEÑA:
        print("Contraseña correcta. Accediendo al sistema...")
        break 
    else:
        print("Contraseña incorrecta. Inténtalo nuevamente.")

# Funciones del menú
def mostrar_maquillaje():
    if maquillaje:
        print("\nLista de Productos de Maquillaje:")
        # Encabezado de la tabla
        encabezado = f"{'Producto':<20}{'Marca':<20}{'Tono':<20}{'Gramos':<10}{'Tamaño':<10}{'Consistencia':<15}{'Lote':<10}{'Duracion':<10}{'Material':<15}{'Precio':<10}"
        print(encabezado)
        print("-" * len(encabezado))  # Línea divisoria

        contador = 1  # Contador para numerar los productos
        for codigo, detalles in maquillaje.items():
            fila =  f"{detalles['Producto']:<20} " \
                    f"{detalles['Marca']:<20} " \
                    f"{detalles['Tono']:<20} " \
                    f"{detalles['Gramos']:<10} " \
                    f"{detalles['Tamaño']:<10} " \
                    f"{detalles['Consistencia']:<15} " \
                    f"{detalles['Lote']:<10} " \
                    f"{detalles['Duracion']:<10} " \
                    f"{detalles['Material']:<15} " \
                    f"{detalles['Precio']:<10}"
            print(fila)
            contador += 1
    else:
        print("No hay más productos de maquillaje en la base de datos.")

def agregar_maquillaje():
    codigo = input("Código (6 dígitos): ")
    if codigo in maquillaje:
        print("Este código ya existe.")
    else:
        producto = input("Producto: ")
        marca = input("Marca: ")
        tono = input("Tono: ")
        gramos = input("Gramos: ")
        tamaño = input("Tamaño: ")
        consistencia = input("Consistencia: ")
        lote = input("Lote: ")
        duracion = input("Duración: ")
        material = input("Material: ")
        precio = input("Precio: ")
        maquillaje[codigo] = {
            "Producto": producto,
            "Marca": marca,
            "Tono": tono,
            "Gramos": gramos,
            "Tamaño": tamaño,
            "Consistencia": consistencia,
            "Lote": lote,
            "Duracion": duracion,
            "Material": material,
            "Precio": precio
        }
        print(f"Producto {producto} agregado con éxito.")

def modificar_maquillaje():
    codigo = input("Código del producto a modificar: ")
    if codigo in maquillaje:
        producto = input("Nuevo Producto: ")
        marca = input("Nueva Marca: ")
        tono = input("Nuevo Tono: ")
        gramos = input("Nuevos Gramos: ")
        tamaño = input("Nuevo Tamaño: ")
        consistencia = input("Nueva Consistencia: ")
        lote = input("Nuevo Lote: ")
        duracion = input("Nueva Duración: ")
        material = input("Nuevo Material: ")
        precio = input("Nuevo Precio: ")
        maquillaje[codigo] = {
            "Producto": producto,
            "Marca": marca,
            "Tono": tono,
            "Gramos": gramos,
            "Tamaño": tamaño,
            "Consistencia": consistencia,
            "Lote": lote,
            "Duracion": duracion,
            "Material": material,
            "Precio": precio
        }
        print(f"Producto {producto} modificado con éxito.")
    else:
        print("Código no encontrado.")

def eliminar_maquillaje():
    codigo = input("Código del producto a eliminar: ")
    if codigo in maquillaje:
        eliminado = maquillaje.pop(codigo)
        print(f"Producto {eliminado['Producto']} eliminado con éxito.")
    else:
        print("Código no encontrado.")

# Menú principal
while True:
    print("\nMenú de Productos de Maquillaje")
    print("1. Agregar = Insertar producto")
    print("2. Mostrar productos")
    print("3. Modificar o Editar")
    print("4. Borrar")
    print("5. Salir del programa")

    opcion = input("Elige una opción (1/2/3/4/5): ")
    if opcion == "1":
        agregar_maquillaje()
    elif opcion == "2":
        mostrar_maquillaje()
    elif opcion == "3":
        modificar_maquillaje()
    elif opcion == "4":
        eliminar_maquillaje()
    elif opcion == "5":
        print("Saliendo del programa.")
        break
    else:
        print("Opción inválida.")
