# Text Extractor (Image → Text)

## Description
Extracts text from images using OCR (Optical Character Recognition).

This project reads images from a folder and converts visible text into .txt files.

It helps understand how computers read images in real life using Python.

It performs:
- Read images from a folder
- Convert image to grayscale
- Extract text using OCR
- Save text into files
- Process multiple images automatically


## Modules Used
- `PIL (Pillow)` – image processing
- `pytesseract` – OCR engine
- `pathlib` – file and folder handling
- `shutil` – folder management


## Output
```
Enter full path of the folder (or 'q' to quit):

No path provided — using default folder: input/
Folder Loaded: input/
Output folder exists. Delete and continue? (y/n): y

---------
image9.jpg
AssalamuAlaikum

Welcome to my Python Projects Roadmap
(From Basics to Advanced)

Image, Video & Media Processing - 14
Projects (Group-4)

Sabir Hussain Balal
Saved: text_8.txt
8 image(s) processed successfully.

Enter full path of the folder (or 'q' to quit): 
```


## Features
- Accepts custom folder path or uses default input folder
- Reads images from folder and subfolders
- Supports `.jpg`, `.jpeg`, `.png`
- Extracts text using OCR
- Saves output into `.txt` files
- Handles empty results safely
- Simple loop-based workflow


## Project Structure
```
04_text_extractor-image/
├── input/        # Input images
├── output/       # Extracted text files
├── main.py
└── README.md
```


## Notes
- OCR is not 100% accurate
- Results depend on image quality, font, and background
- Some images may return messy or partial text
- This is normal for real OCR systems
- Good beginner project for learning image processing
