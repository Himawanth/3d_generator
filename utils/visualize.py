# utils/visualize.py
import trimesh
import pyrender
import matplotlib.pyplot as plt

def visualize_3d_model(model_path):
    print(f"[i] Visualizing: {model_path}")
    mesh = trimesh.load(model_path)
    scene = pyrender.Scene()
    render_mesh = pyrender.Mesh.from_trimesh(mesh)
    scene.add(render_mesh)

    viewer = pyrender.Viewer(scene, use_raymond_lighting=True, run_in_thread=True)
