import requests
from bs4 import BeautifulSoup

url = "https://jv.acb.com/es/103652/estadisticas/ficha"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Ejemplo básico para verificar el contenido HTML
    print(soup.prettify())  # Imprime el HTML formateado para inspección
    
    # Ajusta el código a la estructura real de la página
    jugadores_section = soup.find_all('div', class_='player')  # Ajusta esto

    for jugador in jugadores_section:
        nombre = jugador.find('span', class_='player-name')  # Ajusta esto
        puntos = jugador.find('span', class_='player-points')  # Ajusta esto

        if nombre and puntos:
            print(f'Nombre: {nombre.text.strip()}, Puntos: {puntos.text.strip()}')
        else:
            print("Datos no encontrados para un jugador.")
else:
    print(f'Error al obtener la página: {response.status_code}')
