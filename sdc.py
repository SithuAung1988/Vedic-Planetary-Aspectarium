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
from setting import readSetting, updateSetting

settingJSON = settingFile
tempDir = readSetting(Path(settingJSON), 'tempDir')
varJSON = readSetting(Path(settingJSON), 'varJSON')
aspJSON = readSetting(Path(settingJSON), 'aspJSON')

# Function to calculate SD value
def calculateSD(planet, value):
    if 0 <= value <= 30:
        return 0
    
    elif 30 < value <= 60:
        if planet in ['natal_Sat', 'transit_Sat']:
            return (value - 30) * 2 # Sat rule 1
        else:
            return (value - 30) / 2
    
    elif 60 < value <= 90:
        if planet in ['natal_Mar', 'transit_Mar']:
            return ((value - 60) + ((value - 60) / 2) + 15) # Mar rule 3
        elif planet in ['natal_Sat', 'transit_Sat']:
            return 60 - ((value - 60) / 2) # Sat rule 3
        else:
            return (value - 60) + 15
    
    elif 90 < value <= 120:
        if planet in ['natal_Mar', 'transit_Mar']:
            return 60 - (value - 90) # Mar rule 1
        elif planet in ['natal_Jup', 'transit_Jup']:
            return ((value - 90) / 2) + 45 # Jup rule 1
        else:
            return ((120 - value) / 2) + 30
    
    elif 120 < value <= 150:
        if planet in ['natal_Jup', 'transit_Jup']:
            return 60 - ((value - 120) * 2) # Jup rule 3 #Fixed
        else:
            return 150 - value
    
    elif 150 < value <= 180:
        return (value - 150) * 2
    
    elif 180 < value <= 210:
        return (300 - value) / 2
    
    elif 210 < value <= 240:
        if planet in ['natal_Mar', 'transit_Mar']:
            return 60 - (value - 210) # Mar rule 2
        elif planet in ['natal_Jup', 'transit_Jup']:
            return ((value - 210) / 2) + 45 # Jup rule 2
        else:
            return (300 - value) / 2
    
    elif 240 < value <= 270:
        if planet in ['natal_Jup', 'transit_Jup']:
            return (1.5 * (30 - (value -240))) + 15 # Jup rule 4 ####
        elif planet in ['natal_Sat', 'transit_Sat']:
            return (value - 240) + 30 # Sat rule 4
        else:
            return (300 - value) / 2
    
    elif 270 < value <= 300:
        if planet in ['natal_Sat', 'transit_Sat']:
            return 2 * (30 - (value - 270)) # Sat rule 2
        else:
            return (300 - value) / 2
    
    elif 300 < value <= 360:
        return 0

# Function to process JSON data
def processJSON(data):
    result = {'Aspecting_planets_to_aspected_planets': []}
    valid_planets = ['natal_Sun', 'natal_Moo', 'natal_Mar', 'natal_Mer', 'natal_Jup', 'natal_Ven', 'natal_Sat', 'transit_Sun', 'transit_Moo', 'transit_Mar', 'transit_Mer', 'transit_Jup', 'transit_Ven', 'transit_Sat']

    for item in data['Aspecting_planets_to_aspected_planets']:
        new_item = {}
        for key, value in item.items():
            for sub_key, sub_value in value.items():
                aspecting = sub_key.split('_to_')[0]
                aspected = sub_key.split('_to_')[1]
                aspect_degree = sub_value

                if aspecting in valid_planets:
                    sd_value = calculateSD(aspecting, aspect_degree)
                    new_item[sub_key] = float('%.2f' % abs(round(sd_value, 2)))
                    
        if new_item:
            result['Aspecting_planets_to_aspected_planets'].append({key: new_item})

    return result

# Load JSON data from file
with open((aspJSON), 'r') as file:
     data = json.load(file)

# Process JSON data
processed_data = processJSON(data)

output_json = Path(tempDir) / 'SputaDrishti.json'
updateSetting(Path(settingJSON), 'sdJSON', str(output_json))

# Save processed data to new JSON file
with open(output_json, 'w') as file:
    json.dump(processed_data, file, indent=4)

subprocess.Popen([sys.executable, str(Path(__file__).with_name('dataTable.py'))],
                 creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == 'win32' else 0)
