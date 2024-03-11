"""
QApplication and QPushButton de PySide6.QtWidgets
QApplication -> The main Widget of application
QpushButton -> One button
PySide6.QtWidgets -> Where is the PySide6 widgets

QMainWindow and centralWidget
-> QApplication (app)
    -> QMainWindow (window -> setCentralWidget)
        -> CentralWidget (central_widget)
        -> Layout (layout)
            -> Widget 1 (button_01)
            -> Widget 2 (button_02)
            -> Widget 3 (button_03)
    -> show
    -> exec
"""
import sys

from PySide6.QtCore import Slot
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
window.setWindowTitle('Título Joamir')
window.setCentralWidget(central_widget)

# Create layout
layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(button_with_text_01, 1, 1, 1, 1)
layout.addWidget(button_with_text_02, 1, 2, 1, 1)
layout.addWidget(button_with_text_03, 2, 1, 1, 2)


@Slot()
def slot_example(status_bar_new_message):
    status_bar_new_message.showMessage('Mudando o status')


@Slot()
def another_slot(checked):
    print('Está marcado?', checked)


@Slot()
def third_slot(action):
    def inner():
        another_slot(action.isChecked())

    return inner


# statusBar
status_bar = window.statusBar()
status_bar.showMessage('Mostrar mensagem na barra')

# MenuBar
menu = window.menuBar()
first_menu = menu.addMenu('Menu')

# action
first_action = first_menu.addAction('Primeira ação')
first_action.triggered.connect(lambda: slot_example(status_bar_new_message=status_bar))

second_action = first_menu.addAction('Segunda ação')
second_action.setCheckable(True)
second_action.toggled.connect(another_slot)
second_action.hovered.connect(third_slot(second_action))

button_with_text_01.clicked.connect(third_slot(second_action))

window.show()
# Loop of application
app_one.exec()
