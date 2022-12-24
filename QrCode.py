import qrcode
user=input("Enter the text:")
imge=qrcode.make(user)
name=input("Name for the file:")
imge.save(name+".jpg")