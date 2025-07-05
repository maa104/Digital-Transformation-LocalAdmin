import os
import re
import json
import unicodedata

# Ruta de la carpeta con los JSON
carpeta = '/home/maria/nuevos/'

def normalizar(texto):
    """Normaliza el texto quitando acentos y convirtiendo a minúsculas."""
    texto = unicodedata.normalize('NFD', texto)
    texto = texto.encode('ascii', 'ignore').decode('utf-8')
    return texto.lower()

def limpiar_texto(texto, palabra_a_eliminar):
    if isinstance(texto, str):
        texto_sin_html = re.sub(r'<[^>]+>', '', texto)  # Eliminar etiquetas HTML
        texto_sin_urls = re.sub(r'https?://[^\s"\']+', '', texto_sin_html)  # Eliminar URLs http/https
        texto_sin_urls = re.sub(r'file://[^\s"\']+', '', texto_sin_urls)    # Eliminar URLs file://

        # Normalizar texto y palabra para eliminar aunque haya mayúsculas o acentos
        texto_normalizado = normalizar(texto_sin_urls)
        palabra_normalizada = normalizar(palabra_a_eliminar)

        # Buscar la posición del nombre en el texto normalizado
        patron = re.escape(palabra_normalizada)
        texto_modificado = re.sub(patron, '', texto_normalizado, flags=re.IGNORECASE)

        return texto_modificado
    return texto

def limpiar_datos(data, palabra_a_eliminar):
    if isinstance(data, dict):
        return {clave: limpiar_datos(valor, palabra_a_eliminar) for clave, valor in data.items()}
    elif isinstance(data, list):
        return [limpiar_datos(item, palabra_a_eliminar) for item in data]
    else:
        return limpiar_texto(data, palabra_a_eliminar)

# Recorrer todos los archivos .json
for archivo in os.listdir(carpeta):
    if archivo.endswith('.json'):
        nombre_archivo = os.path.splitext(archivo)[0]  # sin .json
        ruta_completa = os.path.join(carpeta, archivo)

        with open(ruta_completa, 'r', encoding='utf-8') as f:
            try:
                data_original = json.load(f)
            except json.JSONDecodeError:
                print(f'Error al cargar {archivo}')
                continue

        contenido_limpio = limpiar_datos(data_original, nombre_archivo)

        # Guardar como nombre_limpio.json
        ruta_salida = os.path.join(carpeta, f'{nombre_archivo}_limpio.json')
        with open(ruta_salida, 'w', encoding='utf-8') as f_out:
            json.dump(contenido_limpio, f_out, ensure_ascii=False, indent=2)

        print(f'Procesado {archivo} → {nombre_archivo}_limpio.json')
