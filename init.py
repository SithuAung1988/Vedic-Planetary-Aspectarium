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

import os
import time
import json
from datetime import datetime
from pathlib import Path

class TempDir:
    _instance = None
    _path_file = Path(__file__).parent / 'init.json'

    def __new__(cls):
        if cls._instance is None:
            if cls._path_file.exists():
                with open(cls._path_file, 'r') as file:
                    path_data = json.load(file)
                    tempDir = Path(path_data['tempDir'])
            else:
                now = datetime.now()
                time_str = now.strftime('%Y-%m-%d-%H-%M-%S')
                tempDir = Path.home() / '.astro_data_temp' / time_str
                tempDir.mkdir(parents=True, exist_ok=True)
                with open(cls._path_file, 'w') as file:
                    json.dump({'tempDir': str(tempDir)}, file)

            cls._instance = super(TempDir, cls).__new__(cls)
            cls._instance._tempDir = tempDir
        return cls._instance

    @property
    def tempDir(self):
        return self._tempDir

def init():
    path = Path(__file__).parent / 'init.json'
    if path.exists():
        os.remove(path)
        print('Data initiating...')
        time.sleep(1)
        print('Data initiated.')
    else:
        pass

settingFileObj = TempDir()
settingFile = Path(settingFileObj.tempDir) / 'settings.json'
