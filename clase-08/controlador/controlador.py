class Controlador:
    
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        self.vista.btn_sumar.clicked.connect(self.incrementar_sumatoria)
    
    def incrementar_sumatoria():
        sumatoria = self.modelo.sumar_uno()
        self.vista.actualizar_sumatoria(sumatoria)
            