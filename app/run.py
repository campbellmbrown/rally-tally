import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

from score_section import ScoreSection


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rally Tally")

        score_section = ScoreSection()

        layout = QVBoxLayout()
        layout.addWidget(score_section)

        cental_widget = QWidget()
        cental_widget.setLayout(layout)
        self.setCentralWidget(cental_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
