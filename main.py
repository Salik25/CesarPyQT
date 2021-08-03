from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import *
from user_window import Ui_MainWindow  # импорт нашего сгенерированного файла
from PyQt5.QtMultimedia import *
import sys
from os import path

# import  requests
# #https://login.dnevnik.ru/login/esia/nnov?returnUrl=https%3A%2F%2Fdnevnik.ru%2F
# s = requests.Session()
# data = {"login_username":"my_login", "login_password":"my_password"}
# url = "https://login.dnevnik.ru/login/esia/nnov?returnUrl=https%3A%2F%2Fdnevnik.ru%2F"
# r = s.post(url, data=data)
# print(r.text)
# # s = requests.get("https://dnevnik.ru/userfeed")
# # print(s.text)
# #r = s.get("https://httpbin.org/cookies")
RED = (250, 0, 0)
GREEN = (0, 250, 0)
HEIGHT = 700
WIDTH = 900


def klav_codding(messeng, all_klav, back_step):
    codding_string = ""
    for x in messeng:
        for i in all_klav:
            if x in i:
                codding_string += i[i.index(x) - back_step]
    return codding_string


def ancodding_klav(messeng, all_klav, forward_step):
    ancodding_string = ""
    for x in messeng:
        for i in all_klav:
            if x in i:
                if i.index(x) + forward_step < len(i):
                    ancodding_string += i[i.index(x) + forward_step]
                else:
                    ancodding_string += i[i.index(x) + forward_step - len(i)]
    return ancodding_string


def file_of_koddirovka(new_koddirovka, pos):
    if pos:
        file = open("coddirovka.txt", "r")
        your_koddirovka = file.readline()
        file.close()
        return int(your_koddirovka)
    else:
        file = open("coddirovka.txt", "w")
        file.write(new_koddirovka)
        file.close()


