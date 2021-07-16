import random
import time
import matplotlib.pyplot as plt

class Usina:
    def __init__(self, nivel=239):
        self._nivel= nivel
        self._actuator = False
    def get_sensor(self):
        if self._actuator == True:
            self._nivel = self._nivel-(random.random()+1);
        return self._nivel
    def set_actuator(self, actuator):
        """actuator é booleano"""
        self._actuator = actuator
    def get_actuator(self):
        return self._actuator

class Sensor:
    def __init__(self, usina):
        self.aux = usina
        self.nivel=[]
    
    def get_sensor(self):
        self.nivel.append(self.aux.get_sensor()*80/255 + 10)
        return self.nivel[-1]


class Atuador:
    def __init__(self, nivel, usina):
        self.actuator = False
        self.nivel = nivel
        self.usina = usina

    def abrir_fechar(self):
        if self.nivel < 70:
            self.actuator = False
        else:
            self.actuator = True
        
        self.usina.set_actuator(self.actuator)

class Subsystem:
    def __init__(self, atuador, sensor):
        self.atuador = atuador
        self.sensor = sensor

    def controle(self):
        self.atuador.nivel = self.sensor.get_sensor()
        self.atuador.abrir_fechar()
        if self.atuador.actuator == False:
            t.append(i*0.1)
            plt.plot(t, self.sensor.nivel, label = 'Nível da agua pelo tempo')
            plt.xlabel('Time')
            plt.ylabel('Nvl Água')
            plt.xticks(t)
            plt.title('Nível da agua pelo tempo')
            plt.show()


u1 = Usina()
s1 = Sensor(u1)
a1 = Atuador(s1.get_sensor(), u1)
ss1 = Subsystem(a1, s1)
i = 1
t = [0]
ss1.controle()

while u1.get_actuator() == True:
    t.append(i*0.1 )
    ss1.controle()
    i = i+1
    time.sleep(0.1)


    

    