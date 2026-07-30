import OpenEXR
import Imath

# Open EXR file
exr_file = OpenEXR.InputFile("input.exr")

# Get header dictionary
header = exr_file.header()

# Print all metadata keys and values
for key, value in header.items():
    print(f"{key}: {value}")

# Example: get compression type
compression = header.get("compression", None)
print("Compression:", compression)

# Example: get data window
data_window = header.get("dataWindow", None)
if data_window:
    print("Data Window:", data_window)

# Close file when done
exr_file.close()
