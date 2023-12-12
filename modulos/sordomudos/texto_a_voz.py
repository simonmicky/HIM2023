#importamos la libreria de texto a voz que hemos instalado 
import pyttsx3

#decinimos la variable que vamos a utilizar en el modulo y la inicializamos
texto_a_voz= pyttsx3.init()
rate = texto_a_voz.getProperty('rate')
texto_a_voz.setProperty('rate', rate+2)
answer = input("Que quiere decirle a su interlocutor?: ")

texto_a_voz.say(answer)
texto_a_voz.runAndWait()