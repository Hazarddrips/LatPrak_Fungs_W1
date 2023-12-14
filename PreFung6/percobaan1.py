from PIL import ImageDraw, ImageFont, Image

gambarku = Image.open(r'C:\Users\HAIDAR\Desktop\PreFung6\UMM.png')


gambarBW = gambarku.convert("L")

# TODO 3: Tambahkan text sesuai kriteria.
draw = ImageDraw.Draw(gambarBW)
font = ImageFont.truetype('C:\\Users\\HAIDAR\\Desktop\\PreFung6\\krinkes\\KrinkesDecorPERSONAL.ttf',18)
text = "KramGw"
text_width, text_height = draw.textsize(text, font)
text_x = (gambarku.width - text_width) // 2
text_y = 20
draw.text()


# TODO 4: Simpan gambar hasil edit menggunakan fungsi save()
gambarBW.save(r'C:\\Users\\HAIDAR\\Desktop\\PreFung6\\percobaan1.py')


# TODO 5: Tampilkan hasil akhir gambar
gambarBW.show()



