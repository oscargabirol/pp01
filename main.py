from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget
import sys


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        # Llamo al constructor de la clase padre.
        super().__init__()

        # Pongo título a la ventana y le doy tamaño.
        self.setWindowTitle("IBN Gabirol")
        self.setFixedSize(QSize(400, 300))

        # Instancio un objeto, "texto_salida", que muestra texto.
        self.texto_salida = QLabel()

        # Instancio un objeto, "texto_entrada", que almacena texto tecleado.
        self.texto_entrada = QLineEdit()
        self.texto_entrada.textChanged.connect(self.texto_salida.setText)

        # Instancio un objeto, "layout", que alberga a los dos objetos anteriores.
        layout = QVBoxLayout()
        layout.addWidget(self.texto_entrada)
        layout.addWidget(self.texto_salida)
        
        # Instancio un objeto, "contenedor", que contiene al objeto "layout".
        contenedor = QWidget()
        contenedor.setLayout(layout)

        # Pongo el contenedor como widget central de nuestra ventana.
        self.setCentralWidget(contenedor)

# Creo un objeto aplicación.
aplicacion = QApplication(sys.argv)

# Creo un objeto ventana y lo muestro.
ventana = VentanaPrincipal()
ventana.show()

# Ejecuto la aplicación, esperando eventos.
aplicacion.exec()
