# Background Removal

## Description
Removes the background from multiple images inside a folder automatically.
This project reads images from a folder, removes the background, and saves transparent PNG images in a separate output folder.

It helps understand practical AI image processing in Python.

It performs:
- Remove background automatically
- Process many images in one run
- Search images from subfolders
- Convert output to PNG
- Save clean transparent images


## Modules Used
- `rembg` – AI background removal
- `pathlib` – file and folder paths
- `shutil` – folder management
- `PIL (Pillow)` – image support


## Output
```
Enter full path of the folder (or 'q' to quit):

No path provided — using default folder: input/
Folder Loaded: input/
Output folder exists. Delete and continue? (y/n): y

Background removed successfully! Saved to 'output/imag2.png'
Background removed successfully! Saved to 'output/image1.png'
Background removed successfully! Saved to 'output/image3.png'

6 images background removed successfully.
```


## Features
- Accepts custom folder path or uses default input folder
- Processes images from folder and subfolders
- Supports mixed image formats
- Removes background automatically
- Saves output as PNG
- Creates fresh output folder
- Handles errors safely
- Beginner-friendly real project


## Project Structure
```
07_background_removal/
├── input/        # Original images
├── output/       # Background removed images
├── main.py
└── README.md
```


## Notes
- If no path is given, it uses the input folder
- Output folder is recreated each run (with confirmation)
- First run may download AI model files
- Speed depends on image size and system performance
- Good beginner project for learning AI tools
