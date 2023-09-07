import cv2
import numpy as np
from pyzbar.pyzbar import decode
from gtts import gTTS
import playsound

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

with open('myDataFile.text') as f:
    myDataList = f.read().splitlines()


with open('myDataFile1.text') as f1:
    myDataList1= f1.read().splitlines()




while True:

    success, img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        print(myData)

        if myData in myDataList1:
            myOutput = 'Authorized'
            myColor = (0,255,0)

          # Le message de code à convertir en voix
                    
            #code_message = """ rue victor hugo
                               #tourne à gauche tu trouves la municipalité
                                #tourne à droit tu trouves le kiosque """

                # Convertir le message de code en voix
            #tts = gTTS(text=code_message, lang='fr')  # 'fr' pour le français
            #tts.save('code_message_1.mp3')  # Enregistrer le fichier audio

                # Lire le fichier audio à travers le casque
            #playsound.playsound('code_message_1.mp3')
        

        else:
            myOutput = 'Un-Authorized'
            myColor = (0, 0, 255)

        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,myColor,5)
        pts2 = barcode.rect
        cv2.putText(img,myOutput,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,0.9,myColor,2)

        #if myData in myDataList:
         #   myOutput = 'Authorized'
          #  myColor = (0,255,0)

          # Le message de code à convertir en voix
                    
            #code_message = """ Ligne 5B
                            #Départ : 12:15
                            #Arrivée à la destination : 13:30
                            #disponibilité : Tous les jours, sauf le dimanche """

                # Convertir le message de code en voix
            #tts = gTTS(text=code_message, lang='fr')  # 'fr' pour le français
            #tts.save('code_message.mp3')  # Enregistrer le fichier audio

                # Lire le fichier audio à travers le casque
            #playsound.playsound('code_message.mp3')
        

        #else:
         #   myOutput = 'Un-Authorized'
          #  myColor = (0, 0, 255)

        #pts = np.array([barcode.polygon],np.int32)
        #pts = pts.reshape((-1,1,2))
        #cv2.polylines(img,[pts],True,myColor,5)
        #pts2 = barcode.rect
        #cv2.putText(img,myOutput,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,
        #            0.9,myColor,2)

    cv2.imshow('Result',img)
    cv2.waitKey(1)