def kod_sergei(you_messen, pos, you_coddir):  # ниже просто преведен массив с клавишами
    rus_klav = ["ё", "й", "ц", "у", "к", "е", "н", "г", "ш", "щ", "з", "х", "ъ", "ф", "ы", "в", "а", "п", "р", "о", "л",
                "д", "ж", "э", "я", "ч", "с", "м", "и", "т", "ь", "б", "ю", " "]
    eng_klav = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x",
                "c", "v", "b", "n", "m"]
    sumvols = ["~", "`", "1", "!", "2", "@", '""', "3", "#", "№", "4", "$", ";", "5", "%", "6", "^", ":", "7", "&", "?",
               "8", "*", "9", "(", "0", ")", "-", "_", "=",
               "+", "[", "{", "]", "}", "|", "''", ",", "<", ".", "/","\n"]
    caps_rus = ["Ё", "Й", "Ц", "У", "К", "Е", "Н", "Г", "Ш", "Щ", "З", "Х", "Ъ", "Ф", "Ы", "В", "А", "П", "Р", "О", "Л",
                "Д", "Ж", "Э", "Я", "Ч", "С", "М", "И", "Т", "Ь", "Б", "Ю"]
    caps_eng = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X",
                "C", "V", "B", "N", "M"]
    all_klav = [rus_klav, eng_klav, sumvols, caps_rus, caps_eng]
    # codding_or_ancodding_string = ""
    if pos:  # pos - переменная типа булл , она обозначает шифрование и дешифрование
        return klav_codding(you_messen, all_klav, you_coddir)
    else:
        return ancodding_klav(you_messen, all_klav, you_coddir)


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.Codding_button)
        self.ui.pushButton_2.clicked.connect(self.Convert_Button)
        self.ui.pushButton_3.clicked.connect(self.Ancodding_button)
        self.ui.input_key.clicked.connect(self.input_key_and_enter)
        self.ui.lineEdit.setFont(QtGui.QFont('SansSerif', 15))
        self.ui.lineEdit_2.setFont(QtGui.QFont('SansSerif', 15))
        self.ui.pushButton.setFont(QtGui.QFont('SansSerif', 15))
        self.ui.pushButton_2.setFont(QtGui.QFont('SansSerif', 15))
        self.ui.pushButton_3.setFont(QtGui.QFont('SansSerif', 12))
        self.ui.pushButton.setStyleSheet('background: rgb(0,255,0);')
        self.ui.pushButton_2.setStyleSheet('background: rgb(255,255,0);')
        self.ui.pushButton_3.setStyleSheet('background: rgb(255,0,0);')
        self.ui.lineEdit.setStyleSheet("background:transparent;")
        self.ui.graphicsView.setStyleSheet(" background: rgb(75,70,70);")
        self.ui.lineEdit_2.setStyleSheet("background:transparent;")
        self.ui.key_of_shif.setFont(QtGui.QFont('SansSerif', 12))
        self.ui.input_key.setStyleSheet("background: rgb(255,255,0);")
        self.ui.key_of_shif.setStyleSheet("color: rgb(255, 0, 0);")
        self.ui.label.setStyleSheet("color: rgb(255, 255, 0);")
        self.ui.label.setFont(QtGui.QFont('SansSerif', 12))
        self.ui.key_of_shif.setMaxLength(1)
        # self.ui.key_of_shif.setStyleSheet("background:transparent;")
        self.ui.lineEdit_2.setReadOnly(True)
        self.pos_of_convert = True
        self.you_coddirovka = file_of_koddirovka(None, True) # в начале читаем кодировку файла
        self.answer = None
        #self.list_of_all_buttons = [[self.ui.pushButton , self.Codding_button],[self.ui.pushButton_3 , self.Ancodding_button]]
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        self.setWindowTitle('Шифратор v1.1')
        self.playlist = QMediaPlaylist()
        self.url = QUrl.fromLocalFile("./sound2.mp3")
        self.playlist.addMedia(QMediaContent(self.url))
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)
        self.player = QMediaPlayer()
        self.player.setPlaylist(self.playlist)
        self.player.play()
        self.player.setVolume(25)
        # self.player.setCustomAudioRole(self.ui.volumeSlider)
        self.slize_connect()
        self.ui.key_of_shif.setText(str(self.you_coddirovka)) # в начале ставим кодировку файла
    def Codding_button(self):
        self.pos_of_convert = True
        self.ui.pushButton.setStyleSheet('background: rgb(0,255,0);')
        self.ui.pushButton_3.setStyleSheet('background: rgb(255,0,0);')

    def Ancodding_button(self):
        self.pos_of_convert = False
        self.ui.pushButton.setStyleSheet('background: rgb(255,0,0);')
        self.ui.pushButton_3.setStyleSheet('background: rgb(0,255,0);')

    def Convert_Button(self):
        self.answer = self.ui.lineEdit.toPlainText()
        self.ui.lineEdit_2.setPlainText(kod_sergei(self.answer, self.pos_of_convert, self.you_coddirovka))
    def input_key_and_enter(self):
        self.you_coddirovka = int(self.ui.key_of_shif.text())
        file_of_koddirovka(self.ui.key_of_shif.text(),False) # меняем кодировку после нажатия кнопки

    def connect_and_disconnect_button(self, list_of_button, need_pos):
        if need_pos:
            for x in list_of_button:
                x[0].clicked.connect(x[1])
                x[0].setStyleSheet('background: rgb(0,255,0);')

        else:
            for x in list_of_button:
                x[0].disconnect()
                x[0].setStyleSheet('background: rgb(255,0,0);')
    def slize_connect(self):
        self.volum = 25
        self.ui.volumeSlider.setMinimum(0)
        self.ui.volumeSlider.setMaximum(100)
        self.ui.volumeSlider.setSingleStep(5)
        self.ui.volumeSlider.setTickInterval(20)
        self.ui.volumeSlider.setSliderPosition(25)
        self.ui.volumeSlider.valueChanged.connect(self.player.setVolume)

    # def keyPressEvent(self, e):
    #     if e.key() == Qt.Key_Enter:
    #         sezself.ui.lineEdit.text()


app = QtWidgets.QApplication([])
application = mywindow()
application.setFixedSize(WIDTH, HEIGHT)
application.show()
sys.exit(app.exec())
# print(kod_sergei(input(), True, 6))
# print(kod_sergei(input(), False, 6))
# file_of_koddirovka("7",False)
# print(file_of_koddirovka(None,True))
