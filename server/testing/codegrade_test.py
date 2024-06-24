# test_main.py
import pytest
from main import add

def test_add():
    """Test the add function."""
    assert add(1, 2) == 3, "1 + 2 should be 3"
    assert add(-1, 1) == 0, "-1 + 1 should be 0"
    assert add(0, 0) == 0, "0 + 0 should be 0"
    assert add(2, -3) == -1, "2 + (-3) should be -1"

def test_codegrade_placeholder():
    """Codegrade placeholder test"""
    assert 1 == 1, "This test is a placeholder and always passes."

if __name__ == "__main__":
    pytest.main()
