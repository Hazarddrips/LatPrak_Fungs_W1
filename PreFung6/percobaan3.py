from PIL import Image, ImageEnhance

img = Image.open("C:/Users/HAIDAR/Desktop/PreFung6/ganjarsuka.jpg")

enhancer = ImageEnhance.Brightness(img)
brightened_image = enhancer.enhance(1.5)

enhancer = ImageEnhance.Contrast(brightened_image)
final_image = enhancer.enhance(1.2)

final_image.save('hasil_edit_3.webp')

final_image.show()