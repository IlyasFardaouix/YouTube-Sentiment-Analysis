import pandas as pd
import re
from sklearn.model_selection import train_test_split
import os
from pathlib import Path

def clean_text(text):
    """
    Cleans text by removing URLs, mentions, special characters
    """
    if not isinstance(text, str):
        return ""
    
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    
    # Remove @ mentions
    text = re.sub(r'@\w+', '', text)
    
    # Remove special characters (keep letters, numbers, spaces)
    text = re.sub(r'[^\w\s]', '', text) 
    
    # Remove multiple spaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def process_data():
    """
    Processes raw data: cleaning, train/test split
    """
    # Paths relative to project
    project_root = Path(__file__).parent.parent.parent
    input_path = project_root / "data" / "raw" / "reddit.csv"
    train_output_path = project_root / "data" / "processed" / "train.csv"
    test_output_path = project_root / "data" / "processed" / "test.csv"
    
    # Create directories if needed
    train_output_path.parent.mkdir(parents=True, exist_ok=True)
    
    print("Loading raw data...")
    try:
        if not input_path.exists():
            print(f"Error: File {input_path} not found!")
            print("Run first: python src/data/download_data.py")
            return
        
        df = pd.read_csv(input_path)
        print(f"Data loaded: {len(df)} rows")
        print(f"Columns: {list(df.columns)}")
        
        # Adapt according to Reddit dataset format
        # Himanshu-1703 dataset usually has 'clean_comment' and 'category'
        if 'clean_comment' in df.columns and 'category' in df.columns:
            df = df.rename(columns={'clean_comment': 'text', 'category': 'label'})
        elif 'comment' in df.columns and 'sentiment' in df.columns:
            df = df.rename(columns={'comment': 'text', 'sentiment': 'label'})
        elif 'text' not in df.columns or 'label' not in df.columns:
            print(f"Columns found: {list(df.columns)}")
            print("Error: 'text' and 'label' columns not found!")
            return
        
        # Check label values and convert if necessary
        # Model expects -1 (negative), 0 (neutral), 1 (positive)
        if df['label'].dtype == 'object':
            # Convert text to numbers
            label_map = {'negative': -1, 'neutral': 0, 'positive': 1, 
                        'neg': -1, 'neu': 0, 'pos': 1}
            df['label'] = df['label'].map(label_map).fillna(0)
        
        # Clean text
        print("Cleaning text...")
        df['text'] = df['text'].apply(clean_text)
        
        # Remove empty rows
        df = df[df['text'].str.len() > 0]
        print(f"After cleaning: {len(df)} rows")
        
        # Split train/test (80/20)
        print("Splitting train/test...")
        try:
            train_df, test_df = train_test_split(
                df, 
                test_size=0.2, 
                random_state=42, 
                stratify=df['label']
            )
        except ValueError:
            # If stratification fails (not enough samples per class)
            print("Stratification failed, simple split...")
            train_df, test_df = train_test_split(
                df, 
                test_size=0.2, 
                random_state=42
            )
        
        # Save
        print(f"Saving to {train_output_path} and {test_output_path}...")
        train_df.to_csv(train_output_path, index=False)
        test_df.to_csv(test_output_path, index=False)
        
        print("Processing complete!")
        print(f"Train: {len(train_df)} samples")
        print(f"Test: {len(test_df)} samples")
        print(f"Train distribution: {train_df['label'].value_counts().to_dict()}")
        
    except Exception as e:
        print(f"Error during processing: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    process_data()
