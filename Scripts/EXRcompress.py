import OpenEXR
import Imath
import numpy as np
import os



# Batch process all EXR files in the main directory
for file in os.listdir('.'):
    if file.lower().endswith('.exr') and 'dwaa' not in file.lower():
        input_file = file
        output_file = f"{os.path.splitext(file)[0]}_DWAA_f16.exr"

        in_exr = OpenEXR.InputFile(input_file)
        header = in_exr.header()
        dw = header['dataWindow']
        w = dw.max.x - dw.min.x + 1
        h = dw.max.y - dw.min.y + 1

        half = Imath.PixelType(Imath.PixelType.HALF)
        available_channels = list(in_exr.header()['channels'].keys())

        def to_half(arr):
            return np.asarray(arr, dtype=np.float16).tobytes()

        # Handle RGB(A) and grayscale (Y) EXRs
        if all(ch in available_channels for ch in ['R', 'G', 'B']):
            # RGB or RGBA
            r = np.frombuffer(in_exr.channel('R'), dtype=np.float32).reshape((h, w))
            g = np.frombuffer(in_exr.channel('G'), dtype=np.float32).reshape((h, w))
            b = np.frombuffer(in_exr.channel('B'), dtype=np.float32).reshape((h, w))
            write_alpha = 'A' in available_channels
            if write_alpha:
                a = np.frombuffer(in_exr.channel('A'), dtype=np.float32).reshape((h, w))
            in_exr.close()

            out_header = OpenEXR.Header(w, h)
            out_header['compression'] = Imath.Compression(Imath.Compression.DWAA_COMPRESSION)
            out_header['dwaaCompressionLevel'] = 45.0
            if write_alpha:
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

            out_exr = OpenEXR.OutputFile(output_file, out_header)
            if write_alpha:
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
            print(f"Saved {output_file} with DWAA compression and float16 precision ({'RGBA' if write_alpha else 'RGB'}).")

        elif 'Y' in available_channels:
            # Grayscale (Y) or YA
            y = np.frombuffer(in_exr.channel('Y'), dtype=np.float32).reshape((h, w))
            write_alpha = 'A' in available_channels
            if write_alpha:
                a = np.frombuffer(in_exr.channel('A'), dtype=np.float32).reshape((h, w))
            in_exr.close()

            out_header = OpenEXR.Header(w, h)
            out_header['compression'] = Imath.Compression(Imath.Compression.DWAA_COMPRESSION)
            out_header['dwaaCompressionLevel'] = 45.0
            if write_alpha:
                out_header['channels'] = {
                    'Y': Imath.Channel(half),
                    'A': Imath.Channel(half),
                }
            else:
                out_header['channels'] = {
                    'Y': Imath.Channel(half),
                }

            out_exr = OpenEXR.OutputFile(output_file, out_header)
            if write_alpha:
                out_exr.writePixels({
                    'Y': to_half(y),
                    'A': to_half(a),
                })
            else:
                out_exr.writePixels({
                    'Y': to_half(y),
                })
            out_exr.close()
            print(f"Saved {output_file} with DWAA compression and float16 precision ({'YA' if write_alpha else 'Y'}).")

        else:
            print(f"Skipping {input_file}: missing required channels (RGB or Y).")
            in_exr.close()