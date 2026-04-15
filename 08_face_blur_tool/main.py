from pathlib import Path
import shutil
import cv2
from PIL import Image

BASE_DIR = Path(__file__).resolve().parent


def face_blur(path):
    output_dir = BASE_DIR / "output"

    if output_dir.exists():
        confirm = input("Output folder exists. Delete and continue? (y/n): ").lower()
        if confirm != "y":
            print("Cancelled.")
            return
        shutil.rmtree(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)



    records = 0
    cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
  

    try:
        for file in path.rglob("*"):
            file = Path(file)

            if file.is_file() and file.suffix.lower() in [".jpg", ".jpeg", ".png", ".webp", ".avif"]:

            
                face_cascade = cv2.CascadeClassifier(cascade_path)

                image = cv2.imread(file)

                # Convert to grayscale for detection
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

                faces = face_cascade.detectMultiScale(
                gray,
                    scaleFactor=1.1,
                    minNeighbors=5,
                    minSize=(30, 30)
                )

                print(f"Detected {len(faces)} face(s).")

                # Blur each detected face
                for (x, y, w, h) in faces:
                    face_region = image[y:y+h, x:x+w]
                    blurred_face = cv2.GaussianBlur(face_region, (99, 99), 30)
                    image[y:y+h, x:x+w] = blurred_face

                output_path = output_dir / f"{file.stem}.png"

                # Save the output
                cv2.imwrite(output_path, image)
                print(f"Blurred image saved to '{output_path}'.")


                cv2.waitKey(0)
                cv2.destroyAllWindows()
                            
                records += 1

    except Exception as e:
        print(f"Error: {e}")

    if records == 0:
        print("No images found.")
    else:
        print(f"{records} images face blurred successfully.")


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
        face_blur(path)
    else:
        print("404 - Please enter a valid folder path.")