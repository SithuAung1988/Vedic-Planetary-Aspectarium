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

import shutil
import os
from pathlib import Path

def deleteDir(path: Path):
    try:
        shutil.rmtree(path)
        print(f'Directory <{path}> and its contents have been deleted.')
    except FileNotFoundError:
        print(f'The directory <{path}> does not exist.')
    except PermissionError:
        print(f'Permission denied: cannot delete <{path}>.')
    except Exception as e:
        print(f'An error occurred: {e}')

def deleteFile(path: Path):
    try:
        os.remove(path)
        print(f'\nThe file <{path}> has been deleted.')
    except FileNotFoundError:
        print(f'The file <{path}> does not exist.')
    except PermissionError:
        print(f'Permission denied: cannot delete <{path}>.')
    except Exception as e:
        print(f'An error occurred: {e}')

deleteFile(Path(__file__).parent / 'init.json')
deleteDir(Path(__file__).parent / '__pycache__')
deleteDir(Path.home() / '.astro_data_temp')