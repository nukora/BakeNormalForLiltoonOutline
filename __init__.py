# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
import bpy
from .operators import BNFLO_OT_bake_normal

bl_info = {
    "name" : "Bake Normals for lilToon Outline",
    "author" : "Nukora",
    "description" : "Bake normals to vertex colors for lilToon outline.",
    "blender" : (3, 5, 0),
    "version" : (1, 0, 2),
    "location" : "View3D > Object",
    "warning" : "",
    "category" : "Object"
}

classes = (
    BNFLO_OT_bake_normal,
)

def menu_fn(self, context):
    self.layout.operator(BNFLO_OT_bake_normal.bl_idname, text="Bake Normal (lilToon)", icon='PLUGIN')

def register():
    for c in classes:
        bpy.utils.register_class(c)
    bpy.types.VIEW3D_MT_object.append(menu_fn)

def unregister():
    bpy.types.VIEW3D_MT_object.remove(menu_fn)
    for c in classes:
        bpy.utils.unregister_class(c)
