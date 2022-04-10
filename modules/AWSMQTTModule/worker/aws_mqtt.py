from termcolor import colored
import json
import sys
import paho.mqtt.client as mqtt


class aws_mqtt:
    def __init__(self):
        with open("worker/config.json", "r") as jsonfile:
            self.data = json.load(jsonfile)
            print("Config read successfully")
        self.mqtt_client = mqtt.Client()
        self.caPath = "worker/Certs/root.crt"
        self.certPath = "worker/Certs/aws-certificate.pem"
        self.keyPath = "worker/Certs/aws-private.pem"
        self.mqtt_connect()

    def mqtt_connect(self):
        try:
            self.mqtt_client.tls_set(self.caPath, certfile=self.certPath, keyfile=self.keyPath, ciphers=None)
            self.mqtt_client.connect(self.data["URL"], self.data["PORT"])
            self.mqtt_client.loop_start()
            print(colored("Successfully connected to AWS-IoT broker", "green"))
        except KeyError:
            e = sys.exc_info()[0]
            print(colored("Failed to connect to AWS-IoT broker" + str(e), "green"))
            pass


    def MQTT_Send_Data(self, payload):
        try:
            messageJson = json.dumps(payload)
            self.mqtt_client.publish(
                self.data["TOPIC_PUB"], messageJson, self.data["QOS"])
            print(colored("Publishing data to AWS-IoT -:" + str(messageJson), "green"))
            return True
        except:
            e = sys.exc_info()[0]
            print(colored("Exception in sending data to AWS-IoT - " + str(e), "red"))
            pass
