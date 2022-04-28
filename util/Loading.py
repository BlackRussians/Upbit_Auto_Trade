from PySide6.QtCore import QByteArray, Qt
from PySide6.QtGui import QMovie
from PySide6.QtWidgets import QWidget
from UI.load import Ui_Form
import os


class Loading(QWidget, Ui_Form):
    def __init__(self, parent):
        super(Loading, self).__init__(parent)
        self.setupUi(self)
        self.center()

        gif_path = os.path.join(os.path.dirname(__file__), '../data/loading.gif')
        self.movie = QMovie(gif_path, QByteArray(), self)
        self.movie.setCacheMode(QMovie.CacheAll)
        # QLabel에 동적 이미지 삽입
        self.label.setMovie(self.movie)

        self.setWindowFlags(Qt.FramelessWindowHint)

    def stop(self):
        self.hide()

    def start(self):
        self.movie.start()
        self.show()

    def center(self):
        size = self.size()
        ph = self.parent().geometry().height()
        pw = self.parent().geometry().width()
        self.move(int(pw/2 - size.width()/2), int(ph/2 - size.height()/2))
