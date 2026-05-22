"""Formula Zynerji — Blender (Cycles) hero render of the car from car_parts.json.
Run headless:
  "<blender>" --background --python drawings/blender_render.py
Produces drawings/car_hero.png. Maximal local render (path-traced, denoised, CPU).
"""
import bpy, json, os, math, mathutils, sys

# locate the drawings/ dir (script dir; fallback to known path)
try: OUT = os.path.dirname(os.path.abspath(__file__))
except NameError: OUT = r"C:\Users\cknop\.local\bin\FormulaZynerji\drawings"
S = 0.001  # mm -> m

# clean scene
for o in list(bpy.data.objects): bpy.data.objects.remove(o, do_unlink=True)

parts = json.load(open(os.path.join(OUT, "car_parts.json")))
for i, p in enumerate(parts):
    verts = [(v[0]*S, v[1]*S, v[2]*S) for v in p["verts"]]
    faces = [tuple(f) for f in p["faces"]]
    me = bpy.data.meshes.new(f"p{i}"); me.from_pydata(verts, [], faces); me.update()
    for poly in me.polygons: poly.use_smooth = True
    ob = bpy.data.objects.new(f"p{i}", me); bpy.context.collection.objects.link(ob)
    r, g, b = p["color"]
    mat = bpy.data.materials.new(f"m{i}"); mat.use_nodes = True
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value = (r, g, b, 1)
    dark = (r < 0.25 and g < 0.25 and b < 0.25)
    bsdf.inputs["Roughness"].default_value = 0.65 if dark else 0.30
    if "Metallic" in bsdf.inputs:
        bsdf.inputs["Metallic"].default_value = 0.0 if dark else 0.25
    ob.data.materials.append(mat)

# ground plane
gm = bpy.data.meshes.new("ground")
gm.from_pydata([(-14,-14,0),(14,-14,0),(14,14,0),(-14,14,0)], [], [(0,1,2,3)]); gm.update()
go = bpy.data.objects.new("ground", gm); bpy.context.collection.objects.link(go)
gmat = bpy.data.materials.new("gmat"); gmat.use_nodes = True
gb = gmat.node_tree.nodes.get("Principled BSDF")
gb.inputs["Base Color"].default_value = (0.93,0.94,0.96,1); gb.inputs["Roughness"].default_value = 0.85
go.data.materials.append(gmat)

# world
w = bpy.data.worlds.new("w"); bpy.context.scene.world = w; w.use_nodes = True
bg = w.node_tree.nodes.get("Background")
bg.inputs[0].default_value = (0.88,0.91,0.95,1); bg.inputs[1].default_value = 0.7

# lights
sd = bpy.data.lights.new("sun","SUN"); sd.energy = 3.2; sd.angle = math.radians(3)
so = bpy.data.objects.new("sun", sd); bpy.context.collection.objects.link(so)
so.rotation_euler = (math.radians(55), math.radians(10), math.radians(40))
ad = bpy.data.lights.new("fill","AREA"); ad.energy = 800; ad.size = 8
ao = bpy.data.objects.new("fill", ad); bpy.context.collection.objects.link(ao); ao.location = (-2,-6,5)

# camera (3/4 hero)
cd = bpy.data.cameras.new("cam"); cd.lens = 60
co = bpy.data.objects.new("cam", cd); bpy.context.collection.objects.link(co)
bpy.context.scene.camera = co
co.location = (8.2, -6.8, 3.0)
target = mathutils.Vector((2.4, 0.0, 0.35))
co.rotation_euler = (target - co.location).to_track_quat('-Z','Y').to_euler()

# render
sc = bpy.context.scene
sc.render.engine = 'CYCLES'
sc.cycles.device = 'CPU'
sc.cycles.samples = 96
sc.cycles.use_denoising = True
sc.render.resolution_x = 1600; sc.render.resolution_y = 980
sc.render.image_settings.file_format = 'PNG'
sc.render.filepath = os.path.join(OUT, "car_hero.png")
bpy.ops.render.render(write_still=True)
print("BLENDER: wrote", sc.render.filepath)
