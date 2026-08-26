import qrcode as qr

data=input("Enter your website: ").strip()
filename=input("Enter your filename: ").strip()

code=qr.QRCode(
    version=1,
    box_size=20,
    border=5
)

code.add_data(data)
image=code.make(fit=True)
image=code.make_image(fill_color='black', background='white')
image.save(filename)
print(f"Image was saved in {filename}")

