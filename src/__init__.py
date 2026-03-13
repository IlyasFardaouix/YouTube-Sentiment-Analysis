```python
# Importing required libraries
import os
import re
import json
import logging

# Setting up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_config(file_path: str) -> dict:
    """
    Loads configuration from a JSON file.

    Args:
    file_path (str): Path to the configuration file.

    Returns:
    dict: Configuration dictionary.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        logging.error(f"Configuration file not found at {file_path}")
        return {}
    except json.JSONDecodeError:
        logging.error(f"Invalid JSON in configuration file at {file_path}")
        return {}

def extract_emails(text: str) -> list:
    """
    Extracts email addresses from a given text.

    Args:
    text (str): Text to extract email addresses from.

    Returns:
    list: List of extracted email addresses.
    """
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(email_pattern, text)

def main():
    """
    Main function to execute the script.
    """
    config = load_config('config.json')
    if not config:
        logging.error("Configuration is empty")
        return

    # Check if required configuration keys are present
    required_keys = ['input_file', 'output_file']
    if not all(key in config for key in required_keys):
        logging.error("Missing required configuration keys")
        return

    input_file = config['input_file']
    output_file = config['output_file']

    # Check if input file exists
    if not os.path.exists(input_file):
        logging.error(f"Input file not found at {input_file}")
        return

    with open(input_file, 'r') as file:
        text = file.read()

    emails = extract_emails(text)
    with open(output_file, 'w') as file:
        for email in emails:
            file.write(email + '\n')

if __name__ == '__main__':
    main()
```

```python
# config.json
{
    "input_file": "input.txt",
    "output_file": "output.txt"
}
```

```python
# input.txt
Hello, my email is john.doe@example.com and you can also contact me at jane.doe@example.com.
```