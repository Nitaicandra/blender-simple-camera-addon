import bpy
from bpy.types import Panel


bpy.types.Scene.cameratrack = bpy.props.PointerProperty(type=bpy.types.Object)
bpy.types.Scene.target = bpy.props.PointerProperty(type=bpy.types.Object)

class SimplePanel(Panel): # creates a panel 
    bl_space_type = "VIEW_3D" # defines where the panel is created
    bl_region_type = "UI" # what tYpe of panel it is
    bl_label = "Modifier operations"
    bl_category = "RAPTRUTIL"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        col=row.column()
        
        col.prop_search(context.scene, "cameratrack", context.scene, "objects", text="Camera") # Prop search stores its information inside of the property defined above
        col.prop_search(context.scene, "target", context.scene, "objects", text="Target")
        col.operator("object.rotate", text="Tracks") # THIS IS WHAT DEFINES WHAT HAPPENS WHEN YOU CLICK THE BUTTON AND WHAT TEXT IS DISPLAYED ON THE BUTTON

    
