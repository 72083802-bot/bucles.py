while True:
   print("Estoy atrapado en un bucle.")
tamanio_numero = -999999999

numero = int(input("Ingresa un número o escribe -1 para detener: "))
while numero != -1:
   if numero > tamanio_numero:
       tamanio_numero = numero
   numero = int(input("Ingresa un número o escribe -1 para detener: "))

   print("El número más grande ingresado es:", tamanio_numero)

odd_numbers = 0
even_numbers = 0
 
# Lee el primer número.
number = int(input("Introduce un número o escribe 0 para detener: "))
 
# 0 termina la ejecución.
while number != 0:
    # Verificar si el número es impar.
    if number % 2 == 1:
        # Incrementar el contador de números impares odd_numbers.
        odd_numbers += 1
    else:
        # Incrementar el contador de números pares even_numbers.
        even_numbers += 1
    # Leer el siguiente número.
    number = int(input("Introduce un número o escribe 0 para detener: "))
 
# Imprimir resultados.
print("Conteo de números impares:", odd_numbers)
print("Conteo de números pares:", even_numbers)

contador = 5
while contador != 0:
    print("dentro del bucle", contador)
    contador -= 1
    print (" fuera del bucle", contador) 

secret_number = 15


print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número           |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")

numero = int(input("Ingresa el número: "))

while numero != secret_number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    numero = int(input("Ingrese un número nuevamente: "))

print("El número es:", secret_number, "¡Bien hecho, muggle! Eres libre ahora.")
