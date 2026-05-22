"""Formula Zynerji — blockchain spine: legality flow + self-balancing economy + revenue streams.
   python drawings/blockchain_economy.py  ->  drawings/blockchain_economy.{svg,png,pdf}"""
import numpy as np, matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from _draw import style, save, box, arrow, INK, ACC, MUT, FILL
BLUE="#1f6fb2"; GREEN="#1e7d4f"; GOLD="#9a7d18"

fig=plt.figure(figsize=(12,13)); gs=GridSpec(3,1,figure=fig,height_ratios=[0.8,1.1,0.95])
axt=fig.add_subplot(gs[0]); axb=fig.add_subplot(gs[1]); axr=fig.add_subplot(gs[2])

# ---- A: legality / disclosure flow (concise labels that fit the boxes) ----
axt.set_xlim(0,100); axt.set_ylim(0,54); style(axt,"A.  ON-CHAIN LEGALITY  (only on-chain parts may run — M10)")
steps=[(9,"Design\na part"),(30,"Upload\nCAD/FEA/CFD"),(51,"Immutable\nledger (hash)"),
       (72,"Scrutineer\n= hash check"),(92,"LEGAL\nto run")]
for i,(cx,t) in enumerate(steps):
    box(axt,(cx-8,32),16,15,t,fc=("#e3f0e8" if i==4 else FILL),ec=(GREEN if i==4 else INK),
        fs=8.5,bold=(i==4))
    if i: arrow(axt,(steps[i-1][0]+8,39.5),(cx-8,39.5),color=INK)
arrow(axt,(51,32),(51,22),color=BLUE,lw=1.6)
box(axt,(22,9),58,9,"from the deadline, EVERY rival can see and copy it",fc="#dfe9f3",ec=BLUE,fs=9)
axt.text(50,3,"forced disclosure",ha="center",fontsize=8,color=BLUE)

# ---- B: self-balancing economy loop ----
axb.set_xlim(0,100); axb.set_ylim(0,58); style(axb,"B.  THE SELF-BALANCING ECONOMY  (no tokens, no auction, no handicap)")
nodes={"INNOVATE\n(original R&D)":(50,50),"DISCLOSE\n(forced, on-chain)":(83,33),
       "RIVALS COPY\n(free, fast)":(66,9),"FIELD COMPRESSES\n(advantage transient)":(34,9),
       "MUST RE-LEAD\n(out-innovate)":(17,33)}
for t,(x,y) in nodes.items(): box(axb,(x-12,y-5),24,10,t,fc=FILL,fs=8)
seq=[(50,50),(83,33),(66,9),(34,9),(17,33),(50,50)]
labels=["head-start","","copying","","floor (M12)\nforces this",""]
for i in range(len(seq)-1):
    p0=np.array(seq[i]); p1=np.array(seq[i+1]); n=(p1-p0)/np.linalg.norm(p1-p0)
    arrow(axb,tuple(p0+n*13),tuple(p1-n*13),color=(GREEN if i in(0,4) else INK),lw=1.8,
          text=labels[i] or None,fs=8)
box(axb,(35,24),30,11,"net: a compressed,\nmeritocratic field —\nbest team wins, narrowly",
    fc="#e3f0e8",ec=GREEN,fs=8)
axb.text(2,1,"Levers: cap (M1, $75M) bounds spend · floor (M12, 80% of cap) forces innovation · "
         "championship pulls all to the best on-chain parts.",fontsize=7.6,color=MUT)

# ---- C: revenue streams ----
axr.set_xlim(0,100); axr.set_ylim(0,52); style(axr,"C.  REVENUE — the shared R&D corpus is a product that funds the sport")
box(axr,(2,21),17,12,"CHAIN R&D\nCORPUS",fc="#dfe9f3",fs=9,bold=True)
axr.text(10.5,17,"all teams' CAD/FEA/CFD,\ntelemetry, materials",ha="center",va="top",fontsize=7,color=MUT)
box(axr,(28,38),28,9,"Media / journalists  ($)",fc=FILL,fs=8.5)
box(axr,(28,22.5),28,10,"Industry deep-data  ($$$)\nBoeing · Lockheed · OEMs",fc="#f3ecd3",ec=GOLD,fs=8,bold=True)
box(axr,(28,7),28,9,"Public / fans  ($)",fc=FILL,fs=8.5)
for y in (42.5,27.5,11.5): arrow(axr,(19,27),(28,y),color=INK,lw=1.2)
axr.text(42,34,"largest stream",ha="center",fontsize=7,color=GOLD)
box(axr,(61,21),14,12,"SERIES\nREVENUE POOL",fc="#e3f0e8",ec=GREEN,fs=8.5,bold=True)
for y in (42.5,27.5,11.5): arrow(axr,(56,y),(61,27),color=INK,lw=1.2)
box(axr,(79,37),16,8,"sport operations",fc=FILL,fs=7.8)
box(axr,(79,22.5),16,9,"PRIZE MONEY\n(4 championships)",fc="#e3f0e8",ec=GREEN,fs=7.8,bold=True)
box(axr,(79,8),16,8,"small-team\nredistribution",fc=FILL,fs=7.8)
for y in (41,27,12): arrow(axr,(75,27),(79,y),color=GREEN,lw=1.3)
axr.text(50,1.5,"Competitors get the data free (disclosure = how they compete); non-competitors pay. "
         "More innovation $\\to$ more valuable corpus $\\to$ bigger prize fund.",fontsize=7.4,color=MUT,ha="center")

fig.suptitle("FORMULA ZYNERJI — BLOCKCHAIN SPINE, SELF-BALANCING ECONOMY & REVENUE",
             fontsize=12,fontweight="bold",color=INK,x=0.02,ha="left")
save(fig,"blockchain_economy"); print("saved drawings/blockchain_economy.{svg,png,pdf}")
