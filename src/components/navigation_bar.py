from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton

class NavigationBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QHBoxLayout(self)
        self.telemetry_button = QPushButton("Telemetry Data", self)
        self.telemetry_button.clicked.connect(self.show_telemetry_data)
        self.layout.addWidget(self.telemetry_button)

        self.command_center_button = QPushButton("Command Center", self)
        self.command_center_button.clicked.connect(self.show_command_center)
        self.layout.addWidget(self.command_center_button)

        self.calibration_button = QPushButton("Calibration", self)
        self.calibration_button.clicked.connect(self.show_calibration)
        self.layout.addWidget(self.calibration_button)

        self.logs_button = QPushButton("Logs", self)
        self.logs_button.clicked.connect(self.show_logs)
        self.layout.addWidget(self.logs_button)

        self.settings_button = QPushButton("Settings", self)
        self.settings_button.clicked.connect(self.show_settings)
        self.layout.addWidget(self.settings_button)

    def show_telemetry_data(self):
        # Code to navigate to telemetry data page
        pass

    def show_command_center(self):
        # Code to navigate to command center page
        pass

    def show_calibration(self):
        # Code to navigate to calibration page
        pass

    def show_logs(self):
        # Code to navigate to logs page
        pass

    def show_settings(self):
        # Code to navigate to settings page
        pass
