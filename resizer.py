import os
from PIL import Image

def resize_images(input_folder, output_folder, size):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)
            img = img.resize(size)
            save_path = os.path.join(output_folder, filename)
            img.save(save_path)
            print(f"Resized and saved: {save_path}")

if __name__ == "__main__":
    input_folder = "input_images"
    output_folder = "output_images"
    size = (300, 300)  # width, height
    resize_images(input_folder, output_folder, size)