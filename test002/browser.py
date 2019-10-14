import sys
from PyQt4 import QtGui, QtCore
from PySide.QtGui import QApplication
from PySide.QtCore import QUrl
from PySide.QtWebKit import QWebView

class SystemTrayIcon(QtGui.QSystemTrayIcon):
    def __init__(self, icon, parent=None):
       QtGui.QSystemTrayIcon.__init__(self, icon, parent)
       menu = QtGui.QMenu(parent)
       exitAction = menu.addAction("Exit")
       self.setContextMenu(menu)
       QtCore.QObject.connect(exitAction,QtCore.SIGNAL('triggered()'), self.exit)

    def exit(self):
      QtCore.QCoreApplication.exit()

def main():
   app = QtGui.QApplication(sys.argv)
   browser = QWebView()
   browser.setWindowTitle('CreativeDrive Brazil')
   browser.setUrl(QUrl('http://127.0.0.1:5000'))
   browser.showMaximized()

   w = QtGui.QWidget()
   trayIcon = SystemTrayIcon(QtGui.QIcon("static/images/ico.png"), w)

   trayIcon.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
    main()
