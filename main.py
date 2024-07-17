import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
from src.pages.dashboard import DashboardPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ground Control Software")
        
        # Create QLabel for background
        self.background_label = QLabel(self)
        self.background_label.setPixmap(QPixmap('assets/images/background.png'))
        self.background_label.setGeometry(self.rect())
        self.background_label.setScaledContents(True)
        
        # Set Dashboard Page
        self.dashboard = DashboardPage(self)
        self.setCentralWidget(self.dashboard)
        
        # Adjust the background label when window is resized
        self.resizeEvent = self.on_resize
        
    def on_resize(self, event):
        self.background_label.setGeometry(self.rect())
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()  # This line sets the window to maximized
    sys.exit(app.exec_())
