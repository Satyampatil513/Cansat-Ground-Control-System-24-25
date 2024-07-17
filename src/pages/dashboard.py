from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from src.components.navigation_bar import NavigationBar
# from src.components.status_summary import StatusSummary

class DashboardPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)

        # Navigation bar
        self.nav_bar = NavigationBar(self)
        self.layout.addWidget(self.nav_bar)

        # # Mission status summary
        # self.status_summary = StatusSummary(self)
        # self.layout.addWidget(self.status_summary)

        # Refresh button
        self.refresh_button = QPushButton("Refresh", self)
        self.refresh_button.clicked.connect(self.refresh_status)
        self.layout.addWidget(self.refresh_button)

    def refresh_status(self):
        # Code to refresh mission status
        pass
