# Project
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None):
        super().__init__(parent)

        # Configuring basic layout
        self.central_widget = QWidget()
        self.v_layout = QVBoxLayout()
        self.central_widget.setLayout(self.v_layout)
        self.setCentralWidget(self.central_widget)

        # Title od window
        self.setWindowTitle('Calculadora')

    def add_widget_to_VLayout(self, widget: QWidget):
        self.v_layout.addWidget(widget)

    # Final instruction -> Adjust Size
    def adjust_fixed_size(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
