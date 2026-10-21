import sys
from PySide6.QtWidgets import QApplication
from controlador.controlador import Controlador
from modelo.modelo import Modelo
from vista.vista import Vista

if __name__ == "__main__":
  # 1. Inicializamos la aplicación de Qt
  app = QApplication(sys.argv)

  # 2. Creamos los objetos de nuestro patrón MVC
  modelo = Modelo()
  ventana = Vista()
  controlador = Controlador(modelo, ventana)

  # 3. Hacemos visible la ventana
  ventana.show()

  # 4. Arrancamos el ciclo de ejecución del programa
  sys.exit(app.exec())