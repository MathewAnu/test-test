"""
    all fixtures here will be available in the test folder and all subfolders
    of the test folder without importing it
"""

import pytest
import code_1.helper_function as hf

@pytest.fixture
def obj_math():
    '''
        fixtures are functions that can create data, 
        test doubles, or initialize system state for the test suite
    '''
    return hf.math()