import numpy as np
from pathlib import Path


def file_path(basename):
    return  Path('.') / 'data' / basename