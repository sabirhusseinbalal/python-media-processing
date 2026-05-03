# Face Blur Tool

## Description
Detects human faces in images using OpenCV and applies blur automatically.

This project reads images from a folder, finds faces using OpenCV Haar Cascade, applies blur to each detected face, and saves the processed images in a separate output folder.

It helps understand basic computer vision and image processing in Python.

It performs:
- Detect faces in images
- Blur detected face regions
- Process multiple images automatically
- Save results in output folder

**YouTube Video:**
[[Face Blur Tool | Python Image, Video & Media Processing (Project 8)](https://youtu.be/Xo0W7MoyxoY/)]

---

## Modules Used
- `cv2 (OpenCV)` – face detection and image processing
- `pathlib` – file and folder handling
- `shutil` – folder management


## Output Example
```
Enter full path of the folder (or 'q' to quit):

No path provided — using default folder: input/
Folder Loaded: input/
Output folder exists. Delete and continue? (y/n): y

Detected 2 face(s).
Blurred image saved to 'output/image1.png'

Detected 1 face(s).
Blurred image saved to 'output/image2.png'

2 images face blurred successfully.
```


## Features
- Accepts custom folder path or uses default input folder
- Processes images from folder and subfolders
- Supports `.jpg`, `.jpeg`, `.png`, `.webp`, `.avif`
- Detects faces automatically
- Blurs only detected faces
- Saves output as `.png`
- Creates fresh output folder
- Handles errors safely


## Project Structure
```
08_face_blur_tool/
├── input/        # Input images
├── output/       # Processed images
├── main.py
└── README.md
```


## Notes
- If no path is given, it uses the input folder
- Output folder is recreated each run (with confirmation)
- Face detection works best on clear front-facing images
- Some side faces or low-quality images may not detect perfectly
- Good beginner project for learning computer vision
