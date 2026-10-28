from check_db import check_db


def test_check_db_unreachable():
    result = check_db("localhost", 1, timeout=0.5)
    assert "НЕДОСТУПНА" in result
