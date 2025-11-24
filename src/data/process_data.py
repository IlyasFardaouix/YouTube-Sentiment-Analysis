import pandas as pd
import re
from sklearn.model_selection import train_test_split
import os

def clean_text(text):
    if not isinstance(text, str):
        return ""
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    # Remove mentions
    text = re.sub(r'@\w+', '', text)
    # Remove special characters and numbers (keep emojis if needed, but basic cleaning for now)
    # The PDF asks to remove special characters.
    text = re.sub(r'[^\w\s]', '', text) 
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def process_data():
    input_path = os.path.join("data", "raw", "reddit.csv")
    train_output_path = os.path.join("data", "processed", "train.csv")
    test_output_path = os.path.join("data", "processed", "test.csv")
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(train_output_path), exist_ok=True)
    
    print("Loading raw data...")
    try:
        df = pd.read_csv(input_path)
        
        # Rename columns if necessary (PDF says 'text' and 'label')
        # Let's check the columns from the download script output first, but assuming standard names or renaming
        if 'clean_comment' in df.columns:
             df = df.rename(columns={'clean_comment': 'text', 'category': 'label'})
        elif 'comment' in df.columns:
             df = df.rename(columns={'comment': 'text', 'category': 'label'})
             
        # Check if 'text' and 'label' exist
        if 'text' not in df.columns or 'label' not in df.columns:
            # Fallback based on common dataset structures, or print columns to debug
            print(f"Columns found: {df.columns}")
            # If the dataset is the one from Himanshu-1703, it usually has 'clean_comment' and 'category'
            # But let's wait for the download output to be sure. 
            # For now, I'll assume standard names or the ones I just handled.
            pass

        print("Cleaning text...")
        df['text'] = df['text'].apply(clean_text)
        
        # Remove empty rows
        df = df[df['text'].str.len() > 0]
        
        print("Splitting data...")
        train_df, test_df = train_test_split(df, test_size=0.2, random_state=42, stratify=df['label'])
        
        print(f"Saving processed data to {train_output_path} and {test_output_path}...")
        train_df.to_csv(train_output_path, index=False)
        test_df.to_csv(test_output_path, index=False)
        
        print("Data processing complete.")
        print(f"Train set size: {len(train_df)}")
        print(f"Test set size: {len(test_df)}")
        
    except Exception as e:
        print(f"Error processing data: {e}")

if __name__ == "__main__":
    process_data()
