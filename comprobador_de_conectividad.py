import tkinter as tk
from tkinter import messagebox
import urllib.request

def check_connectivity(url):
    """Verifica la conectividad de un sitio web mediante su URL."""
    try:
        # Realiza una solicitud HTTP
        response = urllib.request.urlopen(url)
        # Obtiene el código de estado HTTP
        status_code = response.getcode()
        
        # Verifica si el código de estado es 200
        if status_code == 200:
            return "El sitio web está disponible."
        else:
            return f"El sitio web respondió con el código de estado {status_code}."
    except urllib.error.URLError as e:
        # Captura errores de URL y muestra un mensaje adecuado
        return f"No se pudo acceder al sitio web. Error: {e.reason}"
    except Exception as e:
        # Captura otros errores y muestra un mensaje adecuado
        return f"Se produjo un error inesperado: {e}"

def on_check_button_click():
    """Maneja el clic en el botón 'Comprobar'."""
    url = url_entry.get()
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url
    result = check_connectivity(url)
    # Muestra el resultado en un cuadro de mensaje
    messagebox.showinfo("Resultado", result)

# Crear la ventana principal
root = tk.Tk()
root.title("Comprobador de Conectividad de Sitios Web")

# Crear y colocar el widget de entrada de URL
url_label = tk.Label(root, text="Ingrese la URL del sitio web:")
url_label.pack(pady=10)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=10)

# Crear y colocar el botón 'Comprobar'
check_button = tk.Button(root, text="Comprobar", command=on_check_button_click)
check_button.pack(pady=10)

# Ejecutar el bucle principal de la interfaz gráfica
root.mainloop()
