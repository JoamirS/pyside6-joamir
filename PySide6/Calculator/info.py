from PySide6.QtWidgets import QLabel
from enviroments import SMALL_FONT_SIZE
from PySide6.QtCore import Qt


class Information(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def configuration_style(self):
        self.setStyleSheet(f'font-size: {SMALL_FONT_SIZE}px;')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
