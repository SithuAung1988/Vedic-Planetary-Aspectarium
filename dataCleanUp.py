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
import subprocess
from pathlib import Path
from init import settingFile
from setting import createSetting, updateSetting

settingJSON = settingFile

createSetting(settingJSON)

# Get input file paths from command line arguments
input_files = [sys.argv[1], sys.argv[2]] # Receiving natal.txt, transit.txt
output_files = [Path(settingJSON).parent / 'natal.json', 
                Path(settingJSON).parent / 'transit.json']

updateSetting(Path(settingJSON), 'settingJSON', str(settingJSON))
updateSetting(Path(settingJSON), 'tempDir', str(Path(settingJSON).parent))
updateSetting(Path(settingJSON), 'natalTXT', str(input_files[0]))
updateSetting(Path(settingJSON), 'tranTXT', str(input_files[1]))
updateSetting(Path(settingJSON), 'natalJSON', str(output_files[0]))
updateSetting(Path(settingJSON), 'tranJSON', str(output_files[1]))

# Define planets that always have a retrograde status as false/true
fixed_retro_false = ['Sun', 'Moo', 'Asc']
fixed_retro_true = ['Rah', 'Ket']

# Define zodiac sign values in degrees
sign_values = {
    'Ari': 0, 'Tau': 30, 'Gem': 60, 'Can': 90,
    'Leo': 120, 'Vir': 150, 'Lib': 180, 'Sco': 210,
    'Sag': 240, 'Cap': 270, 'Aqu': 300, 'Pis': 330
}

def isRetrograde(degree):
    # Check if a planet is retrograde based on its degree
    return degree.startswith('R')

def processFile(input_file, output_file):
    # Read data from the input file and process each line
    data = []
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    # Loop through a subset of lines to extract planetary data
    for line in lines[2:12]:
        parts = line.split()
        name, degree, sign = parts[0], parts[1], parts[2]

        # Determine retrograde status based on planet name or degree
        retro = 'true' if name in fixed_retro_true else 'false' if name in fixed_retro_false else 'true' if isRetrograde(degree) else 'false'
        
        degree = degree.lstrip('R')  # Remove 'R' from the degree if present
        data.append({'name': name, 'degree': degree, 'sign': sign, 'retro': retro})
    
    # Write the cleaned data to the output file in JSON format
    with open(output_file, 'w') as file:
        json.dump(data, file, indent=4)

# Process both natal and transit files
for input_file, output_file in zip(input_files, output_files):
    processFile(input_file, output_file)

def convertToDecimal(degree_str, sign):
    # Convert degree in DMS (Degrees, Minutes, Seconds) format to decimal degrees
    degrees, minutes, seconds = map(int, degree_str.replace('°', ' ').replace('′', ' ').replace('″', '').split())
    float_sec = float(seconds/60) # float_sec is a subminute value. E.g., 30 float_sec is equal to 0.5 minute
    float_min = float((minutes/60) + float_sec) # float_min is a subdegree value. E.g., 30 float_min is equal to 0.5 degree
    degrees = float(round(degrees + float_min, 2)) # Now seconds and minutes became decimal values and added to the degree value
    return degrees + sign_values[sign]  # Add the degree offset based on the sign

def combineAndCleanData(natal_file, transit_file, output_file):
    # Load natal and transit data from JSON files
    with open(natal_file, 'r') as file:
        natal_data = json.load(file)
    with open(transit_file, 'r') as file:
        transit_data = json.load(file)

    combined_data = {'natal': [], 'transit': []}

    # Process natal data
    for entry in natal_data:
        cleaned_entry = {
            'name': entry['name'],
            'degree': convertToDecimal(entry['degree'], entry['sign']),
            'retro': entry['retro']
        }
        combined_data['natal'].append(cleaned_entry)

    # Process transit data
    for entry in transit_data:
        cleaned_entry = {
            'name': entry['name'],
            'degree': convertToDecimal(entry['degree'], entry['sign']),
            'retro': entry['retro']
        }
        combined_data['transit'].append(cleaned_entry)

    # Save the cleaned combined data
    with open(output_file, 'w') as file:
        json.dump(combined_data, file, indent=4)

# Define the output file for combined and cleaned data
combined_output_file = Path(settingJSON).parent / 'cleaned.json'
updateSetting(Path(settingJSON), 'cleanedJSON', str(combined_output_file))

combineAndCleanData(output_files[0], output_files[1], combined_output_file)

def createVariables(data):
    # Create variable mappings for each planet's degree and retrograde status
    variables = {}
    for key in data:
        for item in data[key]:
            variables[f'{key}_{item['name']}_degree'] = item['degree']
            variables[f'{key}_{item['name']}_retro'] = item['retro'] == 'true'
    return variables

# Load the combined data and create variable mappings
with open(combined_output_file, 'r') as file:
    combined_data = json.load(file)

variables = createVariables(combined_data)

# Save the variables to a JSON file
variables_output_file = Path(settingJSON).parent / 'variables.json'
updateSetting(Path(settingJSON), 'varJSON', str(variables_output_file))

with open(variables_output_file, 'w') as output_file:
    json.dump({'variable': 'value', **variables}, output_file, indent=4)

# Call the next script for further computation
subprocess.Popen([sys.executable, str(Path(__file__).with_name('dataCompute.py'))],
                 creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == 'win32' else 0)
