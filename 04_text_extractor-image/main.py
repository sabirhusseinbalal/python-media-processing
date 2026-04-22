from pathlib import Path
import shutil
from PIL import Image
import pytesseract

BASE_DIR = Path(__file__).resolve().parent

# Set path only if Tesseract is not in system PATH
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text(path):
    output_dir = BASE_DIR / "output"

    if output_dir.exists():
        confirm = input("Output folder exists. Delete and continue? (y/n): ").lower()
        if confirm != "y":
            print("Cancelled.")
            return
        shutil.rmtree(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)

    img_list = [".jpg", ".jpeg", ".png"]

    records = 0
    count = 1

   
    for file in path.rglob("*"):
        file = Path(file)
        try:

            if file.is_file() and file.suffix.lower() in img_list:
                with Image.open(file) as image:
                    gray_image = image.convert("L")
                    text = pytesseract.image_to_string(gray_image)
                    clean_text = text.replace("\x0c", "").strip()

                print("-" * 9)
                print(file.name)

                if clean_text:
                    print(clean_text)

                    txt_path = output_dir / f"text_{count}.txt"
                    with open(txt_path, "w", encoding="utf-8") as f:
                        f.write(clean_text)

                    print(f"Saved: {txt_path.name}")
                else:
                    print("No text found.")

                records += 1
                count += 1

        except Exception as e:
            print(f"Failed to process {file.name}: {e}")

    if records == 0:
        print("No supported images found.")
    else:
        print(f"{records} image(s) processed successfully.")


while True:
    print()
    user_path = input("Enter full path of the folder (or 'q' to quit): ").strip()
    print()

    default_folder = BASE_DIR / "input"

    if user_path.lower() == "q":
        print("Exiting...")
        break

    if not user_path:
        path = default_folder
        if path.is_dir():
            print(f"No path provided — using default folder: {path}")
        else:
            print("No path provided and default folder is missing.")
            continue
    else:
        path = Path(user_path)

    if path.is_dir():
        print(f"Folder Loaded: {path}")
        extract_text(path)
    else:
        print("Invalid folder path.")
