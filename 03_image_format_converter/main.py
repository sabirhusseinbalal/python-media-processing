from pathlib import Path
import shutil
from PIL import Image

BASE_DIR = Path(__file__).resolve().parent


def get_format():
    formats = [".jpg", ".jpeg", ".png", ".webp", ".bmp"]

    while True:
        choice = input("Choose format:\n.jpg, .jpeg, .png, .webp, .bmp\n: ").strip().lower()

        if choice in formats:
            return choice

        print("Invalid choice.")


def convert_images(path):
    output_dir = BASE_DIR / "output"

    if output_dir.exists():
        confirm = input("Output folder exists. Delete and continue? (y/n): ").lower()
        if confirm != "y":
            print("Cancelled.")
            return
        shutil.rmtree(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)

    img_list = [".jpg", ".jpeg", ".png", ".webp", ".bmp"]
    target_format = get_format()

    records = 0
    count = 1
    for file in path.rglob("*"):
        file = Path(file)

        try:
    
            if file.suffix.lower() in img_list and file.is_file():
                with Image.open(file) as img:
                    old_format = img.format
                    old_size = img.size
                    old_mode = img.mode

                    if img.mode in ("RGBA", "P") and target_format in (".jpg", ".jpeg"):
                        img = img.convert("RGB")

                    new_img = img.copy()

                    img_path = output_dir / f"img_{count}{target_format}"
                    new_img.save(img_path)

                    print("-" * 9)
                    print(file.name)
                    print(f"{old_format}>{target_format.upper().replace('.', '')} | {old_size}>{new_img.size} | {old_mode}>{new_img.mode}")

                    records += 1
                    count += 1

        except Exception as e:
            print(f"Failed to process {file.name}: {e}")

    if records == 0:
        print("No images found to convert.")
    else:
        print(f"{records} images converted successfully.")


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
        convert_images(path)
    else:
        print("Invalid folder path.")
