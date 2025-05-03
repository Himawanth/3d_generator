from rembg import remove
from PIL import Image
import trimesh
import numpy as np

def generate_3d_from_image(image_path, output_path):
    # Remove background
    input_img = Image.open(image_path)
    output_img = remove(input_img)
    output_img.save("temp_nobg.png")

    # For now, generate a placeholder cube mesh
    mesh = trimesh.creation.box(extents=(1.0, 1.0, 1.0))
    mesh.export(output_path)
    print(f"[✓] Dummy 3D cube saved to {output_path}")
