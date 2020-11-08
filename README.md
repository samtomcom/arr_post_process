# \*arr Post Process

A sample post process script for Sonarr/Radarr.  
Currently for Windows, plan to make it system independant eventually.

## Usage

*arr Post Process is a script that simplifies the interface for getting environment variables from *arr. *arr Post Process simply creates a dictionary of the enviroment variables that *arr returns, the full list of which can be found [here (Sonarr)](https://github.com/Sonarr/Sonarr/wiki/Custom-Post-Processing-Scripts) and [here (Radarr)](https://github.com/Radarr/Radarr/wiki/Custom-Post-Processing-Scripts).

If you want to extend this to some other *arr/etc software, extend the list of environment variables, stored in ARR_ENV.txt

## Requirements

* Sonarr/Radarr installed
* Python 3.6+ installed and added to your system PATH

## Installation

1. Clone the repository

    git clone https://github.com/samtomcom/arr_post_process.git

2. Edit `execute.bat` to the correct location.
3. Naviage to Sonarr/Radarr [Settings > Connect > + > Custom Script](https://i.imgur.com/UOhYbNf.png), fill in the Path variable to `your\install\path\execute.bat`
4. Test and save
