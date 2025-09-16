import qrcode

data=input("enter the text or url: ").strip()
filename = input("enter the file name: ").strip()
myqr=qrcode.QRCode(box_size=10,border=5)
myqr.add_data(data)
image=myqr.make_image(fill_color="black", back_color="white")
image.save(filename)
print(f'QR Code saved as {filename}')