from PIL import Image

background = Image.open(r"background.png")
gay = Image.open(r"gay.png")

background.paste(gay, (540, 375), mask=gay)

background.save("output.png")
