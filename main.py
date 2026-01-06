import sys
import os

# Ensure Python can find gui.py in the same folder
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from gui import start_gui

if __name__ == "__main__":
    start_gui()
