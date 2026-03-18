import qrcode # type: ignore

# Replace this with your Vercel link
url = "https://qr-shop-project.vercel.app"

# Generate the QR code
img = qrcode.make(url)

# Save it as an image
img.save("brand_qr.png")

print("✅ QR code generated: brand_qr.png")