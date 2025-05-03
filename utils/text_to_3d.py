import torch
from PIL import Image
from pathlib import Path
import trimesh

# Simulated 3D model output using a basic sphere (since full Point-E takes time/resources)
def generate_3d_from_text(prompt, output_path):
    print(f"[i] Generating 3D for prompt: \"{prompt}\"")

    # Placeholder mesh — sphere
    mesh = trimesh.creation.icosphere(radius=0.5)
    mesh.export(output_path)
    print(f"[✓] Dummy 3D sphere saved to {output_path}")
