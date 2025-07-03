import os
from PIL import Image

# === CONFIGURATION ===
input_folder = "images_input"
output_folder = "images_resized"
target_size = (800, 600)  
output_format = "JPEG"    
quality = 85              

# === SETUP ===
os.makedirs(output_folder, exist_ok=True)

# === PROCESSING ===
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
        img_path = os.path.join(input_folder, filename)
        try:
            with Image.open(img_path) as img:
                img = img.convert("RGB")  # Ensure compatibility (e.g., for JPEG)
                img_resized = img.resize(target_size)
                
                # Build output filename
                base_name = os.path.splitext(filename)[0]
                output_path = os.path.join(output_folder, f"{base_name}.{output_format.lower()}")
                
                img_resized.save(output_path, output_format, quality=quality)
                print(f"✓ Resized and saved: {output_path}")
        except Exception as e:
            print(f"✗ Error processing {filename}: {e}")