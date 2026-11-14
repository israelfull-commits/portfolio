from PIL import Image
import os

site_images = "site/public/images"
verde_images = "portfolio-verde/public/images"

def process_images():
    # 1. Estado atual anotado
    p_atual = os.path.join(site_images, "hiae-estado-atual-anotado.webp")
    if os.path.exists(p_atual):
        im = Image.open(p_atual)
        # crop out the 20px dark border top and bottom
        cropped = im.crop((0, 24, im.width, 1100))
        cropped.save(p_atual, "WEBP", quality=90)
        cropped.save(os.path.join(verde_images, "hiae-estado-atual-anotado.webp"), "WEBP", quality=90)
        print("Updated hiae-estado-atual-anotado.webp:", cropped.size)

    # 2. Estado proposto anotado
    p_proposto = os.path.join(site_images, "hiae-estado-proposto-anotado.webp")
    if os.path.exists(p_proposto):
        im = Image.open(p_proposto)
        cropped = im.crop((0, 24, im.width, 1100))
        cropped.save(p_proposto, "WEBP", quality=90)
        cropped.save(os.path.join(verde_images, "hiae-estado-proposto-anotado.webp"), "WEBP", quality=90)
        print("Updated hiae-estado-proposto-anotado.webp:", cropped.size)

    # 3. Visão futura mamografia
    # Remove baked-in "VISÃO FUTURA" header and focus on responsive tablet & mobile devices
    p_mamo = os.path.join(site_images, "hiae-visao-futura-mamografia.webp")
    if os.path.exists(p_mamo):
        im = Image.open(p_mamo)
        # Devices are from x=331 to 1526, y=260 to 1099.
        # Let's crop x: 260 to 1600, y: 220 to 1115
        cropped = im.crop((260, 220, 1600, 1115))
        cropped.save(p_mamo, "WEBP", quality=90)
        cropped.save(os.path.join(verde_images, "hiae-visao-futura-mamografia.webp"), "WEBP", quality=90)
        print("Updated hiae-visao-futura-mamografia.webp:", cropped.size)

    # 4. Visão futura ressonancia
    p_resso = os.path.join(site_images, "hiae-visao-futura-ressonancia.webp")
    if os.path.exists(p_resso):
        im = Image.open(p_resso)
        cropped = im.crop((260, 220, 1600, 1115))
        cropped.save(p_resso, "WEBP", quality=90)
        cropped.save(os.path.join(verde_images, "hiae-visao-futura-ressonancia.webp"), "WEBP", quality=90)
        print("Updated hiae-visao-futura-ressonancia.webp:", cropped.size)

if __name__ == "__main__":
    process_images()
