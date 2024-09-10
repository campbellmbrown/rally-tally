import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget

from seven_segment_display import SevenSegmentDisplay


class SegmentDisplay(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("7-Segment Display")
        self.seven_segment_display = SevenSegmentDisplay()
        layout = QVBoxLayout()
        layout.addWidget(self.seven_segment_display)
        self.setLayout(layout)

        self.setStyleSheet("background-color: black;")

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_value)
        self.timer.start(500)
        self.number = 0

    def update_value(self):
        self.seven_segment_display.set_value(self.number)
        self.number += 1
        if self.number > 9:
            self.number = 0


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SegmentDisplay()
    window.show()
    sys.exit(app.exec_())
