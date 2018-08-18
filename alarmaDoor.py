import paho.mqtt.client as mqtt
import time
from CamaraIP import CamaraIP
from pushbullet import Pushbullet


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("SENSORPUERTA")
    

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    pb = Pushbullet("SECRET TOKEN")
    push = pb.push_note("Evento", "Se detecto un evento en la puerta")
    archivo = time.strftime("%Y%m%d%H%M%S", time.localtime())+".png"
    print("Evento detectado")
    camara = CamaraIP('url_camara')
    camara.capturar(archivo) 
    print("Enviando imagen ",archivo)
    with open(archivo, "rb") as pic:
        file_data = pb.upload_file(pic, archivo)
    push = pb.push_file(**file_data)   


client = mqtt.Client()
client.username_pw_set("usuario", password="clave") 
client.on_connect = on_connect
client.on_message = on_message

client.connect("host_mqtt", 1883, 60)

client.loop_forever()