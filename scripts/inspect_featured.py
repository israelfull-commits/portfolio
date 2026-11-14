from PIL import Image

im = Image.open("scripts/section_trabalho.png")
# Let's inspect the bounding box of .pf-featured
# In scripts/inspect_cards_dom.py, cards were at top ~1517.
# So pf-featured is between 0 and 1500!
print("Section trabalho image size:", im.size)
# Crop the featured case (from top 100 to 1400)
featured_crop = im.crop((0, 100, im.size[0], 1450))
featured_crop.save("scripts/featured_einstein_current.png")
print("Saved scripts/featured_einstein_current.png")

