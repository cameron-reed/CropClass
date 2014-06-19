import sys

from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MainWindow(QMainWindow):
    """The Main Window"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello World")
        self.create_layout()

    def create_layout(self):
        #create widget
        self.text_box = QLineEdit()
        self.button = QPushButton("Submit")
        self.label = QLabel("Please enter your name")
        
        #create layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text_box)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label)

        #set central widget
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        #connection
        self.button.clicked.connect(self.display_name)
        
    def display_name(self):
        name = self.text_box.text()
        self.label.setText("Hello {0}!".format(name))

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()

