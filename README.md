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

### PyQt6 and darkdetect
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
  A("Generational")
  B("Patches")
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
    H(["Feature"])
    I(["Internal"])
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

## Important Notes

### Aspect Method

> [!WARNING]
> This section is very important. You must read it carefully before using `VPA`.

Before using `VPA`, please be aware that the current version employs what I call the `**Alternative Method**` for calculating planetary aspects. The key difference between the `Traditional Method` and the `Alternative Method` lies in how retrograde planets (including `Rahu` and `Ketu`) create aspects with other planets. 

In the `Alternative Method`, the assumption is that planets can only aspect planets that are ahead of them in their path (i.e., they cannot see backward). If a planet is moving in normal motion, it can only aspect those with a higher degree. Conversely, if a planet is in retrograde motion, it can only aspect those with a lower degree.

I come from a long line of Vedic astrologers. According to our oral tradition, my ancestors migrated from India to Burma in the early 18th century and served as astrologers in the Burmese royal court, advising many kings and princes. This method of calculating planetary aspects has been passed down through generations within my family. It has been tested repeatedly and found to be more reliable than the `traditional method`, which is why I am committed to preserving this tradition.

For example, consider a scenario where `Planet A` is a fast-moving planet and `Planet B` is a slow-moving planet. If A is in `Scorpio` and B is in `Taurus`, their aspect is strong as they move towards each other. Once A completes a full 60 virupas aspect to B, it moves away and stops aspecting B. Later, when A is in `Libra`, its 7th aspect point is in `Aries`. If A starts moving normally again and re-enters `Scorpio`, it makes a 7th aspect to B once more. Initially, A aspected B from the front side, and upon returning, it aspects B from the back side. From B’s perspective, A first aspected it from the front and later from the back.

In the `traditional method`, even if Planet A aspects Planet B twice in similar scenarios, it always aspects B from the back side, never making a face-to-face aspect. Prominent Vedic astrologers like `Prof. K.S. Krishnamurti` (1902-1978) emphasized that aspects made by retrograde planets are stronger than those made by planets in normal motion. This is why I believe this method of calculating aspects is more logical than traditional methods.

Another example involves planets with special aspects. If `Mars` is in `Scorpio` and `Planet A` is in `Leo`, the `traditional method` suggests no aspect between them. However, using the `alternative method`, `Mars` aspects `Planet A` via its `4th` special aspect. When `Mars` returns to normal motion, its `7th` or `8th` aspects fail to aspect `Planet B`. Whether an aspect exists or not can significantly impact predictions.

I believe more research is needed in this area. Classical Vedic treatises like BPHS, Brihat Jataka, Saravali, Phaladeepika, and Jataka Parijata do not mention the `alternative method`, to the best of my knowledge. _I apologize for any shortcomings in my understanding_. However, given the long history of Vedic astrology, I do not believe my ancestors invented this method. Therefore, I refer to it as the `Alternative Method` to distinguish it from the `traditional method`.

> [!TIP]
> In a future release, I will provide an option for users to select between the `Traditional Method` and the `Alternative Method`. For now, if you prefer to use the `Traditional Method`, you can modify the `dataCompute.py` script by yourself. There is a function called `calculateDistance` and you can make your edit there.

### Types of Drishtis

> [!WARNING]
> Again this section is also very important. You must read it carefully before using `VPA`.

There are three types of Drishti:
- `Rasi Drishti`
- `Graha Drishti`
- `Sputa Drishti`

Let me share my understanding of these drishtis, but please remember that this is just my **personal opinion**, so take it with a grain of salt.

Imagine you’re a marketing executive at a local market, and your CEO sends out a memo regarding a new product launch. This memo may cover various issues, such as coordinating production with the production team, budgeting for the launch campaign with the finance team, and, of course, discussing about the marketing campaign with you and your team. The instructions may be quite broad, and the CEO likely has many other priorities to address. To me, this represents `Rasi Drishti.`

Now, let's discuss 'Graha Drishti.' Picture receiving a memo from your regional director. This memo should be much more specific than the one from your CEO, focusing on details relevant to your local market. In my view, this aligns with `Graha Drishti.`

Finally, what about 'Sputa Drishti'? Again, consider receiving instructions from your department head or marketing manager. Their marketing plan will include details on how to execute the 7Ps of marketing or how each stage of the marketing funnel should engage with consumers. As your direct supervisor, you should pay close attention to their instructions. This, for me, embodies `Sputa Drishti.`

At the end of the day, every marketing professional has their own unique approach. Some may lean more towards digital marketing, while others focus on promotions or emphasize omnichannel strategies. The same can be said for planets; each has its own personality (karakas) and dignities, such as friendships with aspecting planets (Naisargika Mitra or Tatkalika Mitra) and signs (Moolatrikona or Uccha). They also have specific duties and responsibilities related to their houses. We must take these factors into account when assessing the effects of Drishtis.

Many Hindu astrologers, as well as Vedic astrology books and software, often overlook `Sputa Drishti.` I believe this is due to issues in the BPHS. In BPHS, the calculation for Jupiter's special Sputa Drishti is somewhat _controversial_.

There are two English translations of BPHS available online: one by `Shri R. Santhanam` and the other by `Girish Chand Sharma`. I have read both, and they translate the relevant sections in a similar manner.

