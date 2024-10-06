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
- Enables users to easily calculate 'Sputa Drishti' in both directions (i.e., natal planets aspecting transit planets and transit planets aspecting natal planets).
- Presents the values of drishti in a tabular format.
- Shows two charts side by side, available in both North and South Indian styles.

## News
### Release 0.0.0.1 (Oct 2024)
- The capability to display North Indian style charts (both natal and transit) in a single window has been introduced, replacing the previous separate windows.
- The application now utilizes the 'darkdetect' library to generate North Indian style charts, allowing it to automatically switch between light and dark themes if the user changes the operating system theme while using the app.
- A new file, 'dataDelete.py', has been added, enabling users to easily remove all temporary and residual files after running the application.

## Prerequisites
I developed and tested this application using the following software, fonts, tools, and libraries. (Oct 2024)
- macOS 14.6.1
- [Maitreya (8.1)](https://saravali.github.io/)
- [Python (3.12.7)](https://www.python.org/)
- [PyQt6 (6.7.1)](https://pypi.org/project/PyQt6/)
- [darkdetect (0.8.0)](https://github.com/albertosottile/darkdetect/releases)
- [Git (2.46.2)](https://git-scm.com/)
- [Roboto Mono font](https://fonts.google.com/specimen/Roboto+Mono)

### Maitreya
- Download the appropriate version of `Maitreya` software for your system and follow the instructions given on the '[Download](https://saravali.github.io/download.html)' page.
- Please make sure `Saravali.ttf` is properly installed.

### Python
#### Windows
To install `Python` on Windows using `winget`, open `PowerShell` and execute the following command to view the available `Python` versions:
```sh
winget search Python.Python
```
After identifying the version you want, use the command `winget install` followed by the version's ID to install it. For instance, to install version `3.12.7`, run:
```sh
winget install Python.Python.3.12.7
```
Using `winget` makes it easier to update and manage your Windows software.

#### macOS
> [!CAUTION]
> On macOS, avoid using the pre-installed version of `Python`, as this application requires `Python 3`.
- Instead, follow this [guide](https://www.freecodecamp.org/news/python-version-on-mac-update/) to install `Python` using `Homebrew` and `pyenv`.
- `Homebrew` and `pyenv` will allow you to easily manage different `Python` versions on your system.

#### Linux
> [!TIP]
> Most major GNU/Linux distros come with `Python` pre-installed. However, in many cases, you may need to use `python3` instead of `python` when running Python scripts.

#### PyQt6 and darkdetect
Once you have installed `Python 3`, you can install `PyQt6` and `darkdetect` using `pip`. Enter the following command in your `Terminal` app (on macOS and Linux) or `PowerShell` (on Windows).
```sh
pip install PyQt6 darkdetect
```

### Git
#### Windows
Just like with Python, you can use `winget` to install `Git` on Windows. Execute the following command in `PowerShell`:
```sh
winget install --id Git.Git -e --source winget
```

#### macOS
> [!WARNING]
> Similar to Python, it is best to avoid using the pre-installed version of `Git`, as it may be quite outdated.  
- You can install `Git` on your system using `Homebrew`. To do so, run the following command:  
```sh
brew install git
```

#### Linux
> [!TIP]
> Most major GNU/Linux distros include `Git` pre-installed. If it is not available on your system, you can install `Git` from your distro's official software repositories using tools like `apt` or `dnf` or `pacman`.

### Roboto Mono
- On Windows and Linux, download the font from [Google Fonts](https://fonts.google.com/specimen/Roboto+Mono) and install it.
- On macOS, you can use Homebrew to install the font.
```sh
brew install --cask font-roboto-mono
```

## Using 'VPA' for the first time
> [!NOTE]
> I won’t be explaining how to use `Maitreya` here. Please consult its [documentation](https://saravali.github.io/documentation.html) if you need guidance on how to use it. I will only cover the essentials in this section.

After finished installing all the prerequisites:

- Clone the repo
```sh
git clone https://github.com/SithuAung1988/Vedic-Planetary-Aspectarium.git <directory>
cd <directory>
```
If you need help, read this article: [`git clone`](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository?tool=webui)
  
- Launch the `Maitreya` application with the following settings:
  - Include only the vedic 9 planets plus Ascendant.
  - You need to create data for two charts (e.g., natal and transit, or natal and Varshaphal).
  - Typically, when `Maitreya` starts, it automatically provides astrological data for the current time; however, you may need to adjust the *location information* in the `Configuration` beforehand.
  - On macOS, press <kbd>Cmd + N</kbd>, and on Windows and Linux, press <kbd>Ctrl + N</kbd> to create a new file. When the new window appears, press <kbd>B</kbd> to edit the horoscope data.
  - Modify the data as needed.
  - Right-click in the appropriate window and select the 'Export As ...' option from the context menu. You will need to do this for both charts.
  - Save these files as `*.txt`.

> [!TIP]
> You can name them anything you like. However, for the sake of simplicity, it is strongly recommended to use appropriate names such as `natal.txt` and `transit.txt`, or `kundali.txt` and `gochar.txt`.

<img src="https://i.imgur.com/emc97MY.png" alt="Data output from 'Maitreya" style="width:600px;"/>

Your example files should look like this:
```
    Longitude      D-9 Nakshatra 
-------------------------------------
Sun 17°22′19″ Vir  Gem Hasta     
Moo 03°57′55″ Lib  Sco Chitra    
Mar 22°21′58″ Gem  Ari Punarvasu 
Mer 20°00′22″ Vir  Can Hasta     
Jup 27°05′36″ Tau  Vir Mrigasira 
Ven 19°26′21″ Lib  Pis Swati     
Sat R19°56′25″ Aqu Pis Satabisha 
Rah 11°59′22″ Pis  Lib U.Bhadra  
Ket 11°59′22″ Vir  Ari Hasta     
Asc 11°59′34″ Cap  Ari Sravana   
```

After downloading the GitHub repository and creating your `*.txt` files, run the `dataInput.py` script using one of the following commands:
```python
python path/to/your/directory/VPA/dataInput.py
```
or
```python
python3 path/to/your/directory/VPA/dataInput.py
```
After the data input window appears, load your `*.txt` files accordingly.

<img src="https://i.imgur.com/XR5ACMj.png" alt="User inputs of Maitreya charts data." style="width:520px;"/>

If everything is correct, you will see a message box like this:

<img src="https://i.imgur.com/2YCaZhT.png" alt="Data calculated and passed." style="width:600px;"/>

If there is an issue with the data inputs, you will see a message box like this:

<img src="https://i.imgur.com/CqDXWAF.png" alt="Data calculated and passed." style="width:600px;"/>

If you see the error message, check your input files and try again.

After clicking 'Continue', you will see the following window:
<img src="https://i.imgur.com/d519CtU.png" alt="Data table window" style="width:600px;"/>

In this table, the rows represent the aspecting planets, and the columns represent the aspected planets. You can switch between the 'Natal to Transit Aspects' and 'Transit to Natal Aspects' tabs.

The program can remember the last input data. Even after closing the `Aspect Table Window`, you can reopen it without restarting the program. Run the following command to display the data table again:
```python
python path/to/your/directory/VPA/dataTable.py
```
If you want to see your natal and transit charts in sorth or south styles, run one of these following command:
```python
python path/to/your/directory/VPA/chartTableN.py
```

<img src="https://i.imgur.com/9QquqPd.png" alt="North Indian Chart" style="width:600px;"/>

or
```python
python path/to/your/directory/VPA/chartTableS.py
```

<img src="https://i.imgur.com/jEqhzXV.png" alt="South Indian Chart" style="width:600px;"/>

Once you finish, you can run the following script to cleanup all temporary data.
```python
python path/to/your/directory/VPA/dataDelete.py
```
> [!CAUTION]
> That script will delete all the saved data. If you want to backup your calculations, then DO NOT RUN that script.

## Version Number Scheme

This is how version number scheme works:

```mermaid
%%{init: {
  "flowchart": {
    "diagramPadding": 1,
    "padding": 0
  },
  "fontFamily": "monospace"
  } }%%
flowchart TD
subgraph Z[" "]
direction LR
  A 
  B
end
subgraph ZA[" "]
direction LR
    D("00#46;")
    E("00#46;")
    F("00#46;")
    G("00")
end
subgraph ZB[" "]
direction LR
    H(["Feature Upgrade"])
    I(["Internal Upgrade"])
end
D --> A
F --> B
H --> E
I --> G

classDef default fill:transparent,stroke:transparent,stroke-width:1px,padding:0px;
style A color: 4285F4;
style D color: 4285F4;
style F color: 34A853;
style B color: 34A853;
style H color: FBBC05;
style E color: FBBC05;
style I color: EA4335;
style G color: EA4335;
style Z fill:transparent,stroke:transparent,stroke-width:1px,padding:0px;
style ZA fill:transparent,stroke:transparent,stroke-width:1px,padding:0px;
style ZB fill:transparent,stroke:transparent,stroke-width:1px,padding:0px;
```

The first part in the version number represents generation of the application and will increases whenever Python or PyQt upgrade their versions. Since Python 3.x is not backward compatible with Python 2.x, and PyQt6 is not backward compatible with PyQt5, I want to avoid any confusion about which version users should run based on their preferred versions of Python and PyQt.

For this reason, I have implemented this versioning system. When I update my code to be compatible with Python 4.x or PyQt7, whichever comes first, I will also increment the first part of the version number.

The second part of the version number indicates the application's features and will increase whenever new features are added. For example, I plan to include `Jagannatha Hora` as a data source and add the ability to input planetary data manually in future releases. After implementing these upgrades, I will increment the second part of the version number.

The third part of the version number signifies bug fixes and patches. For instance, I am aware that the script for displaying the North Indian style chart is not very efficient. I wrote it this way to facilitate easier debugging, allowing me to work on the natal chart without affecting the transit chart code or vice vesa. Once I modify and improve this code, I will increase the third part of the version number.

The fourth part of the version number reflects internal improvements of the software. For example, I have already written the code for the East Indian style chart, but it has some rough edges that need polishing. Therefore, I decided not to include it in this release. Once I complete this functionality, I will add it to the new release and update the version number accordingly.



















