import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QHBoxLayout, QPushButton, QApplication, QMainWindow, QVBoxLayout, QSpacerItem, QSizePolicy)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt


class Header(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle("Header")
        
        # Create the layout
        layout = QHBoxLayout()

        # Create the title label
        title_label = QLabel("   ARKA'24")
        title_font = QFont()
        title_font.setPointSize(40)
        title_font.setBold(True)
        title_label.setFont(title_font)
        # title_label.setStyleSheet("background-color: black; color: white; border: none; border-radius: 5px; padding: 5px; text-shadow: 2px 2px 4px black;")

        # Create the sub-title label
        subtitle_label = QLabel("CANSAT COMPETITION")
        subtitle_font = QFont()
        subtitle_font.setPointSize(10)
        subtitle_label.setFont(subtitle_font)

        # Create the team ID label
        team_id_label = QLabel("TEAM ID: XXXX     ")
        team_id_font = QFont()
        team_id_font.setPointSize(16)
        team_id_font.setBold(True)
        team_id_label.setFont(team_id_font)

        # Add the labels to the layout
        layout.addWidget(title_label, alignment=Qt.AlignLeft)
        layout.addWidget(subtitle_label, alignment=Qt.AlignLeft)
        layout.addWidget(team_id_label, alignment=Qt.AlignRight)

        # Set the layout
        self.setLayout(layout)

        # Set the background color
        self.setStyleSheet("background-color: black ; color: white;")
        self.setFixedHeight(150)

# # Create a QApplication instance
# app = QApplication(sys.argv)

# # Create the header instance
# header = Header()

# # Show the header
# header.show()

# # Run the application
# sys.exit(app.exec_())
