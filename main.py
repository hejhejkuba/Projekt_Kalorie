from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QFont, QIntValidator, QCursor
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
# Only needed for access to command line arguments
import sys
import re
class User():
    def __init__(self):
        super().__init__()
        self.index = 1
        self.wiek=0
        self.wzrost=0
        self.waga=0
        self.aktywnosc=0
        self.cel=0
        self.mezczyzna = True
    def TakeData(self, wiek, wzrost, waga, plec, aktywnosc, cel):
        self.wiek = wiek
        self.wzrost = wzrost
        self.waga = waga
        self.mezczyzna = plec
        self.aktywnosc = aktywnosc
        self.cel = cel
    def addIndex(self):
        self.index = self.index + 1



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui1()

    def init_ui1(self):
        # Czcionka

        font = QFont('Calibri', 24, weight=QFont.Bold)
        font2 = QFont('Calibri Light', 14)

        # Okno
        super().__init__()
        self.window_height = 400
        self.window_width = 600
        self.setFixedSize(self.window_width, self.window_height)

        # tytul okna
        self.setWindowTitle("Aplikacja Jakub Litwin")

        # layout
        layout = QVBoxLayout()

        # Nagłówek Powitalny
        self.naglowek = QLabel('Witaj', self)
        self.naglowek.move(20, 20)
        self.naglowek.resize(150, 50)
        self.naglowek.setFont(font)
        # self.naglowek.adjustSize()

        # informacja o stronie
        self.info = QLabel('Aplikacja pomoże Ci obliczyć twoje dzienne zapotrzebowanie kaloryczne', self)
        self.info.move(20, 70)
        self.info.setFont(font2)
        self.info.adjustSize()

        # przycisk kalkulatora kalorii
        push_button = QPushButton('Przejdź do kalkulatora', self)

        push_button.setGeometry(150, 150, 300, 50)
        push_button.setFont(font2)
        push_button.setStyleSheet("""
        QPushButton {
            background-color: #0080FE; 
            border: 3px solid #0080FE;
            color: white;
            border-radius: 15px;
        }
        QPushButton:hover {
            color: #0080FE;
            background-color: #AAAAAA; 
            border: 3px solid #0080FE;
        }
    """)
        push_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        push_button.clicked.connect(self.gotoKalorie)

    def gotoKalorie(self):
        widget.setCurrentIndex(widget.currentIndex()+1)

 #drugie okno

