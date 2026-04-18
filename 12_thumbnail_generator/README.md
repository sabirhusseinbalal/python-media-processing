# Thumbnail Generator

## Description
Creates simple thumbnails from images by resizing them and adding custom text.
This project reads images from a folder, asks for text for each image, then generates thumbnail-style output images.

It helps practice image editing, text drawing, batch processing, and file handling in Python.

It performs:
- Load images from folder
- Resize image to thumbnail size
- Ask custom text for each image
- Draw text on image
- Save new thumbnails in output folder

## Modules Used
- `Pillow` – image processing and text drawing
- `pathlib` – file and folder paths
- `shutil` – delete old output folder


## Output
```
Enter full path of the folder (or 'q' to quit):

No path provided — using default folder: input/
Folder Loaded: input/
Output folder exists. Delete and continue? (y/n): y

Enter Text for image1.png: Hi, my name is Sabir Hussain, and I feel like a loser.
Saved: output/image1.jpeg

Enter Text for image2.png: But InshaAllah, one day I will rise.
Saved: output/image2.jpeg

2 thumbnails created successfully.

Enter full path of the folder (or 'q' to quit): q
Exiting...
```



## Features
- Uses custom folder path or default input folder
- Supports `.jpg`, `.jpeg`, `.png`
- Asks different text for each image
- Resizes image to thumbnail size
- Adds text overlay
- Creates fresh output folder
- Saves optimized JPEG files
- Handles errors safely


## Project Structure
```
12_thumbnail_generator/
├── input/
│   ├── image1.png
│   └── image2.png
├── output/
├── main.py
└── README.md
```


## Notes
- This is a beginner thumbnail project
- Text position is fixed in code
- You can improve fonts, colors, shadows, wrapping, and design later
- Great project for learning Pillow basics
- Small tools like this build strong foundations