from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont
from src.components.navigation_bar import NavigationBar
# from src.components.header import Header
import random

class DashboardPage(QWidget):
    def __init__(self, data_queue, parent=None):
        super().__init__(parent)
        self.data_queue = data_queue
        self.setStyleSheet("background-color: #2b2b2b; color: #00aaff;")

        main_layout = QVBoxLayout()

        # Add Header
        # header = Header()
        # main_layout.addWidget(header)

        # Add Navigation Bar
        nav_bar = NavigationBar()
        main_layout.addWidget(nav_bar)

        # Summary Widgets
        self.summary_layout = QVBoxLayout()

        # Row 1
        self.row1_layout = QHBoxLayout()
        self.altitude_label = self.create_summary_label("127", "Altitude", "m")
        self.pressure_label = self.create_summary_label("10132", "Pressure", "Pa")
        self.battery_label = self.create_summary_label("60", "Battery", "%")
        self.temperature_label = self.create_summary_label("32", "Temperature", "°C")

        self.row1_layout.addWidget(self.altitude_label)
        self.row1_layout.addWidget(self.pressure_label)
        self.row1_layout.addWidget(self.battery_label)
        self.row1_layout.addWidget(self.temperature_label)

        # Row 2
        self.row2_layout = QHBoxLayout()
        self.latitude_label = self.create_summary_label("-21.1612", "Latitude")
        self.longitude_label = self.create_summary_label("74.1234", "Longitude")
        self.mission_time_label = self.create_summary_label("00:00:00", "Mission Time")

        self.row2_layout.addWidget(self.latitude_label)
        self.row2_layout.addWidget(self.longitude_label)
        self.row2_layout.addWidget(self.mission_time_label)

        # Row 3
        self.row3_layout = QHBoxLayout()
        self.status_label = self.create_summary_label("Connected", "Current Status")
        self.command_label = self.create_summary_label("Parachute Deployment", "Command")

        self.row3_layout.addWidget(self.status_label)
        self.row3_layout.addWidget(self.command_label)

        self.summary_layout.addLayout(self.row1_layout)
        self.summary_layout.addLayout(self.row2_layout)
        self.summary_layout.addLayout(self.row3_layout)

        main_layout.addLayout(self.summary_layout)
        self.setLayout(main_layout)

        # Setup timer to update data every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_data)
        self.timer.start(1000)

    def create_summary_label(self, value, label, unit=""):
        widget = QWidget()
        layout = QVBoxLayout()

        value_label = QLabel(value)
        value_label.setFont(QFont('Arial', 40))
        value_label.setAlignment(Qt.AlignCenter)

        unit_label = QLabel(unit)
        unit_label.setFont(QFont('Arial', 20))
        unit_label.setAlignment(Qt.AlignCenter)

        description_label = QLabel(label)
        description_label.setFont(QFont('Arial', 16))
        description_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(value_label)
        layout.addWidget(unit_label)
        layout.addWidget(description_label)

        widget.setLayout(layout)
        widget.setStyleSheet("background-color: #1f1f1f; border-radius: 10px; padding: 20px;")
        widget.value_label = value_label  # Store reference to value_label
        widget.unit_label = unit_label
        widget.description_label = description_label
        return widget

    def update_data(self):
        if not self.data_queue.empty():
            data = self.data_queue.get()
            self.altitude_label.value_label.setText(str(data["Altitude"]))
            self.pressure_label.value_label.setText(str(data["Pressure"]))
            self.battery_label.value_label.setText(str(data["Voltage"]))
            self.temperature_label.value_label.setText(str(data["Temperature"]))
            self.latitude_label.value_label.setText(str(data["GNSS Latitude"]))
            self.longitude_label.value_label.setText(str(data["GNSS Longitude"]))
            self.mission_time_label.value_label.setText(str(data["GNSS Time"]))
            self.status_label.value_label.setText(data["Flight Software State"])
            self.command_label.value_label.setText("Parachute Deployment")
