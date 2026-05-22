"""Formula Zynerji — the blockchain SPINE made concrete: race-weekend protocol, the on-chain
PartRecord schema, and the two-clause (design-hash + physical-conformance) scrutineering check.
Complements blockchain_economy.py (which shows the legality/economy/revenue logic); this shows
the technical mechanics specified in design/blockchain-spec.md.
   python drawings/blockchain_protocol.py  ->  drawings/blockchain_protocol.{svg,png,pdf}"""
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.patches import FancyBboxPatch
from _draw import style, save, box, arrow, INK, ACC, MUT, FILL
BLUE="#1f6fb2"; GREEN="#1e7d4f"; GOLD="#9a7d18"

fig=plt.figure(figsize=(12,9.2)); gs=GridSpec(2,2,figure=fig,height_ratios=[0.72,1.25],hspace=0.18,wspace=0.12)
axt=fig.add_subplot(gs[0,:]); axl=fig.add_subplot(gs[1,0]); axr=fig.add_subplot(gs[1,1])

# ---------------- A: race-weekend timeline ----------------
axt.set_xlim(0,100); axt.set_ylim(0,30)
style(axt,"A.  RACE-WEEKEND PROTOCOL  (only on-chain parts may run — M10)")
mil=[(8,"Development\n(uploads open)",FILL,INK,False),
     (30,"UPLOAD\nDEADLINE",FILL,ACC,True),
     (52,"Scrutineering\n(§4 check)",FILL,INK,False),
     (73,"Sessions\n(on-chain parts run)",FILL,INK,False),
     (92,"Post-event\n(results · Index)",FILL,INK,False)]
for i,(cx,t,fc,ec,bold) in enumerate(mil):
    box(axt,(cx-7.5,13),15,9,t,fc=("#fdeaec" if bold else fc),ec=ec,fs=8,bold=bold)
    if i: arrow(axt,(mil[i-1][0]+7.5,17.5),(cx-7.5,17.5),color=INK)
axt.annotate("", (30,13),(30,5.5),arrowprops=dict(arrowstyle="-|>",color=ACC,lw=1.4))
axt.text(30,3.3,"disclosure moment — every rival can now read all event parts",
         ha="center",fontsize=7.6,color=ACC)
# head-start bracket: deadline -> next event
axt.annotate("",(31,26.5),(92,26.5),arrowprops=dict(arrowstyle="<->",color=GREEN,lw=1.0))
axt.text(61,28,"head-start = manufacturing lag (rivals can see, must still build)  — M11",
         ha="center",fontsize=7.4,color=GREEN)

# ---------------- B: PartRecord schema card ----------------
axl.set_xlim(0,100); axl.set_ylim(0,100)
style(axl,"B.  ON-CHAIN  PartRecord  (the Designs ledger object)")
axl.add_patch(FancyBboxPatch((5,7),90,84,boxstyle="round,pad=0,rounding_size=2",
              fc="white",ec=INK,lw=1.4,zorder=2))
axl.add_patch(plt.Rectangle((5,82),90,9,fc="#eef2f6",ec=INK,lw=1.0,zorder=3))
axl.text(50,86.5,"PartRecord",ha="center",va="center",fontsize=10,fontweight="bold",color=INK,zorder=4)
rows=[("part_id · team · class","identity + which zone rules apply",False),
      ("timestamp","disclosure clock / provenance",False),
      ("nominal_geometry","SHA-256( canonical solid )",True),
      ("tolerance_spec","per-feature conformance band",False),
      ("material_spec (+hash)","certified properties",False),
      ("analyses","FEA · CFD · wake-test (M4)",False),
      ("cost_entry","→ cap accounting (M1/M9)",False),
      ("provenance","original | derived_from[…] (M11)",True),
      ("signature","team key over the record",False)]
y=78
for name,desc,hl in rows:
    y-=7.7
    if hl: axl.add_patch(plt.Rectangle((8,y-2.3),84,6.6,fc="#e3f0e8",ec="none",zorder=3))
    axl.text(10,y,name,ha="left",va="center",fontsize=8.3,color=INK,
             fontweight="bold" if hl else "normal",family="monospace",zorder=4)
    axl.text(92,y,desc,ha="right",va="center",fontsize=7.6,color=MUT,zorder=4)

# ---------------- C: two-clause scrutineering ----------------
axr.set_xlim(0,100); axr.set_ylim(0,100)
style(axr,"C.  SCRUTINEERING = design-hash ✚ physical-conformance")
box(axr,(28,88),44,9,"fitted part → cite part_id",fc=FILL,fs=8.5)
arrow(axr,(50,88),(50,80),color=INK)
box(axr,(14,64),72,15,"(i)  recompute canonical hash == on-chain ?\n      and  timestamp < Upload Deadline",
    fc="#dfe9f3",ec=BLUE,fs=8)
axr.text(50,60.5,"cryptographic — secret / back-dated parts impossible",ha="center",fontsize=7.2,color=BLUE)
arrow(axr,(50,64),(50,52),color=INK)
box(axr,(14,37),72,13,"(ii)  CMM scan within tolerance_spec ?",fc="#f3ecd3",ec=GOLD,fs=8.5)
axr.text(50,33.5,"metrology — part on car IS the disclosed design",ha="center",fontsize=7.2,color=GOLD)
arrow(axr,(50,37),(50,25),color=GREEN,lw=2.0)
box(axr,(34,13),32,10,"LEGAL",fc="#e3f0e8",ec=GREEN,fs=11,bold=True,tc=GREEN)
# fail branches
box(axr,(84,55),14,12,"ILLEGAL\nno / altered\nrecord",fc="#fdeaec",ec=ACC,fs=7,tc=ACC)
arrow(axr,(86,71.5),(95,67),color=ACC,lw=1.2)
box(axr,(84,30),14,12,"ILLEGAL\nnon-\nconforming",fc="#fdeaec",ec=ACC,fs=7,tc=ACC)
arrow(axr,(86,43.5),(95,42),color=ACC,lw=1.2)

fig.suptitle("FORMULA ZYNERJI — BLOCKCHAIN PROTOCOL: weekend gate · part record · scrutineering-by-hash",
             fontsize=12,fontweight="bold",color=INK,x=0.02,ha="left")
save(fig,"blockchain_protocol"); print("saved drawings/blockchain_protocol.{svg,png,pdf}")
