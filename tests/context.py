import os
import sys

DIR_PATH = ".."
DIR_NAME = "boltiot"
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(DIR_NAME), DIR_PATH)))

from boltiot import Bolt
