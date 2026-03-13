import pytest
from unittest.mock import Mock, patch
from your_module import test_api  # Replace 'your_module' with the actual module name

@pytest.fixture
def mock_requests_get():
    with patch('requests.get') as mock_get:
        yield mock_get

@pytest.fixture
def mock_requests_post():
    with patch('requests.post') as mock_post:
        yield mock_post

def test_test_api_success(mock_requests_get, mock_requests_post):
    """Test test_api function with successful API responses."""
    mock_get = mock_requests_get
    mock_post = mock_requests_post

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {'status': 'ok'}

    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {
        'stats': {'total': 5, 'positive': 3, 'neutral': 1, 'negative': 1},
        'predictions': [
            {'id': '1', 'sentiment': 1, 'confidence': 0.8, 'text': 'This is a positive comment'},
            {'id': '2', 'sentiment': -1, 'confidence': 0.9, 'text': 'This is a negative comment'},
            {'id': '3', 'sentiment': 0, 'confidence': 0.7, 'text': 'This is a neutral comment'}
        ]
    }

    test_api()

def test_test_api_connection_error(mock_requests_get):
    """Test test_api function with connection error."""
    mock_get = mock_requests_get

    mock_get.side_effect = requests.exceptions.ConnectionError

    with pytest.raises(SystemExit):
        test_api()

def test_test_api_health_check_error(mock_requests_get):
    """Test test_api function with health check error."""
    mock_get = mock_requests_get

    mock_get.return_value.status_code = 500
    mock_get.return_value.json.return_value = {'error': 'Internal Server Error'}

    with pytest.raises(SystemExit):
        test_api()

def test_test_api_batch_prediction_error(mock_requests_post):
    """Test test_api function with batch prediction error."""
    mock_post = mock_requests_post

    mock_post.return_value.status_code = 500
    mock_post.return_value.text = 'Internal Server Error'

    with pytest.raises(SystemExit):
        test_api()

def test_test_api_invalid_base_url():
    """Test test_api function with invalid base URL."""
    with pytest.raises(SystemExit):
        test_api(base_url='invalid_url')

def test_test_api_no_base_url():
    """Test test_api function without base URL."""
    with pytest.raises(SystemExit):
        test_api(base_url=None)

def test_test_api_empty_base_url():
    """Test test_api function with empty base URL."""
    with pytest.raises(SystemExit):
        test_api(base_url='')