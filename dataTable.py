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
from pathlib import Path
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QScreen, QFont
from init import settingFile
from setting import readSetting
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, 
    QGroupBox, QTableWidget, QTableWidgetItem, QPushButton,
)

settingJSON = settingFile
varJSON = readSetting(Path(settingJSON), 'varJSON')
sdJSON = readSetting(Path(settingJSON), 'sdJSON')

def loadJSON(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def createTable(title, data, aspecting_planets, aspected_planets):
    group_box = QGroupBox(title)
    layout = QVBoxLayout()

    table = QTableWidget(len(aspecting_planets), len(aspected_planets))
    table.setStyleSheet(
        "QTableWidget { gridline-color: #A9A9A9; font-family: 'Roboto Mono'}"
        "QHeaderView::section { font-size: 14px; font-family: 'Roboto Mono' }"
        )
    
    """Allowing QTable to know which planets are in retrograde motion and label the table header accordingly """

    def processHeader(array, variables):
        processed_json = []
        processed_special = []
        special_aspects = ['natal_Sun', 'natal_Moo', 'natal_Rah', 'natal_Ket', 'natal_Asc', 
                           'transit_Sun', 'transit_Moo', 'transit_Rah', 'transit_Ket', 'transit_Asc']

        for item in array:
            if item not in special_aspects:
                retro_key = f'{item}_retro'
                if retro_key in variables:
                    retro_value = variables[retro_key]
                    planet_name = item.split('_')[1]
                    if retro_value:
                        processed_json.append(f'{planet_name}\u1D3F')
                    else:
                        processed_json.append(planet_name)

        for item in array:
            if item in special_aspects:
                processed_special.append(item.split('_')[1])

        # Recombine the items
        result = []
        for special in ['Sun', 'Moo']:
            if special in processed_special:
                result.append(special)
        result.extend(processed_json)
        for special in ['Rah', 'Ket', 'Asc']:
            if special in processed_special:
                result.append(special)

        return result

    # Load variables from the JSON file
    variables = loadJSON(varJSON) # Receiving variables.json

    # Process the aspecting and aspected arrays
    result_aspecting = processHeader(aspecting_planets, variables)
    result_aspected = processHeader(aspected_planets, variables)

    table.setVerticalHeaderLabels(result_aspecting)
    table.setHorizontalHeaderLabels(result_aspected)

    for row, aspecting_planet in enumerate(aspecting_planets):
        for col, aspected_planet in enumerate(aspected_planets):
            key = f'{aspecting_planet}_to_{aspected_planet}'
            if key in data:
                item = QTableWidgetItem(str(data[key]))
                item.setFont(QFont('Roboto Mono', 14))
                item.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                table.setItem(row, col, item)
                table.setColumnWidth(col, 60) # Set column width to 50 pixels

    layout.addWidget(table)
    group_box.setLayout(layout)
    return group_box

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Sputa Drishti Table')
        self.resize(720, 380)

        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)

        self.natal_to_transit_data = {}
        self.transit_to_natal_data = {}

        self.loadData()
        self.setupTabs()
        self.centeredWindow()

    def loadData(self):
        data = loadJSON(sdJSON)['Aspecting_planets_to_aspected_planets'] # Receiving SputaDrishti.json
        for aspect in data:
            for key, values in aspect.items():
                if key.startswith('natal_'):
                    self.natal_to_transit_data.update(values)
                elif key.startswith('transit_'):
                    self.transit_to_natal_data.update(values)

    def setupTabs(self):
        # Natal to Transit Aspects Tab
        natal_to_transit_tab = QWidget()
        natal_to_transit_layout = QVBoxLayout()
        natal_group_box = createTable(
            'Natal to Transit Aspects',
            self.natal_to_transit_data,
            ['natal_Sun', 'natal_Moo', 'natal_Mar', 'natal_Mer', 'natal_Jup', 'natal_Ven', 'natal_Sat'],
            ['transit_Sun', 'transit_Moo', 'transit_Mar', 'transit_Mer', 'transit_Jup', 'transit_Ven', 'transit_Sat', 'transit_Rah', 'transit_Ket', 'transit_Asc']
        )
        natal_to_transit_layout.addWidget(natal_group_box)
        natal_close_button = QPushButton('Close')
        natal_close_button.clicked.connect(self.close)
        natal_to_transit_layout.addWidget(natal_close_button)
        natal_to_transit_tab.setLayout(natal_to_transit_layout)

        # Transit to Natal Aspects Tab
        transit_to_natal_tab = QWidget()
        transit_to_natal_layout = QVBoxLayout()
        transit_group_box = createTable(
            'Transit to Natal Aspects',
            self.transit_to_natal_data,
            ['transit_Sun', 'transit_Moo', 'transit_Mar', 'transit_Mer', 'transit_Jup', 'transit_Ven', 'transit_Sat'],
            ['natal_Sun', 'natal_Moo', 'natal_Mar', 'natal_Mer', 'natal_Jup', 'natal_Ven', 'natal_Sat', 'natal_Rah', 'natal_Ket', 'natal_Asc']
        )
        transit_to_natal_layout.addWidget(transit_group_box)
        transit_close_button = QPushButton('Close')
        transit_close_button.clicked.connect(self.close)
        transit_to_natal_layout.addWidget(transit_close_button)
        transit_to_natal_tab.setLayout(transit_to_natal_layout)

        # Add tabs to the QTabWidget
        self.tab_widget.addTab(natal_to_transit_tab, 'Natal to Transit Aspects')
        self.tab_widget.addTab(transit_to_natal_tab, 'Transit to Natal Aspects')
    
    def centeredWindow(self):
        screen = QScreen.availableGeometry(QApplication.primaryScreen())
        window_geometry = self.frameGeometry()
        center_point = screen.center()
        window_geometry.moveCenter(center_point)
        self.move(window_geometry.topLeft())

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
