import os
from PIL import Image

def get_average_color(img):
    """Return the average RGB color of the image."""
    small = img.resize((1, 1), Image.Resampling.LANCZOS)
    return small.getpixel((0, 0))[:3]

def get_dominant_colors(img, num_colors=5):
    """Return a list of (count, rgb) tuples for the most dominant colors."""
    # Downscale for speed on large images, doesn't affect color accuracy much
    working = img.copy()
    working.thumbnail((200, 200))

    # Quantize to a small palette using median cut
    quantized = working.quantize(colors=num_colors, method=Image.Quantize.MEDIANCUT)
    palette = quantized.getpalette()
    color_counts = quantized.getcolors()

    results = []
    for count, index in sorted(color_counts, reverse=True):
        r = palette[index * 3]
        g = palette[index * 3 + 1]
        b = palette[index * 3 + 2]
        results.append((count, (r, g, b)))

    return results

def rgb_to_hex(rgb):
    return '#{:02X}{:02X}{:02X}'.format(*rgb)

def save_palette_image(output_path, average_color, dominant_colors):
    """Save a swatch grid (roughly square): average color first, then dominant colors by frequency."""
    import math

    swatch_size = 100
    all_colors = [average_color] + [rgb for _, rgb in dominant_colors]
    total_swatches = len(all_colors)

    # Work out a roughly square grid
    columns = math.ceil(math.sqrt(total_swatches))
    rows = math.ceil(total_swatches / columns)

    grid = Image.new('RGB', (swatch_size * columns, swatch_size * rows))

    for i, rgb in enumerate(all_colors):
        col = i % columns
        row = i // columns
        swatch = Image.new('RGB', (swatch_size, swatch_size), rgb)
        grid.paste(swatch, (col * swatch_size, row * swatch_size))

    grid.save(output_path)

def extract_palette():
    filename = input("Enter the image filename (with extension): ").strip()

    if not os.path.exists(filename):
        print("Error: File does not exist!")
        return

    try:
        num_colors_input = input("How many dominant colors to extract? (default 5): ").strip()
        num_colors = int(num_colors_input) if num_colors_input else 5
        if num_colors < 1:
            print("Please enter a positive number.")
            return
    except ValueError:
        print("Invalid number, using default of 5.")
        num_colors = 5

    try:
        with Image.open(filename) as img:
            img = img.convert('RGB')

            average_color = get_average_color(img)
            dominant_colors = get_dominant_colors(img, num_colors)

            print(f"\nResults for: {filename}")
            print(f"Average color: {rgb_to_hex(average_color)}  RGB{average_color}")
            print("\nDominant colors (most to least frequent):")
            for count, rgb in dominant_colors:
                print(f"  {rgb_to_hex(rgb)}  RGB{rgb}")

            base_name = os.path.splitext(filename)[0]
            output_path = f"{base_name}_palette.png"
            save_palette_image(output_path, average_color, dominant_colors)
            print(f"\nPalette swatch saved as: {output_path}")

    except Exception as e:
        print(f"Error processing {filename}: {str(e)}")

if __name__ == "__main__":
    print("Extract Palette - Dominant & Average Color Sampler")
    print("===================================================")
    extract_palette()