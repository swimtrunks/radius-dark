#!/usr/bin/env python3
"""
BMP Color Inverter for Rockbox Themes (Smart Mode)
Converts dark theme BMP files to light theme versions by:
- Preserving magenta (#FF00FF) transparency
- Preserving colored elements (non-grayscale colors)
- Only inverting grayscale colors (black, white, grays)
"""

from PIL import Image
import os
import sys

# Rockbox uses magenta as transparency color
MAGENTA = (255, 0, 255)

def is_grayscale(r, g, b, tolerance=5):
    """
    Check if a color is grayscale (R ≈ G ≈ B).
    
    Args:
        r, g, b: RGB values
        tolerance: How much R, G, B can differ and still be considered grayscale
    
    Returns:
        True if the color is grayscale
    """
    return abs(r - g) <= tolerance and abs(g - b) <= tolerance and abs(r - b) <= tolerance

def invert_bmp_smart(input_path, output_path):
    """
    Invert colors in a BMP file intelligently:
    - Keep magenta as transparency
    - Keep colored elements (blue, red, green, etc.)
    - Only invert grayscale colors
    
    Args:
        input_path: Path to input BMP file
        output_path: Path to save inverted BMP file
    """
    try:
        # Open the image
        img = Image.open(input_path)
        
        # Convert to RGB
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Get pixel data
        pixels = img.load()
        width, height = img.size
        
        # Track what we're doing
        inverted_count = 0
        preserved_count = 0
        magenta_count = 0
        
        # Process each pixel
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                
                # Check if pixel is magenta (transparency)
                if (r, g, b) == MAGENTA:
                    # Keep magenta as-is for transparency
                    magenta_count += 1
                    continue
                
                # Check if color is grayscale
                if is_grayscale(r, g, b):
                    # Invert grayscale colors
                    pixels[x, y] = (255 - r, 255 - g, 255 - b)
                    inverted_count += 1
                else:
                    # Keep colored pixels as-is
                    preserved_count += 1
        
        # Save as BMP
        img.save(output_path, 'BMP')
        
        total = width * height
        print(f"✓ {os.path.basename(input_path)}")
        print(f"  Inverted: {inverted_count} grayscale pixels")
        print(f"  Preserved: {preserved_count} colored pixels")
        print(f"  Magenta: {magenta_count} transparent pixels")
        
    except Exception as e:
        print(f"✗ Error converting {input_path}: {e}")

def batch_convert(input_dir, output_dir):
    """
    Convert all BMP files in a directory.
    
    Args:
        input_dir: Directory containing dark theme BMP files
        output_dir: Directory to save light theme BMP files
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Find all BMP files
    bmp_files = [f for f in os.listdir(input_dir) if f.lower().endswith('.bmp')]
    
    if not bmp_files:
        print(f"No BMP files found in {input_dir}")
        return
    
    print(f"Found {len(bmp_files)} BMP files to convert...")
    print(f"Smart mode: Preserving colors, inverting grayscale\n")
    
    # Convert each file
    for filename in sorted(bmp_files):
        input_path = os.path.join(input_dir, filename)
        
        # For albumPlaceholder, create a light version filename
        if 'dark' in filename.lower():
            output_filename = filename.replace('dark', 'light').replace('Dark', 'Light')
        else:
            output_filename = filename
        
        output_path = os.path.join(output_dir, output_filename)
        invert_bmp_smart(input_path, output_path)
        print()  # Blank line between files
    
    print(f"Conversion complete! {len(bmp_files)} files processed.")
    print(f"Light theme BMPs saved to: {output_dir}")

def main():
    if len(sys.argv) < 2:
        print("BMP Theme Converter - Smart Mode (Rockbox)")
        print("\nThis script:")
        print("  ✓ Preserves magenta (#FF00FF) transparency")
        print("  ✓ Preserves colored elements (blue, red, green, etc.)")
        print("  ✓ Only inverts grayscale colors (black, white, grays)")
        print("\nUsage:")
        print("  Convert single file:")
        print("    python3 convert_bmps_smart.py <input.bmp> [output.bmp]")
        print("\n  Convert directory:")
        print("    python3 convert_bmps_smart.py <input_dir> <output_dir>")
        print("\nExamples:")
        print("  python3 convert_bmps_smart.py dark_theme/ light_theme/")
        print("  python3 convert_bmps_smart.py batteryStatus-4.bmp battery-light.bmp")
        sys.exit(1)
    
    input_path = sys.argv[1]
    
    # Check if input is a directory or file
    if os.path.isdir(input_path):
        output_dir = sys.argv[2] if len(sys.argv) > 2 else input_path + "_light"
        batch_convert(input_path, output_dir)
    elif os.path.isfile(input_path):
        # Single file conversion
        if len(sys.argv) > 2:
            output_path = sys.argv[2]
        else:
            # Auto-generate output filename
            base, ext = os.path.splitext(input_path)
            output_path = f"{base}_light{ext}"
        
        invert_bmp_smart(input_path, output_path)
    else:
        print(f"Error: {input_path} not found")
        sys.exit(1)

if __name__ == "__main__":
    main()
