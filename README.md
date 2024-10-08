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
**Vedic Planetary Aspectarium** is a Python-based application designed to assist the Vedic/Hindu astrology community in easily calculating and assessing planetary aspects.

## What it does?
- Enables users to easily calculate `Sputa Drishti` in both directions (i.e., natal planets aspecting transit planets and transit planets aspecting natal planets).
- Presents the values of `drishtis` in a tabular format.
- Shows two charts side by side, available in both `North` and `South` Indian styles.
- Can works on every major operating systems.

## News
### Release 0.0.0.1 (Oct 2024)
- The capability to display North Indian style charts (both natal and transit) in a single window has been introduced, replacing the previous separate windows.
- The application now utilizes the `darkdetect` library to generate North Indian style charts, allowing it to automatically switch between light and dark themes if the user changes the operating system theme while using the app.
- A new script, `dataDelete.py`, has been added, enabling users to easily remove all temporary and residual files after running the application.

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
> [!WARNING]
> On macOS, avoid using the pre-installed version of `Python`.
- Instead, follow this [guide](https://www.freecodecamp.org/news/python-version-on-mac-update/) to install `Python` using `Homebrew` and `pyenv`.
- `Homebrew` and `pyenv` will allow you to easily manage different `Python` versions on your system.

#### Linux
> [!TIP]
> Most major GNU/Linux distros come with `Python` pre-installed. However, in many cases, you may need to use `python3` instead of `python` when running Python scripts.

### PyQt6 and darkdetect
Once you have installed `Python`, you can install `PyQt6` and `darkdetect` using `pip`. Enter the following command in your `Terminal` app (on macOS and Linux) or `PowerShell` (on Windows).
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
cd <directory>/VPA/
```
Replace the `<directory>` part with the directory path where you want to store the `VPA's` scripts. For example: my desktop directory path is `~/Desktop/`.

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

- After downloading the GitHub repository and creating your `*.txt` files, run the `dataInput.py` script using one of the following commands:
```python
python path/to/your/directory/VPA/dataInput.py
```
or
```python
python3 path/to/your/directory/VPA/dataInput.py
```
- After the data input window appears, load your `*.txt` files accordingly.

<img src="https://i.imgur.com/XR5ACMj.png" alt="User inputs of Maitreya charts data." style="width:520px;"/>

- If everything is correct, you will see a message box like this:

<img src="https://i.imgur.com/2YCaZhT.png" alt="Data calculated and passed." style="width:600px;"/>

- If there is an issue with the data inputs, you will see a message box like this:

<img src="https://i.imgur.com/CqDXWAF.png" alt="Data calculated and failed." style="width:600px;"/>

- If you see the error message, check your input files and try again.

- After clicking 'Continue', you will see the following window:
<img src="https://i.imgur.com/d519CtU.png" alt="Data table window" style="width:600px;"/>

In this table, the rows represent the aspecting planets, and the columns represent the aspected planets. You can switch between the `Natal to Transit Aspects` and `Transit to Natal Aspects` tabs.

The program can remember the last input data. Even after closing the `Aspect Table Window`, you can reopen it without restarting the program from the beginning. Run the following command to display the data table again:
```python
python path/to/your/directory/VPA/dataTable.py
```
If you want to see your natal and transit charts in North or South styles, run one of these following command:
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
> That script will delete all the previouly saved data. If you want to backup your calculations, then DO NOT RUN that script.

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

## Important notes

> [!TIP]
> In the upcoming sub-sections and paragraphs, I will explain the detailed technical issues surrounding the calculation of planetary aspects and 'Sputa Drishti'. These topics can be highly complex and sometimes involve subjective opinions.
> The detailed explanations might be exhausting and confusing for some readers.
> Therefore, if you are not interested in the technical nitty-gritty, feel free to skip ahead to the [TLDR;: Conclusion](#tldr-conclusion) section.

### Aspect Method

> [!NOTE]
> In this section, I will discuss about a couple of methods for calculating planetary aspects.

<details>
<summary>READ MORE.</summary>
<br />

Before using `VPA`, please be aware that the current version employs what I call the **`Alternative Method`** for calculating planetary aspects. The key difference between the `Traditional Method` and the `Alternative Method` lies in how retrograde planets (including `Rahu` and `Ketu`) create aspects with other planets. In the `Alternative Method`, the assumption is that planets can only aspect planets that are ahead of them in their path (i.e., they cannot see backward). If a planet is moving in normal motion, it can only aspect those with a higher degree. Conversely, if a planet is in retrograde motion, it can only aspect those with a lower degree.

For example, consider a scenario where `Planet A` is a fast-moving planet and `Planet B` is a slow-moving planet. If A is in `Scorpio` and B is in `Taurus`, their aspect is strong as they move towards each other. Once A completes a full 60 virupas aspect to B, it moves away and stops aspecting B. Later, when A is in `Libra`, its 7th aspect point is in `Aries`. If A starts moving normally again and re-enters `Scorpio`, it makes a 7th aspect to B once more. Initially, A aspected B from the front side, and upon returning, it aspects B from the back side. From B’s perspective, A first aspected it from the front and later from the back.

In the `traditional method`, even if Planet A aspects Planet B twice in similar scenarios, it always aspects B from the back side, never making a face-to-face aspect. Prominent Vedic astrologers like `Prof. K.S. Krishnamurti` emphasized that aspects made by retrograde planets are stronger than those made by planets in normal motion. This is why I believe this method of calculating aspects is more logical than traditional methods.

Another example involves planets with special aspects. If `Mars` is in `Scorpio` and `Planet A` is in `Leo`, the `traditional method` suggests no aspect between them. However, using the `alternative method`, `Mars` aspects `Planet A` via its `4th` special aspect. When `Mars` returns to normal motion, its `7th` or `8th` aspects fail to aspect `Planet B`. Whether an aspect exists or not can significantly impact predictions.

I believe more research is needed in this area. Classical Vedic treatises like BPHS, Brihat Jataka, Saravali, Phaladeepika, and Jataka Parijata do not mention the `alternative method`, to the best of my knowledge. If the topic was mentioned in these classics, then **I apologize for any shortcomings in my understanding**.

</details>

### Types of Drishtis

> [!NOTE]
> In this section, I will share my perspective on the different types of Drishtis.

<details>
<summary>READ MORE.</summary>
<br />

There are three types of Drishtis:
- `Rasi Drishti`
- `Graha Drishti`
- `Sputa Drishti`

Let me share my understanding of these drishtis, but please remember that this is just my **personal opinion**, so take it with a grain of salt.

Imagine you’re a marketing executive at a local market, and your CEO who is managing the global operation sends out a memo regarding a new product launch. This memo may cover various issues, such as coordinating production with the production team, budgeting for the launch campaign with the finance team, and, of course, discussing about the marketing campaign with you and your team. The instructions may be quite broad, and the CEO likely has many other priorities to address. To me, this represents `Rasi Drishti.`

Now, let's discuss `Graha Drishti`. Picture receiving a memo from your regional director. This memo should be much more specific than the one from your CEO, focusing on details only relevant to your local market. In my view, this aligns with `Graha Drishti.`

Finally, what about Sputa Drishti? Imagine receiving instructions from your department head or marketing manager. They would outline what you need to do in the next few days. If the launch campaign involves exhibition events, you might need to coordinate with venue owners. If it runs on digital media, you might need to meet with key opinion leaders (KOLs). As your direct supervisor, you should pay close attention to their instructions. This, for me, represents Sputa Drishti.

At the end of the day, every marketing professional has their own unique approach. Some may lean more towards digital marketing, while others focus on promotions or emphasize omnichannel strategies. The same can be said for planets; each has its own personality (karakas) and dignities, such as friendships with aspecting planets (e.g., Naisargika Mitra or Tatkalika Mitra) and signs (e.g., Moolatrikona or Uccha). They also have specific duties and responsibilities related to their houses. We must take these factors into account when assessing the effects of Drishtis.

</details>

### Controvery around Jupiter's special aspects

> [!NOTE]
> In this section, I will discuss the various methods for calculating Jupiter's special aspects as found in different sources.

<details>
<summary>READ MORE.</summary>
<br />

Many Hindu astrologers, as well as Vedic astrology books and software, often overlook `Sputa Drishti.` I believe this is due to issues in the BPHS. In BPHS, the calculation for Sputa Drishti is somewhat _controversial_, especially for `Jupiter` and `Mars`.

There are two English translations of BPHS available online: one by `Shri R. Santhanam` and the other by `Girish Chand Sharma`. I have read both, and they translate the relevant sections in a similar manner.

> 12: SPECIAL CONSIDERATION FOR JUPITER'S ASPECTS.. 
> Deduct the longitude of Jupiter from that of the planet aspected by him. If the resultant sum is 3 Rasis & c or 7 Rasis & c, halve the degrees etc. (ignoring Rasis) and increase it by 45.
> If the sum is 4 Rasis & c or 8 Rasis & c, the degrees etc. (ignoring Rasis) be subtracted from 60.
> This will be the aspectual value. The sum being in conformity with others than these be treated as stated earlier. <br />
> _**Chapter 26 : p.g. 256**_<br />
> _**BPHS Vol. I translated by Shri R. Santhanam**_

> 12-13. SPECIAL CONSIDERATION FOR THE ASPECTS OF JUPITER:
> If after deducting the Longitude of Jupiter from that of the aspected planet the remainder is 3 or 7 signs, then the half of the degrees etc. is to be added to 45;
> and if the remainder is 4 or 8 then degrees etc. are deducted from 60 and this will be the Sphuta Drishti or Aspectual Value of Jupiter (on the given House or planet).
> If the remainder is some other number of sign, then the Aspectual Value is to be known in the manner described above.
> In the same way is stated the Aspectual Value of the Sun and the other planets. The effects of the Houses should be predicted according to this Aspect.
> Notes: The Sage has told us the method of knowing the Aspectual Value of Jupiter through a special process.
> \1. Deduct the longitude of Jupiter from that of the Aspected planet. If the difference is between three or four, or 7 or 8, then the signs are ignored and degrees etc. are halved and 45 is added to it. This will be the Aspectual Value.
> \2. If the difference is between 4 or 5 or 8 or 9 signs, then the signs are ignored and degrees are deducted from 60 to get the Aspectual Value.
> \3. If the difference comes to be other signs than the above mentioned ones, then the Aspectual Value is found out as per Slokas 6 to 8.<br />
> _**Chapter 28 : p.g. 375**_<br />
> _**BPHS Vol. I translated by Girish Chand Sharma**_

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

</details>

### The issue surrounding the Mars' 6th rasi aspect

> [!NOTE]
> In this section, I will discuss the different methods for calculating Mars' 6th rasi aspect as presented in various sources.

<details>
<summary>READ MORE.</summary>
<br />

Regarding Mars' 6th rasi aspect, there are two interpretations of the original Sloka. Both English translations interpreted the term `6th signs` as `exactly 180 degrees.` However, the authors of Maitreya and the unknown document interpreted it as the `entire full 30 degrees` of the 6th rasi.

Personally, I find the latter interpretation less convincing. Since all planets can form a 6th rasi aspect, why should Mars be treated differently? To my knowledge, the concept of special aspects originates from a planet's orbit being outside Earth's orbit. Planets orbiting the Sun within Earth's orbit do not have special aspects, whereas those orbiting outside do. Given that Jupiter and Saturn do not gain a `full 1 rupa aspect` simply by entering a rasi, Mars should not be treated differently.

Therefore, in current release of `VPA`, I followed the value given by both English translations of BPHS, where Mars only gets a `1 rupa aspect` at an `exact 180-degree` angular distance. The rest of the degrees between 180 and 210 are treated the same as for any other planet.

</details>

### Problem with Sputa Drishti tables from English transalations of BPHS

> [!NOTE]
> In this section, I will discuss about the issues of Sputa Drishti tables from English transalations of BPHS

<details>
<summary>READ MORE.</summary>
<br />

Both English translations of BPHS include a table for easier calculation of Sputa Drishti (found on `page 258` in `Shri R. Santhanam's` translation and on `page 377` in `Girish Chand Sharma's` translation).

The idea behind this table is that each planet has the same base formulas for calculating Sputa Drishti. For instance, if a planet has an angular distance of 50 degrees, the formula is `(Angular distance - 30) / 2`. If the angular distance is 80 degrees, the formula is `(Angular distance - 45)`.

After calculating all the planets' angular distances, the following rules should be applied:

1. If Mars is between 90 and 120 degrees or between 210 and 249 degrees, add 15 to the previous value. For example, if Mars is at 100 degrees, the general formula for `90 - 120 degrees` is `30 + (120 - angular distance) / 2`. Thus, `30 + (120 - 100) / 2` is `40 Virupas`. Adding 15 results in a final value of `55 Virupas`.
2. If Jupiter is between 120 and 150 degrees or between 240 and 270 degrees, add 30 to the previous value.
3. If Saturn is between 60 and 90 degrees or between 270 and 300 degrees, add 45 to the previous value.

The authors of both English translations of BPHS calculated all the degrees for the base formulas and presented the values in a table, such as `100.00 = 40.00`. You need to look up your angular distance in that table and add the extra value if necessary.

While this table is useful for planets without special aspects (i.e., Sun, Moon, Mercury, and Venus) and for handling normal aspect degrees of planets with special aspects (e.g., 150 - 180 degrees for all planets with special aspects), it is not helpful for dealing with the special aspects of planets with special aspects. Consequently, the three rules mentioned above do not make sense.

To illustrate further, let’s revisit rule 1(i.e., Mars' rule). BPHS states that if Mars is at 100 degrees, we need to use this rule: `45 + (angular distance - 90) / 2`. So `45 + (100 - 90) / 2` equals 50 virupas. As you can see, the table provides an incorrect value. In some cases, it gives virupa values exceeding 60.

In conclusion, avoid using these tables as their results are unreliable. One thing you can do is the cross-referencing with the table provided in [the unknown document](https://www.scribd.com/doc/278613179/Graha-Drishti-pdf) (on `page 333`). However, be aware that this table also has issues with Mars' 6th rasi aspect.

</details>

### TLDR;: Conclusion

> [!IMPORTANT]
> If you skipped the above sub-sections and paragraphs, please read this section carefully.

In the current release of `VPA`:
- I opted to use what I refer to as the `Alternative Method` for calculating planetary aspects.
  - The primary distinction between the `Alternative Method` and the `Traditional Method` is that the `Alternative Method` assumes planets in retrograde motion make their aspects backward, while planets in direct motion make their aspects forward. In the `Traditional Method`, planets always make their aspects forward regardless of their motion.
- For Jupiter's special aspects in the calculation of `Sputa Drishti`, I adopted the method from the above mentioned `Unknown Document` I found online.
  - Although I don't know the author or title of this document, I found its explanation of `Sputa Drishti` to be superior to any other sources I reviewed. So, I chose its method.
- For Mars' 6th rasi aspect in the calculation of `Sputa Drishti`, I followed the method provided in the English translations of BPHS.
    - The method mentioned in the [Maitreya's webpage](https://saravali.github.io/astrology/drishti_sputa.html) and the [unknown document](https://www.scribd.com/doc/278613179/Graha-Drishti-pdf) assign a full 60 virupas strength to Mars' aspect regardless of its degree in the 6th rasi. I don't think that is a logical method.

> [!NOTE]
> I'm not sure who authored this unknown document, so please let me know if you have any information about the author or the document's title, so I can give proper credit.

> [!TIP]
> While I have selected my preferred methods for calculating planetary aspects and `Sputa Drishti` in this release, I plan to add options in future releases for users to choose their preferred methods of calculation.

## How to interpret the Sputa Drishti Data Table

The data table window includes two tabs: `Natal to Transit Aspects` and `Transit to Natal Aspects`. The `Natal to Transit Aspects` tab displays the aspect values of natal planets aspecting transit planets, while the `Transit to Natal Aspects` tab shows the aspect values of transit planets aspecting natal planets. The maximum aspect value is `60 virupas`, with higher values indicating stronger aspects.

In these tables, the rows represent the aspecting planets and the columns represent the aspected planets. Planets with physical bodies (`Sun`, `Moon`, `Mars`, `Mercury`, `Jupiter`, and `Venus`) can form aspects, while bodiless points (`Rahu`, `Ketu`, and `Ascendant`) cannot create aspects.

<img src="https://i.imgur.com/d519CtU.png" alt="Data table window" style="width:600px;"/>

In above example, `Natal Saturn` aspects transit `Sun`, `Moo`, `Mer`, `Jup`, `Rah`, and `Ket` with strong aspects.

## Tasks

Here is the list of tasks that need to be done before updating the `VPA` to version 0.0.0.2.

- [ ] Add JHora Data Input and Manual Data Input
- [ ] Add East Indian style chart
- [ ] Add option to choose aspects calculation methods
- [ ] Add option to choose Sputa Drishti methods
- [ ] Revamp the North Indian style chart
- [ ] Add Graha Drishti tables
- [ ] Do more testing on Windows and Ubuntu

## FAQs

**Q: How can I help the project?**

A: One of the best ways to support an open-source project like this is to use the application, integrate it into your workflow, and enjoy it. You can also provide suggestions for improvement and share feedback about your experience. Spreading the word in your community is invaluable since 'word of mouth' is the most effective form of marketing. If you write books, articles, or blog posts on Vedic astrology, include screenshots of the application and discuss your experience with it. Additionally, you can contribute by writing documentation on its features, how you customized it for tasks beyond its original scope, and your views on planetary aspects and various drishtis. Sharing your methods of evaluation these would also be beneficial. As a hobbyist, I welcome pull requests from those proficient in programming. All I ask is that you share your code back with the community, as the application is licensed under GPL v3. I appreciate the opportunity to learn from you all. Ultimately, I am doing this project to contribute to the community, not for fame or financial gain. So, enjoy it.

**Q: Can I request features?**

A: Yes, you can. You can set up an issue on GitHub and discuss it there. While I can't promise that I will implement every request, I will certainly consider them. I am continuously improving the application, so we may eventually get to your requested features.

**Q: What is the future of VPA?**

A: Jagannatha Hora and Maitreya have been invaluable tools for me, and I am profoundly thankful to their creators. However, I faced some challenges integrating these softwares into my workflow. JHora has all the features I need, but it is only compatible with Windows, while I mainly use macOS. Maitreya can display transit planets' aspects to natal planets and their strength (such as 1/4, 1/2, 3/4, and full strength). However, it shows this information through charts and arrows, requiring you to hover your mouse and press <kbd>Ctrl</kbd> or <kbd>Shift</kbd> to view the aspects, which is not very intuitive. Unlike JHora, it can only create an aspectarium for planets within the same chart, not for planets aspecting from another chart. While softwares like 'Parashara's Light' and 'Kala' are feature-rich, they are proprietary and require license fees.

My initial goal for this project was to create something that enhances my workflow. Now, we have a tool that can easily calculate aspects between planets in different charts and works on all major operating systems. This small step has already improved my workflow.

For the future of the project, I plan to incorporate more useful information related to Gocharaphala. This includes details like planets' dignities, Vedhanka points, Ashtakavarga Bindus points, Shadbala, dasa lords, and more. My goal is to develop a system that presents all the necessary information at a glance when analyzing Gocharaphala. The ability to print this information on physical paper would be an added bonus. I understand that achieving these goals will take time, but I am committed to the process.

## About me
I'm not a professional software developer or Vedic astrologer; I'm simply a hobbyist with an interest in both areas. Professionally, I am a marketing specialist with a background in media and advertising. Currently, I am working on my thesis for a master's degree in marketing, digital marketing, and marketing analysis.
