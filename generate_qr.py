import pyqrcode

data = input("Enter the URL: ").strip()

if not data:
    print("Error: Input cannot be empty.")
else:
    filename = input("Enter output filename (default: myqr.png): ").strip()
    if not filename:
        filename = "myqr.png"
    elif not filename.endswith(".png"):
        filename += ".png"

    qr = pyqrcode.create(data)
    qr.png(filename, scale=6)

    print(f"QR code generated successfully as '{filename}'.")