import os

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Directory created: {path}")

def create_file(path, content=""):
    with open(path, 'w') as file:
        file.write(content)
        print(f"File created: {path}")

def setup_project_structure(base_path):
    directories = [
        os.path.join(base_path, "network_data"),
        os.path.join(base_path, "notebooks"),
        os.path.join(base_path, "network_security"),
        os.path.join(base_path, "network_security", "components"),
        os.path.join(base_path, "network_security", "constants"),
        os.path.join(base_path, "network_security", "entity"),
        os.path.join(base_path, "network_security", "exception"),
        os.path.join(base_path, "network_security", "logging"),
        os.path.join(base_path, "network_security", "pipeline"),
        os.path.join(base_path, "network_security", "utils"),
        os.path.join(base_path, "network_security", "cloud"),
        os.path.join(base_path, ".github", "workflows")
    ]

    # Create directories
    for directory in directories:
        create_directory(directory)

    # Create files
    create_file(os.path.join(base_path, "requirements.txt"), "pandas\nnumpy\npymongo\npython-dotenv")
    create_file(os.path.join(base_path, ".gitignore"), "venv/\n.env")
    create_file(os.path.join(base_path, "README.md"), "# Project Documentation\n\nDescribe your project here.")
    create_file(os.path.join(base_path, "network_security", "__init__.py"), "")
    create_file(os.path.join(base_path, "setup.py"), "# Setup script for packaging")
    create_file(os.path.join(base_path, "Dockerfile"), "# Dockerfile for containerization")
    create_file(os.path.join(base_path, ".github", "workflows", "main.yml"), "# GitHub Actions Configuration")

if __name__ == "__main__":
    # Set the base path for your project
    project_base_path = "network_security"
    setup_project_structure(project_base_path)

    print("\nProject structure created. Remember to set up your Anaconda environment:")
    print("conda create -p venv python=3.10")
    print("conda activate venv")
