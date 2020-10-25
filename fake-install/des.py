# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'установщик.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(798, 572)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 261, 561))
        self.label_4.setAutoFillBackground(False)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("aml-pages-3.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setOpenExternalLinks(False)
        self.label_4.setObjectName("label_4")
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(270, 10, 501, 541))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(0, 0, 521, 161))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAutoFillBackground(True)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(0, 150, 511, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(0, 200, 481, 91))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setGeometry(QtCore.QRect(390, 500, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.line = QtWidgets.QFrame(self.page)
        self.line.setGeometry(QtCore.QRect(-10, 470, 521, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_7 = QtWidgets.QPushButton(self.page)
        self.pushButton_7.setGeometry(QtCore.QRect(280, 500, 93, 28))
        self.pushButton_7.setObjectName("pushButton_7")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QtCore.QRect(390, 500, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 500, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.checkBox = QtWidgets.QCheckBox(self.page_2)
        self.checkBox.setGeometry(QtCore.QRect(20, 470, 391, 20))
        self.checkBox.setObjectName("checkBox")
        self.textBrowser = QtWidgets.QTextBrowser(self.page_2)
        self.textBrowser.setGeometry(QtCore.QRect(10, 50, 501, 401))
        self.textBrowser.setObjectName("textBrowser")
        self.label_8 = QtWidgets.QLabel(self.page_2)
        self.label_8.setGeometry(QtCore.QRect(110, 0, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.progressBar = QtWidgets.QProgressBar(self.page_3)
        self.progressBar.setGeometry(QtCore.QRect(30, 160, 471, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_5 = QtWidgets.QLabel(self.page_3)
        self.label_5.setGeometry(QtCore.QRect(30, 0, 381, 111))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setGeometry(QtCore.QRect(390, 500, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_5.setGeometry(QtCore.QRect(280, 500, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.textEdit = QtWidgets.QTextEdit(self.page_3)
        self.textEdit.setGeometry(QtCore.QRect(30, 210, 471, 251))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.line_3 = QtWidgets.QFrame(self.page_3)
        self.line_3.setGeometry(QtCore.QRect(0, 110, 521, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_6 = QtWidgets.QLabel(self.page_4)
        self.label_6.setGeometry(QtCore.QRect(30, 30, 431, 111))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.pushButton_6 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_6.setGeometry(QtCore.QRect(390, 500, 93, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.line_2 = QtWidgets.QFrame(self.page_4)
        self.line_2.setGeometry(QtCore.QRect(0, 470, 501, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_7 = QtWidgets.QLabel(self.page_4)
        self.label_7.setGeometry(QtCore.QRect(30, 140, 341, 81))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.stackedWidget.addWidget(self.page_4)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        self.checkBox.clicked['bool'].connect(self.pushButton_2.setEnabled)
        self.pushButton_6.clicked.connect(Form.close)
        self.pushButton_7.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Вас приветствует мастер установки ???"))
        self.label_2.setText(_translate("Form", "Эта программа установит ??? на ваш компьютер"))
        self.label_3.setText(_translate("Form", "Компьютер полностью готов к установке и удовлетворяет минимальным системным требованиям. Для отмены установки нажмите крестик в углу программы"))
        self.pushButton.setText(_translate("Form", "Далее"))
        self.pushButton_7.setText(_translate("Form", "Выйти"))
        self.pushButton_2.setText(_translate("Form", "Далее"))
        self.pushButton_3.setText(_translate("Form", "Назад"))
        self.checkBox.setText(_translate("Form", "Я согласен с условиями Лицензионного соглашения"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Лицензионное соглашение</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Настоящее Соглашение определяет условия использования Пользователями материалов и сервисов ?????</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">1.Общие условия</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">1.1. Использование материалов и сервисов Сайта регулируется нормами действующего законодательства Российской Федерации. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">1.2. Настоящее Соглашение является публичной офертой. Получая доступ к материалам Сайта Пользователь считается присоединившимся к настоящему Соглашению. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">1.3. Администрация Сайта вправе в любое время в одностороннем порядке изменять условия настоящего Соглашения. Такие изменения вступают в силу по истечении 3 (Трех) дней с момента размещения новой версии Соглашения на сайте. При несогласии Пользователя с внесенными изменениями он обязан отказаться от доступа к Сайту, прекратить использование материалов и сервисов Сайта. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">2. Обязательства Пользователя</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">2.1. Пользователь соглашается не предпринимать действий, которые могут рассматриваться как нарушающие российское законодательство или нормы международного права, в том числе в сфере </span><a href=\"http://copyright.ru/intellectual/\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">интеллектуальной собственности</span></a><span style=\" font-size:8pt;\">, </span><a href=\"http://copyright.ru/ru/documents/avtorskoe_pravo/avtorskie_prava/\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">авторских</span></a><span style=\" font-size:8pt; text-decoration: underline;\"> </span><span style=\" font-size:8pt;\">и/или </span><a href=\"http://copyright.ru/ru/documents/avtorskoe_pravo/smegnie_prava/\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">смежных правах</span></a><span style=\" font-size:8pt;\">, а также любых действий, которые приводят или могут привести к нарушению нормальной работы Сайта и сервисов Сайта. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">2.2. Использование материалов Сайта без согласия </span><a href=\"http://copyright.ru/documents/avtorskoe_pravo/pravoobladateli/\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">правообладателей</span></a><span style=\" font-size:8pt;\"> не допускается (статья 1270 Г.К РФ). Для правомерного использования материалов Сайта необходимо заключение </span><a href=\"http://copyright.ru/ru/documents/avtorskoe_pravo/peredacha_avtorskih_prav/\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">лицензионных договоров</span></a><span style=\" font-size:8pt;\"> (получение лицензий) от Правообладателей. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">2.3. При </span><a href=\"http://copyright.ru/library/zakonodatelstvo/gk_rf_obschee_zakonodatel/grazhdanskii_kodeks_RF_4_chast/glava_70__avtorskoe_pravo/#20\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">цитировании</span></a><span style=\" font-size:8pt;\"> материалов Сайта, включая охраняемые авторские произведения, ссылка на Сайт обязательна (подпункт 1 пункта 1 статьи 1274 Г.К РФ). </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">2.4. Комментарии и иные записи Пользователя на Сайте не должны вступать в противоречие с требованиями законодательства Российской Федерации и общепринятых норм морали и нравственности. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">2.5. Пользователь предупрежден о том, что Администрация Сайта не несет ответственности за посещение и использование им внешних ресурсов, ссылки на которые могут содержаться на сайте. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">2.6. Пользователь согласен с тем, что Администрация Сайта не несет ответственности и не имеет прямых или косвенных обязательств перед Пользователем в связи с любыми возможными или возникшими потерями или убытками, связанными с любым содержанием Сайта, </span><a href=\"http://copyright.ru/ru/documents/registraciy_avtorskih_prav/\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">регистрацией авторских прав</span></a><span style=\" font-size:8pt;\"> и сведениями о такой регистрации, товарами или услугами, доступными на или полученными через внешние сайты или ресурсы либо иные контакты Пользователя, в которые он вступил, используя размещенную на Сайте информацию или ссылки на внешние ресурсы. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">2.7. Пользователь принимает положение о том, что все материалы и сервисы Сайта или любая их часть могут сопровождаться рекламой. Пользователь согласен с тем, что Администрация Сайта не несет какой-либо ответственности и не имеет каких-либо обязательств в связи с такой рекламой. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">3. Прочие условия</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">3.1. Все возможные споры, вытекающие из настоящего Соглашения или связанные с ним, подлежат разрешению в соответствии с действующим законодательством Российской Федерации. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">3.2. Ничто в Соглашении не может пониматься как установление между Пользователем и Администрации Сайта агентских отношений, отношений товарищества, отношений по совместной деятельности, отношений личного найма, либо каких-то иных отношений, прямо не предусмотренных Соглашением. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">3.3. Признание судом какого-либо положения Соглашения недействительным или не подлежащим принудительному исполнению не влечет недействительности иных положений Соглашения. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">3.4. Бездействие со стороны Администрации Сайта в случае нарушения кем-либо из Пользователей положений Соглашения не лишает Администрацию Сайта права предпринять позднее соответствующие действия в защиту своих интересов и </span><a href=\"http://copyright.ru/documents/zashita_avtorskih_prav/\"><span style=\" font-size:8pt; text-decoration: underline; color:#0000ff;\">защиту авторских прав</span></a><span style=\" font-size:8pt;\"> на охраняемые в соответствии с законодательством материалы Сайта. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Пользователь подтверждает, что ознакомлен со всеми пунктами настоящего Соглашения и безусловно принимает их.</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">  </span></p></body></html>"))
        self.label_8.setText(_translate("Form", "Лицензионное соглашение"))
        self.label_5.setText(_translate("Form", "Подождите, пока ??? установится на ваш компьютер"))
        self.pushButton_4.setText(_translate("Form", "Завершить"))
        self.pushButton_5.setText(_translate("Form", "Отмена"))
        self.label_6.setText(_translate("Form", "??? успешно установлена на ваш компьютер"))
        self.pushButton_6.setText(_translate("Form", "Закрыть"))
        self.label_7.setText(_translate("Form", "Спасибо, что пользуетесь нашим продуктом."))


