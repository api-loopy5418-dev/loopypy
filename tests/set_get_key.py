import pytest
import src.app as app
from unittest.mock import patch, Mock

def test_checkStatus_ok():
    with patch("src.app.requests.get") as mock_get:
        mock_resp = Mock(status_code=200, text="OK")
        mock_get.return_value = mock_resp
        assert app.checkStatus() is True

def test_checkStatus_not_ok():
    with patch("src.app.requests.get") as mock_get:
        mock_resp = Mock(status_code=500, text="ERROR")
        mock_get.return_value = mock_resp
        assert app.checkStatus() is False

def test_checkStatus_exception():
    with patch("src.app.requests.get", side_effect=Exception("fail")):
        assert app.checkStatus() is False

def test_setApiKey_and_getApiKey():
    app.setApiKey("1234")
    assert app.getApiKey() == "1234"

def test_setApiKey_invalid():
    with pytest.raises(ValueError):
        app.setApiKey(None)
    with pytest.raises(ValueError):
        app.setApiKey(123)

def test_getApiKey_not_set():
    app.API_KEY = None
    with pytest.raises(ValueError):
        app.getApiKey()

def test_ai_success(monkeypatch):
    app.API_KEY = "testkey"
    mock_resp = Mock()
    mock_resp.raise_for_status = lambda: None
    mock_resp.json.return_value = {"success": True, "response": "hi", "model": "gpt", "prompt": "hello"}
    with patch("src.app.requests.get", return_value=mock_resp):
        resp = app.ai("hello", 1)
        assert isinstance(resp, app.airesp)
        assert resp.success is True
        assert resp.response == "hi"

def test_ai_no_apikey():
    app.API_KEY = None
    with pytest.raises(ValueError):
        app.ai("hello")

def test_ai_invalid_prompt():
    app.API_KEY = "test"
    with pytest.raises(ValueError):
        app.ai(None)
    with pytest.raises(ValueError):
        app.ai(123)

def test_ai_invalid_speed():
    app.API_KEY = "test"
    with pytest.raises(ValueError):
        app.ai("hello", 10)

def test_ai_request_fail(monkeypatch):
    app.API_KEY = "test"
    with patch("src.app.requests.get", side_effect=Exception("fail")):
        resp = app.ai("hello")
        assert resp.success is False
        assert "Request failed" in resp.response

def test_owoify_success():
    mock_resp = Mock()
    mock_resp.raise_for_status = lambda: None
    mock_resp.json.return_value = {"result": "owo"}
    with patch("src.app.requests.get", return_value=mock_resp):
        assert app.owoify("hello") == "owo"

def test_owoify_invalid():
    with pytest.raises(ValueError):
        app.owoify(None)
    with pytest.raises(ValueError):
        app.owoify([])

def test_owoify_request_fail():
    with patch("src.app.requests.get", side_effect=Exception("fail")):
        result = app.owoify("hello")
        assert "Error in owoify" in result

def test_emojify_success():
    mock_resp = Mock()
    mock_resp.raise_for_status = lambda: None
    mock_resp.json.return_value = {"result": "😀"}
    with patch("src.app.requests.get", return_value=mock_resp):
        assert app.emojify("hello") == "😀"

def test_emojify_invalid():
    with pytest.raises(ValueError):
        app.emojify(None)
    with pytest.raises(ValueError):
        app.emojify(123)

def test_emojify_request_fail():
    with patch("src.app.requests.get", side_effect=Exception("fail")):
        result = app.emojify("hello")
        assert "Error in emojify" in result

def test_qr_success():
    app.API_KEY = "abc"
    mock_resp = Mock()
    mock_resp.raise_for_status = lambda: None
    mock_resp.content = b"qrcode"
    with patch("src.app.requests.get", return_value=mock_resp):
        assert app.qr("data") == b"qrcode"

def test_qr_no_apikey():
    app.API_KEY = None
    with pytest.raises(ValueError):
        app.qr("test")

def test_qr_invalid_data():
    app.API_KEY = "abc"
    with pytest.raises(ValueError):
        app.qr(None)
    with pytest.raises(ValueError):
        app.qr(123)

def test_qr_request_fail():
    app.API_KEY = "abc"
    with patch("src.app.requests.get", side_effect=Exception("fail")):
        result = app.qr("data")
        assert "Error in qr" in result

def test_currency_success():
    app.API_KEY = "abc"
    mock_resp = Mock()
    mock_resp.raise_for_status = lambda: None
    mock_resp.json.return_value = {"rate": 2, "converted": 10, "amount": 5, "success": True}
    with patch("src.app.requests.get", return_value=mock_resp):
        c = app.currency("USD", "EUR", 5)
        assert isinstance(c, app.currencyinfo)
        assert c.success is True

def test_currency_invalid():
    app.API_KEY = "abc"
    with pytest.raises(ValueError):
        app.currency(None, "EUR", 5)
    with pytest.raises(ValueError):
        app.currency("USD", None, 5)
    with pytest.raises(ValueError):
        app.currency("USD", "EUR", "five")

def test_currency_no_apikey():
    app.API_KEY = None
    with pytest.raises(ValueError):
        app.currency("USD", "EUR", 1)

def test_currency_request_fail():
    app.API_KEY = "abc"
    with patch("src.app.requests.get", side_effect=Exception("fail")):
        c = app.currency("USD", "EUR", 1)
        assert isinstance(c, app.currencyinfo)
        assert c.success is False

def test_seconds_to_time_success():
    mock_resp = Mock()
    mock_resp.raise_for_status = lambda: None
    mock_resp.json.return_value = {"formatted_time": "1:00"}
    with patch("src.app.requests.get", return_value=mock_resp):
        assert app.seconds_to_time(60) == "1:00"

def test_seconds_to_time_invalid():
    with pytest.raises(ValueError):
        app.seconds_to_time(None)
    with pytest.raises(ValueError):
        app.seconds_to_time("sixty")

def test_seconds_to_time_request_fail():
    with patch("src.app.requests.get", side_effect=Exception("fail")):
        result = app.seconds_to_time(60)
        assert "Error in seconds_to_time" in result

def test_pick_success():
    mock_resp = Mock()
    mock_resp.raise_for_status = lambda: None
    mock_resp.json.return_value = {"result": "a"}
    with patch("src.app.requests.get", return_value=mock_resp):
        assert app.pick("a", "b") == "a"

def test_pick_invalid():
    with pytest.raises(ValueError):
        app.pick()

def test_pick_request_fail():
    with patch("src.app.requests.get", side_effect=Exception("fail")):
        result = app.pick("a", "b")
        assert "Error in pick" in result

def test_ascii_art_success():
    mock_resp = Mock()
    mock_resp.raise_for_status = lambda: None
    mock_resp.json.return_value = {"ascii_art": "art"}
    with patch("src.app.requests.get", return_value=mock_resp):
        assert app.ascii_art("hi") == "art"

def test_ascii_art_invalid():
    with pytest.raises(ValueError):
        app.ascii_art(None)
    with pytest.raises(ValueError):
        app.ascii_art(123)

def test_ascii_art_request_fail():
    with patch("src.app.requests.get", side_effect=Exception("fail")):
        result = app.ascii_art("hi")
        assert "Error in ascii_art" in result
