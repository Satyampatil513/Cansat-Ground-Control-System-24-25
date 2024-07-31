from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QSize

class NavigationBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)  # Remove margins
        self.layout.setSpacing(0)  # Remove spacing

        # Set background color with transparency
        self.setStyleSheet("background-color: #00aaff; color: black;")
        self.setFixedHeight(70)

        poppins_font = QFont("Poppins", 14)
        bold_font = QFont("Poppins", 14)
        bold_font.setBold(True)
        

        #  Create buttons with icons (replace with your icon paths)
        self.home_button = QPushButton(QIcon("assets\images\home.png"), "Home", self)
        self.home_button.setFont(bold_font)
        self.home_button.setIconSize(QSize(24, 24))  # Set icon size
        self.home_button.clicked.connect(self.show_home)
        self.layout.addWidget(self.home_button)

        self.telemetry_button = QPushButton(QIcon("assets\images\telemetry.png"), "Telemetry Data", self)
        self.telemetry_button.setFont(bold_font)
        self.telemetry_button.setIconSize(QSize(24, 24))
        self.telemetry_button.clicked.connect(self.show_telemetry_data)
        self.layout.addWidget(self.telemetry_button)

        self.command_center_button = QPushButton(QIcon("assets\images\command.png"), "Command Center", self)
        self.command_center_button.setFont(bold_font)
        self.command_center_button.setIconSize(QSize(24, 24))
        self.command_center_button.clicked.connect(self.show_command_center)
        self.layout.addWidget(self.command_center_button)

        self.calibration_button = QPushButton(QIcon("assets\images\callibration.png"), "Calibration", self)
        self.calibration_button.setFont(bold_font)
        self.calibration_button.setIconSize(QSize(24, 24))
        self.calibration_button.clicked.connect(self.show_calibration)
        self.layout.addWidget(self.calibration_button)

        self.logs_button = QPushButton(QIcon("assets\images\logs-removebg-preview.png"), "Logs", self)
        self.logs_button.setFont(bold_font)
        self.logs_button.setIconSize(QSize(24, 24))
        self.layout.addWidget(self.logs_button)

        self.settings_button = QPushButton(QIcon("assets\images\settings.png"), "Settings", self)
        self.settings_button.setFont(bold_font)
        self.settings_button.setIconSize(QSize(24, 24))
        self.settings_button.clicked.connect(self.show_settings)
        self.layout.addWidget(self.settings_button)

    def show_home(self):
        # Code to navigate to Home page
        pass

    def show_telemetry_data(self):
        # Code to navigate to Telemetry Data page
        pass

    def show_command_center(self):
        # Code to navigate to Command Center page
        pass

    def show_calibration(self):
        # Code to navigate to Calibration page
        pass

    def show_logs(self):
        # Code to navigate to Logs page
        pass

    def show_settings(self):
        # Code to navigate to Settings page
        pass