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


class MyWindow(QMainWindow):
    def __init__(self, parent: None):
        super().__init__(parent)

        # Button

        self.button_with_text_01 = QPushButton('Texto do botão 1')
        self.button_with_text_01.setStyleSheet('font-size: 30px; color: blue;')

        self.button_with_text_01.clicked.connect(self.change_message_status_bar)

        self.window = QMainWindow()

        self.button_with_text_02 = QPushButton('Texto do botão 2')
        self.button_with_text_02.setStyleSheet('font-size: 30px; color: red;')

        self.button_with_text_03 = QPushButton('Texto do botão 3')
        self.button_with_text_03.setStyleSheet('font-size: 25px; color: green')

        self.central_widget = QWidget()
        self.setWindowTitle('Título Joamir')
        self.setCentralWidget(self.central_widget)

        # Create layout
        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)

        self.grid_layout.addWidget(self.button_with_text_01, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.button_with_text_02, 1, 2, 1, 1)
        self.grid_layout.addWidget(self.button_with_text_03, 2, 1, 1, 2)

        # statusBar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Mostrar mensagem na barra')

        # MenuBar
        self.menu = self.menuBar()
        self.first_menu = self.menu.addMenu('Menu')

        # action
        self.first_action = self.first_menu.addAction('Primeira ação')
        self.first_action.triggered.connect(self.change_message_status_bar)

        self.second_action = self.first_menu.addAction('Segunda ação')
        self.second_action.setCheckable(True)
        self.second_action.toggled.connect(self.second_action_toggled)
        self.second_action.hovered.connect(self.second_action_toggled)

    @Slot()
    def change_message_status_bar(self):
        self.status_bar.showMessage('Mudando o status')

    @Slot()
    def second_action_toggled(self):
        print('Está marcado?', self.second_action.isChecked())


if __name__ == '__main__':
    window = MyWindow(None)
    window.show()
    # Loop of application
    app_one.exec()
