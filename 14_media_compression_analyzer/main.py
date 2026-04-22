from pathlib import Path
from PIL import Image
import shutil
import os

BASE_DIR = Path(__file__).resolve().parent


def get_size_kb(path):
    return round(os.path.getsize(path) / 1024, 2)


def compress_image(file, output_dir):
    with Image.open(file) as img:

        original_size = get_size_kb(file)

        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        # Resize (compression effect)
        img.thumbnail((1280, 1280))

        output_path = output_dir / f"{file.stem}_compressed.jpg"
        img.save(output_path, "JPEG", optimize=True, quality=60)

        compressed_size = get_size_kb(output_path)

        # safety check (avoid divide by zero)
        if original_size == 0:
            ratio = 0
        else:
            ratio = round((1 - compressed_size / original_size) * 100, 2)

        print("\n---------------------------")
        print(f"File: {file.name}")
        print(f"Original Size: {original_size} KB")
        print(f"Compressed Size: {compressed_size} KB")
        print(f"Compression Saved: {ratio}%")
        print("---------------------------\n")


def analyze_folder(path):
    output_dir = BASE_DIR / "output"

    if output_dir.exists():
        confirm = input("Output folder exists. Delete and continue? (y/n): ").lower()
        if confirm != "y":
            print("Cancelled.")
            return
        shutil.rmtree(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)

    img_formats = [".jpg", ".jpeg", ".png", ".webp", ".bmp"]
    count = 0

    for file in path.rglob("*"):
        file = Path(file)

        try:
            if file.is_file() and file.suffix.lower() in img_formats:
                compress_image(file, output_dir)
                count += 1

        except Exception as e:
            print(f"Failed to process {file.name}: {e}")

    if count == 0:
        print("No images found.")
    else:
        print(f"\nTotal images analyzed: {count}")


while True:
    print()
    user_path = input("Enter full folder path (or 'q' to quit): ").strip()
    print()

    default_folder = BASE_DIR / "input"

    if user_path.lower() == "q":
        print("Exiting...")
        break

    if not user_path:
        path = default_folder
    else:
        path = Path(user_path)

    if path.is_dir():
        print(f"Folder Loaded: {path}")
        analyze_folder(path)
    else:
        print("Invalid folder path!")
