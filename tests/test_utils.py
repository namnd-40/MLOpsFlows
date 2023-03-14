"""Test utils module"""
import tempfile
from pathlib import Path

import numpy as np # pylint: disable=import-error

from mlopsflows import utils # pylint: disable=import-error


def test_save_and_load_dict():
    """Test save and load dictionary
    """
    with tempfile.TemporaryDirectory() as directory_path:
        dictionary = {"hello": "world"}
        file_path = Path(directory_path, "d.json")
        utils.save_dict(dictionary=dictionary, filepath=file_path)
        dictionary = utils.load_dict(filepath=file_path)
        assert dictionary["hello"] == "world"


def test_set_seed():
    """Test set_seed
    """
    utils.set_seeds()
    first_number = np.random.randn(2, 3)
    second_number = np.random.randn(2, 3)
    utils.set_seeds()
    third_number = np.random.randn(2, 3)
    fourth_number = np.random.randn(2, 3)
    assert np.array_equal(first_number, third_number)
    assert np.array_equal(second_number, fourth_number)
