import queue



class Xbox(object):
    pass

class Playstation(object):
    class ButtonCallbacks:
        def __init__(self, _self): self.parent = _self
        def Cross(self, state): self.parent.buttonQueue.put({"key": "A", "state": state})
        def Circle(self, state): self.parent.buttonQueue.put({"key": "B", "state": state})
        def Square(self, state): self.parent.buttonQueue.put({"key": "X", "state": state})
        def Triangle(self, state): self.parent.buttonQueue.put({"key": "Y", "state": state})

        def DpadUp(self, state): self.parent.buttonQueue.put({"key": "DUP", "state": state})
        def DpadDown(self, state): self.parent.buttonQueue.put({"key": "DDOWN", "state": state})
        def DpadLeft(self, state): self.parent.buttonQueue.put({"key": "DLEFT", "state": state})
        def DpadRight(self, state): self.parent.buttonQueue.put({"key": "DRIGHT", "state": state})

        def L1(self, state): self.parent.buttonQueue.put({"key": "LB", "state": state})
        def L2(self, state): self.parent.triggerQueue.put({"key": "LT", "state": state})
        def L3(self, state): self.parent.buttonQueue.put({"key": "L3", "state": state})

        def R1(self, state): self.parent.buttonQueue.put({"key": "RB", "state": state})
        def R2(self, state): self.parent.triggerQueue.put({"key": "RT", "state": state})
        def R3(self, state): self.parent.buttonQueue.put({"key": "R3", "state": state})

        def Share(self, state): self.parent.buttonQueue.put({"key": "Share", "state": state})
        def Option(self, state): self.parent.buttonQueue.put({"key": "Menu", "state": state})
        def Mute(self, state): self.parent.buttonQueue.put({"key": "Mute", "state": state})
        def PS(self, state): self.parent.buttonQueue.put({"key": "V", "state": state})
    
    class GyroCallbacks:
        def __init__(self, _self): self.parent = _self
        def Accel(self, x, y, z): self.parent.gyroQueue.put({"key": "A", "state": [x, y, z]})
        def Gyro(self, x, y, z): self.parent.gyroQueue.put({"key": "G", "state": [x, y, z]})
    
    class JoystickCallbacks:
        def __init__(self, _self): self.parent = _self
        def L(self, x, y): self.parent.joystickQueue.put({"key": "L", "state": [x, y]})
        def R(self, x, y): self.parent.joystickQueue.put({"key": "R", "state": [x, y]})

    def __init__(self):
        self.controllerid = None
        self.controller = None
        self.stop = None

        self.buttonQueue = queue.Queue()
        self.triggerQueue = queue.Queue()
        self.joystickQueue = queue.Queue()
        self.gyroQueue = queue.Queue(15)


        self.buttonCallbacks = self.ButtonCallbacks(self)
        self.gyroCallbacks = self.GyroCallbacks(self)
        self.joystickCallbacks = self.JoystickCallbacks(self)


    def update(self): pass
    
    def connect(self): pass
    def disconnect(self): pass

    def stop(self): self.stop()