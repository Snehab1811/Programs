import random

class TemperatureSensor:
    def __init__(self, min_temp=20.0, max_temp=40.0):
        self.min_temp = min_temp
        self.max_temp = max_temp

    def read_temperature(self):
        # Simulate sensor reading
       # return round(random.uniform(self.min_temp-10, self.max_temp+10))
        return (random.choice([self.min_temp-10,self.min_temp, self.max_temp,self.max_temp-10, self.max_temp+10]))
        
    def High_Low_temp(self):
        temp = self.read_temperature()
        print(temp)

        if temp <= self.min_temp:
            return "Low"
        elif self.min_temp <= temp <= self.max_temp-10:
            return "Meduim"
        elif self.max_temp-10 <= temp <= self.max_temp:
            return "Meduim"
        elif temp >= self.max_temp:
            return " Very High"
        else:
            return "Invalid"
    
a=TemperatureSensor()
print(a.High_Low_temp())
    
