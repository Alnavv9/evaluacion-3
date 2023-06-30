import requests
import csv

# Obtener los datos de la API
api_url = "https://midas.minsal.cl/farmacia_v2/WS/getLocalesTurnos.php"
response = requests.get(api_url)
data = response.json()

# Nombre del archivo CSV
csv_file = "locales_turnos.csv"

# Guardar los datos en un archivo CSV
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Fecha", "ID", "Nombre local", "Comuna", "Dirección", "Apertura", "Cierre", "Teléfono", "Día funcionamiento"])  # Especifica las columnas deseadas

    for item in data:
        writer.writerow([
            item["fecha"],
            item["local_id"],
            item["local_nombre"],
            item["comuna_nombre"],
            item["local_direccion"],
            item["funcionamiento_hora_apertura"],
            item["funcionamiento_hora_cierre"],
            item["local_telefono"],
            item["funcionamiento_dia"]
        ])

print("Datos guardados exitosamente en el archivo CSV:", csv_file)
