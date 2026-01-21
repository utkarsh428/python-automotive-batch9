import qrcode #to create qr codes

name = input("Enter your Name: ")
subject = input("Enter the subject: ")
score = input("Enter the score: ")

#Using user input for name subject and score and combining into a single string
qr_data = f"Name: {name} | Subject: {subject} | Score: {score}"

#this creates qr code with size and border
qr = qrcode.QRCode(box_size=11, border=4)

#add string to qr code..to ensure the qr code adjusts its size
qr.add_data(qr_data)
qr.make(fit=True)

#creates actual image with black squares on white background
img = qr.make_image(fill_color="black", back_color="white")
img.save("QR-CODE.png") #qr code is saved as png

print("Done! File saved as QR-CODE.png")