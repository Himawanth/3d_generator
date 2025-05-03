#  Photo or Text to 3D Model Generator (Prototype)

This prototype converts either a **photo of a single object** or a **short text prompt** (like "a small toy car") into a simple 3D model (`.obj` or `.stl`). It demonstrates preprocessing, AI-based 3D generation, and visualization using lightweight open-source tools.

---

##  Project Structure

3d_generator/
├── app.py # Main entry point
├── requirements.txt # Dependencies
├── README.md
├── input/ # Example input image or prompt
├── models/ # Output 3D models (.obj or .stl)
└── utils/
├── image_to_3d.py # Converts image to 3D
├── text_to_3d.py # Converts prompt to 3D
└── visualize.py # 3D model viewer

---

## 🧪 Features Demonstrated

- ✅ Accepts image (`.jpg`, `.png`) or text (`.txt`) input
- ✅ Background removal for images (using `rembg`)
- ✅ Simple dummy 3D model generation to simulate output
- ✅ Real-time 3D mesh visualization with `pyrender`
- ✅ Clean, modular Python codebase using virtualenv

## 🔧 Setup Instructions

### 1. Create and activate virtual environment
```bash
python -m venv venv
# Windows
venv\\Scripts\\activate

2. Install dependencies
pip install -r requirements.txt
🚀 How to Run
🖼 From Image:
python app.py --input input/image.jpg --output models/model.obj
💬 From Text Prompt:
Create a file input/prompt.txt with text like:

A small toy car
Run:
python app.py --input input/prompt.txt --output models/model.obj
📌 Thought Process
Image Input: Preprocess with rembg to remove background and simulate object geometry with a placeholder cube.

Text Input: Simulate text-to-3D with a simple icosphere mesh. (Real model like Point-E can be plugged in for full implementation.)

Output: Mesh saved in .obj format and visualized in a window using pyrender.

This approach prioritizes simplicity and speed for demonstration, with real AI models pluggable for production use.

📤 Output Example
models/model.obj — a 3D model of the input object or prompt.

A live 3D viewer opens with the rendered mesh.

