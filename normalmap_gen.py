import cv2
import numpy as np
from PIL import Image

def generate_normal_map(height_map_path, strength=1.0, invert_y=True):
    # Load grayscale height map
    height_img = cv2.imread(height_map_path, cv2.IMREAD_GRAYSCALE)
    height_img = height_img.astype(np.float32) / 255.0  # Normalize to [0,1]

    # Calculate gradients
    grad_x = cv2.Sobel(height_img, cv2.CV_32F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(height_img, cv2.CV_32F, 0, 1, ksize=3)

    # Optionally invert y-gradient for some coordinate systems
    if invert_y:
        grad_y = -grad_y

    # Calculate normal components
    normal_x = -grad_x * strength
    normal_y = -grad_y * strength
    normal_z = np.ones_like(height_img)

    # Normalize the normal vectors
    norm = np.sqrt(normal_x**2 + normal_y**2 + normal_z**2)
    normal_x /= norm
    normal_y /= norm
    normal_z /= norm

    # Convert from [-1,1] to [0,255]
    normal_map = np.zeros((height_img.shape[0], height_img.shape[1], 3), dtype=np.uint8)
    normal_map[..., 0] = ((normal_x + 1.0) * 0.5 * 255).astype(np.uint8)  # Red
    normal_map[..., 1] = ((normal_y + 1.0) * 0.5 * 255).astype(np.uint8)  # Green
    normal_map[..., 2] = ((normal_z + 1.0) * 0.5 * 255).astype(np.uint8)  # Blue

    # Convert to PIL Image and return
    return Image.fromarray(normal_map)

# Usage example
normal_map_img = generate_normal_map("results/texture.png", strength=2.0)
normal_map_img.save("results/normal_map.png")

