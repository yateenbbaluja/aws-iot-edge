from datetime import datetime
import random
from pytz import timezone 

class sensor:
    def __init__(self):
        self.device_id = ["S1", "S2", "S3"]
        #self.device_id = ["S4", "S5", "S6"]
        self.Data_Field = ["Temperature", "Humidity","Battery"]
        self.EdgeID = "1891832b-cbca-43ba-9c6b-192660b316a6"
        #self.EdgeID = "9c2f0f03-5778-4d6b-a6e9-42fa473752e4"
        self.a = 0
 
    def get_payload(self, max, min):
        payload = {}
        for x in range(len(self.Data_Field)): 
            dict = {str(self.Data_Field[x]): int(random.randint(min, max))}
            payload.update(dict)
        return payload

    def add_properties(self,payload, a):
        temp_payload = {
            'EdgeID': self.EdgeID,
            'DeviceID':self. device_id[a],
            'Data': payload,
            'Timestamp': datetime.today().strftime("%d-%b-%Y %H:%M:%S:%f")
        }
        return temp_payload

    def get_data(self):
        payload = self.get_payload(100, 0)
        if self.a < len(self.device_id):
            final_msg = self.add_properties(payload, self.a)
            self.a = self.a + 1
            return [final_msg,self.EdgeID]
        if self.a > len(self.device_id) - 1:
            self.a = 0
            return ["null", self.EdgeID]

