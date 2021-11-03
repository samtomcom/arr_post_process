# \*arr Post Process

A sample post process script for Sonarr/Radarr.

In order to get \*arr to run a python script, I had to use a batch file to call it.  
It's possible that on any \*nix based systems you may have to use a shell file in a similar way,
but I only have \*arr running on Windows so I cannot test that.

## Usage

\*arr Post Process is a script that simplifies the interface for getting environment variables from \*arr. \*arr Post Process simply creates a dictionary of the enviroment variables that \*arr returns, the full list of which can be found [here (Sonarr)](https://github.com/Sonarr/Sonarr/wiki/Custom-Post-Processing-Scripts) and [here (Radarr)](https://github.com/Radarr/Radarr/wiki/Custom-Post-Processing-Scripts).

If you want to extend this to some other \*arr/etc software, extend the list of environment variables, stored in ARR_ENV.txt

## Requirements

* Sonarr/Radarr installed
* Python 3.6+ installed and added to your system PATH

## Installation

1. Clone the repository

    git clone https://github.com/samtomcom/arr_post_process.git

2. Edit `execute.bat` to the correct location.
3. Naviage to Sonarr/Radarr [Settings > Connect > + > Custom Script](https://i.imgur.com/UOhYbNf.png), fill in the Path variable to `your\install\path\execute.bat`
4. Test and save
