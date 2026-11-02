
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout #importing modules and libraries that I need for this project
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget):    #creating a DigitalClock class, inheriting from QWidget
    def __init__(self):
        super().__init__()      #initialize a parent QWidget class
        self.time_label = QLabel(self) #creating a label that will display time
        self.timer = QTimer(self)   #creates a timer
        self.initui() #function I typically use for setting UI

    def initui(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(1400 ,450 ,300, 100)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)    #adds the time label to the layout
        self.setLayout(vbox)               #applies the layout to the main window

        self.time_label.setAlignment(Qt.AlignCenter)

        self.time_label.setStyleSheet("font-size: 150px;"
                                      "color: hsl(111, 100%, 50%);")
        self.setStyleSheet("background-color: black;")

        my_font = QFont("DS-Digital", 150) #creating a font object with QFont
        self.time_label.setFont(my_font)   #applies the font to the table

        self.timer.timeout.connect(self.update_time) #connects the timer signal to update_time function
        self.timer.start(1000)  #starts the time with interval of 1000ms

        self.update_time() #updates the clock

    def update_time(self):  #function for typically and displaying current time
        current_time = QTime.currentTime().toString("hh:mm:ss") #formating the time in hours:minutes:seconds #you can add an AP at the end of this string to get a PM/AM time
        self.time_label.setText(current_time) #updates the label with the newly updated time

def main(): #main function and some boilerplate code for a PyQt app
    app = QApplication(sys.argv)
    clock = DigitalClock()  #instance of DigitalClock class
    clock.show()            #showing the clock window
    sys.exit(app.exec_())


if __name__ == '__main__':  #this ensures that the main function only runs when its executed directly
    main()