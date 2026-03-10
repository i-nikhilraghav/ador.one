# ador_one.py
# Simple art generator from an image
# Requires Python 3 and Pillow

from PIL import Image, ImageFilter, ImageEnhance
import os

INPUT_FOLDER = "images"
OUTPUT_FOLDER = "output"

# Ensure output folder exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def apply_artistic_effects(image_path):
    img = Image.open(image_path)
    
    # Apply a sequence of artistic filters
    img = img.convert("RGB")
    img = img.filter(ImageFilter.CONTOUR)  # Outline effect
    img = img.filter(ImageFilter.DETAIL)   # Enhance details
    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(2)              # Increase color vibrancy
    img = img.filter(ImageFilter.SMOOTH_MORE)
    
    # Save output
    base_name = os.path.basename(image_path)
    name, ext = os.path.splitext(base_name)
    output_path = os.path.join(OUTPUT_FOLDER, f"{name}_art{ext}")
    img.save(output_path)
    
    print(f"Generated art saved at: {output_path}")

if __name__ == "__main__":
    # Apply art effects to all images in the input folder
    input_images = [f for f in os.listdir(INPUT_FOLDER) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    if not input_images:
        print("No images found in the 'images/' folder. Add images to generate art.")
    
    for img_file in input_images:
        apply_artistic_effects(os.path.join(INPUT_FOLDER, img_file))
