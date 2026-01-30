"""
Test script for the API
Allows checking that the API works correctly
"""
import requests
import json

def test_api():
    base_url = "http://127.0.0.1:8000"
    
    # Test 1: Health check
    print("Test 1: Checking API status (/health)...")
    try:
        resp = requests.get(f"{base_url}/health", timeout=5)
        print(f"Status: {resp.status_code}")
        print(f"Response: {json.dumps(resp.json(), indent=2, ensure_ascii=False)}")
    except requests.exceptions.ConnectionError:
        print("Error: API is not running!")
        print("Start it first: python -m uvicorn src.api.main:app --reload")
        return
    except Exception as e:
        print(f"Error during health check: {e}")
        return

    # Test 2: Batch prediction
    print("\nTest 2: Sentiment prediction (/predict_batch)...")
    payload = {
        "comments": [
            {"id": "1", "text": "This video is amazing! I learned so much."},
            {"id": "2", "text": "Terrible content, waste of time."},
            {"id": "3", "text": "It was okay, nothing special."},
            {"id": "4", "text": "I love this video, thank you so much!"},
            {"id": "5", "text": "Not great content..."}
        ]
    }
    
    try:
        resp = requests.post(
            f"{base_url}/predict_batch", 
            json=payload,
            timeout=10
        )
        print(f"Status: {resp.status_code}")
        if resp.status_code == 200:
            result = resp.json()
            print(f"\nStatistics:")
            print(f"  Total: {result['stats']['total']}")
            print(f"  Positive: {result['stats']['positive']} ({result['stats']['positive_pct']}%)")
            print(f"  Neutral: {result['stats']['neutral']} ({result['stats']['neutral_pct']}%)")
            print(f"  Negative: {result['stats']['negative']} ({result['stats']['negative_pct']}%)")
            print(f"\nDetailed predictions:")
            for pred in result['predictions']:
                sentiment_label = "Positive" if pred['sentiment'] == 1 else ("Negative" if pred['sentiment'] == -1 else "Neutral")
                print(f"  [{pred['id']}] {sentiment_label} ({pred['confidence']*100:.1f}%): {pred['text'][:50]}...")
        else:
            print(f"Error: {resp.text}")
    except Exception as e:
        print(f"Error during prediction: {e}")

if __name__ == "__main__":
    test_api()
