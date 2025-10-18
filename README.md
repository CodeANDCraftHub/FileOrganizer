# Python File Organizer

Organize your messy folders automatically with Python in minutes!
This beginner-friendly script sorts files by type, creates folders, and moves everything into place.

---

## Features

* Auto-organize files by extension
* Safe workflow with **dry-run mode** before moving files
* Timestamped **log file** to see what changed
* Duplicate file renaming (`file_1`, `file_2`, …)
* Optional **whitelist/skip extensions**
* Works on Windows & macOS

---

## Prerequisites

* Python 3.x installed
* Basic command line usage
* A test folder with mixed files to practice

---

## Libraries Used

* `os` — file system operations
* `shutil` — move files
* `pathlib` — clean path handling
* `datetime` — timestamped logs

---

## Installation

1. Clone this repository:

```bash
git clone https://github.com/CodeANDCraftHub/FileOrganizer.git
cd FileOrganizer
```

2. Make sure your test folder has some mixed files (or use the included `example_folder/`).

---

## Example Folder Structure

```
example_folder/
├── test_image.jpg
├── test_video.mp4
├── test_doc.pdf
├── test_audio.mp3
├── test_script.py
├── test_archive.zip
├── random_file.xyz
├── test_app.exe
```

---

## How to Run

1. Open `file_organizer.py` and set your folder:

```python
SOURCE_DIR = Path.home() / "Downloads"  # or your folder path
```

2. Run in **dry-run mode** first to preview changes:

```bash
python file_organizer.py
```

3. Check the generated log file to see which files would be moved:

```
file_organizer_log_YYYYMMDD_HHMMSS.txt
```

4. When ready, set:

```python
dry_run = False
```

and run again to actually move files.

---

## Optional Settings

* **Whitelist extensions** to skip certain files:

```python
whitelist_extensions = [".txt", ".md"]
```

* **Add/Update file types** by editing the `file_types` dictionary in the script.

---

## Real-World Use Cases

* Clean Downloads or Desktop clutter
* Batch organize project assets, images, PDFs, and docs
* Keep screenshot folders tidy

---

## Notes

* Duplicate files are automatically renamed
* Safe to re-run: only processes files in the root folder
* Works on both Windows and macOS (update folder path format as needed)

---

## Next Steps

Check out my **Python screenshot automation tool** — automatically timestamps and organizes your screenshots.

---

## Links

* Full script: `file_organizer.py`
* Example folder: `example_folder/`

---

## Support

If this script saved you time, subscribe to **Code & Craft Hub** on YouTube for more Python automation projects and practical, beginner-friendly scripts.


