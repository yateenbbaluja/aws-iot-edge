# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for
# full license information.


from worker.sensor import sensor
from worker.aws_mqtt import aws_mqtt
import time
mqtt = aws_mqtt()
sensor_data = sensor()

while True:
    t_data = sensor_data.get_data()
    if t_data[0] == "null":
        print("Resetting the counter")
    else:
        mqtt.MQTT_Send_Data(t_data[0])
        print("Message sent: {}".format(t_data[0]))
        time.sleep(2)
