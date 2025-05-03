
import argparse
import os
from utils.image_to_3d import generate_3d_from_image
from utils.text_to_3d import generate_3d_from_text
from utils.visualize import visualize_3d_model

def main():
    parser = argparse.ArgumentParser(description="Convert image or text to 3D model")
    parser.add_argument('--input', required=True, help='Path to image file or text prompt file')
    parser.add_argument('--output', default='models/output_model.obj', help='Output .obj or .stl file path')
    args = parser.parse_args()

    os.makedirs(os.path.dirname(args.output), exist_ok=True)

    if args.input.lower().endswith(('.jpg', '.png')):
        generate_3d_from_image(args.input, args.output)
    elif args.input.lower().endswith('.txt'):
        with open(args.input, 'r') as f:
            prompt = f.read().strip()
        generate_3d_from_text(prompt, args.output)
    else:
        print("Unsupported input format. Use .jpg, .png or .txt")
        return

    visualize_3d_model(args.output)

if __name__ == '__main__':
    main()
