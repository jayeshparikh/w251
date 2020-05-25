import paho.mqtt.client as mqtt

LOCAL_MQTT_HOST="169.44.182.148"
LOCAL_MQTT_PORT=1883
LOCAL_MQTT_TOPIC="photo"

def on_connect_local(client, userdata, flags, rc):
        print("connected to local broker with rc: " + str(rc))
        client.subscribe(LOCAL_MQTT_TOPIC)
	
def on_message(client,userdata, msg):
  try:
    print("message received!")	
    print(msg)	
    f = open('/root/w251/hw3/myimage.jpg', 'wb')
    #f = open('/tmp/myimage.jpg', 'wb')
    f.write(msg.payload)
    f.close()
    f = open('/mnt/hw3cos/myimage.jpg', 'wb')
    f.write(msg.payload)
    f.close()
  except:
    print("Unexpected error:", sys.exc_info()[0])

local_mqttclient = mqtt.Client()
local_mqttclient.on_connect = on_connect_local
local_mqttclient.connect(LOCAL_MQTT_HOST, LOCAL_MQTT_PORT, 60)
local_mqttclient.on_message = on_message

# go into a loop
local_mqttclient.loop_forever()
