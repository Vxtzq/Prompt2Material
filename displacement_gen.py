import cv2
import numpy as np
from PIL import Image

def generate_displacement_map(texture_path, contrast=1.0, brightness=0.0):
    # Load the image in color
    img = cv2.imread(texture_path, cv2.IMREAD_COLOR)
    if img is None:
        raise ValueError(f"Failed to load image from {texture_path}")

    # Convert to grayscale (luminance)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = gray.astype(np.float32) / 255.0  # normalize [0,1]

    # Apply contrast and brightness adjustment
    # new_pixel = pixel * contrast + brightness
    gray = np.clip(gray * contrast + brightness, 0, 1)

    # Convert back to 8-bit grayscale image
    displacement_map = (gray * 255).astype(np.uint8)

    # Convert to PIL image for easy saving/handling
    return Image.fromarray(displacement_map)

# Usage example:
disp_map_img = generate_displacement_map("results/texture.png", contrast=2.0, brightness=-0.1)
disp_map_img.save("results/displacement_map.png")
