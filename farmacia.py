import requests
import csv
from google.cloud import storage

# Obtener los datos de la API
api_url = "https://midas.minsal.cl/farmacia_v2/WS/getLocalesTurnos.php"
response = requests.get(api_url)
data = response.json()

# Nombre del archivo CSV
csv_file = "locales_turnos.csv"

# Guardar los datos en un archivo CSV
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Fecha","ID", "Nombre local", "Comuna", "Direccion", "apertura","cierre",
    "telefono","dia funcionamiento"])  # Especifica las columnas deseadas
    
    for item in data:
        writer.writerow([item["fecha"],item["local_id"], item["local_nombre"], item["comuna_nombre"], item["local_direccion"], 
        item["funcionamiento_hora_apertura"],item["funcionamiento_hora_cierre"],item["local_telefono"],
        item["funcionamiento_dia"]])

# Cargar el archivo CSV en Google Cloud Storage
bucket_name = "dataflow-apache-quickstart_evaluacion-3-390120"  # Reemplaza con el nombre de tu bucket en GCP
destination_blob_name = "locales_turnos.csv"  # Nombre y ruta del archivo en GCP

storage_client = storage.Client()
bucket = storage_client.get_bucket(bucket_name)
blob = bucket.blob(destination_blob_name)
blob.upload_from_filename(csv_file)

print("Archivo cargado exitosamente en Google Cloud Storage:", blob.name)
