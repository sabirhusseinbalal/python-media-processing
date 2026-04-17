from pathlib import Path
import shutil
import whisper

BASE_DIR = Path(__file__).resolve().parent


def audio_converter(audio_path):
    output_dir = BASE_DIR / "output"

    if output_dir.exists():
        confirm = input("Output folder exists. Delete and continue? (y/n): ").lower()
        if confirm != "y":
            print("Cancelled.")
            return
        shutil.rmtree(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)

    

    try:

        model = whisper.load_model("small")

        # Transcribe the audio
        result = model.transcribe(str(audio_path))


        for segment in result["segments"]:
            start = segment["start"]
            end = segment["end"]
            text = segment["text"]
            count = segment["id"]

            print("\n")
            print(f"SPK_{int(count)+1}")
            print(f"{start:.1f}s --> {end:.1f}s")
            print(text)
            print("---------")

    except Exception as e:
            print(f"Error: {e}")

while True:
    print()
    user_path = input("Enter full path of the audio (or 'q' to quit): ").strip()
    print()

    default_file = BASE_DIR / "input" / "Interstellar_scene.wav"

    if user_path.lower() == "q":
        print("Exiting...")
        break

    if not user_path:
        path = default_file
        if path.is_file():
            print(f"No path provided — using default file: {path}")
        else:
            print("No path provided and default file is missing.")
            continue
    else:
        path = Path(user_path)

    if not path.is_file():
        print("Invalid path!")
        continue

    if path.suffix.lower() == ".wav":
        print(f"File Loaded: {path}")
        audio_converter(path)
    else:
        print("Invalid file type! Only .wav files allowed.")