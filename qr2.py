import qrcode
upi = "upi://pay?pa=YOUR_UPI_ID&pn=YOUR_NAME&am=" + input("Amount ₹: ") + "&cu=INR"
qrcode.make(upi).save("payment_qr.png")
print("Payment QR created!")