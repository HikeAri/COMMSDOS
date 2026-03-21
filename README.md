![COMMSDOS Banner](https://i.ibb.co/wZt7cjdN/COMMSDOSbanner.png)
# COMMSDOS for ORTHOS-1000B
### A program that simulates the DOS environment in the terminal where the main function is to encrypt and decrypt messages, but it's not limited to those only!
<i>[!] Disclaimer: The stock Python codes work on Windows machines only.</i><br>

Hi! I'm a novice programmer and this is the first big project I've ever made. This is a stupid but fun little project that I use as a medium to improve and maintain my programming skills. I started this project back in November 2025 and on the 20th of March 2026, I decided to give it a shot and release this project out in the public. [If you're interested, learn about the lore behind this!](#the-uninteresting-lore) <br>

### What you can do:
<ul>
  <li>Encrypt messages with 5 different EC channels (VDS, GDR, VDS-2, N2TE, S2TE)</li>
  <li>Auto or manual decrypt messages</li>
  <li>File and directory manipulation</li>
  <li>Run other compatible Python scripts within the DOS (like running a software!)</li>
  <li>Use or add additional commands (user-made or self-made command scripts)</li>
</ul>

### Samples included:
<ul>
  <li>Pynotes: A simple note-taking system for the COMMSDOS system</li>
  <li>Few ACT IPs and CT IDs</li>
  <li>Few encrypted and decrypted message logs</li>
  <li>Few simple executable 'softwares' that are mostly my Uni assignments lmao (located in `./floppy_disks`)</li>
  <li>One additional command script: Koi - The "fancy" file management system (unfinished)</li>
</ul><br>

## Usage Instructions
Please follow the instructions below carefully. Note that you can only use this stock program on Windows machines because it uses the Windows CMD syntax, unless you modify all the commands to your own OS terminal syntax.

#### 1. Download the repo ZIP file and extract all contents into your directory of choice.

#### 2. Download the `commsdos-dirpath-install`, which you can get it <a href="https://github.com/HikeAri/COMMSDOS/releases/tag/script-setup">here</a>

#### 3. PIP install all the required dependencies
```
pip install <package-name>
```
<ul>
  <li>datetime</li>
  <li>getpass</li>
  <li>playsound3</li>
  <li>tabulate</li>
</ul>

#### 4. Run the `commsdos-dirpath-install` (recommended to do inside the terminal)
This modifies the 'bootpath' file inside the COMMSDOS folder so that the DOS can read its directory path. All the required files are automatically created inside the directory that you set in 'bootpath' earlier.
```
cd <dirpath-where-you-have-the-file>
py commsdos-dirpath-install.py
```

#### 5. Follow the steps inside the script
<ol>
  <li>Type in the directory path where your COMMSDOS is located</li>
  <li>Choose the method for where you would want the necessary files to be created (Current path or type in the path of your choice)</li>
  <li>Setup a password to login to your COMMSDOS later</li>
  <li>Complete!</li>
</ol>

#### 6. Go to `./dos_storage_dir` inside your COMMSDOS folder and create a shortcut for `cmd_launch.bat`
Place the shortcut wherever you like (preferably where you can access it easily).<br>
( Optional, but recommended :D ) Right-click the shortcut and go to Properties, make it run in maximised window.<br>

### All done! You can actually just run the `sysbat.py` manually or `test.py` if you want to skip the BIOS and login sequence.<br><br>

## Contributions
Contributions are absolutely welcome! Either you want to improve the messy code structure, add other branches, add additional commands ([see here](#adding-extra-commands)), etc.
And yes, you can reuse the codes here in your projects if you want! There are no licenses whatsoever.<br><br>

## Adding extra commands & Creating the script
Coming soon twt<br><br>

## The (uninteresting) LORE
Coming soon twt<br><br>

## Credits & Resources
<a href="https://www.asciiart.eu/image-to-ascii">Image to ASCII art</a><br>
<a href="https://patorjk.com/software/taag/">ASCII text generator</a><br>
<a href="https://pypi.org/project/playsound3/">Playsound3</a> - Forked from the <a href="https://github.com/TaylorSMarks/playsound">Playsound</a> library, originally created by Taylor Marks<br>
<a href="https://pypi.org/project/tabulate/">Tabulate</a> • <a href="https://github.com/astanin/python-tabulate/tree/master">python-tabulate (GitHub)</a><br>
