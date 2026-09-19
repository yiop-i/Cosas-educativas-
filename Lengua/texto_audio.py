import os
from gtts import gTTS

# 1. Solicitar la oración al usuario
oracion = input("Introduce una oración: ")

# 2. Generar el audio (configurado en español 'es')
tts = gTTS(text=oracion, lang="es", slow=False)

# 3. Guardar el archivo temporalmente
archivo_audio = "oracion.mp3"
tts.save(archivo_audio)

# 4. Reproducir el archivo generado (funciona en Windows)
os.system(f"start {archivo_audio}")