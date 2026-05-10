import subprocess
import sys
import pkgutil

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

if __name__ == "__main__":
    install_requirements()
    print("\n👉 Now run your app using:")
    print("   streamlit run app.py\n")
