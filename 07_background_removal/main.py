from pathlib import Path
import shutil
from rembg import remove
from PIL import Image

BASE_DIR = Path(__file__).resolve().parent


def bg_remover(path):
    output_dir = BASE_DIR / "output"

    if output_dir.exists():
        confirm = input("Output folder exists. Delete and continue? (y/n): ").lower()
        if confirm != "y":
            print("Cancelled.")
            return
        shutil.rmtree(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)



    records = 0
  

    try:
        for file in path.rglob("*"):
            file = Path(file)

            if file.is_file():
                    # Open the input image
                    with open(file, "rb") as inp_file:
                        input_data = inp_file.read()

                    # Remove background
                    output_data = remove(input_data)

                    output_path = output_dir / f"{file.stem}.png"

                    # Save the output image
                    with open(output_path, "wb") as out_file:
                        out_file.write(output_data)

                    print(f"Background removed successfully! Saved to '{output_path}'")

                    records += 1

    except Exception as e:
        print(f"Error: {e}")

    if records == 0:
        print("No images found.")
    else:
        print(f"{records} images background removed successfully.")


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
        bg_remover(path)
    else:
        print("Invalid folder path.")
