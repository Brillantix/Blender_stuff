import bpy

#setting the rendering engine
bpy.context.scene.render.engine = "CYCLES"

#adding a material
materialt = bpy.data.materials.new(name="material testowy")
materialt.use_nodes = True

#assigning it to an object
object = bpy.context.object
object.data.materials[0] = materialt

#adding and setting nodes
outp_node = materialt.node_tree.nodes.get("Material Output")
outp_node.location = (0, 0)

diff_node = materialt.node_tree.nodes.get("Diffuse BSDF")
diff_node.location = (-500, 150)

gloss_node = materialt.node_tree.nodes.new(type="ShaderNodeBsdfGlossy")
gloss_node.location = (-500, -150)
gloss_node.inputs[1].default_value = 0.117

mix_shad_node = materialt.node_tree.nodes.new(type="ShaderNodeMixShader")
mix_shad_node.location = (-300, 0)

mix_shad_node.inputs[0].default_value = 0.3
diff_node.inputs[0].default_value = (0.04, 0.08, 1, 1)

noise_tex_node = materialt.node_tree.nodes.new(type="ShaderNodeTexNoise")
noise_tex_node.location = (-170, - 200)
noise_tex_node.inputs[1].default_value = 7.7
noise_tex_node.inputs[2].default_value = 4.8
noise_tex_node.inputs[3].default_value = 0.3

#linking nodes
materialt.node_tree.links.new(mix_shad_node.outputs[0], outp_node.inputs[0])
materialt.node_tree.links.new(diff_node.outputs[0], mix_shad_node.inputs[1])
materialt.node_tree.links.new(gloss_node.outputs[0], mix_shad_node.inputs[2])
materialt.node_tree.links.new(noise_tex_node.outputs[0], outp_node.inputs[2])

#editing default cube
#switching mode
bpy.ops.object.mode_set(mode="EDIT")

#switching select mode to vertices
bpy.ops.mesh.select_mode(type="VERT")
#deselecting all verts
bpy.ops.mesh.select_all(action="DESELECT")

#switching mode
bpy.ops.object.mode_set(mode="OBJECT")
bpy.types.SpaceView3D.pivot_point='CURSOR'
bpy.types.SpaceView3D.cursor_location = (0.0, 0.0, 0.0)
#selecting 4 vertices
l = [[0,1,2,3],[4,5,6,7]]
for sciana in l:
	for i in range(0,4):
		m = sciana[i]
		object.data.vertices[m].select = True
	#switching mode
	bpy.ops.object.mode_set(mode="EDIT")
	#bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0, 0, .1)})
	bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0, 0, 0)})
	bpy.ops.transform.resize(value=(0.8, 0.8, 0.8))
	bpy.ops.mesh.select_all(action="DESELECT")
	bpy.ops.object.mode_set(mode="OBJECT")
