import pandas as pd # type: ignore
import json
import os

# Ruta de los archivos
EXCEL_FILE = 'datosIA.xlsx'
JSON_FOLDER = 'fragmentos2'
OUTPUT_FILE = 'resultado4.json'

# Cargar el Excel
df = pd.read_excel(EXCEL_FILE)

# Crear la columna 'Web' si no existe
if 'Web' not in df.columns:
    df['Web'] = pd.Series([""] * len(df), dtype='object')



# Función para cargar el JSON de cada ayuntamiento
def cargar_json_ayuntamiento(nombre_ayuntamiento):
    nombre_archivo = f"{nombre_ayuntamiento.lower()}.json"
    ruta_archivo = os.path.join(JSON_FOLDER, nombre_archivo)
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        print(f"No se encontró JSON para: {nombre_ayuntamiento}")
        return None

# Rellenar la columna 'Web' con el JSON de cada ayuntamiento
for idx, row in df.iterrows():
    nombre_ayuntamiento = row[df.columns[0]]  # 'Ayuntamiento' es la primera columna
    datos_web = cargar_json_ayuntamiento(nombre_ayuntamiento)
    df.at[idx, 'Web'] = json.dumps(datos_web, ensure_ascii=False) if datos_web else None

# Crear el diccionario final
resultado = {}

for idx, row in df.iterrows():
    ayuntamiento = row[df.columns[0]]
    datos = row.to_dict()
    datos.pop(df.columns[0])
    resultado[ayuntamiento] = datos

# Guardar el resultado en JSON
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(resultado, f, ensure_ascii=False, indent=4)

print(f"Transformación completada. Archivo guardado como '{OUTPUT_FILE}'.")
