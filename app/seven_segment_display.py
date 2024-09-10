from enum import Enum

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor, QGradient, QPainter, QPixmap
from PyQt5.QtWidgets import QLabel, QWidget


class Segment(int, Enum):
    A_TOP = 0
    B_TOP_RIGHT = 1
    C_BOTTOM_RIGHT = 2
    D_BOTTOM = 3
    E_BOTTOM_LEFT = 4
    F_TOP_LEFT = 5
    G_MIDDLE = 6


SEGMENT_MAP = {
    0: [
        Segment.A_TOP,
        Segment.B_TOP_RIGHT,
        Segment.C_BOTTOM_RIGHT,
        Segment.D_BOTTOM,
        Segment.E_BOTTOM_LEFT,
        Segment.F_TOP_LEFT,
    ],
    1: [Segment.B_TOP_RIGHT, Segment.C_BOTTOM_RIGHT],
    2: [Segment.A_TOP, Segment.B_TOP_RIGHT, Segment.D_BOTTOM, Segment.E_BOTTOM_LEFT, Segment.G_MIDDLE],
    3: [Segment.A_TOP, Segment.B_TOP_RIGHT, Segment.C_BOTTOM_RIGHT, Segment.D_BOTTOM, Segment.G_MIDDLE],
    4: [Segment.B_TOP_RIGHT, Segment.C_BOTTOM_RIGHT, Segment.F_TOP_LEFT, Segment.G_MIDDLE],
    5: [Segment.A_TOP, Segment.C_BOTTOM_RIGHT, Segment.D_BOTTOM, Segment.F_TOP_LEFT, Segment.G_MIDDLE],
    6: [
        Segment.A_TOP,
        Segment.C_BOTTOM_RIGHT,
        Segment.D_BOTTOM,
        Segment.E_BOTTOM_LEFT,
        Segment.F_TOP_LEFT,
        Segment.G_MIDDLE,
    ],
    7: [Segment.A_TOP, Segment.B_TOP_RIGHT, Segment.C_BOTTOM_RIGHT],
    8: [
        Segment.A_TOP,
        Segment.B_TOP_RIGHT,
        Segment.C_BOTTOM_RIGHT,
        Segment.D_BOTTOM,
        Segment.E_BOTTOM_LEFT,
        Segment.F_TOP_LEFT,
        Segment.G_MIDDLE,
    ],
    9: [
        Segment.A_TOP,
        Segment.B_TOP_RIGHT,
        Segment.C_BOTTOM_RIGHT,
        Segment.D_BOTTOM,
        Segment.F_TOP_LEFT,
        Segment.G_MIDDLE,
    ],
}


class SevenSegmentDisplay(QWidget):

    def __init__(self):
        super().__init__()
        self.segment_labels = [QLabel(self) for _ in Segment]

        horizontal_segment = QPixmap("app/resources/7_segment_horizontal.png")
        vertical_segment = QPixmap("app/resources/7_segment_vertical.png")
        horizontal_segment_height = horizontal_segment.height()
        horizontal_segment_width = horizontal_segment.width()
        vertical_segment_height = vertical_segment.height()
        vertical_segment_width = vertical_segment.width()
        spacing = 10

        self.setFixedSize(
            (2 * spacing) + horizontal_segment_width + vertical_segment_width,
            (4 * spacing) + horizontal_segment_height + (2 * vertical_segment_height),
        )

        self.segment_labels[Segment.A_TOP].setPixmap(horizontal_segment)
        self.segment_labels[Segment.B_TOP_RIGHT].setPixmap(vertical_segment)
        self.segment_labels[Segment.C_BOTTOM_RIGHT].setPixmap(vertical_segment)
        self.segment_labels[Segment.D_BOTTOM].setPixmap(horizontal_segment)
        self.segment_labels[Segment.E_BOTTOM_LEFT].setPixmap(vertical_segment)
        self.segment_labels[Segment.F_TOP_LEFT].setPixmap(vertical_segment)
        self.segment_labels[Segment.G_MIDDLE].setPixmap(horizontal_segment)

        self.segment_labels[Segment.A_TOP].move(spacing + int(0.5 * vertical_segment_width), 0)
        self.segment_labels[Segment.B_TOP_RIGHT].move(
            (2 * spacing) + horizontal_segment_width, spacing + int(0.5 * horizontal_segment_height)
        )
        self.segment_labels[Segment.C_BOTTOM_RIGHT].move(
            (2 * spacing) + horizontal_segment_width,
            (3 * spacing) + int(0.5 * horizontal_segment_height) + vertical_segment_height,
        )
        self.segment_labels[Segment.D_BOTTOM].move(
            spacing + int(0.5 * vertical_segment_width), (4 * spacing) + (2 * vertical_segment_height)
        )
        self.segment_labels[Segment.E_BOTTOM_LEFT].move(
            0, (3 * spacing) + int(0.5 * horizontal_segment_height) + vertical_segment_height
        )
        self.segment_labels[Segment.F_TOP_LEFT].move(0, spacing + int(0.5 * horizontal_segment_height))
        self.segment_labels[Segment.G_MIDDLE].move(
            spacing + int(0.5 * vertical_segment_width), (2 * spacing) + vertical_segment_height
        )

    def update_colors(self, segment: Segment, color: QBrush | QColor | Qt.GlobalColor | QGradient):
        label = self.segment_labels[segment]
        pixmap = label.pixmap()
        colored_pixmap = QPixmap(pixmap.size())
        colored_pixmap.fill(Qt.GlobalColor.transparent)
        painter = QPainter(colored_pixmap)
        painter.drawPixmap(0, 0, pixmap)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(pixmap.rect(), color)
        painter.end()
        label.setPixmap(colored_pixmap)

    def set_value(self, value: int):
        if value not in SEGMENT_MAP:
            raise ValueError(f"Unsupported value: {value}")
        segments = SEGMENT_MAP[value]
        for segment in Segment:
            color = Qt.GlobalColor.white if segment in segments else QColor(0x111111)
            self.update_colors(segment, color)
