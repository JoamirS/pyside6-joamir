from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt
from enviroments import BIG_FONT_SIZE, DEFAULT_TEXT_MARGIN, DEFAULT_WIDTH


class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__()

    def configuration_style(self):
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px')
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setMinimumWidth(DEFAULT_WIDTH)

    def margin(self):
        list_text_margin = list()
        for margin_default in range(4):
            list_text_margin.append(DEFAULT_TEXT_MARGIN)
        self.setTextMargins(*list_text_margin)
