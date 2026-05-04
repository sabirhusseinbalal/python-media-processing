# Image Metadata Cleaner

## Description
Removes hidden metadata from images and saves clean copies in a new folder.

This project helps understand image privacy and how hidden file data can be removed before sharing images online.

It performs:
- Reads images from a folder
- Creates clean copies using pixel data only
- Removes hidden metadata
- Saves cleaned images in output folder

**YouTube Video:**
[[Image Metadata Cleaner | Python Image, Video & Media Processing (Project 2)](https://youtu.be/aZ8K_S1caU4?si=NFOJNNjm-FyzNsPU/)]

---

## Modules Used
- `PIL (Pillow)` – image processing
- `pathlib` – file and folder handling
- `shutil` – folder management


## Output Example
```
Enter full path of the folder (or 'q' to quit):

No path provided — using default folder: input/
Folder Loaded: input/
Output folder exists. Delete and continue? (y/n): y

---------
image1.jpg
PNG>JPG | (640, 640)>(640, 640)
---------
image2.jpg
PNG>JPG | (640, 640)>(640, 640)

2 images cleaned successfully.
```


## Features
- Accepts custom folder path or uses default input folder
- Processes images from folder and subfolders
- Supports `.jpg`, `.jpeg`, `.png`
- Removes metadata by rebuilding image data
- Saves clean JPG copies
- Creates fresh output folder
- Handles errors safely


## Project Structure
```
02_Image_metadata_cleaner/
├── input/        # Input images
├── output/       # Cleaned images
├── main.py
└── README.md
```


## Notes
- If no path is given, it uses the input folder
- Output folder is recreated each run (with confirmation)
- Cleaned images keep visual content but remove hidden data
- Good beginner project for privacy-focused image processing
