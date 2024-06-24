import bpy
import mathutils

class BNFLO_OT_bake_normal(bpy.types.Operator):
    bl_idname = "bnflo.bake_normal"
    bl_label = "Bake Normal (lilToon)"
    bl_options = {"REGISTER", "UNDO"}
    bl_description = "Bake normals to vertex colors for lilToon outline."

    @classmethod
    def poll(cls, context):
        return (
            context.mode == "OBJECT" and
            len(context.selected_objects) == 2 and
            context.selected_objects[0].type == "MESH" and
            context.selected_objects[1].type == "MESH" and
            bpy.context.active_object == context.selected_objects[0]
        )

    def execute(self, context):
        obj0 = context.selected_objects[0]
        obj1 = context.selected_objects[1]

        if bpy.context.active_object == obj0:
            bake_normal(obj0, obj1)

        else:
            bake_normal(obj1, obj0)

        return {"FINISHED"}

def bake_normal(obj, src):
    obj.data.calc_tangents()
    src.data.calc_tangents()

    if not obj.data.vertex_colors:
        obj.data.vertex_colors.new()

    for polygon in obj.data.polygons:
        for loop_index in polygon.loop_indices:
            obj_loop = obj.data.loops[loop_index]

            obj_tangent = obj_loop.tangent
            obj_bitangent = obj_loop.bitangent
            obj_normal = obj_loop.normal

            src_loop = src.data.loops[loop_index]
            src_normal = src_loop.normal

            obj.data.vertex_colors.active.data[loop_index].color = (
                mathutils.Vector.dot(src_normal, obj_tangent) * 0.5 + 0.5,
                mathutils.Vector.dot(src_normal, obj_bitangent) * 0.5 + 0.5,
                mathutils.Vector.dot(src_normal, obj_normal) * 0.5 + 0.5,
                1.0
            )
