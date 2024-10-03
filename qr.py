import segno

qrcode = segno.make_qr("https://drive.google.com/drive/u/0/folders/1IugTMKMF0a3P_rFh8U6tNsjRmBH0ThNR")
qrcode.save("basic_qrcode.png", scale = 10)