class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui2()

    def init_ui2(self):
        # Czcionka

        font = QFont('Calibri', 24, weight=QFont.Bold)
        font2 = QFont('Calibri Light', 14)
        font3 = QFont('Calibri Light', 14, weight=QFont.Bold)


        # Okno
        super().__init__()
        self.window_height = 400
        self.window_width = 600
        self.setFixedSize(self.window_width, self.window_height)


        outerLayout = QVBoxLayout()




        #wiek
        #wiek_lineeit
        self.wiek_lineeit = QLineEdit()
        self.wiek_lineeit.setFont(font2)
        self.wiek_lineeit.setFixedWidth(200)
        self.validator_wiek = QIntValidator(18, 80, self)
        self.wiek_lineeit.setValidator(self.validator_wiek)
        self.wiek_lineeit.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        #wiek_label
        self.wiek_label = QLabel("Wiek (18-80):")
        self.wiek_label.setFont(font3)

        # wzrost
        # wzrost_lineeit
        self.wzrost_lineeit = QLineEdit()
        self.wzrost_lineeit.setFont(font2)
        self.wzrost_lineeit.setFixedWidth(200)
        self.validator_wzrost = QIntValidator(self)
        self.wzrost_lineeit.setValidator(self.validator_wzrost)
        self.wzrost_lineeit.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        # wzrost_label
        self.wzrost_label = QLabel("Wzrost (cm):")
        self.wzrost_label.setFont(font3)

        # plec kobieta
        # kobieta_radiobutton
        self.kobieta_radiobutton = QRadioButton()
        self.kobieta_radiobutton.setFont(font2)
        self.kobieta_radiobutton.setFixedWidth(200)
        self.kobieta_radiobutton.setStyleSheet('QRadioButton::indicator { width: 20px; height: 20px;};')
        self.kobieta_radiobutton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        # kobieta_label
        self.kobieta_label = QLabel("Kobieta:")
        self.kobieta_label.setFont(font3)

        # plec mezczyzna
        # mezczyzna_radiobutton
        self.mezczyzna_radiobutton = QRadioButton()
        self.mezczyzna_radiobutton.setFont(font2)
        self.mezczyzna_radiobutton.setFixedWidth(200)
        self.mezczyzna_radiobutton.setStyleSheet('QRadioButton::indicator { width: 20px; height: 20px;};')
        self.mezczyzna_radiobutton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        # mezczyzna_label
        self.mezczyzna_label = QLabel("Mężczyzna:")
        self.mezczyzna_label.setFont(font3)
        # automatycznie ustawiony przycisk na mezczyznie
        self.mezczyzna_radiobutton.setChecked(True)

        # masa
        # masa_lineeit
        self.masa_lineeit = QLineEdit()
        self.masa_lineeit.setFont(font2)
        self.masa_lineeit.setFixedWidth(200)
        self.validator_waga = QIntValidator(self)
        self.masa_lineeit.setValidator(self.validator_waga)
        self.masa_lineeit.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        # masa_label
        self.masa_label = QLabel("Masa (kg):")

        self.masa_label.setFont(font3)




        #aktywnosc
        #aktywnosc_label
        self.aktywnosc_label = QLabel("Aktywnosc:")
        self.aktywnosc_label.setFont(font3)
        #aktywnosc_combo_box
        self.aktywnosc_combo_box = QComboBox()
        self.aktywnosc_combo_box.setFixedWidth(300)
        self.aktywnosc_combo_box.setStyleSheet("border: 1px solid blue;")
        self.aktywnosc_combo_box.setFont(font3)
        self.aktywnosc_combo_box.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.aktywnosc_combo_box.addItem("BMR lub BRAK")
        self.aktywnosc_combo_box.addItem("Lekka: 1-3 razy/tydzień")
        self.aktywnosc_combo_box.addItem("Średnia: 4-5 razy/tydzień")
        self.aktywnosc_combo_box.addItem("Aktywna: Codziennie")


        #cel
        #cel_label
        self.cel_label = QLabel("Cel:")
        self.cel_label.setFont(font3)
        #cel_combo_box
        self.cel_combo_box = QComboBox()
        self.cel_combo_box.setFont(font3)
        self.cel_combo_box.setFixedWidth(300)
        self.cel_combo_box.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.cel_combo_box.setStyleSheet("border: 1px solid blue;")
        self.cel_combo_box.addItem("Utrzymać Wagę")
        self.cel_combo_box.addItem("Schudnąć 0.5kg/tydzień")
        self.cel_combo_box.addItem("Przytyć: 0.5kg/tydzień")


        #topLayout
        topLayout = QFormLayout()
        topLayout.addRow(self.wiek_label, self.wiek_lineeit)
        topLayout.addRow(self.wzrost_label, self.wzrost_lineeit)
        topLayout.addRow(self.kobieta_label, self.kobieta_radiobutton)
        topLayout.addRow(self.mezczyzna_label, self.mezczyzna_radiobutton)
        topLayout.addRow(self.masa_label, self.masa_lineeit)
        topLayout.addRow(self.aktywnosc_label, self.aktywnosc_combo_box)
        topLayout.addRow(self.cel_label, self.cel_combo_box)



        bottomLayout = QHBoxLayout()

        #przycisk_wroc
        self.przycisk_wroc = QPushButton("Wróć")
        self.przycisk_wroc.setFont(font2)
        self.przycisk_wroc.setStyleSheet("""
        QPushButton {
            background-color: #0080FE; 
            border: 3px solid #0080FE;
            color: white;
            border-radius : 15px;
        }
        QPushButton:hover {
            color: #0080FE;
            background-color: #AAAAAA; 
            border: 3px solid #0080FE;
        }
    """)
        self.przycisk_wroc.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.przycisk_wroc.clicked.connect(self.gotoWelcomePage)

        #przycisk_oblicz
        self.przycisk_oblicz = QPushButton("Oblicz")
        self.przycisk_oblicz.setFont(font2)
        self.przycisk_oblicz.setStyleSheet("""
                QPushButton {
                    background-color: #0080FE; 
                    border: 3px solid #0080FE;
                    color: white;
                    border-radius : 15px;
                }
                QPushButton:hover {
                    color: #0080FE;
                    background-color: #AAAAAA; 
                    border: 3px solid #0080FE;
                }
            """)
        self.przycisk_oblicz.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.przycisk_oblicz.clicked.connect(self.goCheckData)


        bottomLayout.addWidget(self.przycisk_wroc)
        bottomLayout.addWidget(self.przycisk_oblicz)
        
        outerLayout.addLayout(topLayout)

        outerLayout.addLayout(bottomLayout)




        self.setLayout(outerLayout)

    def goCheckData(self):
        zmienna_pom = 0;
        if self.wiek_lineeit is not None:
            if self.wiek_lineeit.text() != "":
                if(int(self.wiek_lineeit.text())>=18):
                    print(self.wiek_lineeit.text())
                    zmienna_pom = zmienna_pom + 1
                    self.wiek_lineeit.setStyleSheet("border: 2px solid green")
                else:
                    self.wiek_lineeit.setStyleSheet("border: 2px solid red")
            else:
                self.wiek_lineeit.setStyleSheet("border: 2px solid red")

        if self.masa_lineeit is not None:
            if self.masa_lineeit.text() != "":
                print(self.masa_lineeit.text())
                zmienna_pom = zmienna_pom + 1
                self.masa_lineeit.setStyleSheet("border: 2px solid green")
            else:
                self.masa_lineeit.setStyleSheet("border: 2px solid red")
        else:
            self.masa_lineeit.setStyleSheet("border: 2px solid red")

        if self.wzrost_lineeit is not None:
            if self.wzrost_lineeit.text() != "":
                print(self.wzrost_lineeit.text())
                zmienna_pom = zmienna_pom +1
                self.wzrost_lineeit.setStyleSheet("border: 2px solid green")
            else:
                self.wzrost_lineeit.setStyleSheet("border: 2px solid red")
        if zmienna_pom == 3:
            user.TakeData(int(self.wiek_lineeit.text()), int(self.wzrost_lineeit.text()), int(self.masa_lineeit.text()), self.mezczyzna_radiobutton.isChecked(), self.aktywnosc_combo_box.currentIndex(), self.cel_combo_box.currentIndex())

            zmienna_pom = 0
            thirdwindow = ThirdWindow()
            widget.addWidget(thirdwindow)
            user.addIndex()
            widget.setCurrentIndex(user.index)




        else:
            zmienna_pom = 0




    def gotoWelcomePage(self):
        widget.setCurrentIndex(0)




