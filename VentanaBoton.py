import sys
from PySide import QtGui


app= QtGui.QApplication(sys.argv)

class Ventana (QtGui.QDialog):
	def __init__(self):
		super (Ventana, self).__init__()

		self.setGeometry(20, 20, 300, 300)

		btn= QtGui.QPushButton(self)
		btn.setText("ya esta listo!!!")
		btn.clicked.connect(self.Mensajear)

	def show(self):
		super (Ventana, self).show()
		print("Sipi")

	def Mensajear(self):
		print("Me Presionaste")
		QtGui.QMessageBox.information(self, "Titulo", "informacion!!!")


Ventanita = Ventana()
Ventanita.show()


sys.exit(app.exec_())