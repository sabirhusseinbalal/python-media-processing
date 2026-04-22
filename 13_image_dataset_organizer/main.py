from torchvision.models import resnet50, ResNet50_Weights
from torchvision.io import decode_image
from pathlib import Path
import shutil
from PIL import Image

BASE_DIR = Path(__file__).resolve().parent


def organize_images(path):
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

    # Load model ONCE (important fix)
    weights = ResNet50_Weights.DEFAULT
    model = resnet50(weights=weights)
    model.eval()
    preprocess = weights.transforms()

    
    for file in path.rglob("*"):
        file = Path(file)

        try:

            if file.is_file() and file.suffix.lower() in img_list:

                # Load image tensor
                img = decode_image(file)

                # Preprocess
                batch = preprocess(img).unsqueeze(0)

                # Predict
                prediction = model(batch).squeeze(0).softmax(0)

                class_id = prediction.argmax().item()
                score = prediction[class_id].item()
                label = weights.meta["categories"][class_id]

                confidence = round(score * 100, 1)

                print(f"{file.name} → {label} ({confidence}%)")

                # Low confidence filter
                if confidence < 40:
                    label = "others"

                # Create folder
                folder = output_dir / label
                folder.mkdir(parents=True, exist_ok=True)

                # Save image
                with Image.open(file) as img_pil:
                    if img_pil.mode in ("RGBA", "P"):
                        img_pil = img_pil.convert("RGB")

                    save_path = folder / file.name
                    img_pil.save(save_path, optimize=True, quality=60)

                records += 1

            else:
                print(f"Skipped: {file.name}")

        except Exception as e:
            print(f"Failed to process {file.name}: {e}")

    if records == 0:
        print("No images found.")
    else:
        print(f"{records} images organized successfully.")


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
        if not path.is_dir():
            print("Default folder missing.")
            continue
    else:
        path = Path(user_path)

    if path.is_dir():
        print(f"Folder Loaded: {path}")
        organize_images(path)
    else:
        print("Invalid folder path!")
