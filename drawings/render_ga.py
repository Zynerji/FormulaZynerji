"""Formula Zynerji — compose the FreeCAD-TechDraw HLR projections (ga_edges.json) into a
true engineering general-arrangement sheet: third-angle orthographic trio (plan, side, front)
sharing one 1:1 scale, plus a fit-to-box isometric, with dimension callouts, a 1 m scale bar
and a title block.  Outputs car_ga_cad.{pdf,svg,png}.

Pipeline:  car_3d.step --(freecad_ga.py: TechDraw.project HLR)--> ga_edges.json --(this)--> sheet
"""
import os, json
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.patches import Rectangle

OUT = os.path.dirname(os.path.abspath(__file__))
INK = "#1b2430"; ACC = "#b3122b"; MUT = "#7a8694"; PAPER = "#ffffff"
data = json.load(open(os.path.join(OUT, "ga_edges.json")))

KEY = {"plan": "PLAN  (top)", "side": "SIDE ELEVATION",
       "front": "FRONT ELEVATION", "iso": "ISOMETRIC"}

def bbox(polys):
    xs = [p[0] for pl in polys for p in pl]; ys = [p[1] for pl in polys for p in pl]
    return min(xs), min(ys), max(xs), max(ys)

def placed(polys, dx, dy, s=1.0, ox=0.0, oy=0.0):
    """translate (after optional scale about view min) -> sheet coords."""
    return [[((p[0]-ox)*s+dx, (p[1]-oy)*s+dy) for p in pl] for pl in polys]

def add(ax, polys, lw=0.5, color=INK, z=3):
    ax.add_collection(LineCollection(polys, colors=color, linewidths=lw, zorder=z))

fig = plt.figure(figsize=(16.5, 11.7))           # ~A3 landscape
ax = fig.add_axes([0, 0, 1, 1]); ax.set_aspect("equal"); ax.axis("off")

# ---- placement of the three orthographic views (shared 1:1 scale, mm) ----
# side & plan share the length axis (vertically aligned, true third angle)
sx0, sy0, sx1, sy1 = bbox(data[KEY["side"]])     # x[-40,4875] y[0,970]
px0, py0, px1, py1 = bbox(data[KEY["plan"]])     # x[-40,4875] y[-900,900]
fx0, fy0, fx1, fy1 = bbox(data[KEY["front"]])    # x[-900,900] y[0,970]

GAP = 520
side_dx, side_dy = -sx0, 4100 - sy0              # side at top, min->(0,4100)
plan_dx, plan_dy = -px0, 1850 - py0              # plan below, x-aligned, min->(0,1850)
front_dx, front_dy = -fx0, 0 - fy0              # front bottom-left, min->(0,0)

side  = placed(data[KEY["side"]],  side_dx, side_dy)
plan  = placed(data[KEY["plan"]],  plan_dx, plan_dy)
front = placed(data[KEY["front"]], front_dx, front_dy)
add(ax, side); add(ax, plan); add(ax, front)

# ---- isometric: own scale, fit to bottom-centre cell ----
ix0, iy0, ix1, iy1 = bbox(data[KEY["iso"]])
boxW, boxH = 1750, 1650
iscale = min(boxW/(ix1-ix0), boxH/(iy1-iy0))
icell_x, icell_y = 2250, 60
iso = placed(data[KEY["iso"]], icell_x, icell_y, s=iscale, ox=ix0, oy=iy0)
add(ax, iso, lw=0.45, color=INK)

# ---- view labels ----
def vlabel(x, y, t, sub=None):
    ax.text(x, y, t, fontsize=11, fontweight="bold", color=INK, ha="left", va="top")
    if sub: ax.text(x, y-130, sub, fontsize=8, color=MUT, ha="left", va="top")
vlabel(0, 5180, "SIDE ELEVATION", "scale 1:1 (true)")
vlabel(0, 1820, "PLAN")
vlabel(0, -60, "FRONT ELEVATION")
vlabel(icell_x, iy0*0+ (iy1-iy0)*iscale+250+icell_y, "ISOMETRIC", "not to scale")

# ---- dimension helper ----
def dim(p0, p1, text, off, vert=False, fs=8.5):
    (x0, y0), (x1, y1) = p0, p1
    if vert:
        x = x0 + off
        ax.plot([x0, x], [y0, y0], color=MUT, lw=.5); ax.plot([x1, x], [y1, y1], color=MUT, lw=.5)
        ax.annotate("", (x, y0), (x, y1), arrowprops=dict(arrowstyle="<|-|>", color=INK, lw=.8, mutation_scale=8))
        ax.text(x+ (40 if off>0 else -40), (y0+y1)/2, text, rotation=90, ha="center", va="center",
                fontsize=fs, color=INK, backgroundcolor="white")
    else:
        y = y0 + off
        ax.plot([x0, x0], [y0, y], color=MUT, lw=.5); ax.plot([x1, x1], [y1, y], color=MUT, lw=.5)
        ax.annotate("", (x0, y), (x1, y), arrowprops=dict(arrowstyle="<|-|>", color=INK, lw=.8, mutation_scale=8))
        ax.text((x0+x1)/2, y+ (40 if off>0 else -90), text, ha="center", va="center",
                fontsize=fs, color=INK, backgroundcolor="white")

