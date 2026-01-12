# Radius Light Theme for Rockbox

This is a light version of the Radius Dark theme with intelligently inverted colors.

## Contents

This package includes:

### Theme Files
- `theme-light.wps` - Now Playing Screen (light theme)
- `filebrowser-light.sbs` - File Browser Screen (light theme)

### Converted BMP Assets (20 files)
All icon and UI element bitmaps have been converted from dark to light theme with **smart color preservation**:

**UI Elements:**
- bar-bottom-cap.bmp
- bar-left-cap.bmp  
- bar-right-cap.bmp
- bar-top-cap.bmp
- volume_backdrop.bmp
- volume_overlay_bg.bmp

**Icons:**
- batteryStatus-4.bmp (11 battery states with colored indicators)
- VolumeIcons.bmp (4 volume states)
- lock.bmp / lock_null.bmp
- play_small.bmp / pause_small.bmp (with colored elements)
- repeat.bmp / repeat_all.bmp / repeatOne.bmp / repeatShuffle.bmp / repeat_null.bmp
- shuffle.bmp / shuffle_null.bmp
- losslessIndicator.bmp

## Color Scheme

**Theme Files:**
- Background: `#000000` (black) → `#EAEAEA` (light gray)
- Dark background: `#151515` → `#EAEAEA`
- Primary text: `#EAEAEA` (light) → `#1A1A1A` (almost black)
- Secondary text: `#AAAAAA` → `#555555` (darker gray)

**BMP Assets (Smart Conversion):**
- ✅ Transparency color: `#FF00FF` (magenta) - **PRESERVED**
- ✅ Colored elements (blue, cyan, red, green, etc.) - **PRESERVED**
- ✅ Grayscale colors inverted: Black → White, Dark Gray → Light Gray
- ✅ Battery indicators, lock icon colors, and other colored elements remain unchanged

## Smart Conversion Technology

The conversion script intelligently processes each pixel:

1. **Magenta pixels** (`#FF00FF`) → Stay magenta (transparency)
2. **Colored pixels** (blue, cyan, red, etc.) → Stay unchanged
3. **Grayscale pixels** (black, white, grays) → Inverted

This ensures that:
- Battery status colors (blue charging indicator, cyan states) remain visible
- Lock icon colors are preserved
- Play/pause colored elements stay correct
- UI structure (black/white) is properly inverted

## Example: Battery Status Icon

**Original (Dark Theme):**
- Blue charging indicator: `#0000FF` 
- Cyan state indicator: `#00FFFF`
- Black outline: `#000000`
- Gray levels: Various grays
- Transparent: `#FF00FF` (magenta)

**Converted (Light Theme):**
- Blue charging indicator: `#0000FF` ✅ **PRESERVED**
- Cyan state indicator: `#00FFFF` ✅ **PRESERVED**
- White outline: `#FFFFFF` ✅ **INVERTED**
- Inverted gray levels ✅ **INVERTED**
- Transparent: `#FF00FF` ✅ **PRESERVED**

## Installation

1. Copy all files to your Rockbox themes directory:
   ```
   .rockbox/wps/radius-light/
   ```

2. Copy the theme files to the parent directory:
   - `theme-light.wps` → `.rockbox/wps/radius-light.wps`
   - `filebrowser-light.sbs` → `.rockbox/wps/radius-light.sbs`

3. On your device, go to:
   ```
   Settings → Theme Settings → Browse Theme Files
   ```
   
4. Select `radius-light.wps`

## Fonts Required

- `14-InterTight-Medium-14pt-CJK.fnt`
- `32-Gabarito-SemiBold-32pt-CJK.fnt` (for Now Playing screen)

Make sure these fonts are installed in your `.rockbox/fonts/` directory.

## Additional Assets Needed

You may need to create a light version of:
- `albumPlaceholder_dark.bmp` → `albumPlaceholder_light.bmp`

You can use the included conversion script for this.

## Conversion Script

The included `convert_bmps_smart.py` script uses intelligent color detection:

**Features:**
- ✅ Preserves magenta (#FF00FF) transparency
- ✅ Preserves all colored elements automatically
- ✅ Only inverts grayscale (black, white, grays)
- ✅ Perfect for icons with color indicators

**Usage:**
```bash
# Convert a directory
python3 convert_bmps_smart.py dark_theme/ light_theme/

# Convert a single file
python3 convert_bmps_smart.py input.bmp output.bmp
```

**How it works:**
The script analyzes each pixel and determines if it's:
1. Magenta (transparency) - keep as-is
2. Colored (R≠G≠B) - keep as-is
3. Grayscale (R≈G≈B) - invert it

This ensures colored elements like battery indicators, status icons, and decorative elements remain vibrant and correct in the light theme!

## Technical Details

**Color Detection Algorithm:**
- A pixel is considered "grayscale" if R, G, and B values are within 5 units of each other
- All other pixels are considered "colored" and preserved
- Magenta is always preserved as the transparency color

**Conversion Statistics (example from batteryStatus-4.bmp):**
- Inverted: 1,408 grayscale pixels (black/gray outline)
- Preserved: 407 colored pixels (blue/cyan indicators)
- Magenta: 7,271 transparent pixels

---

Based on the Radius Dark theme by swimtrunks - converted to light theme with intelligent color preservation.
