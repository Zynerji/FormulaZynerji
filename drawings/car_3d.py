"""Formula Zynerji — parametric 3D general arrangement (CadQuery).
Builds a simplified GA solid from the dimensional set, exports STEP (real CAD interchange),
and renders an isometric view (PNG/PDF) for the whitepaper via tessellation + matplotlib 3D.
   python drawings/car_3d.py  ->  drawings/car_3d.step, car_3d.{png,pdf}
"""
import os, numpy as np
import cadquery as cq
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

OUT = os.path.dirname(os.path.abspath(__file__))
# --- dimension set (mm) ---
WB, FOH, ROH = 3300, 900, 650
L = WB+FOH+ROH                      # 4850
Wd, Hd = 1800, 950
FAX, RAX = FOH, FOH+WB             # 900, 4200
R, WFr, WRr = 350, 280, 375
TF, TR = 1520, 1425
GREY="#c9d0d8"; DARK="#2b2f36"; RED="#b3122b"; FLR="#9aa4b0"

def boxp(dx,dy,dz,center):                       # box centered at 'center'
    return cq.Workplane("XY").box(dx,dy,dz).translate(center).val()
def wheel(axle_x, y, w):                          # cylinder, axis along Y
    return (cq.Workplane("XY").cylinder(w, R)
            .rotate((0,0,0),(1,0,0),90).translate((axle_x, y, R)).val())

parts = []                                        # (solid, color)
# floor
parts.append((boxp(WB+300, 1200, 40, (FAX+WB/2, 0, 30)), FLR))
# central body (survival cell + engine bay), tapered via two stacked boxes
parts.append((boxp(2700, 700, 480, (2150, 0, 360)), GREY))
parts.append((boxp(1500, 520, 360, (1500, 0, 300)), GREY))     # nose-ward taper
# nose cone
parts.append((boxp(900, 300, 200, (450, 0, 250)), GREY))
# air-box / roll structure behind cockpit
parts.append((boxp(700, 360, 420, (2550, 0, 560)), GREY))
# sidepods
for s in (1,-1):
    parts.append((boxp(1500, 320, 360, (2300, s*470, 300)), GREY))
# wheels
for ax_x,tr,w in [(FAX,TF,WFr),(RAX,TR,WRr)]:
    for s in (1,-1):
        parts.append((wheel(ax_x, s*tr/2, w), DARK))
# front wing (full width, low)
parts.append((boxp(360, Wd, 60, (150, 0, 110)), RED))
# rear wing (elevated on posts)
parts.append((boxp(420, 1000, 50, (4650, 0, 880)), RED))
for s in (1,-1):
    parts.append((boxp(40, 60, 480, (4650, s*300, 620)), DARK))

# --- export STEP (single compound; real CAD asset) ---
compound = cq.Compound.makeCompound([s for s,_ in parts])
cq.exporters.export(compound, os.path.join(OUT, "car_3d.step"))

# --- render isometric via tessellation ---
fig = plt.figure(figsize=(11,5.5));
def draw(ax, elev, azim, title):
    for solid, col in parts:
        verts, tris = solid.tessellate(2.0)
        P = np.array([[v.x, v.y, v.z] for v in verts])
        faces = [P[list(t)] for t in tris]
        ax.add_collection3d(Poly3DCollection(faces, facecolor=col, edgecolor="#33373d",
                                             linewidths=0.15, alpha=1.0))
    ax.set_xlim(0,L); ax.set_ylim(-L/2,L/2); ax.set_zlim(0,L)   # equal cube
    ax.set_box_aspect((L, L, L)); ax.view_init(elev=elev, azim=azim)
    ax.set_axis_off(); ax.set_title(title, fontsize=10, color="#1b2430", fontweight="bold")
ax1 = fig.add_subplot(1,2,1, projection="3d"); draw(ax1, 22, -60, "ISOMETRIC")
ax2 = fig.add_subplot(1,2,2, projection="3d"); draw(ax2, 8, -90, "SIDE")
fig.suptitle("FORMULA ZYNERJI — PARAMETRIC 3D GENERAL ARRANGEMENT  (CadQuery → STEP)",
             fontsize=12, fontweight="bold", color="#1b2430", x=0.02, ha="left")
fig.text(0.02,0.02,"Simplified parametric solid from the dimensional set (WB 3300 · L 4850 · W 1800 · 18\" wheels). "
         "STEP exported as car_3d.step.", fontsize=8, color="#7a8694")
fig.savefig(os.path.join(OUT,"car_3d.pdf"), bbox_inches="tight")
fig.savefig(os.path.join(OUT,"car_3d.png"), dpi=150, bbox_inches="tight")
print("saved drawings/car_3d.step, car_3d.{png,pdf}")
