
"""
QApplication and QPushButton de PySide6.QtWidgets
QApplication -> The main Widget of application
QpushButton -> One button
PySide6.QtWidgets -> Where is the PySide6 widgets
"""
import sys

from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget, QGridLayout, QMainWindow

app_one = QApplication(sys.argv)

window = QMainWindow()

button_with_text_01 = QPushButton('Texto do botão 1')
button_with_text_01.setStyleSheet('font-size: 30px; color: blue;')

button_with_text_02 = QPushButton('Texto do botão 2')
button_with_text_02.setStyleSheet('font-size: 30px; color: red;')

button_with_text_03 = QPushButton('Texto do botão 3')
button_with_text_03.setStyleSheet('font-size: 25px; color: green')


central_widget = QWidget()
window.setCentralWidget(central_widget)

# Create layout
layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(button_with_text_01, 1, 1, 1, 1)
layout.addWidget(button_with_text_02, 1, 2, 1, 1)
layout.addWidget(button_with_text_03, 2, 1, 1, 2)


def slot_example(status_bar_new_message):
    status_bar_new_message.showMessage('Mudando o status')


# statusBar
status_bar = window.statusBar()
status_bar.showMessage('Mostrar mensagem na barra')


# MenuBar
menu = window.menuBar()
first_menu = menu.addMenu('Menu')
first_action = first_menu.addAction('Primeira ação')
# action
first_action.triggered.connect(lambda: slot_example(status_bar_new_message=status_bar))

window.show()
# Loop of application
app_one.exec()