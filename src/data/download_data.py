import requests
import os
import pandas as pd
from pathlib import Path


def download_data():
    """
    Downloads Reddit dataset from GitHub
    """
    url = "https://raw.githubusercontent.com/Himanshu-1703/reddit-sentiment-analysis/refs/heads/main/data/reddit.csv"

    # Path relative to project
    project_root = Path(__file__).parent.parent.parent
    output_path = project_root / "data" / "raw" / "reddit.csv"

    # Create directory if needed
    output_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"Downloading dataset from {url}...")
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        with open(output_path, "wb") as f:
            f.write(response.content)

        print(f"Dataset saved to {output_path}")

        # Display some stats
        df = pd.read_csv(output_path)
        print(f"\nDataset statistics:")
        print(f"Total comments: {len(df)}")
        print(f"Columns: {list(df.columns)}")

        # Display distribution if sentiment column exists
        if "sentiment" in df.columns:
            print(f"\nSentiment distribution:")
            print(df["sentiment"].value_counts())
        elif "category" in df.columns:
            print(f"\nCategory distribution:")
            print(df["category"].value_counts())

        # Display a sample
        print(f"\nFirst comment:")
        if "clean_comment" in df.columns:
            print(df["clean_comment"].iloc[0][:100] + "...")
        elif "comment" in df.columns:
            print(df["comment"].iloc[0][:100] + "...")

    except Exception as e:
        print(f"Error downloading dataset: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    download_data()
