from PIL import Image, ImageFilter

img = Image.open('./pokedex/pikachu.jpg')
astro = Image.open('./pokedex/astro.jpg')

# new_astro = astro.resize((400, 400))
astro.thumbnail((400, 400))
astro.save('thumbnail.jpg')


filtered_img = img.filter(ImageFilter.BLUR)
grey_img = img.convert('L')

filtered_img.save("blur.png", "png")
grey_img.save("grey.png", "png")

print(img.format)
print(img.size)
print(img.mode)

# grey_img.show()
