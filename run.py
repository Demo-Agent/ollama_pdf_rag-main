import subprocess
from pathlib import Path
import nltk
import os

def initialize_nltk():
    """Initialize NLTK resources before starting the app"""
    resources = [
        'punkt',
        'punkt_tab',
        'averaged_perceptron_tagger',
        'averaged_perceptron_tagger_eng',
        'maxent_ne_chunker',
        'words',
        'stopwords',
        'universal_tagset'
    ]
    
    for resource in resources:
        try:
            print(f"Downloading {resource}...")
            nltk.download(resource, quiet=False)
        except Exception as e:
            print(f"Warning: Failed to download {resource}: {e}")

def main():
    try:
        # Initialize NLTK first
        initialize_nltk()
        
        # Get the path to main.py
        app_dir = Path(__file__).parent / "src" / "app"
        app_path = app_dir / "main.py"
        
        if not app_path.exists():
            raise FileNotFoundError(f"Could not find {app_path}")
        
        # Run the Streamlit app
        print("Starting Streamlit app...")
        subprocess.run(["streamlit", "run", str(app_path)], check=True)
        
    except Exception as e:
        print(f"Error running app: {e}")
        raise

if __name__ == "__main__":
    main() 