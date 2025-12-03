# utils.py
import os
from PIL import Image

def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)

def save_image(img: Image.Image, path: str, mode: str = 'L'):
    # img: PIL Image
    if img.mode != mode:
        img = img.convert(mode)
    img.save(path)
