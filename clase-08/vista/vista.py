import os
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QMainWindow

class Vista(QMainWindow):
    
    def __init__(self):
        super().__init__()  # Activamos los superpoderes de la ventana de PyQt/PySide

        # Obtenemos la ruta exacta de la carpeta donde vive este archivo (vista.py)
        ruta_directorio = os.path.dirname(os.path.abspath(__file__))
        
        # Construimos la ruta completa hacia ventana.ui dentro de la misma carpeta
        ruta_ventana = os.path.join(ruta_directorio, "ventana.ui")
        
        # 1. Abrimos nuestro archivo .ui (asegúrate de poner el nombre exacto de tu archivo)
        archivo_ui = QFile(ruta_ventana)
        archivo_ui.open(QFile.ReadOnly)

        # 2. Cargamos la interfaz usando el loader y se la aplicamos a esta ventana (self)
        loader = QUiLoader()
        loader.load(archivo_ui, self)

        # 3. Cerramos el archivo para liberar memoria
        archivo_ui.close()
        
    def actualizar_sumatoria(self, valor):
      # Tomamos la etiqueta de texto y le asignamos el nuevo valor convertido a texto
      self.lbl_sumatoria.setText(str(valor))