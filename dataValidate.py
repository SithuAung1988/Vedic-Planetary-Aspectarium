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

import json
import sys
import subprocess
from pathlib import Path
from init import settingFile
from setting import readSetting
from PyQt6.QtWidgets import (QApplication, QDialog, QGridLayout,
                             QPushButton, QLabel, QGroupBox, QStyle)

settingJSON = settingFile
tempDir = readSetting(Path(settingJSON), 'tempDir')
varJSON = readSetting(Path(settingJSON), 'varJSON')
aspJSON = readSetting(Path(settingJSON), 'aspJSON')

# Load the variables file (contains planetary data such as degrees and retrograde status)
with open(varJSON) as var:
    var_data = json.load(var)

# Copy the loaded variables for further processing
variables = var_data.copy()

# Load the aspects file (contains calculated angular distances between planets)
with open(aspJSON) as asp:
    asp_data = json.load(asp)

# Update the variables dictionary with the aspect distances (natal_to_transit and transit_to_natal)
for aspect in asp_data['Aspecting_planets_to_aspected_planets']:
    for key, value in aspect.items():
        variables.update(value)

# List of planetary names to evaluate
names = ['Sun', 'Moo', 'Mar', 'Mer', 'Jup', 'Ven', 'Sat', 'Rah', 'Ket', 'Asc']

# Function to retrieve a variable (degree or retrograde status) from the variables dictionary
def getVariable(name):
    return variables.get(name)

# Flag to track if all results are true (for validation purposes)
all_results_true = True

# Function to evaluate the aspects between natal and transit planets
def evaluateNatalTransit(natal_name, transit_name):
    global all_results_true  # Use the global flag to track validation result

    # Get the retrograde statuses and aspect distances between the natal and transit planets
    natal_retro = getVariable(f'natal_{natal_name}_retro')
    transit_retro = getVariable(f'transit_{transit_name}_retro')
    natal_to_transit = getVariable(f'natal_{natal_name}_to_transit_{transit_name}')
    transit_to_natal = getVariable(f'transit_{transit_name}_to_natal_{natal_name}')

    # List to track any missing data
    missing_data = []
    if natal_retro is None:
        missing_data.append(f'natal_{natal_name}_retro')
    if transit_retro is None:
        missing_data.append(f'transit_{transit_name}_retro')
    if natal_to_transit is None:
        missing_data.append(f'natal_{natal_name}_to_transit_{transit_name}')
    if transit_to_natal is None:
        missing_data.append(f'transit_{transit_name}_to_natal_{natal_name}')

    # Print missing data and return early if any required data is absent
    if missing_data:
        print(f'Missing data for natal_{natal_name} and transit_{transit_name}: {', '.join(missing_data)}') # errMsg01
        return

    # Logic to validate the aspect distances based on retrograde statuses
    if natal_retro == False and transit_retro == False:
        # Both planets are direct: check if their sum equals 360 degrees
        result = (natal_to_transit + transit_to_natal) == 360
    elif natal_retro == True and transit_retro == True:
        # Both planets are retrograde: check if their sum equals 360 degrees
        result = (natal_to_transit + transit_to_natal) == 360
    else:
        # One planet is direct and the other is retrograde: check if their distances are equal
        result = natal_to_transit == transit_to_natal

    # If the validation fails, print the result and update the global flag
    if not result:
        print(f'Result for natal_{natal_name} and transit_{transit_name} is False') # errMsg02
        all_results_true = False

