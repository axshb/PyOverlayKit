<h1 align="center">PyOverlayKit</h1>
<p align="center">
  <img src="https://socket.dev/api/badge/pypi/package/PyOverlayKit/0.2.0?artifact_id=tar-gz" alt="Socket">
  <img src="https://img.shields.io/badge/Platform-Windows-blue.svg" alt="Platform">
  <img src="https://img.shields.io/badge/PRs-Welcome-brightgreen.svg" alt="PRs Welcome">
  <img src="https://img.shields.io/github/last-commit/axshb/hwinsight.svg" alt="Last Commit">
</p>


This package provides a customizable overlay for PySide6/PyQt6 applications, allowing you to create always-on-top windows with adjustable background colors, transparency, and layouts. Specifically, this package allows these overlays to stay on top of full-screened applications. 

Find PyOverlayKit on PyPi [here](https://pypi.org/project/PyOverlayKit/).

## Installation

You can install the package using pip:

`pip install PyOverlayKit`

## Example Usage
```
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QGridLayout
from PySide6.QtGui import QColor
from PyOverlayKit.overlay import Overlay

app = QApplication([])

overlay = Overlay()
overlay.set_background_color(QColor(0, 255, 0, 150))  # Green with 150 transparency
overlay.set_geometry(100, 100, 400, 200)

grid_layout = QGridLayout()
overlay.setLayout(grid_layout)

label1 = QLabel("Label 1")
button1 = QPushButton("Button 1")
grid_layout.addWidget(label1, 0, 0)
grid_layout.addWidget(button1, 0, 1)

overlay.show()
app.exec()
```

## Contributing
Contributions are welcome. Please fork the repository and submit a pull request.
