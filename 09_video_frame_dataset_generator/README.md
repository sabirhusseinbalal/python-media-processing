# Video Frame Dataset Generator

## Description
Extracts frames from video files and saves them as images automatically for dataset creation.

This project reads a video, captures frames at intervals, and stores them in a separate output folder. It helps create image datasets from videos for learning, analysis, and machine learning projects.


It performs:
- Read video files
- Extract frames automatically
- Save frames as images
- Create dataset from video content

**YouTube Video:**
[[Video Frame Dataset Generator | Python Image, Video & Media Processing (Project 9)](https://youtu.be/EophbTofyzw/)]

---

## Modules Used
- `cv2 (OpenCV)` – video reading and frame extraction
- `pathlib` – file and folder handling
- `shutil` – folder management


## Output Example
```
Enter full path of the video (or 'q' to quit):

No path provided — using default file: input/sample.mp4
File Loaded: input/sample.mp4
Output folder exists. Delete and continue? (y/n): y

Total frames read: 688
23 frames extracted successfully.
```


## Features
- Accepts custom video path or uses default input file
- Supports `.mp4` files
- Extracts frames automatically
- Saves every 30th frame
- Creates fresh output folder
- Handles invalid paths safely
- Useful for dataset creation


## Project Structure
```
09_video_frame_dataset_generator/
├── input/
│   └── sample.mp4
├── output/
├── main.py
└── README.md
```


## Notes
- If no path is given, it uses the default video file
- Output folder is recreated each run (with confirmation)
- Saving every 30th frame reduces duplicate images
- Great beginner project for learning video processing
- Useful for future computer vision and ML datasets
