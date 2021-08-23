import bpy
from bpy.types import Panel

class SimplePanel(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Modifier operations"
    bl_category = "RAPTRUTIL"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        col=row.column()
        col.operator("object.rotate", text="Track")
    