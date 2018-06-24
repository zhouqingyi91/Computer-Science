from PIL import Image


# im = Image.new('RGBA', (100, 200), 'purple')
# im.save('purpleImage.png')
# im2 = Image.new('RGBA', (20, 20))
# im2.save('transparentImage.png')

cat = Image.open('zophie.png')
face = cat.crop((335, 345, 565, 560))
# catcopy = cat.copy()

# cat_w, cat_h = cat.size
# face_w, face_h = face.size
# for left in range(0, cat_w, face_w):
#     for top in range(0, cat_h, face_h):
#         # print(left, top)
#         catcopy.paste(face, (left, top))
# catcopy.save('tiled.png')
cat.rotate(6).save('rotate6.png')
