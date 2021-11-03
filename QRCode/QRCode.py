import qrcode

data = "name: Ashley, age: 12, from: New York"

img = qrcode.make(data)
img.save('C:/Users/Vasil/PycharmProjects/myQR.png')  # saves the file on the PC

