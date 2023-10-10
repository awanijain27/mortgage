from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSignal, pyqtSlot

class PopupWindow(QWidget):
    closed = pyqtSignal()  # Custom signal emitted when the window is closed

    def __init__(self, parent=None):
        super(PopupWindow, self).__init__(parent)
        self.setWindowTitle("Add Record")
        self.setGeometry(100, 100, 300, 200)
        # ... Add your UI elements for adding records

    def closeEvent(self, event):
        self.closed.emit()  # Emit the signal when the window is closed
        event.accept()


class Dashboard(QMainWindow):
    def __init__(self):
        super(Dashboard, self).__init__()
        self.setWindowTitle("Dashboard")
        self.setGeometry(100, 100, 800, 600)
        self.initUI()

    def initUI(self):
        self.button = QPushButton("Add Record", self)
        self.button.setGeometry(10, 10, 150, 30)
        self.button.clicked.connect(self.openPopup)

    def openPopup(self):
        self.popup = PopupWindow(self)
        self.popup.closed.connect(self.refreshDashboard)  # Connect the signal to the slot
        self.popup.show()

    @pyqtSlot()
    def refreshDashboard(self):
        # Logic to refresh or reload the dashboard goes here
        print("Dashboard refreshed")


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    dashboard = Dashboard()
    dashboard.show()
    sys.exit(app.exec_())
