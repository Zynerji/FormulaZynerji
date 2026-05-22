"""Formula Zynerji — driver-vectored twin wet-clutch differential (open-loop) + control law.
   python drawings/diff_schematic.py  ->  drawings/diff_schematic.{svg,png,pdf}"""
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, FancyArrowPatch
from _draw import style, save, box, arrow, INK, ACC, MUT, FILL
BLUE="#1f6fb2"; GREEN="#1e7d4f"; RED="#b3122b"

fig, ax = plt.subplots(figsize=(12, 7.6)); ax.set_xlim(0,100); ax.set_ylim(0,100); style(ax)

# steering wheel + two analog triggers
ax.add_patch(Circle((50,90),6, fc="white", ec=INK, lw=2)); ax.text(50,90,"wheel",ha="center",va="center",fontsize=8)
box(ax,(20,85),16,8,"LEFT trigger\n(% lockup L)",fc="#dfe9f3",fs=8)
box(ax,(64,85),16,8,"RIGHT trigger\n(% lockup R)",fc="#dfe9f3",fs=8)
# ECU
box(ax,(34,64),32,11,"Standard Safety ECU\nmaps trigger position -> clutch clamp",fc=FILL,fs=8.5)
arrow(ax,(28,85),(40,75),color=GREEN); arrow(ax,(72,85),(60,75),color=GREEN)
ax.text(50,80,"driver command (open-loop)",ha="center",fontsize=8,color=GREEN,backgroundcolor="white")
# final drive
box(ax,(40,48),20,8,"final drive\n(from 2013 gearbox)",fc=FILL,fs=8)
arrow(ax,(50,64),(50,56),color=INK,lw=1.2,st="-")  # ECU sits above; visual link
# clutch packs
box(ax,(16,30),24,9,"wet multi-plate\nclutch — LEFT",fc="#efe6c8",fs=8.5)
box(ax,(60,30),24,9,"wet multi-plate\nclutch — RIGHT",fc="#efe6c8",fs=8.5)
arrow(ax,(44,48),(30,39),color=INK,text="drive",fs=8)      # final drive -> clutches
arrow(ax,(56,48),(72,39),color=INK,text="drive",fs=8)
arrow(ax,(40,69),(28,39),color=GREEN,lw=1.6)               # ECU clamp -> L
arrow(ax,(60,69),(72,39),color=GREEN,lw=1.6)               # ECU clamp -> R
ax.text(20,52,"clamp\npressure",ha="center",fontsize=7,color=GREEN)
ax.text(80,52,"clamp\npressure",ha="center",fontsize=7,color=GREEN)
# wheels
box(ax,(18,12),20,8,"REAR WHEEL L",fc="#2b2f36",tc="white",fs=8.5)
box(ax,(62,12),20,8,"REAR WHEEL R",fc="#2b2f36",tc="white",fs=8.5)
arrow(ax,(28,30),(28,20),color=INK); arrow(ax,(72,30),(72,20),color=INK)
ax.text(50,25,"more clamp on a side  ->  more torque to that wheel  (no central diff)",
        ha="center",fontsize=8.5,color=INK)
# legality / safety notes
box(ax,(1,0.5),47,10,"OPEN-LOOP & LEGAL\ntrigger→clamp map is fixed, declared, on-chain;\n"
    "ECU adds NO sensor feedback.\nFail-safe → even baseline · clamp-rate limited (~0.4 s)",
    fc="#e3f0e8",ec=GREEN,fs=7)
box(ax,(52,0.5),47,10,"BANNED (Art. 8.4.3)\nany CLOSED-LOOP vectoring from\nyaw / wheel-slip / steering sensors\n"
    "= an automated car-control aid",
    fc="#f6e1e1",ec=RED,fs=7)

fig.suptitle("FORMULA ZYNERJI — DRIVER-VECTORED REAR DIFFERENTIAL  (twin wet-clutch, GKN Twinster-type)",
             fontsize=12,fontweight="bold",color=INK,x=0.02,ha="left")
save(fig,"diff_schematic"); print("saved drawings/diff_schematic.{svg,png,pdf}")
