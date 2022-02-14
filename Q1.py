import numpy as np 
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


################################# 1-a-b

img1=[]
img2=[]

with open('Image-I1.txt') as file:
    for line in file :
        img1.append(line.rstrip('\n'))

with open('Image-I2.txt') as file:
    for line in file :
        img2.append(line.rstrip('\n'))


entete = img1[:2]
entetec=""
for i in range(2):
    entetec += ''.join(str(e) for e in entete[i])


img1=img1[2:]
img2=img2[2:]


for j in range(0,9):
    l = list(img1[j].strip(" "))
    for i in range(0,9) :
        l[i] = int(l[i])
    img1[j]=l


for j in range(0,9):
    l = list(img2[j].strip(" "))
    for i in range(0,9) :
        l[i] = int(l[i])
    img2[j]=l


img1=np.array(img1)
img2=np.array(img2)


img3=img1+img2
for i in range(len(img3)):
    for j in range(len(img3[i])):
        if img3[i][j] > 1 :
            img3[i][j] = 1


img4=img1-img2
for i in range(len(img4)):
    for j in range(len(img4[i])):
        if img4[i][j] < 0 :
            img4[i][j] = 0




img3l=img3.tolist()
img4l=img4.tolist()


img3lc= [""]*len(img3l)
img4lc= [""]*len(img4l)


for i in range(len(img3l)):
    for j in range (len(img3l[i])):
        img3lc [i] = ''.join(str(e) for e in img3l[i])
    

for i in range(len(img4l)):
    for j in range (len(img4l[i])):
        img4lc [i] = ''.join(str(e) for e in img4l[i])




with open('Image-Iad.txt', 'w') as f:
    f.writelines('\n'.join(entete+img3lc))

with open('Image-Is.txt', 'w') as f:
    f.writelines('\n'.join(entete+img4lc))


######################### 1-c
l=['P5', '9 9','15','000000000', '000000000', '033445560', '033445560', '066554430', '078978970', '099887770', '000000000','000000000' ]
with open('Image-I.txt', 'w') as f:
    f.writelines('\n'.join(l))

imgi=[]
with open('Image-I.txt') as file:
    for line in file :
        imgi.append(line.rstrip('\n'))

entete2 = imgi[:3]
entetec2=""
for i in range(3):
    entetec2 += ''.join(str(e) for e in entete2[i])

imgi=imgi[3:]

for j in range(len(imgi)):
    l = list(imgi[j].strip(" "))
    for i in range(0,9) :
        l[i] = int(l[i])
    imgi[j]=l

imgi=np.array(imgi)
print(imgi)
imgi=imgi*2
print(imgi)
for i in range(len(imgi)):
    for j in range(len(imgi[i])):
        if imgi[i][j] > 15 :
            imgi[i][j] = 15

print(imgi)

imgil=imgi.tolist()
imgilc= [""]*len(imgil)
for i in range(len(imgil)):
    for j in range (len(imgil[i])):
        imgilc [i] = ' '.join(str(e) for e in imgil[i])

with open('Image-Ip.txt', 'w') as f:
    f.writelines('\n'.join(entete2+imgilc))