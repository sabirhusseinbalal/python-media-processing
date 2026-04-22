from pathlib import Path
import shutil
import whisper

BASE_DIR = Path(__file__).resolve().parent
model = whisper.load_model("small")

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

        # Transcribe the audio
        result = model.transcribe(str(audio_path))

        output_path = output_dir / "text.txt"
        

        
        with output_path.open('w', encoding="utf-8") as f:

            for i, segment in enumerate(result["segments"], start=1):
                start = segment["start"]
                end = segment["end"]
                text = segment["text"]
              
                print("\n")
                print(f"SPK_{i}")
                print(f"{start:.1f}s --> {end:.1f}s")
                print(text)
                print("---------")

                f.write(f"\nSPK_{i}\n{start:.1f}s --> {end:.1f}s\n{text}\n---------")
            


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
