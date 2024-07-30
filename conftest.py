import pytest
from browserstack.local import Local
import os, json
from jsonmerge import merge
from dotenv import load_dotenv
import time

load_dotenv()

CONFIG_FILE = os.environ['CONFIG_FILE'] if 'CONFIG_FILE' in os.environ else 'resources/single.json'
TASK_ID = int(os.environ['TASK_ID']) if 'TASK_ID' in os.environ else 0


with open(CONFIG_FILE) as data_file:
    CONFIG = json.load(data_file)

timenow = None

@pytest.fixture(scope='session')
def base_url():
  print(CONFIG['base_url'])
  return CONFIG['base_url']



