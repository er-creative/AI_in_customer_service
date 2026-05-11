import subprocess
import sys
import pkgutil
import os

def install_requirements():
    print("Checking required packages...\n")

    try:
        with open("requirements.txt") as f:
            required = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("❌ requirements.txt not found")
        return

    missing = []

    for pkg in required:
        pkg_name = pkg.split("==")[0].lower()

        if pkgutil.find_loader(pkg_name) is None:
            missing.append(pkg)

    if missing:
        print("Installing missing packages:\n", missing, "\n")
        subprocess.check_call([sys.executable, "-m", "pip", "install", *missing])
        print("\n✅ Installation complete!")
    else:
        print("✅ All required packages are already installed!")

def check_database():
    # Change database filename if needed
    db_file = "ai_data.db"

    print("\nChecking database status...\n")

    if os.path.exists(db_file):
        print("✅ Database already exists.")
        print('\n👉 Run the app using:')
        print("   streamlit run app.py\n")
    else:
        print("❌ Database not found.")
        print('\n👉 Next command to create database:')
        print("   python db.py\n")
        print("After database creation, run:")
        print("   streamlit run app.py\n")

if __name__ == "__main__":
    install_requirements()
    check_database()