from PIL import Image

im = Image.open("scripts/card_4.png")
print("Card 4 size:", im.size)
im_sec = Image.open("scripts/section_trabalho.png")
print("Section size:", im_sec.size)

