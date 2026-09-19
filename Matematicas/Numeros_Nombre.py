from text_to_num import text2num

texto = "tres mil doscientos cuarenta y cinco"

# Convertimos el texto a su número correspondiente en español ('es')
numero = text2num(texto, lang="es")

print(f"Resultado numérico: {numero}")
# Salida: Resultado numérico: 3245

