"""Formula Zynerji — TRUE CAD general-arrangement projection via FreeCAD TechDraw HLR.

Run headless:
  "C:\\Program Files\\FreeCAD 1.0\\bin\\freecadcmd.exe" drawings/freecad_ga.py

Loads car_3d.step and uses TechDraw's hidden-line-removal engine (TechDraw.project)
to compute true orthographic + isometric projections of the solid. Each view's
visible edges are discretised to 2D polylines and written to ga_edges.json, which
render_ga.py composes into the engineering general-arrangement sheet (car_ga_cad.pdf).

Driving TechDraw.project() directly (rather than DrawViewPart + writeDXFPage) is
required because DrawViewPart.execute() does not run HLR without the GUI, so the
page-export route yields empty geometry headless.
"""
import FreeCAD as App, Part, os, json

OUT = r"C:\Users\cknop\.local\bin\FormulaZynerji\drawings"
STEP = os.path.join(OUT, "car_3d.step")
import TechDraw

shape = Part.Shape(); shape.read(STEP)
print("source: edges=%d faces=%d" % (len(shape.Edges), len(shape.Faces)))

# (name, projection direction, (h,v) extractor from projected point p)
VIEWS = [
    ("PLAN  (top)",        (0, 0, 1),  lambda p: (p.x,  p.y)),   # length x, width y
    ("SIDE ELEVATION",     (0, -1, 0), lambda p: (p.y, -p.x)),   # length, height(=Z)
    ("FRONT ELEVATION",    (1, 0, 0),  lambda p: (p.y,  p.x)),   # width, height(=Z)
    ("ISOMETRIC",          (1, 1, 1),  lambda p: (p.x,  p.y)),
]

def polylines_from(grp, mapfn):
    out = []
    for e in grp.Edges:
        try:
            pts = e.discretize(Deflection=1.2)
        except Exception:
            pts = [e.Vertexes[0].Point, e.Vertexes[-1].Point]
        if len(pts) < 2:
            continue
        out.append([list(mapfn(p)) for p in pts])
    return out

data = {}
for name, d, mapfn in VIEWS:
    groups = TechDraw.project(shape, App.Vector(*d))
    # group 0 = visible sharp edges, group 2 = visible smooth/outline silhouette
    vis = []
    for gi in (0, 2):
        if gi < len(groups):
            vis += polylines_from(groups[gi], mapfn)
    data[name] = vis
    nseg = sum(len(pl) - 1 for pl in vis)
    print("%-16s polylines=%4d segments=%5d" % (name, len(vis), nseg))

with open(os.path.join(OUT, "ga_edges.json"), "w") as f:
    json.dump(data, f)
print("WROTE", os.path.join(OUT, "ga_edges.json"))
