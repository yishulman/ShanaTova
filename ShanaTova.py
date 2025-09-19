from ascii_magic import AsciiArt
from PIL import Image, ImageDraw, ImageFont

# Rebuild artwork with overlaid text
base_img = Image.open('images/apple.jpg')
draw = ImageDraw.Draw(base_img)

text = "Shana Tova!"
position = (10, 10)  # (x, y) coordinates
font_size = 40  
font = ImageFont.truetype("arial.ttf", font_size)

draw.text(position, text, font=font, fill="black")

tmp_path = "_tmp_with_text.jpg"
base_img.save(tmp_path)

my_art = AsciiArt.from_image(tmp_path)
my_art.to_html_file('shanaTova.html',columns=200)