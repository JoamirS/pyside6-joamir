# Run the application
from main_window import MainWindow
from PySide6.QtWidgets import QApplication
from styles import setup_theme
from PySide6.QtGui import QIcon
from display import Display
from Button import Button, ButtonGrid
from info import Information
from enviroments import WINDOW_ICON_PATH
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    setup_theme()
    window_main = MainWindow(None)

    # icon
    icon = QIcon(str(WINDOW_ICON_PATH))
    window_main.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Information about numeric expression
    info = Information()
    info.setText('25 ^ 2 = 625')
    info.configuration_style()
    window_main.add_widget_to_VLayout(info)

    # Display
    display = Display()
    display.configuration_style()
    display.margin()
    window_main.add_widget_to_VLayout(display)

    # Grid
    button_grid = ButtonGrid()
    window_main.v_layout.addLayout(button_grid)

    # Button
    button_01 = Button('Texto do botão')
    button_grid.addWidget(button_01, 0, 0)

    button_02 = Button('Text Two')
    button_grid.addWidget(button_02, 0, 1)

    window_main.adjust_fixed_size()

    window_main.show()
    app.exec()
