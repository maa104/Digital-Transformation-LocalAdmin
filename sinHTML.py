import json
import re
import os
from bs4 import BeautifulSoup


def limpiar_texto(texto):
    soup = BeautifulSoup(texto, 'html.parser')
    texto_plano = soup.get_text(separator=' ', strip=True)
    texto_plano = re.sub(r'\[\d+\]', '', texto_plano)
    texto_plano = re.sub(r'(javascript:void\(0\);?)|(mailto:[^\s]+)', '', texto_plano, flags=re.IGNORECASE)
    texto_plano = re.sub(r'\S+@\S+', '', texto_plano)
    texto_plano = re.sub(r'index\.html\S*', '', texto_plano)
    texto_plano = re.sub(r'\S*index\.txt', '', texto_plano)
    texto_plano = re.sub(r'\s+', ' ', texto_plano).strip()
    return texto_plano


def limpiar_archivo_json(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    lista_valores = [limpiar_texto(valor) for valor in data.values()]

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(lista_valores, f, ensure_ascii=False, indent=4)


def limpiar_carpeta_json(carpeta):
    salida = '/home/maria/sinHTMLniclaves'
    for archivo in os.listdir(carpeta):
        if archivo.endswith('.json'):
            ruta_entrada = os.path.join(carpeta, archivo)
            nombre_salida = f"limpio_{archivo}"
            ruta_salida = os.path.join(salida, nombre_salida)
            limpiar_archivo_json(ruta_entrada, ruta_salida)
            print(f"Archivo limpio generado: {ruta_salida}")


if __name__ == "__main__":
    carpeta = '/home/maria/definitivos/'  # Cambia este nombre a la carpeta que contiene los archivos
    limpiar_carpeta_json(carpeta)
    print("Proceso completado para todos los archivos JSON en la carpeta.")
