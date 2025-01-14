from PIL import Image, ImageFilter
image = Image.open('stock-photo-jpg-key-shows-image-format.jpg')

#Изменить размер
resized_image = image.resize((200, 200))

#фильтр размытия
blurred_image = resized_image.filter(ImageFilter.BLUR)

#Сохранение
blurred_image.save('blurred_image.jpg')

print("Исходный размер:", image.size)
print("Новый размер:", resized_image.size)