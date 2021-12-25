import bpy 
from bpy.types import Operator
import math 



class SimpleOperator(Operator): # creates a class that inherits from bpy.types.Operator, operator inherits from bpy.types
    bl_idname = "object.rotate" #for some reason you must have a . in the bl_idname
    bl_label = "Apply all" 
    bl_description = "Apply all operators of the active object"

    # @classmethod
    # def poll(cls,context):
    #    obj = context.object
    #    if obj is not None:
    #        if obj.mode == "OBJECT":
    #         return True
    #    return False

    def execute(self, context): # defines a method of the simple operator named execute w
       
        so = bpy.context.active_object # unecessary gets context of active object
        
        # gets all data from the object selected in panel
        camera = context.scene.cameratrack
        Cx = camera.location[0]
        
        Cy = camera.location[1]
        Cz = camera.location[2]
        Crx = camera.rotation_euler[0]
        Crz = camera.rotation_euler[2]

        # gets all data from empty based on the object selected in panel
        empty = context.scene.target
        Ex = empty.location[0]
        Ey = empty.location[1]
        Ez = empty.location[2]
        Erx = empty.rotation_euler[0]
        Erz = empty.rotation_euler[2]

        # declare variables used in equation
        Xdistance = Ex-Cx
        Ydistance = Ey-Cy
        Zdistance = Ez-Cz
        XYPythagorusDistance = (Xdistance**2 + Ydistance**2)**(1/2)
        DoublePythagorus = (XYPythagorusDistance**2 + Zdistance**2)**(1/2)

        camera.rotation_euler[0] = 0
        camera.rotation_euler[1] = 0
        camera.rotation_euler[2] = 0
        Yeq = 1
        Xeq = 1
        
        Yeq = math.atan(Zdistance/XYPythagorusDistance)+1.5708
        if not(Ydistance == 0): #fixes division by zero error
            
            Xeq = -1*math.atan(Xdistance/Ydistance)
        else:
            Xeq = math.radians(270)
        #fixes xy error
         if(Cy == 0 and Cx<Ex):
            Xeq = Xeq + math.radians(180)
        # orignal sine method works but is less efficient
        #Xeq =-1*math.asin((Ex - Cx)/((((Ex-Cx)**2)+((Ey-Cy)**2))**(1/2)))
        #Yeq =math.asin((Ez - Cz)/((((Ez-Cz)**2)+((Ex-Cx)**2))**(1/2)))+ 1.5708

        # corrects for arctan -1-1 range using ifstatement if the object passes the x axis then it will add 180 degrees to the necessary rotation in order to track
        if Cy >= Ey:
            Xeq = (Xeq + math.radians(180))

        camera.rotation_euler[0] = Yeq
        camera.rotation_euler[2] = Xeq

        return {'FINISHED'}
