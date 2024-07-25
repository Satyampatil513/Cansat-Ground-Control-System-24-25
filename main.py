import sys
import multiprocessing
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
from src.pages.dashboard import DashboardPage
from src.script.dummy_serial_port import data_generation_process

class MainWindow(QMainWindow):
    def __init__(self, data_queue):
        super().__init__()
        self.setWindowTitle("Ground Control Software")
        
        # Create QLabel for background
        self.background_label = QLabel(self)
        self.background_label.setPixmap(QPixmap('assets/images/background.png'))
        self.background_label.setGeometry(self.rect())
        self.background_label.setScaledContents(True)
        
        # Set Dashboard Page
        self.dashboard = DashboardPage(data_queue, self)
        self.setCentralWidget(self.dashboard)
        
        # Adjust the background label when window is resized
        self.resizeEvent = self.on_resize
        
    def on_resize(self, event):
        self.background_label.setGeometry(self.rect())
        event.accept()

if __name__ == "__main__":
    data_queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=data_generation_process, args=(data_queue, 1))
    process.start()

    app = QApplication(sys.argv)
    window = MainWindow(data_queue)
    window.showMaximized()
    sys.exit(app.exec_())

    process.terminate()
