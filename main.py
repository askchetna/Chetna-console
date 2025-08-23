# ChetnaGPT Web Application
# For CLI version, run: python main_cli.py
# For web version (default), run: python backend/main.py

import subprocess
import sys

def main():
    print("🕉️ ChetnaGPT - Choose your interface:")
    print("1. Web Application (default)")
    print("2. CLI Application")

    choice = input("\nSelect interface (1 or 2, default=1): ").strip()

    if choice == "2":
        # Run CLI version
        subprocess.run([sys.executable, "main_cli.py"])
    else:
        # Run web version
        subprocess.run([sys.executable, "backend/main.py"])

if __name__ == "__main__":
    main()