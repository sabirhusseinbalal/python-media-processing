from pathlib import Path
import shutil
import pdfplumber

BASE_DIR = Path(__file__).resolve().parent



def extract_text(file_path):
    output_dir = BASE_DIR / "output"

    if output_dir.exists():
        confirm = input("Output folder exists. Delete and continue? (y/n): ").lower()
        if confirm != "y":
            print("Cancelled.")
            return
        shutil.rmtree(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)


    try:

        save_path = output_dir / "data.txt"


        with pdfplumber.open(file_path) as pdf, open(save_path, "w", encoding="utf-8") as f:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    #f.write(text + '\n')
                    f.write(f"{"-"*9}\nPage: {page.page_number}\n{"-"*9}\n{text}\n\n\n")
        
        print(f"\nText saved successfully: {save_path}")



    except Exception as e:
        print(f"Error: {e}")


while True:
    print()
    user_path = input("Enter full path of the pdf file (or 'q' to quit): ").strip()
    print()

    default_folder = BASE_DIR / "input" / "30-Short-Stories-with-Moral-10-Line-Short-Stories.pdf"

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
        extract_text(path)
    else:
        print("Invalid file type! only .pdf files allowed.")