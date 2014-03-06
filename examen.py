import sys
from PySide import QtGui

app=QtGui.QApplication(sys.argv)

class Botones(QtGui.QDialog):
	
	def __init__(self):
		super(Botones, self).__init__()


		btn=QtGui.QPushButton(self)
		btn.setText("Informacion")
		btn.clicked.connect(Botones.Mensaje)
		btn.setGeometry(20,20,40,50)

		btn2=QtGui.QPushButton(self)
		btn2.setText("Informacion")
		btn2.clicked.connect(Botones.Mensaje2)
		btn.setGeometry(20,80,40,50)

		btn3=QtGui.QPushButton(self)
		btn3.setText("Informacion")
		btn3.clicked.connect(Botones.Mensaje3)
		btn.setGeometry(20,100,40,50)

		btn4=QtGui.QPushButton(self)
		btn4.setText("Informacion")
		btn4.clicked.connect(Botones.Mensaje4)
		btn.setGeometry(20,120,40,50)

	def Mensaje (self):
		print("Hola Mundo")
		QtGui.QMessageBox.information("Informacion", "Estoy Mejorando")


	def Mensaje2 (self):
		print("Hola Mundo")
		QtGui.QMessageBox.critical("Critica", "Porque no me ayudo")


	def Mensaje3 (self):
		print("Hola Mundo")
		QtGui.QMessageBox.question("Informacion", "El dia va ha ser lindo")


	def Mensaje4 (self):
		print("Hola Mundo")
		QtGui.QMessageBox.warning("Warning", "Ahhhhhhhhhh!!!")



ventana=Botones()
ventana.show()


sys.exit(app_exec)

