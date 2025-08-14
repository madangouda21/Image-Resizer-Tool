# Image-Resizer-Tool

## 📌 Objective
A simple Python script to resize and convert images in batch using **Pillow**.

## 📂 Project Structure
```
image_resizer/
│
├── resizer.py          # Main script
├── requirements.txt    # Dependencies
├── input_images/       # Place your original images here
└── output_images/      # Resized images will be saved here
```

## 🛠 Installation
1. Clone this repository or create the folder manually.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 📁 Creating Required Folders
Run these commands to create the input and output folders:
```bash
mkdir input_images
mkdir output_images
```

## ▶️ Usage
1. Place your images inside `input_images/`.
2. Run the script:
   ```bash
   python resizer.py
   ```
3. Resized images will be saved in `output_images/`.

## 📦 Dependencies
- **Pillow** – Python Imaging Library for image processing.

## 📌 Notes
- Supported formats: `.png`, `.jpg`, `.jpeg`, `.webp`
- Default resize size is **300x300**, but you can modify it in `resizer.py`.
