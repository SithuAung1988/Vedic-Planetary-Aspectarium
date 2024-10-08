# Vedic Planetary Aspectarium (Version 0.0.0.1)
#
# Copyright (C) 2024 Sithu Aung <https://github.com/SithuAung1988>
# 
# This file is part of Vedic Planetary Aspectarium.
# 
# Vedic Planetary Aspectarium is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Vedic Planetary Aspectarium is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Vedic Planetary Aspectarium.  If not, see <https://www.gnu.org/licenses/>.

"""
NOTE:
I'm aware that this code is not efficient, but it works well enough for me.
I'll improve it later. But I don't have time to do that for now.
May be in next release.
We have the South Indian style chart as well. So this is not a mission critical.
For the time being, let's go with 'if it ain't broke, don't fix it' approach.
"""

import sys
import json
import darkdetect
from init import settingFile
from setting import readSetting
from pathlib import Path
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QMainWindow
from PyQt6.QtGui import QPainter, QPen, QFont, QFontMetrics, QPolygon
from PyQt6.QtCore import Qt, QPoint, QRect, QTimer

# Load settings
settingJSON = settingFile
natalJSON = readSetting(Path(settingJSON), 'natalJSON')
transitJSON = readSetting(Path(settingJSON), 'tranJSON')
cleanedJSON = readSetting(Path(settingJSON), 'cleanedJSON')

class NatalChartWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.current_theme = self.get_system_theme()
        self.setWindowTitle(f'Natal Chart and Transit Chart: North Indian Style')
        self.setFixedSize(501, 501)
        self.default_font_size = 12

        # Timer to check for theme change
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_theme_change)
        self.timer.start(1000)  # Check every second

    def get_system_theme(self):
        return 'dark' if darkdetect.isDark() else 'light'

    def check_theme_change(self):
        new_theme = self.get_system_theme()
        if new_theme != self.current_theme:
            self.current_theme = new_theme
            self.setWindowTitle(f'Natal Chart and Transit Chart: North Indian Style')
            self.update()  # Trigger a repaint

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Define the box's rectangle and draw it
        rect = self.rect().adjusted(10, 10, -10, -10)
        self.drawBorder(painter, rect)

        # Draw diagonal lines and diamond shape
        self.drawDiagonalLines(painter, rect)
        self.drawDiamond(painter, rect)

        # Handle rasi numbers
        asc_sign = self.getAscendantSign()
        cells = self.getRasiCells(asc_sign)
        self.drawRasiNumbers(painter, rect, cells)

        """ Filling up the planets' data """

        # Load the JSON data from the file
        with open(cleanedJSON, 'r') as file:
            data = json.load(file)

        # Extract the natal data
        natal_data = data['natal']

        # Define the signs based on degree ranges
        signs = [
            (0, 30, 'sign01'), (30, 60, 'sign02'), (60, 90, 'sign03'), (90, 120, 'sign04'),
            (120, 150, 'sign05'), (150, 180, 'sign06'), (180, 210, 'sign07'), (210, 240, 'sign08'),
            (240, 270, 'sign09'), (270, 300, 'sign10'), (300, 330, 'sign11'), (330, 360, 'sign12')
        ]

        # Determine the sign for a given degree
        def get_sign(degree):
            for start, end, sign in signs:
                if start <= degree < end:
                    return sign
            return None

        # Create a dictionary to store planets in their respective signs
        sign_dict = {sign: [] for _, _, sign in signs}

        # Find the Asc sign and place other planets in their respective signs
        asc_sign = None
        for planet in natal_data:
            sign = get_sign(planet['degree'])
            if planet['name'] == 'Asc':
                asc_sign = sign
            sign_dict[sign].append(planet)

        # Create cell arrays based on the Asc sign
        sign_names = [sign for _, _, sign in signs]
        asc_index = sign_names.index(asc_sign)
        cell_dict = {f'cell{(i + 1):02}': sign_dict[sign_names[(asc_index + i) % 12]] for i in range(12)}

        # Process each cell to format the planets' names, including retrograde and degrees
        def format_planet_name(planet):
            if planet['name'] in ['Rah', 'Ket']:
                return f'{planet['name']} {planet['degree']}°'
            retro_symbol = '\u1D3F' if planet['retro'].lower() == 'true' else ''
            return f'{planet['name']}{retro_symbol} {planet['degree']}°'

        for cell in cell_dict:
            cell_dict[cell] = [format_planet_name(planet) for planet in cell_dict[cell]]

        # Handle planets' data
        planets_data = [
            (QRect(rect.left() + 205, rect.top() + 85, 87, 72), cell_dict['cell01']), # Cell01
            (QRect(rect.left() + 80, rect.top() + 5, 87, 72), cell_dict['cell02']), # Cell02
            (QRect(rect.left() + 5, rect.top() + 85, 87, 72), cell_dict['cell03']), # Cell03
            (QRect(rect.left() + 80, rect.top() + 205, 87, 72), cell_dict['cell04']), # Cell04
            (QRect(rect.left() + 5, rect.top() + 325, 87, 72), cell_dict['cell05']), # Cell05
            (QRect(rect.left() + 80, rect.top() + 405, 87, 72), cell_dict['cell06']), # Cell06
            (QRect(rect.left() + 205, rect.top() + 325, 87, 72), cell_dict['cell07']), # Cell07
            (QRect(rect.left() + 317, rect.top() + 405, 87, 72), cell_dict['cell08']), # Cell08
            (QRect(rect.left() + 395, rect.top() + 325, 87, 72), cell_dict['cell09']), # Cell09
            (QRect(rect.left() + 317, rect.top() + 205, 87, 72), cell_dict['cell10']), # Cell10
            (QRect(rect.left() + 395, rect.top() + 85, 87, 72), cell_dict['cell11']), # Cell11
            (QRect(rect.left() + 317, rect.top() + 5, 87, 72), cell_dict['cell12']) # Cell12
        ]

        for rect, data in planets_data:
            self.drawPlanetsData(painter, rect, data)

    def getAscendantSign(self):
        """Retrieve the ascendant sign from the JSON file."""
        with open(natalJSON, 'r') as file:
            ascJSON = json.load(file)
        for item in ascJSON:
            if item['name'] == 'Asc':
                return item['sign']
        return None

    def getRasiCells(self, asc_sign):
        """Calculate the Rasi cells based on the ascendant sign."""
        signs = ['Ari', 'Tau', 'Gem', 'Can', 'Leo', 'Vir', 'Lib', 'Sco', 'Sag', 'Cap', 'Aqu', 'Pis']
        numbers = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        asc_index = signs.index(asc_sign)
        return [(numbers[(asc_index + i) % 12]) for i in range(12)]

    def drawBorder(self, painter, rect):
        if self.current_theme == 'dark':
            pen = QPen(Qt.GlobalColor.white)
        else:
            pen = QPen(Qt.GlobalColor.black)
        pen.setWidth(1)
        painter.setPen(pen)
        painter.drawRect(rect)

    def drawDiagonalLines(self, painter, rect):
        painter.drawLine(rect.topLeft(), rect.bottomRight())
        painter.drawLine(rect.topRight(), rect.bottomLeft())

    def drawDiamond(self, painter, rect):
        midpoints = [
            QPoint((rect.left() + rect.right()) // 2, rect.top()),
            QPoint(rect.right(), (rect.top() + rect.bottom()) // 2),
            QPoint((rect.left() + rect.right()) // 2, rect.bottom()),
            QPoint(rect.left(), (rect.top() + rect.bottom()) // 2)
        ]
        diamond = QPolygon(midpoints)
        painter.drawPolygon(diamond)

    def drawRasiNumbers(self, painter, rect, cells):
        """Draw Rasi numbers in their respective positions."""
        painter.save()
        if self.current_theme == 'dark':
            pen = QPen(Qt.GlobalColor.yellow)
        else:
            pen = QPen(Qt.GlobalColor.blue)
        painter.setPen(pen)
        
        center = rect.center()
        anchor_points = [
            (center.x(), center.y() - 25),  # Center Top
            (rect.left() + 120, rect.top() + 95),  # Top Left
            (rect.left() + 95, rect.top() + 120),  # Top Left Inner
            (center.x() - 25, center.y()),  # Center Left
            (rect.left() + 95, rect.bottom() - 120),  # Bottom Left Inner
            (rect.left() + 120, rect.bottom() - 95),  # Bottom Left
            (center.x(), center.y() + 25),  # Center Bottom
            (rect.right() - 120, rect.bottom() - 95),  # Bottom Right
            (rect.right() - 95, rect.bottom() - 120),  # Bottom Right Inner
            (center.x() + 25, center.y()),  # Center Right
            (rect.right() - 95, rect.top() + 120),  # Top Right Inner
            (rect.right() - 120, rect.top() + 95)   # Top Right
        ]        
        font = QFont('Roboto Mono', self.default_font_size)
        painter.setFont(font)

        for i, point in enumerate(anchor_points):
            text = cells[i]
            # Calculate the bounding rectangle for the text
            bounding_rect = painter.fontMetrics().boundingRect(text)
            # Calculate the position to center the text
            x = point[0] - bounding_rect.width() // 2
            y = point[1] + bounding_rect.height() // 2  # Adjusting y for vertical centering
            painter.drawText(QPoint(x, y), text)
        
        painter.restore()

    def drawPlanetsData(self, painter, rect, data):
        """Draw planets' data within a given rectangle."""
        painter.save()
        font = QFont('Roboto Mono', self.default_font_size)
        painter.setFont(font)

        # Calculate the available height for each line
        metrics = QFontMetrics(font)
        line_height = metrics.lineSpacing()
        rect_height = rect.height()
        num_lines = rect_height // line_height

        # Truncate data if it exceeds the available lines
        if len(data) > num_lines:
            data = data[:num_lines]

        # Calculate the starting y-position to center the text vertically
        total_text_height = len(data) * line_height
        start_y = rect.top() + (rect.height() - total_text_height) // 2

        # Draw each line of data within the rectangle
        for i, line in enumerate(data):
            # Calculate the bounding rectangle of the text
            text_rect = QRect(rect.left(), start_y + i * line_height, rect.width(), line_height)
            # Center the text vertically and horizontally within the bounding rectangle
            painter.drawText(text_rect, Qt.AlignmentFlag.AlignCenter, line)

        painter.restore()

class TransitChartWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.current_theme = self.get_system_theme()
        self.setWindowTitle(f'Natal Chart and Transit Chart: North Indian Style')
        self.setFixedSize(501, 501)
        #self.setGeometry(400, 300, 501, 501)
        self.default_font_size = 12

        # Timer to check for theme change
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_theme_change)
        self.timer.start(1000)  # Check every second

    def get_system_theme(self):
        return 'dark' if darkdetect.isDark() else 'light'

    def check_theme_change(self):
        new_theme = self.get_system_theme()
        if new_theme != self.current_theme:
            self.current_theme = new_theme
            self.setWindowTitle(f'Natal Chart and Transit Chart: North Indian Style')
            self.update()  # Trigger a repaint

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Define the box's rectangle and draw it
        rect = self.rect().adjusted(10, 10, -10, -10)
        self.drawBorder(painter, rect)

        # Draw diagonal lines and diamond shape
        self.drawDiagonalLines(painter, rect)
        self.drawDiamond(painter, rect)

        # Handle rasi numbers
        asc_sign = self.getAscendantSign()
        cells = self.getRasiCells(asc_sign)
        self.drawRasiNumbers(painter, rect, cells)

        """ Filling up the planets' data """

        # Load the JSON data from the file
        with open(cleanedJSON, 'r') as file:
            data = json.load(file)

        # Extract the transit data
        transit_data = data['transit']

        # Define the signs based on degree ranges
        signs = [
            (0, 30, 'sign01'), (30, 60, 'sign02'), (60, 90, 'sign03'), (90, 120, 'sign04'),
            (120, 150, 'sign05'), (150, 180, 'sign06'), (180, 210, 'sign07'), (210, 240, 'sign08'),
            (240, 270, 'sign09'), (270, 300, 'sign10'), (300, 330, 'sign11'), (330, 360, 'sign12')
        ]

        # Determine the sign for a given degree
        def get_sign(degree):
            for start, end, sign in signs:
                if start <= degree < end:
                    return sign
            return None

        # Create a dictionary to store planets in their respective signs
        sign_dict = {sign: [] for _, _, sign in signs}

        # Find the Asc sign and place other planets in their respective signs
        asc_sign = None
        for planet in transit_data:
            sign = get_sign(planet['degree'])
            if planet['name'] == 'Asc':
                asc_sign = sign
            sign_dict[sign].append(planet)

        # Create cell arrays based on the Asc sign
        sign_names = [sign for _, _, sign in signs]
        asc_index = sign_names.index(asc_sign)
        cell_dict = {f'cell{(i + 1):02}': sign_dict[sign_names[(asc_index + i) % 12]] for i in range(12)}

        # Process each cell to format the planets' names, including retrograde and degrees
        def format_planet_name(planet):
            if planet['name'] in ['Rah', 'Ket']:
                return f'{planet['name']} {planet['degree']}°'
            retro_symbol = '\u1D3F' if planet['retro'].lower() == 'true' else ''
            return f'{planet['name']}{retro_symbol} {planet['degree']}°'

        for cell in cell_dict:
            cell_dict[cell] = [format_planet_name(planet) for planet in cell_dict[cell]]

        # Handle planets' data
        planets_data = [
            (QRect(rect.left() + 205, rect.top() + 85, 87, 72), cell_dict['cell01']), # Cell01
            (QRect(rect.left() + 80, rect.top() + 5, 87, 72), cell_dict['cell02']), # Cell02
            (QRect(rect.left() + 5, rect.top() + 85, 87, 72), cell_dict['cell03']), # Cell03
            (QRect(rect.left() + 80, rect.top() + 205, 87, 72), cell_dict['cell04']), # Cell04
            (QRect(rect.left() + 5, rect.top() + 325, 87, 72), cell_dict['cell05']), # Cell05
            (QRect(rect.left() + 80, rect.top() + 405, 87, 72), cell_dict['cell06']), # Cell06
            (QRect(rect.left() + 205, rect.top() + 325, 87, 72), cell_dict['cell07']), # Cell07
            (QRect(rect.left() + 317, rect.top() + 405, 87, 72), cell_dict['cell08']), # Cell08
            (QRect(rect.left() + 395, rect.top() + 325, 87, 72), cell_dict['cell09']), # Cell09
            (QRect(rect.left() + 317, rect.top() + 205, 87, 72), cell_dict['cell10']), # Cell10
            (QRect(rect.left() + 395, rect.top() + 85, 87, 72), cell_dict['cell11']), # Cell11
            (QRect(rect.left() + 317, rect.top() + 5, 87, 72), cell_dict['cell12']) # Cell12
        ]

        for rect, data in planets_data:
            self.drawPlanetsData(painter, rect, data)

    def getAscendantSign(self):
        """Retrieve the ascendant sign from the JSON file."""
        with open(transitJSON, 'r') as file:
            ascJSON = json.load(file)
        for item in ascJSON:
            if item['name'] == 'Asc':
                return item['sign']
        return None

    def getRasiCells(self, asc_sign):
        """Calculate the Rasi cells based on the ascendant sign."""
        signs = ['Ari', 'Tau', 'Gem', 'Can', 'Leo', 'Vir', 'Lib', 'Sco', 'Sag', 'Cap', 'Aqu', 'Pis']
        numbers = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        asc_index = signs.index(asc_sign)
        return [(numbers[(asc_index + i) % 12]) for i in range(12)]

    def drawBorder(self, painter, rect):
        if self.current_theme == 'dark':
            pen = QPen(Qt.GlobalColor.white)
        else:
            pen = QPen(Qt.GlobalColor.black)
        pen.setWidth(1)
        painter.setPen(pen)
        painter.drawRect(rect)

    def drawDiagonalLines(self, painter, rect):
        painter.drawLine(rect.topLeft(), rect.bottomRight())
        painter.drawLine(rect.topRight(), rect.bottomLeft())

    def drawDiamond(self, painter, rect):
        midpoints = [
            QPoint((rect.left() + rect.right()) // 2, rect.top()),
            QPoint(rect.right(), (rect.top() + rect.bottom()) // 2),
            QPoint((rect.left() + rect.right()) // 2, rect.bottom()),
            QPoint(rect.left(), (rect.top() + rect.bottom()) // 2)
        ]
        diamond = QPolygon(midpoints)
        painter.drawPolygon(diamond)

    def drawRasiNumbers(self, painter, rect, cells):
        """Draw Rasi numbers in their respective positions."""
        painter.save()
        if self.current_theme == 'dark':
            pen = QPen(Qt.GlobalColor.yellow)
        else:
            pen = QPen(Qt.GlobalColor.blue)
        painter.setPen(pen)
        
        center = rect.center()
        anchor_points = [
            (center.x(), center.y() - 25),  # Center Top
            (rect.left() + 120, rect.top() + 95),  # Top Left
            (rect.left() + 95, rect.top() + 120),  # Top Left Inner
            (center.x() - 25, center.y()),  # Center Left
            (rect.left() + 95, rect.bottom() - 120),  # Bottom Left Inner
            (rect.left() + 120, rect.bottom() - 95),  # Bottom Left
            (center.x(), center.y() + 25),  # Center Bottom
            (rect.right() - 120, rect.bottom() - 95),  # Bottom Right
            (rect.right() - 95, rect.bottom() - 120),  # Bottom Right Inner
            (center.x() + 25, center.y()),  # Center Right
            (rect.right() - 95, rect.top() + 120),  # Top Right Inner
            (rect.right() - 120, rect.top() + 95)   # Top Right
        ]

        font = QFont('Roboto Mono', self.default_font_size)
        painter.setFont(font)

        for i, point in enumerate(anchor_points):
            text = cells[i]
            # Calculate the bounding rectangle for the text
            bounding_rect = painter.fontMetrics().boundingRect(text)
            # Calculate the position to center the text
            x = point[0] - bounding_rect.width() // 2
            y = point[1] + bounding_rect.height() // 2  # Adjusting y for vertical centering
            painter.drawText(QPoint(x, y), text)
        
        painter.restore()

    def drawPlanetsData(self, painter, rect, data):
        """Draw planets' data within a given rectangle."""
        painter.save()
        font = QFont('Roboto Mono', self.default_font_size)
        painter.setFont(font)

        # Calculate the available height for each line
        metrics = QFontMetrics(font)
        line_height = metrics.lineSpacing()
        rect_height = rect.height()
        num_lines = rect_height // line_height

        # Truncate data if it exceeds the available lines
        if len(data) > num_lines:
            data = data[:num_lines]

        # Calculate the starting y-position to center the text vertically
        total_text_height = len(data) * line_height
        start_y = rect.top() + (rect.height() - total_text_height) // 2

        # Draw each line of data within the rectangle
        for i, line in enumerate(data):
            # Calculate the bounding rectangle of the text
            text_rect = QRect(rect.left(), start_y + i * line_height, rect.width(), line_height)
            # Center the text vertically and horizontally within the bounding rectangle
            painter.drawText(text_rect, Qt.AlignmentFlag.AlignCenter, line)

        painter.restore()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Natal Chart and Transit Chart: North Indian Style')

        # Create instances of the two windows
        self.first_window = NatalChartWindow()
        self.second_window = TransitChartWindow()

        # Set a central widget to contain the two windows
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a vertical layout for the central widget
        main_layout = QVBoxLayout()

        # Create a horizontal layout for the labels
        label_layout = QHBoxLayout()
        natalLabel = QLabel('Natal:')
        transitLabel = QLabel('Transit:')
        natalLabel.setStyleSheet("font-family: 'Roboto Mono'; font-size: 14px;")
        transitLabel.setStyleSheet("font-family: 'Roboto Mono'; font-size: 14px;")

        # Add labels to the label layout
        label_layout.addWidget(natalLabel)
        label_layout.addWidget(transitLabel)

        # Add the label layout to the main layout
        main_layout.addLayout(label_layout)

        # Create a horizontal layout for the existing windows
        window_layout = QHBoxLayout()
        window_layout.addWidget(self.first_window)
        window_layout.addWidget(self.second_window)

        # Add the window layout to the main layout
        main_layout.addLayout(window_layout)

        # Set the main layout to the central widget
        central_widget.setLayout(main_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.resize(1000, 550)
    main_window.show()

    sys.exit(app.exec())
