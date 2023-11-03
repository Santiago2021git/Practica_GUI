import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGroupBox, QComboBox, QLabel, QLineEdit, QPushButton, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Cargar la interfaz de Qt Designer desde el archivo .ui
        self.load_ui()

        # Conectar los botones a las funciones correspondientes
        self.pushButton.clicked.connect(self.agregar_propietario)
        self.pushButton_2.clicked.connect(self.agregar_finca)

    def load_ui(self):
        # Cargar la interfaz de Qt Designer desde el archivo .ui
        from PyQt5.uic import loadUi
        loadUi('Ventana.ui', self)

    def agregar_propietario(self):
        nombre = self.lineEdit.text()
        apellido = self.lineEdit_2.text()
        telefono = self.lineEdit_3.text()
        correo = self.lineEdit_4.text()

        if not nombre or not apellido or not telefono or not correo:
            self.show_message("Campo vacío", "error")
        else:
            self.show_message("Propietario agregado", "exito")
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()

    def agregar_finca(self):
        cultivo = self.comboBox.currentText()
        registro_castral = self.lineEdit_6.text()
        municipio = self.lineEdit_7.text()

        if not cultivo or not registro_castral or not municipio:
            self.show_message("Campo vacío", "error")
        else:
            self.show_message("Finca agregada", "exito")
            self.comboBox.clear()
            self.lineEdit_6.clear()
            self.lineEdit_7.clear()

    def show_message(self, message, tipo):
        msg = QMessageBox()
        msg.setWindowTitle("Mensaje")

        if tipo == "error":
            msg.setIcon(QMessageBox.Critical)  # Icono de error crítico
        elif tipo == "exito":
            msg.setIcon(QMessageBox.Information)  # Icono de información

        msg.setText(message)
        msg.exec_()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
