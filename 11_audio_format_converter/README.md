# Audio Format Converter

## Description
Converts audio files between different formats in batch mode.

This project reads audio files from a folder, changes their format, and saves them in a separate output folder.

It helps understand basic audio processing in Python.

It performs:
- Load multiple audio files
- Choose target output format
- Convert audio formats
- Copy files if format is already the same
- Save all files in output folder

**YouTube Video:**
[[Audio Format Converter | Python Image, Video & Media Processing (Project 11)](https://youtu.be/aPOmx7EzGdo/)]

---

## Modules Used
- `pydub` – audio loading and conversion
- `pathlib` – file and folder handling
- `shutil` – folder management


## Output Example
```
Enter full path of the folder (or 'q' to quit): 

No path provided — using default folder: \input
Folder Loaded: \input
Output folder exists. Delete and continue? (y/n): y
Choose format:
.mp3, .wav, .ogg, .flac, .aac, .m4a
: .wav
Interstellar_scene.wav
Loving Someone More Than Yourself  Good Will Hunting.mp3
Motivation Keep Moving Forward  ROCKY BALBOA.mp3
Pursuit Of Happyness Iconic Speech.mp3
What is Hope  Tim Robbins, Morgan Freeman, Bob Gunton  The Shawshank Redemption #shorts.mp3
5 audio converted successfully.

Enter full path of the folder (or 'q' to quit): q

Exiting...
```



## Features
- Accepts custom folder path or uses default input folder
- Processes files from folder and subfolders
- Supports `.mp3`, `.wav`, `.ogg`, `.flac`, `.aac`, `.m4a`
- Lets user choose target format
- Converts all supported audio files
- Copies files directly if they are already in the target format
- Creates fresh output folder
- Handles errors safely


## Project Structure
```
11_audio_format_converter/
├── input/        # Input audio files
├── output/       # Converted audio files
├── main.py
└── README.md
```


## Notes
- Requires ffmpeg installed for some formats
- Conversion speed depends on file size
- Output quality may vary by format
- If no path is given, it uses the input folder
- Good beginner project for learning audio processing
