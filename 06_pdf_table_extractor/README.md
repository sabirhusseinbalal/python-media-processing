# PDF Table Extractor

## Description
Extracts structured tables from PDF files and saves them as CSV files.
This project reads a PDF, finds table data page by page, and stores the results inside the output folder.

It helps understand PDF data extraction in Python

It performs:
- Detect tables from PDF pages
- Read rows and columns
- Handle multiple tables
- Save tables as CSV files


## Modules Used
- `pdfplumber` – read PDF and extract tables
- `csv` – save table data
- `pathlib` – file paths
- `shutil` – folder management


## Output
```
Enter full path of the pdf file (or 'q' to quit):

No path provided — using default file: input/sample.pdf
File Loaded: input/sample.pdf

------------------------------
Page 1 - Table 1:
['Name', 'Age', 'City']
['Ali', '20', 'Karachi']

Table saved: output/table_page1_1.csv

Total tables extracted: 1
```


## Features
- Accepts custom PDF path or uses default file
- Extracts tables page by page
- Supports multiple tables in one PDF
- Saves each table separately as CSV
- Fresh output folder each run
- Handles errors safely


## Project Structure
```
06_pdf_table_extractor/
├── input/        # Input PDF files
├── output/       # Extracted CSV tables
├── main.py
└── README.md
```


## Notes
- Best results come from PDFs with clear table structure
- Scanned PDFs may need OCR tools
- Merged cells or complex layouts may extract imperfectly

