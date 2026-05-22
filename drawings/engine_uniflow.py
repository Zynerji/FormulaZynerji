"""Formula Zynerji — 2.5 L I5 two-stroke UNIFLOW diesel: cylinder cross-section + gas-path.
   python drawings/engine_uniflow.py  ->  drawings/engine_uniflow.{svg,png}"""
import numpy as np, matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle, Circle, FancyArrowPatch
from _draw import style, label, save, box, arrow, INK, ACC, MUT, FILL

BLUE="#1f6fb2"; RED="#b3122b"

fig, (axc, axs) = plt.subplots(1, 2, figsize=(12, 7), gridspec_kw=dict(width_ratios=[1, 1.25]))

# ---------- LEFT: single-cylinder cross-section (uniflow) ----------
axc.set_xlim(-3.2, 3.2); axc.set_ylim(-1.2, 10.2); style(axc, "UNIFLOW CYLINDER (cross-section)")
# bore walls
axc.add_patch(Rectangle((-2,0),4,8.2, fc="white", ec=INK, lw=1.6, zorder=1))
# head
axc.add_patch(Rectangle((-2.2,8.2),4.4,1.2, fc=FILL, ec=INK, lw=1.6, zorder=2))
# exhaust poppet valves in head (two)
for vx in (-1.0,1.0):
    axc.add_patch(Polygon([(vx-0.45,8.3),(vx+0.45,8.3),(vx+0.18,9.0),(vx-0.18,9.0)],closed=True,
                          fc="#cfd6de",ec=INK,lw=1.2,zorder=3))
    axc.plot([vx,vx],[9.0,10.0],color=INK,lw=2.2,zorder=3)            # valve stem
# central injector
axc.plot([0,0],[8.2,9.6],color=RED,lw=2.6,zorder=4)
axc.add_patch(Circle((0,8.05),0.13,fc=RED,ec=RED,zorder=5))
# piston near BDC (uncovering intake ports)
axc.add_patch(Rectangle((-2,1.2),4,1.5, fc="#2b2f36", ec=INK, lw=1.4, zorder=4))
axc.plot([0,0],[-1.2,1.2],color=INK,lw=2.0,zorder=3)                  # con-rod hint
# intake ports: two openings in the lower liner (piston-uncovered near BDC), fresh air in
axc.add_patch(Rectangle((-2.0,0.3),0.5,0.9, fc=BLUE, ec=INK, lw=1, alpha=.5, zorder=5))
axc.add_patch(Rectangle(( 1.5,0.3),0.5,0.9, fc=BLUE, ec=INK, lw=1, alpha=.5, zorder=5))
arrow(axc,(-3.0,0.75),(-1.5,0.9),color=BLUE,lw=2.2)
arrow(axc,( 3.0,0.75),( 1.5,0.9),color=BLUE,lw=2.2)
# uniflow sweep arrows (bottom -> top)
for ax_x in (-0.9,0.9):
    arrow(axc,(ax_x,3.2),(ax_x,7.6),color=BLUE,lw=1.8)
# exhaust out (red, up through valves)
arrow(axc,(-1.0,9.4),(-1.0,10.1),color=RED,lw=2.2); arrow(axc,(1.0,9.4),(1.0,10.1),color=RED,lw=2.2)
label(axc,(1.0,8.65),"exhaust poppet valves (in head)",(1.6,6.4))
label(axc,(0,9.0),"common-rail DI injector",(0.4,9.9))
label(axc,(-2.0,0.75),"intake ports (piston-uncovered, blower-fed)",(-3.1,-0.9))
label(axc,(2.0,2.0),"piston",(2.4,2.4))
axc.text(0,5.4,"UNIFLOW\nair sweeps\nbottom → top",ha="center",va="center",fontsize=9,color=BLUE,fontweight="bold")

# ---------- RIGHT: gas-path / system schematic ----------
axs.set_xlim(0,100); axs.set_ylim(0,100); style(axs,"GAS PATH & SYSTEM (2.5 L I5 · 7000 rpm · ~1015 hp)")
box(axs,(4,78),20,12,"air\nintake",fc="white")
box(axs,(30,78),26,12,"screw (Lysholm)\nsupercharger",fc="#dfe9f3")
box(axs,(62,78),22,12,"intercooler",fc="#dfe9f3")
arrow(axs,(24,84),(30,84),color=BLUE); arrow(axs,(56,84),(62,84),color=BLUE)
arrow(axs,(73,78),(73,64),color=BLUE)                      # down to plenum
box(axs,(20,52),64,10,"intake plenum  →  intake ports (uniflow)",fc="#dfe9f3",fs=9)
arrow(axs,(73,62),(73,52),color=BLUE)
# the five cylinders
for i in range(5):
    box(axs,(20+i*13,34),11,12,f"cyl {i+1}",fc=FILL,fs=8)
for i in range(5):
    arrow(axs,(25.5+i*13,52),(25.5+i*13,46),color=BLUE,lw=1.3)   # plenum -> cyl
    arrow(axs,(25.5+i*13,34),(25.5+i*13,28),color=RED,lw=1.3)    # cyl -> exhaust
box(axs,(18,16),62,10,"exhaust  →  VLEM (tuned, set-and-run)",fc="#f3dfe3",fs=9)
arrow(axs,(80,21),(95,21),color=RED,text="out",fs=8)
axs.text(50,6,"compression-ignition · JP-8-class synthetic e-kerosene · NO traction hybrid",
         ha="center",fontsize=8.5,color=MUT)
axs.text(73,92,"blue = fresh charge   red = exhaust",ha="center",fontsize=8,color=MUT)

fig.suptitle("FORMULA ZYNERJI — 2.5 L INLINE-5 TWO-STROKE UNIFLOW DIESEL",
             fontsize=12,fontweight="bold",color=INK,x=0.02,ha="left")
save(fig,"engine_uniflow"); print("saved drawings/engine_uniflow.{svg,png}")
