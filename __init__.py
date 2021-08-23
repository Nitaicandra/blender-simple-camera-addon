'''
Copyright (C) CURRENT_YEAR YOUR NAME
YOUR@MAIL.com

Created by YOUR NAME

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

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


import bpy

from. op import SimpleOperator
from. panel import SimplePanel

classes = (SimpleOperator, SimplePanel)

def register():
   for c in classes:
       bpy.utils.register_class(c)

def unregister():
   for c in classes:
       bpy.utils.unregister_class(c)