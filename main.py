import sys
from custome_errors import *
sys.excepthook = my_excepthook
import requests
import urllib
import threading
from webbrowser import open as openLink
import language
import app
import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
from PyQt6.QtCore import Qt
language.init_translation()
class main (qt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(app.name + _("version : ") + str(app.version))
        self.link=qt.QLineEdit()
        self.link.setAccessibleName(_("link"))
        self.generate=qt.QPushButton(_("generate"))
        self.generate.setDefault(True)
        self.generate.clicked.connect(self.short1)
        self.re=qt.QLineEdit()
        self.re.setReadOnly(True)
        self.re.setAccessibleName(_("result"))
        self.open=qt.QPushButton(_("open link"))
        self.open.setDefault(True)
        self.open.clicked.connect(lambda:openLink(self.re.text()))
        layout=qt.QVBoxLayout()
        layout.addWidget(self.link)
        layout.addWidget(self.generate)
        layout.addWidget(self.re)
        layout.addWidget(self.open)
        w=qt.QWidget()
        w.setLayout(layout)
        self.setCentralWidget(w)
        mb=self.menuBar()
        help=mb.addMenu(_("help"))
        cus=help.addMenu(_("contact us"))
        telegram=qt1.QAction("telegram",self)
        cus.addAction(telegram)
        telegram.triggered.connect(lambda:openLink("https://t.me/mesteranasm"))
        telegramc=qt1.QAction(_("telegram channel"),self)
        cus.addAction(telegramc)
        telegramc.triggered.connect(lambda:openLink("https://t.me/tprogrammers"))
        donate=qt1.QAction(_("donate"),self)
        help.addAction(donate)
        donate.triggered.connect(lambda:openLink("https://www.paypal.me/AMohammed231"))
        about=qt1.QAction(_("about"),self)
        help.addAction(about)
        about.triggered.connect(lambda:qt.QMessageBox.information(self,_("about"),_("{} version: {} description: {} developer: {}").format(app.name,str(app.version),app.description,app.creater)))
        self.setMenuBar(mb)
    def short(self):
        link = "http://tinyurl.com/api-create.php"
        try:
            url = link + "?" \
            + urllib.parse.urlencode({"url": self.link.text()})
            res = requests.get(url)
            self.re.setText(res.text)
        except:
            self.re.setText(_("can't short this link"))
        self.re.setFocus()
    def short1(self):
        t=threading.Thread(target=self.short)
        t.start()


App=qt.QApplication([])
w=main()
w.show()
App.exec()