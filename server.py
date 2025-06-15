import sys
import time
import socket
import struct

sys.path.append("C:/Users/Daniella/Descargas/pynaoqi-python2.7-2.1.4.13-win32-vs2015")

from naoqi import ALProxy

NAO_IP = "192.168.108.90"
SERVER_IP = "192.168.108.235"
SERVER_PORT = 5050

tts = ALProxy("ALTextToSpeech", NAO_IP, 9559)
tts.setLanguage("English") 
tts.say("Ready to take a picture.")

camProxy = ALProxy("ALVideoDevice", NAO_IP, 9559)
resolution = 2  # 640x480
colorSpace = 11 # RGB
fps = 5
nameId = camProxy.subscribeCamera("test", 0, resolution, colorSpace, fps)

time.sleep(1)
naoImage = camProxy.getImageRemote(nameId)
camProxy.unsubscribe(nameId)

if naoImage is None:
    tts.say("I could not take the picture.")
    exit()

# get
imageWidth = naoImage[0]
imageHeight = naoImage[1]
array = naoImage[6]

# send
sock = socket.socket()

sock.connect((SERVER_IP, SERVER_PORT))
sock.sendall(struct.pack('>I', len(array)))
sock.sendall(bytearray(array))
prediccion = sock.recv(1024)
print("Prediccion cruda:", prediccion)
print("Tipo de prediccion:", type(prediccion))

if isinstance(prediccion, bytes):
    texto = prediccion.decode('utf-8')
else:
    texto = prediccion

print("Texto final:", texto)

frase = "Lo que veo es " + texto
print("Texto a decir:", frase)
tts.say(frase.encode("utf-8")) 
#saldrá con acento gringo
tts.say(frase)