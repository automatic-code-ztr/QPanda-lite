import json
from pathlib import Path

def create_ibm_online_config(default_token = None):    

    if not default_token:
        raise RuntimeError('You should input your token.')

    default_online_config = {
        'default_token' : default_token,
    }

    with open(Path.cwd() / 'ibm_online_config.json', 'w') as fp:
        json.dump(default_online_config, fp)

if __name__ == '__main__':

    # The originq qpilot login state token
    token = ''

    create_ibm_online_config(default_token = token)