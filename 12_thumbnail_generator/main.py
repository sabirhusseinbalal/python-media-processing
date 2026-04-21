from pathlib import Path
import shutil
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = Path(__file__).resolve().parent


def thumbnail_create(path):
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

    try:
        font = ImageFont.load_default()

        for file in path.rglob("*"):
            file = Path(file)

            if file.is_file() and file.suffix.lower() in img_list:

                while True:
                    text = input(f"Enter Text for {file.name}: ").strip()

                    if text:
                        break

                    print("Text cannot be empty!")

                with Image.open(file) as img:

                    if img.mode in ("RGBA", "P"):
                        img = img.convert("RGB")

                    new_img = img.copy()
                    new_img.thumbnail((1280, 720))

                    draw = ImageDraw.Draw(new_img)

                    draw.rectangle((0, 0, new_img.width, 80), fill="black")

                    draw.text(
                        xy=(20, 25),
                        text=text,
                        fill="white",
                        font=font
                    )

                    img_path = output_dir / f"{file.stem}.jpeg"
                    new_img.save(img_path, optimize=True, quality=60)

                    print(f"Saved: {img_path}")
                    records += 1

    except Exception as e:
        print(f"Error: {e}")

    if records == 0:
        print("No images found.")
    else:
        print(f"{records} thumbnails created successfully.")


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
        thumbnail_create(path)
    else:
        print("Invalid folder path.")
