import os
import subprocess

def batch_convert_to_jpg(directory):
    # Supported image extensions
    image_exts = ['.png', '.bmp', '.gif', '.tiff', '.webp', '.jpeg', '.jpg']
    jpg_folder = os.path.join(directory, "jpg")
    webp_folder = os.path.join(directory, "webp")
    os.makedirs(jpg_folder, exist_ok=True)
    os.makedirs(webp_folder, exist_ok=True)
    for filename in os.listdir(directory):
        name, ext = os.path.splitext(filename)
        if ext.lower() in image_exts and ext.lower() != '.jpg':
            input_path = os.path.join(directory, filename)
            jpg_output_path = os.path.join(jpg_folder, f"{name}.jpg")
            webp_output_path = os.path.join(webp_folder, f"{name}.webp")
            
            # Convert to JPG
            try:
                subprocess.run(["magick", input_path, jpg_output_path], check=True)
                print(f"Converted: {filename} -> jpg/{name}.jpg")
            except subprocess.CalledProcessError as e:
                print(f"Failed to convert {filename} to JPG: {e}")
            
            # Convert to WEBP with monochromatic noise + quality settings
            try:
                subprocess.run([
                    "magick", input_path,
                    "(",
                        "+clone",
                        "-colorspace", "Gray",
                        "-attenuate", "10", "+noise", "Gaussian",
                        "-alpha", "set",
                        "-channel", "A", "-evaluate", "set", "1%",
                    ")",
                    "-compose", "Over", "-composite",
                    "-quality", "80",
                    "-define", "webp:method=6",
                    "-define", "webp:alpha-quality=80",
                    webp_output_path
                ], check=True)

                print(f"Converted: {filename} -> webp/{name}.webp (monochrome noise, quality 90, method 6)")
            except subprocess.CalledProcessError as e:
                print(f"Failed to convert {filename} to WEBP: {e}")

if __name__ == "__main__":
    batch_convert_to_jpg(os.getcwd())
