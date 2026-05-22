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

# --- dump tessellated mesh + colors as JSON (for the Blender renderer) ---
import json
_dump=[]
for _solid,_c in parts:
    _vs,_ts=_solid.tessellate(0.8)
    _dump.append({"color":list(_c),"verts":[[v.x,v.y,v.z] for v in _vs],"faces":[list(t) for t in _ts]})
json.dump(_dump, open(os.path.join(OUT,"car_parts.json"),"w"))

# --- render with PyVista ---
def to_mesh(solid, tol=1.0):
    vs, ts = solid.tessellate(tol)
    pts = np.array([[v.x,v.y,v.z] for v in vs])
    f = np.empty((len(ts),4),np.int64); f[:,0]=3; f[:,1:]=np.array(ts)
    return pv.PolyData(pts, f.ravel())

pv.OFF_SCREEN=True
ground = pv.Plane(center=(L/2,0,0), direction=(0,0,1), i_size=L*1.22, j_size=L*0.72)
meshes = [(to_mesh(s), c) for s,c in parts]

def render(view, fname, wsize, zoom):
    pl = pv.Plotter(off_screen=True, window_size=wsize, border=False)
    pl.set_background("white")
    pl.add_mesh(ground, color=(0.95,0.96,0.97), ambient=0.55, diffuse=0.45, specular=0)
    for m,c in meshes:
        pl.add_mesh(m, color=c, smooth_shading=True, specular=0.25, specular_power=12,
                    ambient=0.30, diffuse=0.80)
    if view=="iso": pl.view_isometric()
    else: pl.camera_position="xz"               # side profile (length x height)
    pl.camera.zoom(zoom)
    try: pl.enable_anti_aliasing("ssaa")
    except Exception: pass
    try: pl.enable_shadows()
    except Exception: pass
    pl.screenshot(fname); pl.close()

# window aspect matched to each view's natural framing (squarer iso, wide-short side)
render("iso",  os.path.join(OUT,"_car3d_iso.png"),  (1300,1120), 1.62)
render("side", os.path.join(OUT,"_car3d_side.png"), (1950, 720), 1.55)

# compose iso (hero, top) + side (full-width strip, below) -> car_3d.png/pdf for LaTeX
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
def autocrop(img, thr=0.93, pad=12):                       # trim near-white margins to content
    rgb = img[..., :3]; mask = (rgb < thr).any(2)
    if not mask.any(): return img
    ys, xs = np.where(mask)
    y0 = max(0, ys.min()-pad); y1 = min(img.shape[0], ys.max()+1+pad)
    x0 = max(0, xs.min()-pad); x1 = min(img.shape[1], xs.max()+1+pad)
    return img[y0:y1, x0:x1]
iso = autocrop(plt.imread(os.path.join(OUT,"_car3d_iso.png")))
sde = autocrop(plt.imread(os.path.join(OUT,"_car3d_side.png")))
ari = iso.shape[1]/iso.shape[0]; ars = sde.shape[1]/sde.shape[0]
W = 6.6                                                     # figure width (in)
iso_w = 0.74*W; iso_h = iso_w/ari                           # iso centred on top
sde_w = W;       sde_h = sde_w/ars                          # side full-width strip below
lab, gap, mb = 0.34, 0.30, 0.06
Hf = mb + sde_h + lab + gap + iso_h + lab
fig = plt.figure(figsize=(W, Hf))
ax_i = fig.add_axes([(W-iso_w)/2/W, (mb+sde_h+lab+gap)/Hf, iso_w/W, iso_h/Hf])
ax_i.imshow(iso); ax_i.axis("off")
ax_i.set_title("ISOMETRIC", fontsize=11, fontweight="bold", color="#1b2430")
ax_s = fig.add_axes([0.0, mb/Hf, sde_w/W, sde_h/Hf])
ax_s.imshow(sde); ax_s.axis("off")
ax_s.set_title("SIDE ELEVATION", fontsize=11, fontweight="bold", color="#1b2430")
fig.savefig(os.path.join(OUT,"car_3d.png"), dpi=200, bbox_inches="tight")
fig.savefig(os.path.join(OUT,"car_3d.pdf"), bbox_inches="tight"); plt.close(fig)
for t in ("_car3d_iso.png","_car3d_side.png","_pvtest.png"):
    p=os.path.join(OUT,t)
    if os.path.exists(p): os.remove(p)
print("saved drawings/car_3d.step, car_3d.{png,pdf}")
