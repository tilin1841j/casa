import folium
import webbrowser

# Reemplaza estas variables con las coordenadas reales de tu ubicación
longitud = -74.157148
latitud = 4.584508

# Crear un mapa centrado en la longitud y latitud determinada
mapa = folium.Map(location=[latitud, longitud], zoom_start=12)

# Añadir una marca en la longitud y latitud determinada
folium.Marker([latitud, longitud], popup="Mi ubicación").add_to(mapa)

# Guardar el mapa en un archivo HTML
mapa.save("mapa.html")

# Abrir el archivo HTML en el navegador predeterminado
url = "mapa.html"
webbrowser.open(url)