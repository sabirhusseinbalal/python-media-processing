# Batch Image Optimizer

## Description
Optimizes multiple images from a folder by resizing and compressing them.

This project reads images from a folder, processes them, and saves optimized versions in a separate output folder.

It helps understand basic image processing in Python.

**YouTube Video:**
[[Batch Image Optimizer | Python Image, Video & Media Processing (Project 1)](https://youtu.be/cxRD5TqnJDY?si=kX_DNgN3RfPQAFTV/)]

---

It performs:
- Resize images to smaller dimensions
- Convert images to JPG format
- Reduce file size using compression
- Process many images automatically


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
image1.png
PNG>JPG | (640, 640)>(300, 300) | RGB>RGB
---------
image2.jpg
JPG>JPG | (512, 512)>(300, 300) | RGB>RGB

2 images optimized successfully.
```


## Features
- Accepts custom folder path or uses default input folder
- Processes images from folder and subfolders
- Supports `.jpg`, `.jpeg`, `.png`
- Converts images to JPG
- Resizes images for optimization
- Compresses images to reduce file size
- Creates fresh output folder
- Handles errors safely


## Project Structure
```
01_batch_image_optimizer/
├── input/        # Input images
├── output/       # Optimized images
├── main.py
└── README.md
```


## Notes
- If no path is given, it uses the input folder
- Output folder is recreated each run (with confirmation)
- Image quality may reduce slightly because of compression
- Good beginner project for learning media processing
