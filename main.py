import sys

from pathlib import Path

from PyQt6.QtWidgets import QApplication
from qt_material import apply_stylesheet

from src.startup_window import StartupWindow


def load_stylesheet(name: str):
    with open(Path("src") / "styles" / name) as f:
        style_src = f.read()
        app.setStyleSheet(app.styleSheet() + style_src)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    startup_window = StartupWindow()

    # window = MainWindow()

    apply_stylesheet(app, theme='dark_cyan.xml')

    load_stylesheet("override.qss")
    load_stylesheet("main.qss")

    startup_window.show()
    app.exec()
