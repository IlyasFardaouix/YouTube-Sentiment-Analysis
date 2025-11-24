import requests
import json

def test_api():
    base_url = "http://127.0.0.1:8000"
    
    # Test Health
    print("Testing /health...")
    try:
        resp = requests.get(f"{base_url}/health")
        print(resp.json())
    except Exception as e:
        print(f"Health check failed: {e}")
        return

    # Test Predict Batch
    print("\nTesting /predict_batch...")
    payload = {
        "comments": [
            {"id": "1", "text": "This video is amazing! I learned so much."},
            {"id": "2", "text": "Terrible content, waste of time."},
            {"id": "3", "text": "It was okay, nothing special."}
        ]
    }
    
    try:
        resp = requests.post(f"{base_url}/predict_batch", json=payload)
        print(json.dumps(resp.json(), indent=2))
    except Exception as e:
        print(f"Prediction failed: {e}")

if __name__ == "__main__":
    test_api()
