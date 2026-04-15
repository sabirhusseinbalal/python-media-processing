from pathlib import Path
import shutil
import pdfplumber
import csv

BASE_DIR = Path(__file__).resolve().parent



def extract_tables(file_path):
    output_dir = BASE_DIR / "output"

    if output_dir.exists():
        confirm = input("Output folder exists. Delete and continue? (y/n): ").lower()
        if confirm != "y":
            print("Cancelled.")
            return
        shutil.rmtree(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)



    try: 

        output_csv = True

        with pdfplumber.open(file_path) as pdf:
            table_count = 0
            for page_num, page in enumerate(pdf.pages, start=1):
                tables = page.extract_tables()
                if not tables:
                    continue  # Skip pages without tables

                for table_index, table in enumerate(tables, start=1):
                    table_count += 1
                    print("-" * 30)
                    print(f"\nPage {page_num} - Table {table_index}:")


                    for row in table:
                        if any(row):
                            print(row)


                    # Save table as CSV if requested
                    if output_csv:
                        csv_filename = output_dir / f"table_page{page_num}_{table_index}.csv"
                        with open(csv_filename, "w", newline="", encoding="utf-8") as f:
                            writer = csv.writer(f)
                            writer.writerows(table)
                        print(f"Table saved: {csv_filename}")

            if table_count == 0:
                print("No tables found in the PDF.")
            else:
                print(f"\nTotal tables extracted: {table_count}")


    except Exception as e:
        print(f"Error: {e}")


while True:
    print()
    user_path = input("Enter full path of the pdf file (or 'q' to quit): ").strip()
    print()

    default_folder = BASE_DIR / "input" / "sample.pdf"

    if user_path.lower() == "q":
        print("Exiting...")
        break

    if not user_path:
        path = default_folder
        if path.is_file():
            print(f"No path provided — using default file: {path}")
        else:
            print("No path provided and default file is missing.")
            continue
    else:
        path = Path(user_path)

        if not path.is_file():
            print("Invalid Path!")
            continue

    if path.suffix.lower() == ".pdf":
        print(f"File Loaded: {path}")
        extract_tables(path)
    else:
        print("Invalid file type! only .pdf files allowed.")