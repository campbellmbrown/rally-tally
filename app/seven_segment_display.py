from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QHBoxLayout, QWidget

from seven_segment_display_digit import SevenSegmentDisplayDigit


class SevenSegmentDisplay(QWidget):
    def __init__(self, digits: int):
        super().__init__()
        layout = QHBoxLayout()
        self.display_digits = [SevenSegmentDisplayDigit() for _ in range(digits)]
        for idx, display_digit in enumerate(reversed(self.display_digits)):
            layout.addWidget(display_digit)
            if idx < digits - 1:
                layout.addSpacing(10)
        self.setLayout(layout)

    def set_number(self, number: int):
        # trailing 0s should be displayed as blank
        for idx, digit in enumerate(self.display_digits):
            if number == 0 and idx != 0:
                digit.set_value(None)
            else:
                digit.set_value(number % 10)
            number //= 10

    def set_color(self, color: QColor) -> None:
        for digit in self.display_digits:
            digit.set_color(color)
