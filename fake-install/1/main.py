import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import QBasicTimer
import random
import time 
from random_data import genSecuence, dlllist, words


import ddes

class App(QtWidgets.QMainWindow, ddes.Ui_Form):

	"""docstring for App"""
	def nextPage(self):
		pass

	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.maxCount = 100
		self.programName = random.choice(['Realtek High Definition Audio v4.6', 'Keyboard Driver ADATA', 
			'Win32 Network Tools', 'AudioMIXER v1.2', 'HDD Health', 'USB Hardware Exist'])
		self.setWindowTitle(self.programName + ' - setup.exe')
		self.label.setText("Вас приветствует мастер установки " + self.programName)
		self.label_2.setText("Эта программа установит {} на ваш компьютер".format(self.programName))
		self.label_5.setText("Подождите, пока {} установится на ваш компьютер".format(self.programName))
		self.label_6.setText("{} успешно установлена на ваш компьютер".format(self.programName))
		self.cursor = QtGui.QTextCursor(self.textEdit.document())
		self.textEdit.setTextCursor(self.cursor)
		self.thisPage = -1
		self.progress = False
		self.step = 12
		self.nextPage()
		self.tick = False
		self.progressBar.setValue(self.step)
		self.pushButton.clicked.connect(self.nextPage)
		self.pushButton_2.clicked.connect(self.startInstall)
		self.pushButton_3.clicked.connect(self.previousPage)
		self.pushButton_5.clicked.connect(self.act)


		self.timer = QBasicTimer()
		self.timer2 = QBasicTimer()

	def generator(self):
		for i in genSecuence(words[random.randint(0, 5)], 1, random.randint(100, 300)):
			yield "Распаковка " + i
		for i in genSecuence(words[random.randint(0, 5)], 1, random.randint(150, 350)):
			yield "Копирование " + i
		for i in getDLL(random.randint(50, 400)):
			yield i

	def act(self):
		self.doANew(2000)

	def doANew(self, ms):
		if self.timer2.isActive():
			self.timer2.stop()
		else:
			self.timer2.start(ms, self)

	def doAction(self, ms):
		self.timer.stop()
		self.timer.start(ms, self)

	def nextPage(self):
		self.thisPage += 1
		self.stackedWidget.setCurrentIndex(self.thisPage)
	def previousPage(self):
		self.thisPage -= 1
		self.stackedWidget.setCurrentIndex(self.thisPage)

	def startInstall(self):
		self.nextPage()
		self.doAction(5)
		self.period = 0
		self.index = 0
		


	def timerEvent(self, e):
		if e.timerId() == self.timer.timerId():
			# text = self.generator()
			if random.randint(1, 8) < 3:
				self.doAction(random.randint(2, 100))
			if self.period < len(words):
				if self.period // 3 == 0:
					sit = "Распаковка "
				elif self.period // 3 == 1:
					self.doAction(15)
					sit = "Создание "
				else:
					sit = "Копирование "
				text = sit + words[self.period] % self.index
				self.index += 1
				if self.index == self.maxCount:
					self.period = random.randint(0, 5)
					self.index = 0
					self.maxCount = random.randint(50, 200)
					if self.period > 3:
						self.period = len(words)
			elif self.period >= len(words):
				self.doAction(random.randint(2, 70))
				text = random.choice(["Копирование ", "Копирование ", "Копирование ", "Обновление ", "Создание "]) + dlllist[random.randint(0, len(dlllist)-1)] + '.dll'
				self.index += 1
				if self.index == 200:
					self.period = random.randint(0, len(words) + len(dlllist) - 1)
					self.index = 0
					self.period = random.randint(0, len(words) - 1 )
			self.cursor.insertText(text + '\n')
			self.textEdit.moveCursor(QtGui.QTextCursor.End)
		elif e.timerId() == self.timer2.timerId():
			self.step += 1
			if self.step >= 80:
				self.doANew(10000)
			self.progressBar.setValue(self.step)
			if self.step >= 100:
				self.timer.stop()







	


def main():
	app = QtWidgets.QApplication(sys.argv)
	window = App()
	window.show()
	app.exec_()

if __name__ == '__main__':
	main()
