from unittest.mock import patch, MagicMock
from check_db import check_db


def test_check_db_unreachable():
    result = check_db("localhost", 1, timeout=0.5)
    assert "НЕДОСТУПНА" in result


def test_check_db_reachable():
    with patch("check_db.socket.create_connection", return_value=MagicMock()):
        result = check_db("localhost", 5432)
    assert result == "База localhost:5432 доступна"