#trzecie okno
class ThirdWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui3()

    def init_ui3(self):
        super().__init__()
        self.window_height = 400
        self.window_width = 600

        font5 = QFont('Calibri', 30, weight=QFont.Bold)
        font6 = QFont('Calibri Light', 14)
        font7 = QFont('Calibri Light', 12)

        grid = QGridLayout()


        #mnoznik

        aktywnosc = user.aktywnosc
        cel = user.cel
        mnoznik_cel = 1.0
        if(cel==0):
            mnoznik_cel = 1.0
        elif(cel==1):
            mnoznik_cel = 0.8
        elif(cel==2):
            mnoznik_cel = 1.2

        mnoznik_akt = 1.0
        if (aktywnosc == 0):
            mnoznik_akt = 1.0
        elif (aktywnosc == 1):
            mnoznik_akt = 1.2
        elif (aktywnosc == 2):
            mnoznik_akt = 1.3
        elif (aktywnosc == 2):
            mnoznik_akt = 1.4
        elif (aktywnosc == 3):
            mnoznik_akt = 1.6



        #Kalkulator Wzory


        Proteins = 2.0 * user.waga * mnoznik_cel * mnoznik_akt
        Proteins_low = 1.0 * user.waga * mnoznik_cel * mnoznik_akt
        Proteins_high = 3.0 * user.waga * mnoznik_cel * mnoznik_akt

        Fates = 0.9 * user.waga* mnoznik_cel * mnoznik_akt
        Fates_low = 0.8 * user.waga* mnoznik_cel * mnoznik_akt
        Fates_high = 1.2 * user.waga* mnoznik_cel * mnoznik_akt

        Carbesss = 4.2 * user.waga* mnoznik_cel * mnoznik_akt
        Carbesss_low = 3.2 * user.waga* mnoznik_cel * mnoznik_akt
        Carbesss_high = 5.0 * user.waga* mnoznik_cel * mnoznik_akt

        Sugars = 0.8*user.waga* mnoznik_cel * mnoznik_akt
        Kcal = 0



        if(user.mezczyzna == True):
            Kcal = (66.47+(13.75*user.waga)+(5*user.wzrost)-(6.75*user.wiek))*(mnoznik_cel * mnoznik_akt)
        else:
            Kcal = (665.1+(9.563*user.waga)+(1.85*user.wzrost)-(4.676*user.wiek))*(mnoznik_cel * mnoznik_akt)


        print("Proteins " + str(Proteins))
        print("Fates " + str(Fates))
        print("Carbesss " + str(Carbesss))
        print("Sugars " + str(Sugars))
        print("Kcal " + str(Kcal))
        print("cel " + str(cel))
        print("aktywnosc " + str(aktywnosc))

        #Kalkulator Style

        self.Protein_Label = QLabel("Białko")
        self.Protein_Label.setFont(font5)


        self.Protein_Wynik = QLabel(str(round(Proteins,2))+"g")
        self.Protein_Wynik.setFont(font7)
        self.Protein_Zasieg = QLabel("Range: " + str(round(Proteins_low,2)) + "g - " + str(round(Proteins_high,2))+"g")
        self.Protein_Zasieg.setFont(font7)


        self.Carbs_Label = QLabel("Węglowodany")
        self.Carbs_Label.setFont(font5)

        self.Carbs_Wynik = QLabel(str(round(Carbesss,2)) + "g")
        self.Carbs_Wynik.setFont(font7)
        self.Carbs_Zasieg = QLabel("Range: " + str(round(Carbesss_low,2)) + "g - " + str(round(Carbesss_high,2))+"g")
        self.Carbs_Zasieg.setFont(font7)

        self.Fat_Label = QLabel("Tłuszcz")
        self.Fat_Label.setFont(font5)

        self.Fat_Wynik = QLabel(str(round(Fates,2))+"g")
        self.Fat_Wynik.setFont(font7)
        self.Fat_Zasieg = QLabel("Range: " + str(round(Fates_low,2)) + "g - " + str(round(Fates_high,2))+"g")
        self.Fat_Zasieg.setFont(font7)

        self.Sugar_Label = QLabel("Cukry")
        self.Sugar_Label.setFont(font5)

        self.Sugar_Wynik = QLabel(str(round(Sugars,2))+"g")
        self.Sugar_Wynik.setFont(font7)


        self.Kcal_Label = QLabel("Kalorie")
        self.Kcal_Label.setFont(font5)

        self.Kcal_Wynik = QLabel(str(round(Kcal,2)))
        self.Kcal_Wynik.setFont(font5)




        grid.addWidget(self.Protein_Label, 0, 0, 2, 1, Qt.AlignCenter)
        grid.addWidget(self.Protein_Wynik, 0, 1, Qt.AlignCenter)
        grid.addWidget(self.Protein_Zasieg, 1, 1, Qt.AlignCenter)

        grid.addWidget(self.Carbs_Label, 2, 0, 2, 1, Qt.AlignCenter)
        grid.addWidget(self.Carbs_Wynik, 2, 1, Qt.AlignCenter)
        grid.addWidget(self.Carbs_Zasieg, 3, 1, Qt.AlignCenter)

        grid.addWidget(self.Fat_Label, 4, 0, 2, 1, Qt.AlignCenter)
        grid.addWidget(self.Fat_Wynik, 4, 1, Qt.AlignCenter)
        grid.addWidget(self.Fat_Zasieg, 5, 1, Qt.AlignCenter)

        grid.addWidget(self.Sugar_Label, 6, 0, 2, 1, Qt.AlignCenter)
        grid.addWidget(self.Sugar_Wynik, 6, 1, 2, 1, Qt.AlignCenter)


        grid.addWidget(self.Kcal_Label, 8, 0, 2, 1, Qt.AlignCenter)
        grid.addWidget(self.Kcal_Wynik, 8, 1, 2, 1, Qt.AlignCenter)
        def gotoWelcomeBack(self):
            widget.setCurrentIndex(1)

        def saveFile(self):
            texttoSave = "Wartości\n" + "Białko : " + str(round(Proteins,2)) + "g\nTłuszcze : " + str(round(Fates,2)) + "g\nWęglowodany : " + str(round(Carbesss,2)) + "g\nCukier : " + str(round(Sugars,2)) + "g\nKalorie : " + str(round(Kcal,2)) + "kcal"
            f = open("C:/Users/jakub/Downloads/Macros.txt", "w")
            f.write(texttoSave)
            f.close()
            ZapiszButton.setText("Zapisano")
            ZapiszButton.setStyleSheet("""
                        QPushButton {
                            background-color: #0080FE; 
                            border: 3px solid #0080FE;
                            color: white;
                            border-radius : 15px;
                        }
                    """)
            ZapiszButton.setCursor(QCursor(QtCore.Qt.ForbiddenCursor))



        BackButton = QPushButton("Wróć", self)
        BackButton.setFont(font6)
        BackButton.setStyleSheet("""
                        QPushButton {
                            background-color: #0080FE; 
                            border: 3px solid #0080FE;
                            color: white;
                            border-radius : 15px;
                        }
                        QPushButton:hover {
                            color: #0080FE;
                            background-color: #AAAAAA; 
                            border: 3px solid #0080FE;
                        }
                    """)
        BackButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        BackButton.clicked.connect(gotoWelcomeBack)

        grid.addWidget(BackButton, 10,0)


        ZapiszButton = QPushButton("Zapisz w Pobranych", self)
        ZapiszButton.setFont(font6)
        ZapiszButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        ZapiszButton.setStyleSheet("""
                                QPushButton {
                                    background-color: #0080FE; 
                                    border: 3px solid #0080FE;
                                    color: white;
                                    border-radius : 15px;
                                }
                                QPushButton:hover {
                                    color: #0080FE;
                                    background-color: #AAAAAA; 
                                    border: 3px solid #0080FE;
                                }
                            """)
        ZapiszButton.clicked.connect(saveFile)
        grid.addWidget(ZapiszButton, 10, 1)




        self.setLayout(grid)
#app
app = QApplication(sys.argv)

#widget
user = User()
widget = QtWidgets.QStackedWidget()
mainwindow = MainWindow()
secondwindow = SecondWindow()


widget.addWidget(mainwindow)
widget.addWidget(secondwindow)


widget.setWindowTitle("Kalkulator Kalorii - Jakub Litwin")
widget.setWindowIcon(QtGui.QIcon('apple.png'))
widget.setFixedSize(600, 400)
widget.setStyleSheet("background-color: white")
widget.show()
# create pyqt5 app
if __name__ == '__main__':

    sys.exit(app.exec())