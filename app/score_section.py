from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QColorDialog, QPushButton, QVBoxLayout, QWidget

from seven_segment_display import SevenSegmentDisplay


class ScoreSection(QWidget):
    def __init__(self):
        super().__init__()

        self.seven_segment_display = SevenSegmentDisplay(digits=2)
        self.color_picker_button = QPushButton("Pick Color")
        self.color_picker_button.clicked.connect(self._pick_color)

        layout = QVBoxLayout()
        layout.addWidget(self.seven_segment_display)
        layout.addWidget(self.color_picker_button)
        self.setLayout(layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_value)
        self.timer.start(200)
        self.number = 0

    def update_value(self):
        self.seven_segment_display.set_number(self.number)
        self.number += 1
        if self.number > 99:
            self.number = 0

    def _pick_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.seven_segment_display.set_color(color)
