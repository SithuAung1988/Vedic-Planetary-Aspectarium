<!--
 Vedic Planetary Aspectarium (Version 0.0.0.1)
 
 Copyright (C) 2024 Sithu Aung <https://github.com/SithuAung1988>
 
 This file is part of Vedic Planetary Aspectarium.
 
 Vedic Planetary Aspectarium is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.
 
 Vedic Planetary Aspectarium is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
 
 You should have received a copy of the GNU General Public License
 along with Vedic Planetary Aspectarium.  If not, see <https://www.gnu.org/licenses/>.
-->

# Vedic Planetary Aspectarium

## What it is?
'Vedic Planetary Aspectarium' is a supplimentary application written in Python for [Maitreya](https://saravali.github.io/) program, which is an Open Source platform for Vedic and western astrology.

## What it does?
- Can calculate 'Sputa Drishti' both ways easily (i.e., natal planets aspecting transit planets and transit planets aspecting natal planets).
- Display values of drishti as a table.
- Diplay two charts side-by-side both in North and South Indian styles.

## News
### Release 0.0.0.1 (Oct 2024)
- The ablity to display North Indian style charts (both natal and transit) in a sigle window is added. Previously separate windows.
- The 'darkdetect' library is used to build North Indian style charts. So application now has the ablity to swicth between light and dark themes automatically if user has changed the operating system theme while using the application.
- The 'dataDelete.py' was added. So users can now easily delete all the temporary and residual files after running the app.

## Prerequisites
I wrote and tested this application by using these softwares, fonts, tools and libraries. (Oct 2024)
- macOS 14.6.1
- [Maitreya (8.1)](https://saravali.github.io/)
- [Python (3.12.6)](https://www.python.org/)
- [PyQt6 (6.7.1)](https://pypi.org/project/PyQt6/)
- [darkdetect (0.8.0)](https://github.com/albertosottile/darkdetect/releases)
- [Roboto Mono font](https://fonts.google.com/specimen/Roboto+Mono)

### Maitreya
- Download the appropriate version of `Maitreya` software for your system and follow the instructions given on the '[Download](https://saravali.github.io/download.html)' page.

### Python

**Windows**
- To install `Python` on Windows via `winget`, open `PowerShell`. Then, run the following command to see the available `Python` versions.
```sh
winget search Python.Python
```
- Once you find the desired version, use the command `winget install` followed by the version's ID to install it. For example, for `version 3.12.6`, run:
```sh
winget install Python.Python.3.12.6
```
`winget` will provide you the easier way to update and maintain your Windows softwares.

**macOS**
- On macOS, don't use the pre-installed version of `Python` since this application uses `Python 3`.
- Instead follow this [guide](https://www.freecodecamp.org/news/python-version-on-mac-update/) to install `Python` via `Homebrew` and `pyenv`.
- [`Homebrew`](https://brew.sh/) will help you keep up-to-date your `Python` version.
- [`pyenv`](https://github.com/pyenv/pyenv) will let you easily manage various `Python` versions on your system.

**Linux**
- Almost every major GNU/Linux distributions includes `Python` as default.
- But in most cases, you may need to use `python3` instead of `python` when runnning the Python scripts.

### PyQt6 and darkdetect
- After you have installed Python 3, install 'PyQt6' and 'darkdetect' via pip.
- Type the following code in your 'Terminal' app (on macOS and Linux) or 'PowerShell' (on Windows).
```sh
pip install PyQt6 darkdetect
```

### Roboto Mono
- Download the font from [Google Fonts](https://fonts.google.com/specimen/Roboto+Mono) and install it.

## Using 'VPA' for the first time
After finished installing all the prerequisites:

Run the `Maitreya` application with default settings.
> [!CAUTION]
> Possible negative outcomes resulting from an action.


<!--
As far as I know, major both open source and free (free as in beer) vedic / jyotish software such as Maitreya and Jagannatha Hora cannot perform calculation and displaying planetary aspect (angular distances between planets) information between two charts such as between natal chart and transit chart or between natal chart and Tajaka chart, etc.
Although there is a way to see natal and transit chart side by side in JHora, it just simply display two charts and not much useful for my use cases.


At current stage, 
-->
