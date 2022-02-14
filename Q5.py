from PIL import Image
from cv2 import cv2
import numpy as np
#from matplotlib import pyplot as plt


#Fonction pour calculer la moyenne

def moyenne(tab):
    somme = 0
    for i in tab :
       somme += i
    return somme/len(tab)
    

#Fonction pour calculer la variance

def variance(tab,moyenne) :
    somme = 0
    for i in  tab : 
        somme += (i-moyenne)**2
    return somme/len(tab)



imageOrig = cv2.imread("ImageTest.jpg")
#resizing an image
img = cv2.resize(imageOrig,(600,600))

data = np.asarray(img)
newdata = np.ones((604, 604), dtype=np.int32)
newdata2 = np.ones((604, 604), dtype=np.int32)
#Ajouter la partie frontiere

k = 0
p = 0
for i in range(604):
    for j in range(604):
        if i > 1 and j > 1 and p < 600 and k < 600:
            newdata[i][j] = int(img[k][p])
            p += 1
    if i > 1 and k < 600:
        p = 0
        k += 1

nagao  = np.ones( (7), dtype=np.int32 )
nagao2  = np.ones( (9), dtype=np.int32 )
VarMoy = np.ones( (9,2), dtype=np.int32 )

for i in range(604)[2:602]:
    for j in range(604)[2:602]:
            vm=0
            #Domaine 1 :
            n=0
            for l in [i-2,i-1]:
                for c in [j-1,j,j+1]:
                    nagao[n] = newdata[l][c]
                    n+=1
            nagao[n] = newdata[i][j]
            moyenneCas1 = moyenne(nagao)
            varianceCas1 = variance(nagao,moyenneCas1)
            
            VarMoy[vm][0] = moyenneCas1
            VarMoy[vm][1] = varianceCas1
            vm+=1
        

            #Domaine 2 :
            n=0
            for l in [i-1,i,i+1]:
                for c in [j-2,j-1]:
                    nagao[n] = newdata[l][c]
                    n+=1
            nagao[n] = newdata[i][j]
            moyenneCas2 = moyenne(nagao)
            varianceCas2 = variance(nagao,moyenneCas2)

            VarMoy[vm][0] = moyenneCas2
            VarMoy[vm][1] = varianceCas2
            vm+=1

            #Domaine 3 :
            n=0
            for l in [i+1,i+2]:
                for c in [j-1,j,j+1]:
                    nagao[n] = newdata[l][c]
                    n+=1
            nagao[n] = newdata[i][j]
            moyenneCas3 = moyenne(nagao)
            varianceCas3 = variance(nagao,moyenneCas3)

            VarMoy[vm][0] = moyenneCas3
            VarMoy[vm][1] = varianceCas3
            vm+=1

            #Domaine 4 :
            n=0
            for l in [i-1,i,i+1]:
                for c in [j+1,j+2]:
                    nagao[n] = newdata[l][c]
                    n+=1
            nagao[n] = newdata[i][j]
            moyenneCas4 = moyenne(nagao)
            varianceCas4 = variance(nagao,moyenneCas4)

            VarMoy[vm][0] = moyenneCas4
            VarMoy[vm][1] = varianceCas4
            vm+=1

           
            #Domaine 5 :
            n=0
            for l in [i-2,i-1,i]:
                for c in [j-2,j-1,j]:
                    if not(( l==i and c == j-2) or (l==i-2 and c==j)) :
                        nagao[n] = newdata[l][c]
                        n+=1
            moyenneCas5 = moyenne(nagao)
            varianceCas5 = variance(nagao,moyenneCas5)

            VarMoy[vm][0] = moyenneCas5
            VarMoy[vm][1] = varianceCas5
            vm+=1


             #cas 6 :
            n=0
            for l in [i-2,i-1,i]:
                for c in [j,j+1,j+2]:
                    if not(( l==i and c == j+2) or (l==i-2 and c==j)) :
                        nagao[n] = newdata[l][c]
                        n+=1
            moyenneCas6 = moyenne(nagao)
            varianceCas6 = variance(nagao,moyenneCas6)

            VarMoy[vm][0] = moyenneCas6
            VarMoy[vm][1] = varianceCas6
            vm+=1

            
            #Domaine 7 :
            n=0
            for l in [i,i+1,i+2]:
                for c in [j-2,j-1,j]:
                    if not(( l==i and c == j-2) or (l==i+2 and c==j)) :
                        nagao[n] = newdata[l][c]
                        n+=1
            moyenneCas7 = moyenne(nagao)
            varianceCas7 = variance(nagao,moyenneCas7)

            VarMoy[vm][0] = moyenneCas7
            VarMoy[vm][1] = varianceCas7
            vm+=1


            #Domaine 8 :
            n=0
            for l in [i,i+1,i+2]:
                for c in [j,j+1,j+2]:
                    if not(( l==i and c == j+2) or (l==i+2 and c==j)) :
                        nagao[n] = newdata[l][c]
                        n+=1
            moyenneCas8 = moyenne(nagao)
            varianceCas8 = variance(nagao,moyenneCas8)

            VarMoy[vm][0] = moyenneCas8
            VarMoy[vm][1] = varianceCas8
            vm+=1

            #Domaine 9:
            n=0
            for l in [i-1,i,i+1]:
                for c in [j-1,j,j+1]:
                    nagao2[n] = newdata[l][c]
                    n+=1
            moyenneCas9 = moyenne(nagao2)
            varianceCas9 = variance(nagao2,moyenneCas9)

            VarMoy[vm][0] = moyenneCas9
            VarMoy[vm][1] = varianceCas9
            vm+=1

    
            Varmin = int (min(varianceCas1,varianceCas2,varianceCas3,varianceCas4,varianceCas5,varianceCas6,varianceCas7,varianceCas8,varianceCas9) )
            minFinal = 0
            for vm in VarMoy:
                if vm[1] == Varmin :
                    minFinal = vm[0]
            newdata2[i][j] = minFinal       
            

datafinal = np.ones( (600,600), dtype=np.int32 )

for i in range(len(newdata)+4)[2:len(newdata)-2]:
    for j in range(len(newdata)+4)[2:len(newdata)-2]:
        datafinal[i-2][j-2] = newdata2[i][j]


image = Image.new('L',(600,600),'black')

for i in range(600):
    for j in range(600):
        image.putpixel((i,j),int(datafinal[j][i]))
        
image.save("ImageResult.jpg")           