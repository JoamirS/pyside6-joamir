"""
QApplication and QPushButton de PySide6.QtWidgets
QApplication -> The main Widget of application
QpushButton -> One button
PySide6.QtWidgets -> Where is the PySide6 widgets
"""
import sys

from PySide6.QtWidgets import QApplication, QPushButton

app_one = QApplication(sys.argv)

# Add the widget hierarchy and show window
button_with_text = QPushButton('Texto do botão')
button_with_text.setStyleSheet('font-size: 40px; color: blue;')
button_with_text.show()

# Loop of application
app_one.exec()
