import bpy #Blender python API
import math #This is just to use the sin function behivor and some conversions

class Cube: #An object that will make the calls easier
    def __init__(self, id):
        self.object = bpy.data.objects[id]        
    def setScale(self, scale):
        self.object.scale = scale
    def setLocation(self, location):
        self.object.location = location
    def setRotation(self, rotation):
        self.object.rotation_euler = rotation
    
cube1 = Cube("Cube 1")
cube2 = Cube("Cube 2")
cube3 = Cube("Cube 3")
        
def onFrameChangeHandler(scene): #Creates a method that will be executed on frame change
    value = math.sin(math.radians(scene.frame_current)) #each frame would be the degree, then we convert it to radian
    #which gives a value between -1 and 1. but only 180 frames are used, so the final range will be [0, 1].
    cube1.setScale( (1, 1 , value) ) #x y z Scales
    cube2.setLocation( (0,  0, value) ) #x y z Location
    cube3.setRotation( (0, 0, value*2*math.pi) ) #x y z Rotation in radians
            
bpy.app.handlers.frame_change_pre.append(onFrameChangeHandler) #we add our frame event handler to the app.

#Press ALT + P to run this script or go to the menu "Text" -> "Run Script"
#More info here https://docs.blender.org/api/current/index.html
