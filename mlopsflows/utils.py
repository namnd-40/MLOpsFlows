"""The utility module
"""
import json
import random
from typing import Dict
import sys
import os

import numpy as np # pylint: disable=import-error

sys.path.append(os.path.dirname(__file__))

def load_dict(filepath: str) -> Dict:
    """Load a dictionary from a JSON's filepath.
    Args:
        filepath (str): location of file.
    Returns:
        Dict: loaded JSON data.
    """
    with open(filepath, encoding="UTF-8") as file_path:
        data = json.load(file_path)
    return data


def save_dict(dictionary: Dict, filepath: str, cls=None, sortkeys: bool = False) -> None:
    """Save a dictionary to a specific location.
    Args:
        dictionary (Dict): data to save.
        filepath (str): location of where to save the data.
        cls (optional): encoder to use on dict data. Defaults to None.
        sortkeys (bool, optional): whether to sort keys alphabetically. Defaults to False.
    """
    with open(filepath, "w", encoding="UTF-8") as file_path:
        json.dump(dictionary, indent=2, fp=file_path, cls=cls, sort_keys=sortkeys)
        file_path.write("\n")


def set_seeds(seed: int = 42) -> None:
    """Set seed for reproducibility.
    Args:
        seed (int, optional): number to be used as the seed. Defaults to 42.
    """
    # Set seeds
    np.random.seed(seed)
    random.seed(seed)
