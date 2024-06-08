from pydualsense import *

from _Engine.Builtin import Controller


class Dualsense(Controller.Playstation):

    def __init__(self, cid=1) -> None:
        super().__init__()

        self.controller = pydualsense()
        self.controller.init()
        self.controllerid = cid
        
        self.controller.cross_pressed = self.buttonCallbacks.Cross
        self.controller.circle_pressed = self.buttonCallbacks.Circle
        self.controller.square_pressed = self.buttonCallbacks.Square
        self.controller.triangle_pressed = self.buttonCallbacks.Triangle

        self.controller.dpad_down = self.buttonCallbacks.DpadDown
        self.controller.dpad_up = self.buttonCallbacks.DpadUp
        self.controller.dpad_left = self.buttonCallbacks.DpadLeft
        self.controller.dpad_right = self.buttonCallbacks.DpadRight

        self.controller.l1_changed = self.buttonCallbacks.L1
        self.controller.l2_changed = self.buttonCallbacks.L2
        self.controller.l3_changed = self.buttonCallbacks.L3

        self.controller.r1_changed = self.buttonCallbacks.R1
        self.controller.r2_changed = self.buttonCallbacks.R2
        self.controller.r3_changed = self.buttonCallbacks.R3

        self.controller.share_pressed = self.buttonCallbacks.Share
        self.controller.option_pressed = self.buttonCallbacks.Option
        self.controller.microphone_pressed = self.buttonCallbacks.Mute
        self.controller.ps_pressed = self.buttonCallbacks.PS


        self.controller.accelerometer_changed = self.gyroCallbacks.Accel
        self.controller.gyro_changed = self.gyroCallbacks.Gyro


        self.controller.left_joystick_changed = self.joystickCallbacks.L
        self.controller.right_joystick_changed = self.joystickCallbacks.R
    
    def get(self, k):
        if k == 1:
            return self.buttonQueue.get()
        if k == 2:
            return self.gyroQueue.get()
        if k == 3:
            return self.joystickQueue.get()

        return None
    
    def setMode(self, trigger, mode: TriggerModes):
        if trigger == 1:
            self.controller.triggerL.setMode(mode)
        if trigger == 2:
            self.controller.triggerR.setMode(mode)
    
    def setForce(self, trigger, index, force):
        if trigger == 1:
            self.controller.triggerL.setForce(index, force)
        if trigger == 2:
            self.controller.triggerR.setForce(index, force)

