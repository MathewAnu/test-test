import pytest

#command python -m pytest 

class TestMath:
    '''
    MOVED TO conftest.py
    @pytest.fixture
    def obj_math(self):
        """
            fixtures are functions that can create data, 
            test doubles, or initialize system state for the test suite
        """
        return hf.math()
    '''
    @pytest.mark.positive_test
    def test_int_addition(self, obj_math):
        assert obj_math.addition(5, 3) == 8

    @pytest.mark.positive_test
    def test_string_addition(self, obj_math):
        assert obj_math.addition("Apple", "Pie") == "ApplePie"

    @pytest.mark.positive_test
    def test_float_addition(self, obj_math):
        assert obj_math.addition(6.8, 7.2) == 14

    @pytest.mark.negative_test
    def test_int_string_addition(self, obj_math):
        with pytest.raises(TypeError):
            obj_math.addition("Apple", 7)
    
    @pytest.mark.skip
    def test_skip_addition(self, obj_math):
        """ will be skipped"""
        assert obj_math.addition(1, 2) == 3

    # parametrize
    @pytest.mark.negative_test
    @pytest.mark.parametrize("obj_math, val1, val2, result", [
            ("obj_math", 1, 2, 1),
            ("obj_math", -2, 1, -1),
        ],
        indirect=["obj_math"])
    def test_subtraction_fail(self, obj_math, val1, val2, result):
            assert not obj_math.subtraction(val1, val2) == result

@pytest.mark.positive_test
@pytest.mark.parametrize("obj_math, val1, val2, result", [
        ("obj_math", 1, 2, -1),
        ("obj_math", 3, 2, 1),
        ("obj_math", -2, -3, 1)
    ],
    indirect=["obj_math"])
def test_subtraction_pass(obj_math, val1, val2, result):
        assert obj_math.subtraction(val1, val2) == result