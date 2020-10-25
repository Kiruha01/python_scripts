words = [['аэропорт', 5], ['банты', 1], ['бороду', 1], ['бухгалтеров', 4], ['вероисповедание', 9], ['гражданство', 5], 
['дефис', 3], ['дешевизна', 5], ['диспансер', 7], ['договореvb                 hnbbbbbbb bnnb nh,m,нность', 7], ['документ', 5], ['досуг', 3], ['еретик', 4], 
['жалюзи', 5], ['значимость', 2], ['иксы', 0], ['каталог', 5], ['квартал', 5], ['километр', 5], ['сантиметр', 6], 
['конусов', 1], ['корысть', 3], ['краны', 2], ['кремень', 4], ['кремня', 5], ['местностей', 1], ['мусоропровод', 10], 
['газопровод', 8], ['нефтепровод', 9], ['водопровод', 8], ['намерение', 3], ['нарост', 3], ['недруг', 1], ['недуг', 3], 
['некролог', 6], ['ненависть', 1], ['новости', 1], ['новостей', 6], ['ноготь', 1], ['ногтя', 1], ['отрочество', 0], 
['партер', 4], ['портфель', 5], ['поручни', 1], ['приданое', 4], ['призыв', 4], ['свекла', 2], ['сироты', 3], ['средства', 2], 
['столяр', 4], ['дояр', 2], ['школяр', 4], ['торты', 1], ['шарфы', 1], ['верна', 4], ['значимый', 2], ['красивее', 4], 
['кухонный', 1], ['ловка', 4], ['мозаичный', 4], ['оптовый', 3], ['прозорлива', 7], ['сливовый', 2], ['брала', 4], 
['бралась', 4], ['взяла', 4], ['взялась', 4], ['влилась', 4], ['ворволась', 6], ['воссоздала', 9], ['вручит', 4], 
['гнала', 4], ['гналась', 4], ['добрала', 6], ['добралась', 6], ['дождалась', 6], ['ждала', 4], ['житься', 1], ['жилось', 3], 
['закупорить', 3], ['занять', 3], ['заняла', 5], ['занял', 1], ['заняло', 1], ['заняли', 1], ['исчерпать', 3], ['клала', 2], 
['кралась', 2], ['лгала', 4], ['лила', 3], ['лилась', 3], ['наврала', 6], ['наделит', 5], ['надорвалась', 8], ['назвалась', 6], 
['накренится', 6], ['облегчить', 6], ['облегчит', 6], ['облилась', 5], ['озлобить', 3], ['оклеить', 3], ['окружит', 5], 
['опломбировать', 10], ['опошлить', 2], ['осведомиться', 3], ['осведомишься', 3], ['откупорить', 3], ['откупорил', 3], 
['плодоносить', 8], ['послала', 4], ['прибыть', 4], ['прибыл', 2], ['прибыла', 6], ['прибыло', 2], ['принять', 4], 
['принял', 2], ['приняли', 2], ['приняла', 6], ['принудить', 4], ['сверлить', 5], ['сверлишь', 5], ['сверлит', 5], 
['сорит', 3], ['убыстрить', 6], ['углубить', 5], ['черпать', 1], ['щемить', 3], ['щемит', 3], ['защемит', 5], 
['щелкать', 1], ['балованный', 3], ['включенный', 5], ['включен', 5], ['загнутый', 1], ['занятый', 1], 
['занята', 5], ['запертый', 1], ['заперта', 6], ['избалованный', 5], ['кормящий', 4], ['наживший', 3], 
['нажитый', 1], ['нажита', 5], ['наливший', 3], ['налита', 5], ['нанявший', 3], ['начавший', 3], ['начатый', 1], 
['начата', 5], ['ободрен', 5], ['ободрена', 7], ['отключенный', 6], ['повторенный', 6], ['поделенный', 5], ['понявший', 3], 
['принятый', 2], ['прирученный', 6], ['проживший', 4], ['снятый', 2], ['снята', 4], ['согнутый', 1], ['балуясть', 3], 
['закупорив', 3], ['начав', 3], ['отдав', 3], ['подняв', 4], ['поняв', 3], ['прибыв', 4], ['создав', 4], ['вовремя', 1], 
['добела', 5], ['доверху', 1], ['донельзя', 3], ['донизу', 1], ['досуха', 1], ['завидно', 3], ['загодя', 1], ['засветло', 1], 
['затемно', 1], ['красивее', 4], ['наверх', 3], ['надолго', 3], ['ненадолго', 5]]

