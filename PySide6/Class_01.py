
"""
QApplication and QPushButton de PySide6.QtWidgets
QApplication -> The main Widget of application
QpushButton -> One button
PySide6.QtWidgets -> Where is the PySide6 widgets
"""
import sys

from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QGridLayout

app_one = QApplication(sys.argv)

button_with_text_01 = QPushButton('Texto do botão 1')
button_with_text_01.setStyleSheet('font-size: 30px; color: blue;')

button_with_text_02 = QPushButton('Texto do botão 2')
button_with_text_02.setStyleSheet('font-size: 30px; color: red;')

button_with_text_03 = QPushButton('Texto do botão 3')
button_with_text_03.setStyleSheet('font-size: 25px; color: green')


central_widget = QWidget()
# Create layout
layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(button_with_text_01, 1, 1, 1, 1)
layout.addWidget(button_with_text_02, 1, 2, 1, 1)
layout.addWidget(button_with_text_03, 2, 1, 1, 2)

central_widget.show()

# Loop of application
app_one.exec()
