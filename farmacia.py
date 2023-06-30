import requests
import csv

# Obtener los datos de la API
api_url = "https://midas.minsal.cl/farmacia_v2/WS/getLocalesTurnos.php"
response = requests.get(api_url)

# Verificar si la respuesta es válida
if response.ok:
    try:
        data = response.json()

        # Nombre del archivo CSV
        csv_file = "datos_api.csv"

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
    except ValueError as e:
        print("Error al decodificar la respuesta JSON:", e)
else:
    print("Error al obtener los datos de la API. Código de estado:", response.status_code)

