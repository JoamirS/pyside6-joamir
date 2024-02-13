
"""
QApplication and QPushButton de PySide6.QtWidgets
QApplication -> The main Widget of application
QpushButton -> One button
PySide6.QtWidgets -> Where is the PySide6 widgets
"""
import sys

from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

app_one = QApplication(sys.argv)

# Add the widget hierarchy and show window
button_with_text = QPushButton('Texto do botão')
button_with_text.setStyleSheet('font-size: 30px; color: blue;')


central_widget = QWidget()
# Create layout
layout = QVBoxLayout()
central_widget.setLayout(layout)

layout.addWidget(button_with_text)

central_widget.show()

# Loop of application
app_one.exec()
