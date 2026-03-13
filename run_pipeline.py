"""
Script to run the complete pipeline
Downloads data, processes it, and trains the model
"""

import subprocess
import sys
from pathlib import Path


def run_command(command, description):
    """
    Executes a command and displays the result
    """
    print(f"\n{'='*50}")
    print(f"Step: {description}")
    print(f"Command: {command}")
    print(f"{'='*50}\n")

    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=False)
        print(f"✓ {description} completed successfully\n")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Error during {description}")
        print(f"Error code: {e.returncode}")
        return False


def main():
    """
    Runs the complete pipeline
    """
    print("=" * 50)
    print("Complete Pipeline - YouTube Sentiment Analysis")
    print("=" * 50)

    steps = [
        ("python src/data/download_data.py", "Downloading data"),
        ("python src/data/process_data.py", "Processing data"),
        ("python src/models/train_model.py", "Training model"),
    ]

    for command, description in steps:
        if not run_command(command, description):
            print(f"\n❌ Pipeline stopped at step: {description}")
            print("Check the errors above.")
            sys.exit(1)

    print("\n" + "=" * 50)
    print("✅ Pipeline completed successfully!")
    print("=" * 50)
    print("\nYou can now run the API with:")
    print("  python -m uvicorn src.api.main:app --reload")


if __name__ == "__main__":
    main()