# side: overall length (above), wheelbase (in gap below), overall height (left of nose)
dim((side_dx+sx0, side_dy+970), (side_dx+sx1, side_dy+970), "OVERALL LENGTH  4850", 300)
dim((side_dx+900, side_dy+350), (side_dx+4200, side_dy+350), "WHEELBASE  3300", -560)
dim((side_dx+sx0, side_dy+0), (side_dx+sx0, side_dy+970), "≈930", -360, vert=True)
# plan: overall width (left of body)
dim((plan_dx-360, plan_dy+0), (plan_dx-360, plan_dy+(py1-py0)), "WIDTH  1800", 0, vert=True)
# front: track / width + height
dim((front_dx+0, front_dy-300), (front_dx+(fx1-fx0), front_dy-300), "TRACK 1520 / 1425", 0)
dim((front_dx+(fx1-fx0)+330, front_dy), (front_dx+(fx1-fx0)+330, front_dy+970), "≈930", 0, vert=True)

# ---- 1 m scale bar (orthographic views) — in the clear zone right of the plan ----
bx, by = 5020, 2780
for i in range(5):
    ax.add_patch(Rectangle((bx+i*200, by), 200, 70, fc=(INK if i % 2 else "white"),
                           ec=INK, lw=0.7, zorder=5))
ax.text(bx, by+150, "0", fontsize=7.5, ha="center", color=INK)
ax.text(bx+1000, by+150, "1000 mm", fontsize=7.5, ha="center", color=INK)
ax.text(bx+500, by-120, "SCALE BAR (orthographic views, 1:1)", fontsize=7.5, ha="center", color=MUT)

# ---- title block (bottom-right) ----
tbx, tby, tbw, tbh = 4150, 0, 1760, 1180
ax.add_patch(Rectangle((tbx, tby), tbw, tbh, fc="white", ec=INK, lw=1.4, zorder=6))
def trow(yfrac, h, label, val, big=False):
    y = tby + tbh*yfrac
    ax.plot([tbx, tbx+tbw], [y, y], color=INK, lw=0.7, zorder=7)
    ax.text(tbx+60, y - tbh*h*0.5, label, fontsize=7, color=MUT, ha="left", va="center", zorder=7)
    ax.text(tbx+tbw-60, y - tbh*h*0.5, val, fontsize=10 if big else 8.5,
            fontweight="bold" if big else "normal", color=INK, ha="right", va="center", zorder=7)
ax.text(tbx+tbw/2, tby+tbh-150, "FORMULA  ZYNERJI", fontsize=14, fontweight="bold",
        color=ACC, ha="center", va="center", zorder=7)
ax.text(tbx+tbw/2, tby+tbh-300, "GENERAL ARRANGEMENT — Mk.0 vehicle", fontsize=8.5,
        color=INK, ha="center", va="center", zorder=7)
ax.plot([tbx, tbx+tbw], [tby+tbh-380, tby+tbh-380], color=INK, lw=0.7, zorder=7)
trow(0.62, 0.16, "PROJECTION", "third angle")
trow(0.46, 0.16, "UNITS", "millimetres")
trow(0.30, 0.16, "DRAWN BY", "FreeCAD TechDraw (HLR)")
trow(0.14, 0.16, "SOURCE", "car_3d.step")
ax.text(tbx+60, tby+tbh*0.07, "DATE  2026-05  ·  SHEET 1/1  ·  REV 0", fontsize=7,
        color=MUT, ha="left", va="center", zorder=7)

# third-angle projection symbol (cone) by the title block
cx, cy = 4220, 1320
ax.add_patch(plt.Circle((cx, cy), 55, fill=False, ec=INK, lw=0.9, zorder=6))
ax.add_patch(plt.Circle((cx+150, cy), 90, fill=False, ec=INK, lw=0.9, zorder=6))
for r, xc in ((55, cx), (90, cx+150)):
    ax.plot([xc-r, xc+r], [cy, cy], color=INK, lw=0.6, zorder=6)
    ax.plot([xc, xc], [cy-r, cy+r], color=INK, lw=0.6, zorder=6)
ax.text(cx+75, cy+150, "third-angle", fontsize=6.5, ha="center", color=MUT, zorder=6)

# ---- outer frame ----
ax.add_patch(Rectangle((-650, -700), 6900, 6300, fill=False, ec=INK, lw=1.8, zorder=1))
ax.add_patch(Rectangle((-520, -560), 6640, 6020, fill=False, ec=INK, lw=0.6, zorder=1))

ax.set_xlim(-800, 6400); ax.set_ylim(-850, 5750)
for ext in ("pdf", "svg"):
    fig.savefig(os.path.join(OUT, "car_ga_cad." + ext), bbox_inches="tight")
fig.savefig(os.path.join(OUT, "car_ga_cad.png"), dpi=150, bbox_inches="tight")
plt.close(fig)
print("saved drawings/car_ga_cad.{pdf,svg,png}")
