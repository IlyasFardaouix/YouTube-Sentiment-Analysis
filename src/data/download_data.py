import requests
import os
import pandas as pd

def download_data():
    url = "https://raw.githubusercontent.com/Himanshu-1703/reddit-sentiment-analysis/refs/heads/main/data/reddit.csv"
    output_path = os.path.join("data", "raw", "reddit.csv")
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    print(f"Downloading dataset from {url}...")
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        with open(output_path, "wb") as f:
            f.write(response.content)
        
        print(f"Dataset saved to {output_path}")
        
        # Display statistics
        df = pd.read_csv(output_path)
        print("\nDataset Statistics:")
        print(f"Total comments: {len(df)}")
        print("\nLabel Distribution:")
        print(df['sentiment'].value_counts())
        
    except Exception as e:
        print(f"Error downloading dataset: {e}")

if __name__ == "__main__":
    download_data()
