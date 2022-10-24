import qrcode

i=input("enter qr image title : ")
data=input("enter your text : ")
img=qrcode.make(data=data)
img.save(i+".jpg")