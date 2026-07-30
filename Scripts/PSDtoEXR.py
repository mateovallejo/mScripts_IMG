#!/usr/bin/env python3
import OpenImageIO as oiio
import sys

def psd_to_exr(input_file, output_file):
    # Open PSD
    in_image = oiio.ImageInput.open(input_file)
    if not in_image:
        print("Error: Could not open input PSD:", oiio.geterror())
        return False

    spec = in_image.spec()
    print(f"Input: {input_file}")
    print(f"Resolution: {spec.width}x{spec.height}")
    print(f"Channels: {spec.channelnames}")

    # Always read as float internally
    pixels = in_image.read_image(format=oiio.FLOAT)
    in_image.close()
    if pixels is None:
        print("Error reading pixels:", oiio.geterror())
        return False

    # Always force EXR output to 16-bit half float
    out_spec = oiio.ImageSpec(spec.width, spec.height, spec.nchannels, oiio.HALF)
    out_spec.channelnames = spec.channelnames

    out = oiio.ImageOutput.create(output_file)
    if not out:
        print("Error: Could not create output EXR:", oiio.geterror())
        return False

    out.open(output_file, out_spec)
    out.write_image(pixels)
    out.close()

    print(f"✅ Wrote EXR (16-bit half float): {output_file}")
    return True

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python psd_to_exr.py input.psd output.exr")
        sys.exit(1)

    psd_to_exr(sys.argv[1], sys.argv[2])
