from PySide6.QtWidgets import QPushButton, QGridLayout
from enviroments import MEDIUM_FONT_SIZE


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def configuration_style(self):
        font_style = self.font()
        font_style.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font_style)
        self.setMinimumSize(75, 60)


class ButtonGrid(QGridLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._grid_mask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['', '0', '.', '='],
        ]