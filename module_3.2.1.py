f=open("temp3.2.txt","r")

content=f.read()
print(content)

f.close()

f=open("temp3.2.txt","w")

f.write("open upon a time ,there was a lalala")

f.close()

f=open("temp3.2.txt","a")
f.write("file tmi kmn acho!,notun kicu shiklam")

f.close()