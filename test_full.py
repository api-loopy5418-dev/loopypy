import pytest
import src.app as loopypy
import os
from unittest.mock import patch, MagicMock

@pytest.fixture(autouse=True)
def setup_api_key():
    loopypy.setApiKey("dummy_key")

def test_check_status_ok():
    with patch("src.app.requests.get") as mock_get:
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.text = "OK"
        mock_get.return_value = mock_resp
        assert loopypy.checkStatus() is True

def test_check_status_fail():
    with patch("src.app.requests.get") as mock_get:
        mock_resp = MagicMock()
        mock_resp.status_code = 500
        mock_resp.text = "bad"
        mock_get.return_value = mock_resp
        assert loopypy.checkStatus() is False

def test_set_get_api_key():
    assert loopypy.getApiKey() == os.environ.get("TESTPY_API_KEY")

def test_ai_success():
    with patch("src.app.requests.get") as mock_get:
        mock_resp = MagicMock()
        mock_resp.json.return_value = {
            "success": True,
            "response": "Hello!",
            "model": "test-model",
            "prompt": "hi"
        }
        mock_resp.raise_for_status = lambda: None
        mock_get.return_value = mock_resp
        resp = loopypy.ai("hi", speed=1)
        assert resp.success
        assert resp.response == "Hello!"

def test_qr_success():
    with patch("src.app.requests.get") as mock_get:
        mock_resp = MagicMock()
        mock_resp.content = b"qrdata"
        mock_resp.raise_for_status = lambda: None
        mock_get.return_value = mock_resp
        resp = loopypy.qr("test data")
        assert resp == b"qrdata"

def test_currency_success():
    with patch("src.app.requests.get") as mock_get:
        mock_resp = MagicMock()
        mock_resp.json.return_value = {
            "rate": "1.2",
            "converted": "120",
            "amount": "100",
            "success": True
        }
        mock_resp.raise_for_status = lambda: None
        mock_get.return_value = mock_resp
        res = loopypy.currency("USD", "EUR", 100)
        assert res.success
        assert res.converted == "120"

def test_seconds_to_time_success():
    with patch("src.app.requests.get") as mock_get:
        mock_resp = MagicMock()
        mock_resp.json.return_value = {"formatted_time": "1h 2m 3s"}
        mock_resp.raise_for_status = lambda: None
        mock_get.return_value = mock_resp
        res = loopypy.seconds_to_time(3723)
        assert res == "1h 2m 3s"

def test_pick_success():
    with patch("src.app.requests.get") as mock_get:
        mock_resp = MagicMock()
        mock_resp.json.return_value = {"result": "A"}
        mock_resp.raise_for_status = lambda: None
        mock_get.return_value = mock_resp
        res = loopypy.pick("A", "B", "C")
        assert res == "A"

def test_ascii_art_success():
    with patch("src.app.requests.get") as mock_get:
        mock_resp = MagicMock()
        mock_resp.json.return_value = {"ascii_art": "ascii"}
        mock_resp.raise_for_status = lambda: None
        mock_get.return_value = mock_resp
        res = loopypy.ascii_art("hi")
        assert res == "ascii"
