from pathlib import Path
import shutil
import cv2

BASE_DIR = Path(__file__).resolve().parent


def video_frame(video_path):
    output_dir = BASE_DIR / "output"

    if output_dir.exists():
        confirm = input("Output folder exists. Delete and continue? (y/n): ").lower()
        if confirm != "y":
            print("Cancelled.")
            return
        shutil.rmtree(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)

    try:
        cap = cv2.VideoCapture(str(video_path))

        if not cap.isOpened():
            print("Unable to open video file.")
            return

        frame_count = 0
        saved_count = 0
        interval = 30   # save every 30th frame

        while True:
            ret, frame = cap.read()

            if not ret:
                break

            if frame_count % interval == 0:
                output_path = output_dir / f"frame{saved_count:05d}.jpg"
                cv2.imwrite(str(output_path), frame)
                saved_count += 1

            frame_count += 1

        cap.release()

        print(f"Total frames read: {frame_count}")
        print(f"{saved_count} frames extracted successfully.")

    except Exception as e:
        print(f"Error: {e}")


while True:
    print()
    user_path = input("Enter full path of the video (or 'q' to quit): ").strip()
    print()

    default_file = BASE_DIR / "input" / "sample.mp4"

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

    if path.suffix.lower() == ".mp4":
        print(f"File Loaded: {path}")
        video_frame(path)
    else:
        print("Invalid file type! Only .mp4 files allowed.")