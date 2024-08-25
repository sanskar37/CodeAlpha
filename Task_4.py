import os
import shutil
from pathlib import Path

source_dir = "/path"

target_dir = "/path"

file_types = {
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'Music': ['.mp3', '.wav', '.aac'],
    'Archives': ['.zip', '.rar', '.7z'],
    'Scripts': ['.py', '.js', '.sh'],
}

def create_folders():
    for folder in file_types.keys():
        folder_path = Path(target_dir) / folder
        if not folder_path.exists():
            folder_path.mkdir(parents=True, exist_ok=True)

def organize_files():
    for filename in os.listdir(source_dir):
        file_path = Path(source_dir) / filename
        if file_path.is_file():
            file_extension = file_path.suffix.lower()
            moved = False

            for folder, extensions in file_types.items():
                if file_extension in extensions:
                    shutil.move(str(file_path), str(Path(target_dir) / folder / filename))
                    moved = True
                    break

            # If file doesn't match any known types, move it to 'Others'
            if not moved:
                other_folder = Path(target_dir) / 'Others'
                if not other_folder.exists():
                    other_folder.mkdir(parents=True, exist_ok=True)
                shutil.move(str(file_path), str(other_folder / filename))

def main():
    create_folders()
    organize_files()
    print("Files have been organized!")

if __name__ == "__main__":
    main()
