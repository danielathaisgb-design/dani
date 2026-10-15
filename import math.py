import math

# 1. Define el número al que deseas calcularle la raíz cuadrada aproximada
numero = float(
    input("Ingresa el número para calcular su raíz cuadrada: ")
)  # O puedes asignarlo directamente, por ejemplo: numero = 25.0

# 2. Define una tolerancia (precisión) y un valor inicial para la aproximación
tolerancia = 1e-7
aproximacion = numero / 2.0  # Un valor inicial razonable

if numero < 0:
    print("No se puede calcular la raíz cuadrada real de un número negativo.")
elif numero == 0:
    aproximacion = 0.0
    print("La raíz cuadrada es 0.0")
else:
    contador = 1
    print(f"--- Iniciando aproximaciones para {numero} ---")

    # Bucle while para refinar la aproximación
    while True:
        # Fórmula de aproximación (Método babilónico / Herón)
        siguiente_aproximacion = 0.5 * (aproximacion + (numero / aproximacion))

        # Muestra la aproximación obtenida en cada iteración
        print(f"Iteración {contador}: {siguiente_aproximacion}")

        # Comprueba si la diferencia es menor que la tolerancia para detener el bucle
        if abs(siguiente_aproximacion - aproximacion) < tolerancia:
            break

        aproximacion = siguiente_aproximacion
        contador += 1

    print("\n--- Resultado Final ---")
    print(f"Resultado aproximado con while: {siguiente_aproximacion}")

    # 3. Compara tu resultado con math.sqrt()
    resultado_real = math.sqrt(numero)
    print(f"Resultado usando math.sqrt(): {resultado_real}")