import os

# Define the folder structure
folders = [
    "app/pages",
    "app/components",
    "app/assets/images",
    "app/assets/data",
    ".github/workflows",
    ".streamlit",
    "tests"
]

# Define the files
files = [
    "app/__init__.py",
    "app/main.py",
    "app/pages/__init__.py",
    "app/pages/page1.py",
    "app/pages/page2.py",
    "app/components/__init__.py",
    "app/components/sidebar.py",
    "app/components/widgets.py",
    "app/assets/images/logo.png",
    "app/assets/data/sample_data.csv",
    ".github/workflows/deploy.yml",
    ".streamlit/config.toml",
    "tests/__init__.py",
    "tests/test_main.py",
    "tests/test_components.py",
    "requirements.txt",
    "README.md",
    ".gitignore"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for file in files:
    with open(file, 'w') as f:
        pass

print("Folder structure created successfully.")