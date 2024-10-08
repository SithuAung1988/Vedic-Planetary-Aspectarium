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
from pathlib import Path
from init import settingFile

settingJSON = settingFile

def createSetting(settingJSON):
    data = {
        'GUIMode': 'dark',
        'aspectMethod': 'alternative',
        'drishtiMethod': 'sputa',
        'sputaDrishtiMethod': 'alternative',
        'chartStyle': 'south',
        'mainDir': str(Path(__file__).parent),
        'tempDir': str(Path(settingJSON).parent),
        'settingJSON': str(Path(settingJSON)),
        'natalTXT': '',
        'tranTXT': ''
    }
    with open(settingJSON, 'w') as file:
        json.dump(data, file, indent=4)
    return

def readSetting(settingJSON: Path, key: str):
    with open(settingJSON, 'r') as file:
        data = json.load(file)
    return data.get(key)

def updateSetting(settingJSON: Path, key: str, value: str):
    with open(settingJSON, 'r') as file:
        data = json.load(file)
    data[key] = value
    with open(settingJSON, 'w') as file:
        json.dump(data, file, indent=4)
    return data
