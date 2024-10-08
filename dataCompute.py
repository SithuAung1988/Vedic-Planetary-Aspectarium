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

def calculateDistance(aspecting_degree, aspected_degree, aspecting_retro, aspected_retro):
    # Calculate the distance between two planets considering their retrograde statuses.
    if aspecting_retro:
        if aspected_retro:
            # Both planets are retrograde
            if aspecting_degree >= aspected_degree:
                return aspecting_degree - aspected_degree
            else:
                return (360 + aspecting_degree) - aspected_degree
        else:
            # Aspecting planet is retrograde, aspected planet is direct
            if aspecting_degree >= aspected_degree:
                return aspecting_degree - aspected_degree
            else:
                return (360 + aspecting_degree) - aspected_degree
    else:
        if aspected_retro:
            # Aspecting planet is direct, aspected planet is retrograde
            if aspecting_degree <= aspected_degree:
                return aspected_degree - aspecting_degree
            else:
                return (360 + aspected_degree) - aspecting_degree
        else:
            # Both planets are direct
            if aspected_degree >= aspecting_degree:
                return aspected_degree - aspecting_degree
            else:
                return (360 + aspected_degree) - aspecting_degree

# Load the variables (degree and retrograde information) from the JSON file
with open(varJSON, 'r') as file:
    data = json.load(file)

# Split the data into natal and transit planets
natal_planets = {k: v for k, v in data.items() if k.startswith('natal')}
transit_planets = {k: v for k, v in data.items() if k.startswith('transit')}

# Initialize an empty results dictionary
results = {'Aspecting_planets_to_aspected_planets': []}

def calculateAspects():
    # Calculate aspects (angular distances) between natal and transit planets.

    # Calculate aspects where natal planets aspect transit planets
    for natal_key in natal_planets:
        if natal_key.endswith('_degree'):
            natal_planet_name = natal_key.split('_')[1]
            natal_degree = natal_planets[natal_key]
            natal_retro = natal_planets[f'natal_{natal_planet_name}_retro']

            aspect_dict = {}

            # Compare natal planet with all transit planets
            for transit_key in transit_planets:
                if transit_key.endswith('_degree'):
                    transit_planet_name = transit_key.split('_')[1]
                    transit_degree = transit_planets[transit_key]
                    transit_retro = transit_planets[f'transit_{transit_planet_name}_retro']

                    aspecting_planet = f'natal_{natal_planet_name}'
                    aspected_planet = f'transit_{transit_planet_name}'

                    # Calculate the angular distance between planets
                    distance = calculateDistance(natal_degree, transit_degree, natal_retro, transit_retro)
                    # If we didn't do float(round(x,n)) here, validator won't be happy because some rounding ups end up making degree values to be over 359.
                    aspect_dict[f'{aspecting_planet}_to_{aspected_planet}'] = float(round(distance, 2)) 
            
            # Add the calculated distances to results
            results['Aspecting_planets_to_aspected_planets'].append({f'{aspecting_planet}_to_transit_planets': aspect_dict})
        
    # Similarly, calculate aspects where transit planets aspect natal planets
    for transit_key in transit_planets:
        if transit_key.endswith('_degree'):
            transit_planet_name = transit_key.split('_')[1]
            transit_degree = transit_planets[transit_key]
            transit_retro = transit_planets[f'transit_{transit_planet_name}_retro']

            aspect_dict = {}

            for natal_key in natal_planets:
                if natal_key.endswith('_degree'):
                    natal_planet_name = natal_key.split('_')[1]
                    natal_degree = natal_planets[natal_key]
                    natal_retro = natal_planets[f'natal_{natal_planet_name}_retro']

                    aspecting_planet = f'transit_{transit_planet_name}'
                    aspected_planet = f'natal_{natal_planet_name}'

                    # Calculate the angular distance between planets
                    distance = calculateDistance(transit_degree, natal_degree, transit_retro, natal_retro)
                    # If we didn't do float(round(x,n)) here, validator won't be happy because some rounding ups end up making degree values to be exceeded over 360.
                    aspect_dict[f'{aspecting_planet}_to_{aspected_planet}'] = float(round(distance, 2))

            # Add the calculated distances to results
            results['Aspecting_planets_to_aspected_planets'].append({f'{aspecting_planet}_to_natal_planets': aspect_dict})

# Perform the aspect calculation
calculateAspects()

# Save the calculated aspect data to a JSON file
output_file = Path(tempDir) / 'aspects.json'
updateSetting(Path(settingJSON), 'aspJSON', str(output_file))

with open(output_file, 'w') as file:
    json.dump(results, file, indent=4)

# Call the data validating script with variables.json and aspects.json file paths as arguments
subprocess.Popen([sys.executable, str(Path(__file__).with_name('dataValidate.py'))],
                creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == 'win32' else 0)