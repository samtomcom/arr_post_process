from datetime import datetime
import os

SCRIPT_PATH = os.path.realpath(__file__)
SCRIPT_DIR = os.path.dirname(SCRIPT_PATH)
TIME = datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
LOG_FILE = f"{SCRIPT_DIR}\\logs\\{TIME}.txt"
ENV_FILE = f"{SCRIPT_DIR}\\ARR_ENV.txt"

envs = {}

with open(ENV_FILE, 'r') as f:
    for line in f:
        env = line.rstrip()
        if env in os.environ:
            envs[env] = os.environ[env]

    if len(envs) == 0:
        envs['TEST'] = 'This was a test'

with open(LOG_FILE, 'w') as f:
    for env in envs:
        f.write(f'{env} = {envs[env]}\n')
	


