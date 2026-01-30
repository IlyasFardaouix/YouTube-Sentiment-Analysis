"""
Setup script to initialize the project
Creates necessary directories and checks dependencies
"""
import os
from pathlib import Path

def setup_project():
    """
    Creates necessary directory structure
    """
    project_root = Path(__file__).parent
    
    directories = [
        project_root / "data" / "raw",
        project_root / "data" / "processed",
        project_root / "models",
        project_root / "logs"
    ]
    
    print("Creating directory structure...")
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)
        print(f"  ✓ {directory}")
    
    # Create .gitkeep files if needed
    gitkeep_files = [
        project_root / "data" / ".gitkeep",
        project_root / "models" / ".gitkeep",
        project_root / "logs" / ".gitkeep"
    ]
    
    for gitkeep in gitkeep_files:
        if not gitkeep.exists():
            gitkeep.touch()
    
    print("\nStructure created successfully!")
    print("\nNext steps:")
    print("1. Download data: python src/data/download_data.py")
    print("2. Process data: python src/data/process_data.py")
    print("3. Train model: python src/models/train_model.py")
    print("4. Run API: python -m uvicorn src.api.main:app --reload")

if __name__ == "__main__":
    setup_project()
