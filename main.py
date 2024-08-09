from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


class Game:
    def __init__(self, browser):
        self.browser = browser
    
    def run(self):
        pass

class MyWebBrowser():

    def __init__(self):

        self.window = QWidget()
        self.window.setWindowTitle("Webbing With The Web")
        self.window.resize(1600, 900)

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(30)

        self.go_btn = QPushButton("Go")
        self.go_btn.setMinimumHeight(30)
        
        self.back_btn = QPushButton("<")
        self.back_btn.setMinimumHeight(30)
        
        self.forward_btn = QPushButton(">")
        self.forward_btn.setMinimumHeight(30)

        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)

        self.browser = QWebEngineView()

        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))
        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)
        self.browser.setUrl(QUrl("https://loopydoo.github.io/web-browser/level_1"))

        self.window.setLayout(self.layout)
        self.window.show()

    def navigate(self, url):
        if url=="https://loopydoo.github.io/web-browser/fina8" or "loopydoo.github.io/web-browser/fina8":
            self.browser.setUrl("https://loopydoo.github.io/web-browser/fina8")


app = QApplication([])
window = MyWebBrowser()
app.exec_()