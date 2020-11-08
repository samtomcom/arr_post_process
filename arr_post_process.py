import os

SCRIPT_PATH = os.path.realpath(__file__)
SCRIPT_DIR = os.path.dirname(SCRIPT_PATH)
ENV_FILE = f"{SCRIPT_DIR}\\ARR_ENV.txt"

envs = {}

# Checking all potentiall environment variables
with open(ENV_FILE, 'r') as f:
    for line in f:
        env = line.rstrip()
        if env in os.environ:
            envs[env] = os.environ[env]

    # No environment variables were found
    # Either the script was run manually as a test (ie Not ran by *arr)
    #  or, something went wrong : )
    if len(envs) == 0:
        raise Exception('No *arr Environment variables were found.')

# envs is now a dictionary containing any *arr variables found
# Call your own script here, or do what you want with the environment variables found
# Information on what these variables could be can be found at:
# https://github.com/Radarr/Radarr/wiki/Custom-Post-Processing-Scripts
# https://github.com/Sonarr/Sonarr/wiki/Custom-Post-Processing-Scripts

	


