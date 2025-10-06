# Python PyQt5 Digital Clock

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Digital Clock')
        self.resize(250, 100)

        # Create a label to display time
        self.time_label = QLabel(self)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size: 40px; font-family: 'Courier';")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.time_label)
        self.setLayout(layout)

        # Timer to update the time every second
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)  # 1000 ms = 1 second

        self.showTime()  # Display the current time immediately

    def showTime(self):
        current_time = QTime.currentTime().toString('hh:mm:ss')
        self.time_label.setText(current_time)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())