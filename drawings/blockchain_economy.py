"""Formula Zynerji — blockchain spine: legality flow + self-balancing economy + revenue streams.
   python drawings/blockchain_economy.py  ->  drawings/blockchain_economy.{svg,png,pdf}"""
import numpy as np, matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from _draw import style, save, box, arrow, INK, ACC, MUT, FILL
BLUE="#1f6fb2"; GREEN="#1e7d4f"; GOLD="#9a7d18"

fig=plt.figure(figsize=(12,13)); gs=GridSpec(3,1,figure=fig,height_ratios=[0.8,1.1,0.95])
axt=fig.add_subplot(gs[0]); axb=fig.add_subplot(gs[1]); axr=fig.add_subplot(gs[2])

# ---- A: legality / disclosure flow ----
axt.set_xlim(0,100); axt.set_ylim(0,52); style(axt,"A.  ON-CHAIN LEGALITY  (only on-chain parts may run — M10)")
steps=[("Team designs\na part",4),("Upload by the\nUpload Deadline\n(CAD/FEA/CFD)",23),
       ("Immutable,\ntimestamped\nledger (hash)",44),("Scrutineering\n= hash check",65),("LEGAL\nto run",86)]
for i,(t,x) in enumerate(steps):
    box(axt,(x,30),14,16,t,fc=(FILL if i<4 else "#e3f0e8"),fs=8,ec=(GREEN if i==4 else INK),bold=(i==4))
    if i: arrow(axt,(steps[i-1][1]+14,38),(x,38),color=INK)
arrow(axt,(51,30),(51,20),color=BLUE,lw=1.6)
box(axt,(20,8),62,10,"... and from the deadline, EVERY rival can see and copy it (forced disclosure)",
    fc="#dfe9f3",ec=BLUE,fs=9)

# ---- B: self-balancing economy loop ----
axb.set_xlim(0,100); axb.set_ylim(0,58); style(axb,"B.  THE SELF-BALANCING ECONOMY  (no tokens, no auction, no handicap)")
nodes={"INNOVATE\n(original R&D)":(50,50),"DISCLOSE\n(forced, on-chain)":(82,33),
       "RIVALS COPY\n(free, fast)":(66,9),"FIELD COMPRESSES\n(advantage transient)":(34,9),
       "MUST RE-LEAD\n(out-innovate)":(18,33)}
for t,(x,y) in nodes.items(): box(axb,(x-11,y-5),22,10,t,fc=FILL,fs=8)
seq=[(50,50),(82,33),(66,9),(34,9),(18,33),(50,50)]
labels=["head-start\n(score points first)","","copying","","floor (M12) FORCES\nre-innovation",""]
for i in range(len(seq)-1):
    p0=np.array(seq[i]); p1=np.array(seq[i+1]); n=(p1-p0)/np.linalg.norm(p1-p0)
    arrow(axb,tuple(p0+n*12),tuple(p1-n*12),color=(GREEN if i in(0,4) else INK),lw=1.8,
          text=labels[i] or None,fs=7.5)
box(axb,(34,24),32,12,"net: a naturally compressed,\nmeritocratic field — the best\nteam wins, but narrowly",
    fc="#e3f0e8",ec=GREEN,fs=8.5)
axb.text(1,1,"Levers: cap (M1, $75M) bounds spend · floor (M12, 80% of cap) forces innovation · "
         "championship pulls all to the best on-chain parts.",fontsize=7.6,color=MUT)

# ---- C: revenue streams ----
axr.set_xlim(0,100); axr.set_ylim(0,50); style(axr,"C.  REVENUE — the shared R&D corpus is a product that funds the sport")
box(axr,(1,18),17,16,"CHAIN R&D CORPUS\nall teams' CAD/FEA/CFD,\ntelemetry, materials,\ncontrol systems",fc="#dfe9f3",fs=7.3)
# tiers
box(axr,(28,37),26,9,"Media / journalists  ($)",fc=FILL,fs=8)
box(axr,(28,22),26,9,"Industry deep-data tier  ($$$)\nBoeing · Lockheed · OEMs",fc="#f3ecd3",ec=GOLD,fs=7.6,bold=True)
box(axr,(28,7),26,9,"Public / fans  ($)",fc=FILL,fs=8)
for y in (41.5,26.5,11.5): arrow(axr,(18,26),(28,y),color=INK,lw=1.2)
axr.text(41,33,"largest stream",ha="center",fontsize=7,color=GOLD)
# pool
box(axr,(60,20),14,12,"SERIES\nREVENUE POOL",fc="#e3f0e8",ec=GREEN,fs=8,bold=True)
for y in (41.5,26.5,11.5): arrow(axr,(54,y),(60,26),color=INK,lw=1.2)
# destinations
box(axr,(80,36),19,8,"sport operations\n(racing, chain, safety)",fc=FILL,fs=7.3)
box(axr,(80,22),19,8,"PRIZE MONEY\n(4 championships)",fc="#e3f0e8",ec=GREEN,fs=7.6,bold=True)
box(axr,(80,8),19,8,"small-team\nredistribution",fc=FILL,fs=7.3)
for y in (40,26,12): arrow(axr,(74,26),(80,y),color=GREEN,lw=1.3)
axr.text(50,2,"Competitors get the data free (disclosure = how they compete); non-competitors pay. "
         "Innovation -> more valuable corpus -> bigger prize fund.",fontsize=7.4,color=MUT,ha="center")

fig.suptitle("FORMULA ZYNERJI — BLOCKCHAIN SPINE, SELF-BALANCING ECONOMY & REVENUE",
             fontsize=12,fontweight="bold",color=INK,x=0.02,ha="left")
save(fig,"blockchain_economy"); print("saved drawings/blockchain_economy.{svg,png,pdf}")
