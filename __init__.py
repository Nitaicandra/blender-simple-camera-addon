

bl_info = {
    "name": "RAPTRS FRIST ADDON",
    "description": "",
    "author": "Your Name",
    "version": (0, 0, 1),
    "blender": (3, 0, 0),
    "location": "View3D",
    "warning": "This addon is still in development.",
    "wiki_url": "",
    "category": "Object" }



if "bpy" in locals():
    import importlib
    importlib.reload(op)
    importlib.reload(panel)
else:
    import bpy
    from . op import SimpleOperator # imports the simpleOperator class found in the op file
    from . panel import SimplePanel # imports the simplePanel class found in the panel


classes = (SimpleOperator, SimplePanel) # Creates a tuple that will be iterated on in order to register each class

def register(): # a function named register that goes through the classes defined by classes and registers each might be able to be named anything
   for c in classes: # for loop iterates through the classes
       bpy.utils.register_class(c) #for each stage calles a a method form bpy.utils

def unregister(): # does the same 
   for c in classes:
       bpy.utils.unregister_class(c)
