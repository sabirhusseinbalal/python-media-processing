# PDF Text Extractor

## Description
Extracts text from PDF files and saves it into a `.txt` file.
This project reads a PDF, gets text page by page, and stores the result in an output folder.

It helps understand basic PDF handling in Python.

It performs:
- Read PDF files
- Extract text from each page
- Save text into one file
- Process pages in order


## Modules Used
- `pdfplumber` – PDF text extraction
- `pathlib` – file and folder handling
- `shutil` – folder management


## Output
```
Enter full path of the pdf file (or 'q' to quit): 

No path provided — using default file: input\30-Short-Stories-with-Moral-10-Line-Short-Stories.pdf
File Loaded: input\30-Short-Stories-with-Moral-10-Line-Short-Stories.pdf
Output folder exists. Delete and continue? (y/n): y

Text saved successfully: output\data.txt

Enter full path of the pdf file (or 'q' to quit): 
```


## Features
- Accepts custom PDF path or uses default input file
- Supports `.pdf` files only
- Extracts text page by page
- Saves all text into data.txt
- Creates fresh output folder
- Handles errors safely
- Simple beginner-friendly structure


## Project Structure
```
05_text_extractor-pdf/
├── input/        # Input PDF files
├── output/       # Extracted text file
├── main.py
└── README.md
```


## Notes
- Works best with text-based PDFs
- Some PDFs may give messy output
- Result depends on PDF structure and formatting
- Scanned/image PDFs need OCR tools

