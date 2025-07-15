from seasons import takestr
import pytest

def test_1():
    assert str(takestr("2025-02-12", "2025-02-13")) == "One thousand, four hundred forty minutes"

def test_2():
    with pytest.raises(SystemExit) as exit_info:
        takestr("ljasflj", "2025-02-13")

    assert exit_info.value.code == 1

def test_3():
    with pytest.raises(SystemExit) as exit_info:
        takestr("january 01 2025", "2025-02-13")

    assert exit_info.value.code == 1
