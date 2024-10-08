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

import sys
import json
from init import settingFile
from setting import readSetting
from pathlib import Path
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QScreen
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QGroupBox, QWidget
)

settingJSON = settingFile
natalJSON = readSetting(Path(settingJSON), 'natalJSON')
tranJSON = readSetting(Path(settingJSON), 'tranJSON')

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Natal Chart and Transit Chart: South Indian Style')
        self.setGeometry(600, 300, 1080, 480)
        
        # Create a central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        
        # Create a QHBoxLayout for the central widget to place group boxes side by side
        main_layout = QHBoxLayout(central_widget)
        
        # Create the first QGroupBox with the table
        self.natal_table = self.create_group_box('Natal')
        main_layout.addWidget(self.natal_table)
        
        # Create the second QGroupBox with the table
        self.transit_table = self.create_group_box('Transit')
        main_layout.addWidget(self.transit_table)
        
        # Set the layout for the central widget
        central_widget.setLayout(main_layout)
        
        # Load data from JSON files and populate the tables
        self.load_and_populate_data(natalJSON, self.natal_table.findChild(QTableWidget), 'natal')
        self.load_and_populate_data(tranJSON, self.transit_table.findChild(QTableWidget), 'transit')
        self.centeredWindow()

    def create_group_box(self, table_name):
        # Create a QGroupBox
        group_box = QGroupBox(self)
        # Create a QVBoxLayout for the QGroupBox
        group_box_layout = QVBoxLayout(group_box)
        # Create a QTableWidget
        table_widget = QTableWidget(4, 4, self)
        # Hide the horizontal and vertical headers
        table_widget.horizontalHeader().setVisible(False)
        table_widget.verticalHeader().setVisible(False)
        # Merge the cells (B2, C2, B3, C3)
        table_widget.setSpan(1, 1, 2, 2)
        
        # Add the table name in the merged cell
        item = QTableWidgetItem(table_name)
        font = QFont()
        font.setPointSize(20)
        font.setFamily('Roboto Mono')
        item.setFont(font)
        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
        table_widget.setItem(1, 1, item)
        
        # Populate the table with initial items
        for row in range(4):
            for col in range(4):
                if not (row == 1 and col in [1, 2]) and not (row == 2 and col in [1, 2]):
                    item = QTableWidgetItem('')
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                    table_widget.setItem(row, col, item)
                    table_widget.setColumnWidth(col, 120)
                    table_widget.setRowHeight(row, 100)
        
        # Center the table within the QGroupBox
        group_box_layout.addWidget(table_widget)
        
        # Apply a stylesheet to the table to set a border and reduce padding
        table_widget.setStyleSheet(
            "QTableWidget { gridline-color: #A9A9A9;}"
        )
        
        # Return the created group box
        return group_box

    def load_and_populate_data(self, file_path, table_widget, table_prefix):
        # Load data from the JSON file
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        # Define the mapping of signs to table cells
        sign_to_cell = {
            'Pis': (0, 0), 'Ari': (0, 1), 'Tau': (0, 2), 'Gem': (0, 3),
            'Aqu': (1, 0), 'Can': (1, 3), 'Cap': (2, 0), 'Leo': (2, 3),
            'Sag': (3, 0), 'Sco': (3, 1), 'Lib': (3, 2), 'Vir': (3, 3)
        }
        
        # Initialize a dictionary to hold concatenated text for each cell
        cell_contents = {}

        # Populate the table with data from the JSON file
        for entry in data:
            sign = entry['sign']
            name = entry['name']
            degree = entry['degree']
            retro = entry['retro']
            
            # Determine the cell based on the sign
            if sign in sign_to_cell:
                row, col = sign_to_cell[sign]
                cell_id = f'{table_prefix}_R{row + 1}C{col + 1}'
                
                # Format the retrograde symbol and degree string
                retro_symbol = '\u1D3F' if retro == 'true' and name not in ['Rah', 'Ket'] else ''
                degree = degree.replace('\u00b0', '°').replace('\u2032', '\'').replace('\u2033', '"')
                cell_text = f'{name}{retro_symbol} {degree}'
                
                # Append the text to the existing content of the cell
                if cell_id in cell_contents:
                    cell_contents[cell_id] += f'\n{cell_text}'
                else:
                    cell_contents[cell_id] = cell_text

        # Set the content of each cell in the table
        for cell_id, content in cell_contents.items():
            _, row_col = cell_id.split('_')
            row, col = int(row_col[1]) - 1, int(row_col[3]) - 1
            item = QTableWidgetItem(content)
            item.setFont(QFont('Roboto Mono', 12))
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
            table_widget.setItem(row, col, item)

    def centeredWindow(self):
        screen = QScreen.availableGeometry(QApplication.primaryScreen())
        window_geometry = self.frameGeometry()
        center_point = screen.center()
        window_geometry.moveCenter(center_point)
        self.move(window_geometry.topLeft())

# Initialize the application
app = QApplication(sys.argv)
# Create and show the main window
window = MainWindow()
window.show()
# Run the application's event loop
sys.exit(app.exec())
