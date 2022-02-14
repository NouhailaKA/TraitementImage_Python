from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt
# from PIL import Image

while True :

 histo = input("Voulez vous afficher l'histogramme de l'image convertit en Noir&Blanc (NB) ou en niveau de gris (NG)")

 if(histo == 'NB' or histo == 'NG'):
    if(histo == 'NB'):
        imageOrig = cv2.imread("ImageTest.jpg", cv2.IMREAD_GRAYSCALE)
        #resizing an image
        imageOrig = cv2.resize(imageOrig,(600,600))
        # Conversion en image binaire
        imgconvertie = cv2.threshold(imageOrig, 127, 255, cv2.THRESH_BINARY)[1]
        cv2.imshow('Noir & Blanc',imgconvertie)
        


    else :
        imageOrig = cv2.imread("ImageTest.jpg")
        #resizing an image
        imageOrig = cv2.resize(imageOrig,(600,600))
        #convertir vers une image en niveau de gris
        imgconvertie = cv2.cvtColor(imageOrig, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Niveau de gris',imgconvertie)


    s = imgconvertie.shape    #obtenir la taille de l'image
    H = np.zeros(shape=(256,1))  #créer un tableau H contient 256 cases tout en les initialisants par des zéros
    for i in range(s[0]):        #parcourir les colonnes
     for j in range(s[1]):       #parcourir les lignes
        k = imgconvertie[i,j]
        H[k,0]= H[k,0]+1
    
    #print(H)

    plt.hist(H,range=(0,256),bins=20,align="mid",rwidth=0.9,color="b",edgecolor="red",label="occurrence")
    plt.title("Histogramme")
    plt.xlabel("niveau de gris")
    plt.show()
    cv2.waitKey(0)
    break

 else:
     print("Vous devez préciser votre choix \n NB pour la conversion Noir & Blanc \n NG NB pour la conversion en Niveau de gris")    
