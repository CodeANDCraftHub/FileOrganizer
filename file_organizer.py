# file_organizer.py

import os
import shutil
from pathlib import Path
from datetime import datetime

# ==========================
# CONFIGURATION
# ==========================
# Path to the folder you want to organize
SOURCE_DIR = Path.home() / "Downloads"  # Change as needed

# Dry run mode: True = only print actions, False = move files
dry_run = True

# Optional whitelist: files with these extensions will be skipped
whitelist_extensions = []  # e.g., [".txt", ".md"]

# Log file path
log_file = SOURCE_DIR / f"file_organizer_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

# ==========================
# FILE TYPES
# ==========================
file_types = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff", ".webp", ".heic"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv", ".webm"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".odt", ".rtf", ".log"],
    "Spreadsheets": [".xls", ".xlsx", ".csv", ".ods"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
    "Scripts": [".py", ".js", ".html", ".css", ".bat", ".sh", ".ps1"],
    "Applications": [".exe", ".msi", ".apk", ".dmg"],
    "PDFs & eBooks": [".epub", ".mobi", ".azw3"],
    "Misc": []  # fallback for unknown files
}

# ==========================
# FUNCTIONS
# ==========================
def log_action(message: str):
    print(message)
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(message + "\n")


def get_unique_filename(dest_folder: Path, filename: str) -> str:
    """If file exists, append _1, _2, etc."""
    base, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    while (dest_folder / new_filename).exists():
        new_filename = f"{base}_{counter}{ext}"
        counter += 1
    return new_filename


def organize_files():
    log_action(f"Organizing folder: {SOURCE_DIR}")
    files = [f for f in SOURCE_DIR.iterdir() if f.is_file()]

    for file_path in files:
        file_ext = file_path.suffix.lower()

        if file_ext in whitelist_extensions:
            log_action(f"Skipped (whitelist): {file_path.name}")
            continue

        moved = False

        # Match file type
        for folder_name, extensions in file_types.items():
            if file_ext in extensions and folder_name != "Misc":
                dest_folder = SOURCE_DIR / folder_name
                dest_folder.mkdir(exist_ok=True)
                new_name = get_unique_filename(dest_folder, file_path.name)

                if dry_run:
                    log_action(f"[DRY RUN] Move '{file_path.name}' → '{folder_name}/{new_name}'")
                else:
                    shutil.move(str(file_path), str(dest_folder / new_name))
                    log_action(f"Moved '{file_path.name}' → '{folder_name}/{new_name}'")
                moved = True
                break

        # If no match, move to Misc
        if not moved:
            misc_folder = SOURCE_DIR / "Misc"
            misc_folder.mkdir(exist_ok=True)
            new_name = get_unique_filename(misc_folder, file_path.name)

            if dry_run:
                log_action(f"[DRY RUN] Move '{file_path.name}' → 'Misc/{new_name}'")
            else:
                shutil.move(str(file_path), str(misc_folder / new_name))
                log_action(f"Moved '{file_path.name}' → 'Misc/{new_name}'")

    log_action("✅ Files organized successfully!")
    log_action(f"Log saved to: {log_file}")


if __name__ == "__main__":
    organize_files()
