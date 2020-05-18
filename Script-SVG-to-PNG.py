import os
import cairosvg 

# Length x Width for output PNG, in pixels
OUTPUT_SIZE = 24

# Load SNG input and PNG output directories
dir_svg = os.path.join(os.getcwd(), "twemoji-gh-pages", "emojilib", "svg")
dir_png = os.path.join(os.getcwd(), "twemoji-gh-pages", "emojilib", "png")


# Loop through SVG files in folder and convert to PNG
for filename in os.listdir(dir_svg):
    
    file_input = os.path.join(dir_svg, filename)
    file_output = os.path.join(dir_png, filename[:-4] + ".png")

    cairosvg.svg2png(url=file_input, write_to=file_output, parent_width=OUTPUT_SIZE, parent_height=OUTPUT_SIZE)

print("Conversion Complete")
