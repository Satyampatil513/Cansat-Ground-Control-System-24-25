from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from src.components.navigation_bar import NavigationBar


# from src.components.header import header
from src.components.header import Header

class DashboardPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: #2b2b2b; color: #00aaff;")
        
        main_layout = QVBoxLayout()

        # Add Header
        header = Header()
        # header.setFixedHeight(100)
        main_layout.addWidget(header)
        # header = Header()
        # main_layout.addWidget(header)
        
        nav_bar = NavigationBar()
        main_layout.addWidget(nav_bar)

        summary_layout = QVBoxLayout()

        # Row 1
       
       
        row1_layout = QHBoxLayout()
        # self.layout = QHBoxLayout(self)
        # self.layout.setContentsMargins(0, 0, 0, 0)  # Remove margins
        # self.layout.setSpacing(0)  # Remove spacing

        altitude_label = self.create_summary_label("127", "Altitude", "m")
        pressure_label = self.create_summary_label("10132", "Pressure", "Pa")
        battery_label = self.create_summary_label("60", "Battery", "%")
        temperature_label = self.create_summary_label("32", "Temperature", "°C")
       
        row1_layout.addWidget(altitude_label)
        row1_layout.addWidget(pressure_label)
        row1_layout.addWidget(battery_label)
        row1_layout.addWidget(temperature_label)
        # self.layout.setContentsMargins(0, 0, 0, 0)  # Remove margins
        # self.layout.setSpacing(0)  # Remove spacing

        # Row 2
        row2_layout = QHBoxLayout()
        latitude_label = self.create_summary_label("-21.1612", "Latitude")
        longitude_label = self.create_summary_label("74.1234", "Longitude")
        mission_time_label = self.create_summary_label("00:00:00", "Mission Time")

        row2_layout.addWidget(latitude_label)
        row2_layout.addWidget(longitude_label)
        row2_layout.addWidget(mission_time_label)

        # Row 3
        row3_layout = QHBoxLayout()
        status_label = self.create_summary_label("Connected", "Current Status")
        command_label = self.create_summary_label("Parachute Deployment", "Command")

        row3_layout.addWidget(status_label)
        row3_layout.addWidget(command_label)

        summary_layout.addLayout(row1_layout)
        summary_layout.addLayout(row2_layout)
        summary_layout.addLayout(row3_layout)

        main_layout.addLayout(summary_layout)
        self.setLayout(main_layout)

    def create_summary_label(self, value, label, unit=""):
        widget = QWidget()
        layout = QVBoxLayout()
        value_unit_layout = QHBoxLayout()
        value_label = QLabel(value)
        value_label.setFont(QFont('Poppins', 30, QFont.Bold))
        value_label.setAlignment(Qt.AlignCenter)

        unit_label = QLabel(unit)
        unit_label.setFont(QFont('Poppins', 14, QFont.Bold))
        unit_label.setAlignment(Qt.AlignCenter)
        value_unit_layout.addWidget(value_label)
        value_unit_layout.addWidget(unit_label)

        description_label = QLabel(label)
        description_label.setFont(QFont('Poppins', 24, QFont.Bold))
        description_label.setStyleSheet("color: white;") 
        description_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(value_label)
        layout.addWidget(unit_label)
        layout.addWidget(description_label)

        widget.setLayout(layout)
        widget.setStyleSheet("background-color: #1f1f1f; border-radius: 5px; padding: 10px;")
        return widget

