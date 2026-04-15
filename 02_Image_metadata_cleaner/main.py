from pathlib import Path
import shutil
from PIL import Image

BASE_DIR = Path(__file__).resolve().parent


def clean_metadata(path):
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

    try:
        for file in path.rglob("*"):
            file = Path(file)

            if file.is_file() and file.suffix.lower() in img_list:
                with Image.open(file) as img:
                    old_format = img.format
                    old_size = img.size

                    if img.mode in ("RGBA", "P"):
                        img = img.convert("RGB")

                    data = list(img.getdata())

                    new_img = Image.new(img.mode, img.size)
                    new_img.putdata(data)

                    img_path = output_dir / f"clean_{count}.jpg"
                    new_img.save(img_path, optimize=True, quality=90)

                    print("-" * 9)
                    print(file.name)
                    print(f"{old_format}>JPG | {old_size}>{new_img.size}")

                    records += 1
                    count += 1

    except Exception as e:
        print(f"Error: {e}")

    if records == 0:
        print("No images found to clean.")
    else:
        print(f"{records} images cleaned successfully.")


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
        clean_metadata(path)
    else:
        print("404 - Please enter a valid folder path.")