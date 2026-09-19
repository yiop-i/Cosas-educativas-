from num2words import num2words

# 1. Solicitar el número al usuario y convertirlo a entero
entrada = input("Introduce un número: ")
numero = int(entrada)

# 2. Convertir el número a texto en español
numero_en_palabras = num2words(numero, lang='es')

# 3. Mostrar el resultado
print(f"El número escrito es: {numero_en_palabras}")