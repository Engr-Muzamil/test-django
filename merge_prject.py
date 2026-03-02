import os

# Jis folder ko scan karna hai (current directory)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Output file name
OUTPUT_FILE = "FULL_PROJECT_CODE.txt"

# Kaun kaun si file types include karni hain
ALLOWED_EXTENSIONS = [".py", ".html", ".css", ".js"]

# Kaun se folders ignore karne hain
IGNORE_DIRS = ["venv", "__pycache__", ".git", "migrations", "node_modules"]

with open(OUTPUT_FILE, "w", encoding="utf-8") as outfile:

    for root, dirs, files in os.walk(BASE_DIR):

        # Ignore unwanted directories
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        for file in files:
            if any(file.endswith(ext) for ext in ALLOWED_EXTENSIONS):

                file_path = os.path.join(root, file)

                # Relative path show kare
                relative_path = os.path.relpath(file_path, BASE_DIR)

                outfile.write("\n\n")
                outfile.write("=" * 80 + "\n")
                outfile.write(f"FILE: {relative_path}\n")
                outfile.write("=" * 80 + "\n\n")

                try:
                    with open(file_path, "r", encoding="utf-8") as infile:
                        outfile.write(infile.read())
                except Exception as e:
                    outfile.write(f"Error reading file: {e}\n")

print(f"\n✅ Done! All code merged into {OUTPUT_FILE}")