"""Formula Zynerji — parametric 3D general arrangement (CadQuery), rendered with PyVista.
Builds a lofted GA solid from the dimensional set, exports STEP, and renders lit isometric +
side views (high-res PNG, wrapped to PDF for LaTeX).
   python drawings/car_3d.py  ->  drawings/car_3d.step, car_3d.{png,pdf}
"""
import os, numpy as np
import cadquery as cq
import pyvista as pv

OUT = os.path.dirname(os.path.abspath(__file__))
# --- dimensions (mm) ---
FOH, WB, ROH = 900, 3300, 650
L = FOH+WB+ROH
FAX, RAX = FOH, FOH+WB
R, WFr, WRr = 350, 280, 375
TF, TR = 1520, 1425
GREY=(0.80,0.82,0.85); DARK=(0.17,0.18,0.21); RED=(0.70,0.07,0.17); FLOORC=(0.30,0.33,0.37)

def boxc(dx,dy,dz,c):
    return cq.Solid.makeBox(dx,dy,dz, cq.Vector(c[0]-dx/2,c[1]-dy/2,c[2]-dz/2))
def wheelc(x,yc,w):                       # cylinder, axis +Y, centered at (x,yc,R)
    return cq.Solid.makeCylinder(R, w, cq.Vector(x, yc-w/2, R), cq.Vector(0,1,0))
def rect_wire(x,w,h,zc):                  # closed rectangle in the YZ plane at world x
    pts=[cq.Vector(x,-w/2,zc-h/2),cq.Vector(x, w/2,zc-h/2),cq.Vector(x, w/2,zc+h/2),
         cq.Vector(x,-w/2,zc+h/2),cq.Vector(x,-w/2,zc-h/2)]
    return cq.Wire.makePolygon(pts)

# lofted body: rectangular sections (x, width, height, z-center)
sections=[(0,220,150,110),(700,480,300,230),(1500,700,470,320),
          (2400,680,540,360),(3400,600,460,330),(4200,470,420,300),(L,340,320,255)]
body = cq.Solid.makeLoft([rect_wire(x,w,h,zc) for (x,w,h,zc) in sections], False)

parts=[(body,GREY)]
parts.append((boxc(WB+260,1180,46,(FAX+WB/2,0,30)),FLOORC))                 # floor
parts.append((boxc(900,300,180,(420,0,250)),GREY))                          # nose tip block
for s in (1,-1):
    parts.append((boxc(1500,300,360,(2300,s*470,300)),GREY))                # sidepods
for ax_x,tr,w in [(FAX,TF,WFr),(RAX,TR,WRr)]:                               # wheels
    for s in (1,-1):
        parts.append((wheelc(ax_x, s*tr/2, w),DARK))
# front wing + endplates
parts.append((boxc(380,1740,55,(150,0,105)),RED))
for s in (1,-1): parts.append((boxc(380,40,230,(150,s*860,170)),DARK))
# rear wing + endplates + posts
parts.append((boxc(430,1000,55,(4660,0,900)),RED))
for s in (1,-1): parts.append((boxc(430,40,300,(4660,s*500,820)),DARK))
for s in (1,-1): parts.append((boxc(50,60,520,(4660,s*250,620)),DARK))
# roll hoop / halo (upper half-torus arching over the cockpit, axis along X)
try:
    halo = cq.Solid.makeTorus(330, 28, cq.Vector(2150,0,540), cq.Vector(1,0,0), 0, 180)
    parts.append((halo,DARK))
except Exception as e:
    print("halo skipped:", e)

# --- export STEP ---
cq.exporters.export(cq.Compound.makeCompound([s for s,_ in parts]), os.path.join(OUT,"car_3d.step"))

# --- render with PyVista ---
def to_mesh(solid, tol=1.0):
    vs, ts = solid.tessellate(tol)
    pts = np.array([[v.x,v.y,v.z] for v in vs])
    f = np.empty((len(ts),4),np.int64); f[:,0]=3; f[:,1:]=np.array(ts)
    return pv.PolyData(pts, f.ravel())

pv.OFF_SCREEN=True
ground = pv.Plane(center=(L/2,0,0), direction=(0,0,1), i_size=L*1.7, j_size=L*1.2)
meshes = [(to_mesh(s), c) for s,c in parts]

def render(view, fname):
    pl = pv.Plotter(off_screen=True, window_size=(1500,1050), border=False)
    pl.set_background("white")
    pl.add_mesh(ground, color=(0.95,0.96,0.97), ambient=0.55, diffuse=0.45, specular=0)
    for m,c in meshes:
        pl.add_mesh(m, color=c, smooth_shading=True, specular=0.25, specular_power=12,
                    ambient=0.30, diffuse=0.80)
    if view=="iso": pl.view_isometric()
    else: pl.camera_position="xz"               # side profile (length x height)
    pl.camera.zoom(1.35)
    try: pl.enable_anti_aliasing("ssaa")
    except Exception: pass
    try: pl.enable_shadows()
    except Exception: pass
    pl.screenshot(fname); pl.close()

render("iso",  os.path.join(OUT,"_car3d_iso.png"))
render("side", os.path.join(OUT,"_car3d_side.png"))

# compose iso + side -> car_3d.png/pdf for LaTeX
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
iso = plt.imread(os.path.join(OUT,"_car3d_iso.png")); sde = plt.imread(os.path.join(OUT,"_car3d_side.png"))
fig = plt.figure(figsize=(11,4.6))
a1=fig.add_axes([0.00,0.02,0.60,0.86]); a1.imshow(iso); a1.axis("off"); a1.set_title("ISOMETRIC",fontsize=10,color="#1b2430")
a2=fig.add_axes([0.60,0.02,0.40,0.86]); a2.imshow(sde); a2.axis("off"); a2.set_title("SIDE",fontsize=10,color="#1b2430")
fig.suptitle("FORMULA ZYNERJI — PARAMETRIC 3D GENERAL ARRANGEMENT  (CadQuery → STEP)",
             fontsize=12, fontweight="bold", color="#1b2430", x=0.02, ha="left")
fig.text(0.02,0.01,"Lofted parametric solid from the dimensional set (WB 3300 · L 4850 · W 1800 · 18\" wheels). "
         "STEP: car_3d.step.", fontsize=8, color="#7a8694")
fig.savefig(os.path.join(OUT,"car_3d.png"), dpi=150, bbox_inches="tight")
fig.savefig(os.path.join(OUT,"car_3d.pdf"), bbox_inches="tight"); plt.close(fig)
for t in ("_car3d_iso.png","_car3d_side.png","_pvtest.png"):
    p=os.path.join(OUT,t)
    if os.path.exists(p): os.remove(p)
print("saved drawings/car_3d.step, car_3d.{png,pdf}")
