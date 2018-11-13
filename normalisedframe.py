import bpy
import math

bl_info = {
    "name": "F Normalised Frame Value",
    "author": "Frankie",
    "version": (0,1),
    "blender": (2, 7, 7),    
    "location": "View3D > N thing",
    "description": "Shows current frame normalised between 0 and 1 based on start and end point of timeline",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "3d View"}

import bpy                                      #needed in a script-text-window!
def fget(self):                                 # custom get function
    #normframe = (bpy.context.scene.frame_current-bpy.context.scene.frame_start) / ( bpy.context.scene.frame_end - bpy.context.scene.frame_start) # normalised
    normframe = (bpy.context.scene.frame_current) / ( bpy.context.scene.frame_end) # normalised
    return normframe                             # return value
bpy.types.Object.distance = 0
bpy.types.Object.distance = property(fget)      # assign function to property, dont know if it should be byp types object but was in the example I grabbed and it seems to work
 
class NormalisedFrameValue(bpy.types.Panel):                 # panel to display new property
    bl_space_type = "VIEW_3D"                   # show up in: 3d-window
    bl_region_type = "UI"                       # show up in: properties panel
    bl_label = "Normalised Frame Value"         # name of the new panel
 
    def draw(self, context):
        # display "distance" of the active object
        if bpy.context.active_object != None:
            if bpy.context.selected_objects == []:
                bpy.types.Object.distance = 0
            else:
                bpy.types.Object.distance = property(fget)
            self.layout.label(text=str(bpy.context.active_object.distance))
 
#bpy.utils.register_class(NormalisedFrameValue)               # register panel

def register():
    bpy.utils.register_class(NormalisedFrameValue)

def unregister():
    bpy.utils.unregister_class(NormalisedFrameValue)