> 12. SPECIAL CONSIDERATION FOR JUPITER'S ASPECTS.. Deduct the longitude of Jupiter from that of the planet aspected by him. If the resultant sum is 3 Rasis & c or 7 Rasis & c, halve the degrees etc. (ignoring Rasis) and increase it by 45. If the sum is 4 Rasis & c or 8 Rasis & c, the degrees etc. (ignoring Rasis) be subtracted from 60. This will be the aspectual value. The sum being in conformity with others than these be treated as stated earlier.<br>
_**Chapter 26 : p.g. 256**_<br>
_**BPHS Vol. I translated by Shri R. Santhanam**_

> 12-13. SPECIAL CONSIDERATION FOR THE ASPECTS OF JUPITER: If after deducting the Longitude of Jupiter from that of the aspected planet the remainder is 3 or 7 signs, then the half of the degrees etc. is to be added to 45; and if the remainder is 4 or 8 then degrees etc. are deducted from 60 and this will be the Sphuta Drishti or Aspectual Value of Jupiter (on the given House or planet). If the remainder is some other number of sign, then the Aspectual Value is to be known in the manner described above.
> In the same way is stated the Aspectual Value of the Sun and the other planets. The effects of the Houses should be predicted according to this Aspect
> Notes: The Sage has told us the method of knowing the Aspectual Value of Jupiter through a special process.
> 1. Deduct the longitude of Jupiter from that of the Aspected planet. If the difference is between three or four, or 7 or 8, then the signs are ignored and degrees etc. are halved and 45 is added to it. This will be the Aspectual Value.
> 2. If the difference is between 4 or 5 or 8 or 9 signs, then the signs are ignored and degrees are deducted from 60 to get the Aspectual Value.
> 3. If the difference comes to be other signs than the above mentioned ones, then the Aspectual Value is found out as per Slokas 6 to 8.<br>
_**Chapter 28 : p.g. 375**_<br>
_**BPHS Vol. I translated by Girish Chand Sharma**_

I even went through `Dr. Suresh Chandra Mishra's` Hindi translation, even though I don't understand Hindi. I used Google Translate to help me with that. You can find the book on [archive.org](https://archive.org/details/brihat-parashar-hora-shastra-vol-2-suresh-chandra-mishra). Although it is labeled as Volume 2, it is actually Volume 1. Despite my extensive efforts, I was unable to locate the chapter discussing `Sputa Drishti.` It appears that `Dr. Suresh Chandra Mishra` did not translate that entire chapter.

I also came across some information about `Sputa Drishti` on [Maitreya's webpage](https://saravali.github.io/astrology/drishti_sputa.html), which presents a very different calculation for Jupiter's special aspects compared to the aforementioned English translations. While the calculations for the `3rd` and `7th` rasis are consistent, the calculations for the `4th` and `8th` rasis differ significantly.

Both English translations indicate:
- For the `4th` rasi: $$60 - (\text{angular distance} - 120)$$
- For the `8th` rasi: $$60 - (\text{angular distance} - 240)$$

In contrast, Maitreya's calculations suggest:
- For the `4th` rasi: $$2 \cdot (150 - \text{angular distance})$$
- For the `8th` rasi: $$15 + \left(2 \cdot \frac{270 - \text{angular distance}}{3}\right)$$

[Another document](https://www.scribd.com/doc/278613179/Graha-Drishti-pdf) I found online proposed different calculations:
- For the `4th` rasi: $$60 - \left(2 \cdot (\text{angular distance} - 120)\right)$$
- For the `8th` rasi: $$15 + \left(1.5 \cdot \left(30 - \left(\text{angular distance} - 240\right)\right)\right)$$

In my view, [the unknown document](https://www.scribd.com/doc/278613179/Graha-Drishti-pdf) I discovered online provides the clearest explanation of `Sputa Drishti,` and I prefer its interpretation over the others. However, this is just my **subjective opinion**.

In the current version of `VPA,` I adopted the method of the unknown document which I referred to as the `Alternative Method.`

> [!NOTE]
> I'm not sure who authored this unknown document, so please let me know if you have any information about the author or the document's title, so I can give proper credit.

A


To summarize, all the documents I have reviewed agree on the calculations for all drishtis except for Jupiter's 4th and 8th special drishtis:
- Both `English translations` are in agreement, but `Maitreya/Saravali's` calculations and the `Unknown Document's` calculations diverge for both the `4th` and `8th` rasis.
- `Maitreya/Saravali's` calculations and the `Unknown Document's` calculations align on the `4th` rasi but disagree on the `8th`. They are in agreement regarding the other drishti calculations.
- In this release of `VPA,` I opted to use the calculation from the Unknown Document because I believe it provide a better explanation of drishtis than the others.

> [!TIP]
> Although I prefer the `Alternative Method` for calculating `Sputa Drishti` as outlined in the `unknown document`, I plan to include an option for users to select different calculation methods in future releases.

## How to interpret the Sputa Drishti Data Table

The data table window includes two tabs: `Natal to Transit Aspects` and `Transit to Natal Aspects`. The `Natal to Transit Aspects` tab displays the aspect values of natal planets aspecting transit planets, while the `Transit to Natal Aspects` tab shows the aspect values of transit planets aspecting natal planets. The maximum aspect value is `60 virupas`, with higher values indicating stronger aspects.

In these tables, the rows represent the aspecting planets and the columns represent the aspected planets. Planets with physical bodies ('Sun', 'Moon', 'Mars', 'Mercury', 'Jupiter', and 'Venus') can form aspects, while bodiless points ('Rahu', 'Ketu', and 'Ascendant') cannot create aspects.

<img src="https://i.imgur.com/d519CtU.png" alt="Data table window" style="width:600px;"/>

In above example, `Natal Saturn` aspects transit `Sun`, `Moo`, `Mer`, `Jup`, `Rah`, and `Ket` with strong aspects.

## Credit


































