# Image Dataset Organizer (AI Based)

## Description
Organizes a mixed image dataset using a pretrained AI model (ResNet50).
The program detects objects inside images and automatically sorts them into folders based on predicted categories.

If confidence is low, images are moved to an `"others"` folder.

---

## What It Does
- Reads images from input folder
- Uses pretrained ResNet50 model
- Predicts image category (cat, dog, car, etc.)
- Creates folders automatically
- Moves images into correct category folder
- Handles unknown images using confidence threshold

---

## Modules Used
- `torchvision` – pretrained AI model (ResNet50)
- `Pillow` – image handling and saving
- `pathlib` – file system handling
- `shutil` – folder cleanup

---


## Output
```
Enter full path of the folder (or 'q' to quit): 

Folder Loaded: \input
Output folder exists. Delete and continue? (y/n): y
ai.jpg → tripod (19.0%)
cat.jpg → tiger cat (32.4%)
cat_2.jpg → tiger cat (14.7%)
cat_3.jpg → tabby (19.2%)
dog.jpg → Border collie (29.6%)
....

20 images organized successfully.

Enter full path of the folder (or 'q' to quit): q

Exiting...
```

---

## Features
- AI-based image classification
- Automatic folder creation
- Batch image processing
- Confidence-based filtering
- Handles unknown images safely
- Simple dataset organizer for ML preparation

---

## Project Structure
```
13_image_dataset_organizer/
├── input/
│ ├── cat.jpg
│ ├── dog.jpg
│ └── lion.jpg
├── output/
│ ├── cat/
│ ├── dog/
│ ├── lion/
│ └── others/
├── main.py
└── README.md
```

---

## Notes
- First run may download pretrained model
- Accuracy depends on image quality
- Model may misclassify unusual images
- This is a beginner-friendly AI project for dataset preparation