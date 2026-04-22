# Audio to Text Converter

## Description
Converts spoken audio into text using OpenAI Whisper speech recognition model.

This project reads a `.wav` audio file, transcribes speech, displays text with timestamps, and saves the transcript into a text file.

It helps understand basic speech recognition and audio processing in Python.

It performs:
- Load audio file
- Convert speech to text
- Split text into timed segments
- Display transcript in terminal
- Save transcript to `.txt` file

## Modules Used
- `whisper` – speech-to-text transcription
- `pathlib` – file and folder handling
- `shutil` – folder management


## Output
```
Enter full path of the video (or 'q' to quit):

No path provided — using default file: input/Interstellar_scene.wav
File Loaded: input/Interstellar_scene.wav
Output folder exists. Delete and continue? (y/n): y

SPK_1
0.0s --> 1.2s
 Hey, Mark.
---------


SPK_2
1.2s --> 2.7s
 You son of a *****.
---------


SPK_3
7.2s --> 9.6s
 I never made one of these when you were still responding,
---------


SPK_4
9.6s --> 11.4s
 because I was so mad at you for leaving.
---------


SPK_5
15.0s --> 16.6s
 And then when you went quiet,
---------


SPK_6
19.7s --> 22.2s
 it seemed like I should live with that decision and I have.
---------


SPK_7
27.1s --> 29.0s
 But today is my birthday.
---------


SPK_8
31.0s --> 34.0s
 And it's a special one because you told me...
---------


SPK_9
38.0s --> 42.0s
 You once told me that when you came back we might be the same age.
---------


SPK_10
44.0s --> 47.0s
 And today I'm the age you were when you left.
---------


SPK_11
50.0s --> 53.0s
 It would be a real good time for you to come back.
---------

Enter full path of the audio (or 'q' to quit): q

Exiting...
```

Transcript also saved to:
```
output/text.txt
```


## Features
- Accepts custom audio path or uses default input file
- Supports `.wav` audio files
- Converts speech into text
- Shows timestamps for each segment
- Saves transcript into text file
- Uses local OpenAI Whisper model for transcription
- Creates fresh output folder
- Handles errors safely


## Project Structure
```
10_audio_to_text_converter/
├── input/
│   └── Interstellar_scene.wav
├── output/
│   └── text.txt
├── main.py
└── README.md
```


## Notes
- First run may download Whisper model files
- Processing speed depends on CPU/GPU
- Accuracy depends on audio quality and noise
- Better microphone/audio = better results
- Great beginner project for learning AI audio tools
