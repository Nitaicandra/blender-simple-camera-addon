import bpy
from bpy.types import Operator
import math

camera = bpy.data.objects["Camera.001"]
empty = bpy.data.objects["LOOKAT"]


class SimpleOperator(Operator):
    bl_idname = "object.rotate"
    bl_label = "Apply all"
    bl_description = "Apply all operators of the active object"

    def modal(self, context):

        if():
            so = bpy.context.active_object

            Cx = camera.location[0]
            Cy = camera.location[1]
            Cz = camera.location[2]
            Crx = camera.rotation_euler[0]
            Crz = camera.rotation_euler[2]

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

            # sine method works but is not ideal
            # fix zero error
            Yeq = math.atan(Zdistance/XYPythagorusDistance)+1.5708
            if(not(Xdistance == 0 and Ydistance == 0)):
                Xeq = -1*math.atan(Xdistance/Ydistance)

            # orignal sine method
            #Xeq =-1*math.asin((Ex - Cx)/((((Ex-Cx)**2)+((Ey-Cy)**2))**(1/2)))
            #Yeq =math.asin((Ez - Cz)/((((Ez-Cz)**2)+((Ex-Cx)**2))**(1/2)))+ 1.5708

            # corrects for arcsine -1-1 range using ifstatement based on position on the y axis rotates and flips tracking
                if Cy >= Ey:
                    Xeq = (Xeq + math.radians(180))

                camera.rotation_euler[0] = Yeq
                camera.rotation_euler[2] = Xeq
        return {'PASS_THROUGH'}

    def execute(self, context):
        #

        return {'FINISHED'}