# Function to evaluate the aspects between transit and natal planets
# Note: This redundancy is intentional for thorough error checking.
def evaluateTransitNatal(transit_name, natal_name):
    global all_results_true  # Use the global flag to track validation result

    # Get the retrograde statuses and aspect distances between the transit and natal planets
    transit_retro = getVariable(f'transit_{transit_name}_retro')
    natal_retro = getVariable(f'natal_{natal_name}_retro')
    transit_to_natal = getVariable(f'transit_{transit_name}_to_natal_{natal_name}')
    natal_to_transit = getVariable(f'natal_{natal_name}_to_transit_{transit_name}')

    # List to track any missing data
    missing_data = []
    if transit_retro is None:
        missing_data.append(f'transit_{transit_name}_retro')
    if natal_retro is None:
        missing_data.append(f'natal_{natal_name}_retro')
    if transit_to_natal is None:
        missing_data.append(f'transit_{transit_name}_to_natal_{natal_name}')
    if natal_to_transit is None:
        missing_data.append(f'natal_{natal_name}_to_transit_{transit_name}')

    # Print missing data and return early if any required data is absent
    if missing_data:
        print(f'Missing data for transit_{transit_name} and natal_{natal_name}: {', '.join(missing_data)}') # errMsg03
        return

    # Logic to validate the aspect distances based on retrograde statuses
    if transit_retro == False and natal_retro == False:
        # Both planets are direct: check if their sum equals 360 degrees
        result = (transit_to_natal + natal_to_transit) == 360
    elif transit_retro == True and natal_retro == True:
        # Both planets are retrograde: check if their sum equals 360 degrees
        result = (transit_to_natal + natal_to_transit) == 360
    else:
        # One planet is direct and the other is retrograde: check if their distances are equal
        result = transit_to_natal == natal_to_transit

    # If the validation fails, print the result and update the global flag
    if not result:
        print(f'Result for transit_{transit_name} and natal_{natal_name} is False') # errMsg04
        all_results_true = False

# Perform validation by comparing natal to transit planets for all planet names
for natal_name in names:
    for transit_name in names:
        evaluateNatalTransit(natal_name, transit_name)

# Perform validation by comparing transit to natal planets for all planet names
for transit_name in names:
    for natal_name in names:
        evaluateTransitNatal(transit_name, natal_name)

# Print the final validation result
def usrFeedbackDialog(all_results_true, aspJSON):
    app = QApplication([])
    dialog = QDialog()
    dialog.setWindowTitle('Validation Results')

    main_layout = QGridLayout()

    icon_label = QLabel()

    def onClick():
        subprocess.Popen([sys.executable, str(Path(__file__).with_name('sdc.py'))],
                         creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == 'win32' else 0)
        dialog.accept() 

    if all_results_true:
        icon_label.setPixmap(app.style().standardPixmap(QStyle.StandardPixmap.SP_MessageBoxInformation))
        validation_message = 'Validation Result: <span style="color: #34A853 ;">[Passed]</span>.'
        button = QPushButton('Continue')
        button.clicked.connect(onClick)
    else:
        icon_label.setPixmap(app.style().standardPixmap(QStyle.StandardPixmap.SP_MessageBoxCritical))
        validation_message = 'Validation Result: <span style="color: #EA4335;">[Failed]</span>.'
        button = QPushButton('Close')
        button.clicked.connect(dialog.reject)

    data_group_box = QGroupBox('Data Path')
    data_layout = QGridLayout()

    data_header_label = QLabel()
    data_header_label.setText('Aspect distances have been calculated and saved to:')
    data_header_label.setStyleSheet('font-weight: bold')

    data_layout.addWidget(data_header_label, 0, 0)
    data_layout.addWidget(QLabel(str(aspJSON)), 1, 0)
    data_group_box.setLayout(data_layout)

    err_msg_box = QGroupBox('Feedback Message')
    msg_layout = QGridLayout()
    msg_layout.addWidget(QLabel(validation_message), 0, 0)
    err_msg_box.setLayout(msg_layout)
    
    main_layout.addWidget(icon_label, 0, 0, 2, 1)
    main_layout.addWidget(data_group_box, 0, 1)
    main_layout.addWidget(err_msg_box, 1, 1)
    main_layout.addWidget(button, 2, 1)

    dialog.setLayout(main_layout)
    dialog.exec()

usrFeedbackDialog(all_results_true, aspJSON)
