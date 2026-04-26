# Image Format Converter

## Description
Converts multiple images into another format.

This project reads images from a folder and saves converted copies in a new output folder.

It helps understand how image formats work in Python.

It performs:
- Convert images to another format
- Process multiple files automatically
- Save clean output copies

**YouTube Video:**
[[Image Format Converter | Python Image, Video & Media Processing (Project 3)](https://youtu.be/Nu8Pv16ovag?si=yUUUYV248EQoRaj2/)]

---

## Modules Used
- `PIL (Pillow)` – image processing
- `pathlib` – file and folder handling
- `shutil` – folder management


## Output
```
Enter full path of the folder (or 'q' to quit):

No path provided — using default folder: input/
Folder Loaded: input/

Choose format:
.jpg, .jpeg, .png, .webp, .bmp
: .png

---------
image1.jpg
JPEG>PNG | (640, 640)>(640, 640) | RGB>RGB

---------
image2.png
PNG>PNG | (512, 512)>(512, 512) | RGBA>RGBA

2 images converted successfully.
```


## Features
- Accepts custom folder path or uses default input folder
- Supports multiple images
- Converts to selected format
- Supports `.jpg`, `.jpeg`, `.png`, `.webp`, `.bmp`
- Creates clean output folder
- Handles errors safely


## Project Structure
```
03_image_format_converter/
├── input/
├── output/
├── main.py
└── README.md
```


## Notes
- If no path is given, the program uses the input folder
- Output folder is recreated each run (with confirmation)
- JPG does not support transparency
- Good beginner project for learning image formats
