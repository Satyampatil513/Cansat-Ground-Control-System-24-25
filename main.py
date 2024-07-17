import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from src.pages.dashboard import DashboardPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ground Control Software")
        self.setGeometry(100, 100, 800, 600)
        self.dashboard = DashboardPage(self)
        self.setCentralWidget(self.dashboard)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
