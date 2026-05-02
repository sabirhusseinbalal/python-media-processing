# Media Compression Analyzer

## Description
This project analyzes image compression by reducing file size and comparing before/after results using Python.

It helps understand how compression affects image quality and file size in real-world media processing.


**YouTube Video:**
[[Media Compression Analyzer | Python Image, Video & Media Processing (Project 14)](https://youtu.be/yqgYdCAoHRY?si=e7ZLHSewCpt7q37K/)]

---

## What this project does

- Reads images from a folder
- Compresses them using PIL
- Saves compressed versions
- Compares file sizes
- Calculates compression percentage

---

## What you learn

- File handling using Python
- Image processing basics
- Compression trade-offs (size vs quality)
- Real-world media optimization concepts

---

## Supported formats

- .jpg
- .jpeg
- .png
- .webp
- .bmp

---

## Output Example
```
Enter full folder path (or 'q' to quit): 

Folder Loaded: ...\input
Output folder exists. Delete and continue? (y/n): y

---------------------------
File: ai.jpg
Original Size: 327.31 KB
Compressed Size: 31.83 KB
Compression Saved: 90.28%
---------------------------


---------------------------
File: cat.jpg
Original Size: 37.25 KB
Compressed Size: 13.79 KB
Compression Saved: 62.98%
---------------------------


---------------------------
File: Main.jpg
Original Size: 143.05 KB
Compressed Size: 61.9 KB
Compression Saved: 56.73%
---------------------------


---------------------------
File: peoples.jpg
Original Size: 455.98 KB
Compressed Size: 44.73 KB
Compression Saved: 90.19%
---------------------------


Total images analyzed: 4

Enter full folder path (or 'q' to quit): 
```

---

## Features
- Batch image compression analysis
- Before/after size comparison
- Compression percentage calculation
- Automatic output folder handling

---

## Project Structure
```
14_media_compression_analyzer/
├── input/
│ └── images...
├── output/
│ └── compressed images...
├── main.py
└── README.md
```
