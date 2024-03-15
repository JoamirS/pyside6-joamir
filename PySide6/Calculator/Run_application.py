# Run the application
from main_window import MainWindow
from PySide6.QtWidgets import QApplication, QLabel
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window_main = MainWindow(None)

    label1 = QLabel('O meu texto')
    label1.setStyleSheet('font-size: 150px;')
    window_main.add_widget_to_VLayout(label1)

    window_main.adjust_fixed_size()

    window_main.show()
    app.exec()
