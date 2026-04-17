from pathlib import Path
import shutil
from pydub import AudioSegment

BASE_DIR = Path(__file__).resolve().parent


def get_format():
    formats = [".mp3", ".wav", ".ogg", ".flac", ".aac", ".m4a"]

    while True:
        choice = input("Choose format:\n.mp3, .wav, .ogg, .flac, .aac, .m4a\n: ").strip().lower()

        if choice in formats:
            return choice

        print("Invalid choice.")


def convert_audio(path):
    output_dir = BASE_DIR / "output"

    if output_dir.exists():
        confirm = input("Output folder exists. Delete and continue? (y/n): ").lower()
        if confirm != "y":
            print("Cancelled.")
            return

        shutil.rmtree(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)

    format_list = [".mp3", ".wav", ".ogg", ".flac", ".aac", ".m4a"]
    target_format = get_format()

    records = 0

    try:
        for file in path.rglob("*"):
            file = Path(file)

            if file.is_file() and file.suffix.lower() in format_list:

                print(file)

                # same format → just copy
                if file.suffix.lower() == target_format:
                    shutil.copy(file, output_dir / file.name)

                # different format → convert
                else:
                    audio = AudioSegment.from_file(
                        str(file),
                        format=file.suffix.lower().replace(".", "")
                    )

                    audio.export(
                        output_dir / f"{file.stem}{target_format}",
                        format=target_format.replace(".", "")
                    )

                records += 1

    except Exception as e:
        print(f"Error: {e}")

    if records == 0:
        print("No audio found to convert.")
    else:
        print(f"{records} audio converted successfully.")


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
        convert_audio(path)
    else:
        print("404 - Please enter a valid folder path.")