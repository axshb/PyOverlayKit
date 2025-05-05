from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QGridLayout
from PySide6.QtGui import QColor

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyOverlayKit.overlay import Overlay

if __name__ == "__main__":
    app = QApplication([])

    # Create an instance of the Overlay
    overlay = Overlay()

    # Set custom background color and transparency
    overlay.set_background_color(QColor(0, 0, 0, 150))  # Green with 150 transparency

    # Set position and size
    overlay.set_geometry(100, 100, 400, 200)  # x, y, width, height

    # Create a grid layout and set it to the overlay
    grid_layout = QGridLayout()
    overlay.setLayout(grid_layout)

    # Add widgets to the grid layout
    label1 = QLabel("Label 1")
    label2 = QLabel("Label 2")
    button1 = QPushButton("Button 1")
    button2 = QPushButton("Button 2")

    grid_layout.addWidget(label1, 0, 0)   # Row 0, Column 0
    grid_layout.addWidget(button1, 0, 1)  # Row 0, Column 1
    grid_layout.addWidget(label2, 1, 0)   # Row 1, Column 0
    grid_layout.addWidget(button2, 1, 1)  # Row 1, Column 1

    # Show the overlay
    overlay.show()

    # Run the application
    app.exec()