import form

import sys
import random
from PyQt5 import QtWidgets, QtCore



class App(QtWidgets.QMainWindow, form.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.letters = [self.let_0, self.let_1,self.let_14, self.let_15, self.let_16,self.let_17, self.let_18, self.let_19,
                        self.let_20, self.let_21,self.let_22,self.let_23,self.let_24,self.let_25]

        self.next.clicked.connect(self.nextWord)
        self.but_0.clicked.connect(self._0)
        self.but_1.clicked.connect(self._1)
        self.but_14.clicked.connect(self._2)
        self.but_15.clicked.connect(self._3)
        self.but_16.clicked.connect(self._4)
        self.but_17.clicked.connect(self._5)
        self.but_18.clicked.connect(self._6)
        self.but_19.clicked.connect(self._7)
        self.but_20.clicked.connect(self._8)
        self.but_21.clicked.connect(self._9)
        self.but_22.clicked.connect(self._10)
        self.but_23.clicked.connect(self._11)
        self.but_24.clicked.connect(self._12)
        self.but_25.clicked.connect(self._13)

        self.flag = True
        self.word = []
        self.currentUdar = 0

        self.errorsStr = ''
        

    def setText(self, text):
        for l in self.letters:
            l.clear()
        for w, l in zip(text, self.letters):
            l.insert(w)


    def nextWord(self):
        if self.currentUdar == -1:
            self.status.setText('Ответь сначала')
            return
        self.currentUdar = -1
        try:
            self.word = words.pop(random.randint(0, len(words)-1))
            self.setText(self.word[0])
            self.status.setText('')
            self.left.setText('Осталось ' + str(len(words)))
            self.flag = True
        except ValueError:
            self.status.setText('Слова закончились')

    def check(self):
        idx = self.word[1]
        word = self.word[0]
        ww = word[:idx] + word[idx].upper() + word[idx+1:]
        if self.currentUdar == self.word[1]:
            self.status.setText('Правильно!')
        else:
            idx = self.word[1]
            word = self.word[0]
            ww = word[:idx] + word[idx].upper() + word[idx+1:]
            self.status.setText('Нет! Правильный ответ: ' + ww)
            if self.flag:
                self.errorsStr +=  ww + '\n'
                self.errors.setPlainText(self.errorsStr)
                self.flag = False
        self.setText(ww)

    def _0(self):
        self.currentUdar = 0
        self.check()

    def _1(self):
        self.currentUdar = 1
        self.check()    
        
    def _2(self):
        self.currentUdar = 2
        self.check()

    def _3(self):
        self.currentUdar = 3
        self.check()

    def _4(self):
        self.currentUdar = 4
        self.check()

    def _5(self):
        self.currentUdar = 5
        self.check()

    def _6(self):
        self.currentUdar = 6
        self.check()

    def _7(self):
        self.currentUdar = 7
        self.check()

    def _8(self):
        self.currentUdar = 8
        self.check()

    def _9(self):
        self.currentUdar = 9
        self.check()

    def _10(self):
        self.currentUdar = 10
        self.check()

    def _11(self):
        self.currentUdar = 11
        self.check()

    def _12(self):
        self.currentUdar = 12
        self.check()

    def _13(self):
        self.currentUdar = 13
        self.check()



def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()