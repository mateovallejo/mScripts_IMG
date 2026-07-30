import OpenEXR
import Imath
import numpy as np
import os
from PIL import Image

# Output directory for compressed EXR files
dst_dir = "compressed"
os.makedirs(dst_dir, exist_ok=True)

# Batch process all PNG files in the main directory
for file in os.listdir('.'):
    if file.lower().endswith('.png'):
        input_file = file
        output_file = os.path.join(dst_dir, f"{os.path.splitext(file)[0]}_DWAA_half.exr")

        img = Image.open(input_file)
        img = img.convert('RGBA') if img.mode in ('RGBA', 'LA', 'P') else img.convert('RGB')
        arr = np.array(img).astype(np.float32) / 255.0
        h, w = arr.shape[:2]
        has_alpha = arr.shape[2] == 4

        half = Imath.PixelType(Imath.PixelType.HALF)
        out_header = OpenEXR.Header(w, h)
        out_header['compression'] = Imath.Compression(Imath.Compression.DWAA_COMPRESSION)
        out_header['dwaaCompressionLevel'] = 45.0
        if has_alpha:
            out_header['channels'] = {
                'R': Imath.Channel(half),
                'G': Imath.Channel(half),
                'B': Imath.Channel(half),
                'A': Imath.Channel(half),
            }
        else:
            out_header['channels'] = {
                'R': Imath.Channel(half),
                'G': Imath.Channel(half),
                'B': Imath.Channel(half),
            }

        def to_half(arr2d):
            return np.asarray(arr2d, dtype=np.float16).tobytes()

        r = arr[:, :, 0]
        g = arr[:, :, 1]
        b = arr[:, :, 2]
        if has_alpha:
            a = arr[:, :, 3]

        out_exr = OpenEXR.OutputFile(output_file, out_header)
        if has_alpha:
            out_exr.writePixels({
                'R': to_half(r),
                'G': to_half(g),
                'B': to_half(b),
                'A': to_half(a),
            })
        else:
            out_exr.writePixels({
                'R': to_half(r),
                'G': to_half(g),
                'B': to_half(b),
            })
        out_exr.close()
        print(f"Saved {output_file} with DWAA compression and float16 precision ({'RGBA' if has_alpha else 'RGB'}).")
