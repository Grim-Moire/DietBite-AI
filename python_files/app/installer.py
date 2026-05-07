import sys
import subprocess

subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas", "scikit-learn", "matplotlib", "joblib"])