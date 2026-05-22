"""Formula Zynerji — Car General Arrangement (side / plan / front), dimensioned. Units: mm.
   python drawings/car_ga.py  ->  drawings/car_ga.{svg,png}"""
import numpy as np, matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle, Circle, Arc, FancyBboxPatch
from matplotlib.gridspec import GridSpec
from _draw import style, dim, label, save, INK, ACC, MUT, FILL

# --- dimension set (model/regs) ---
WB, FOH, ROH = 3300, 900, 650
L, H, Wd = WB+FOH+ROH, 950, 1800          # length 4850
FAX, RAX = FOH, FOH+WB                      # axle x-positions: 900, 4200
R, WF, WR = 350, 280, 375                   # wheel radius (≈700 dia), tyre widths F/R
TF, TR = 1520, 1425                         # tracks F/R

def wheel_side(ax, cx):
    ax.add_patch(Circle((cx,R), R, fc="#2b2f36", ec=INK, lw=1.2, zorder=3))
    ax.add_patch(Circle((cx,R), R*0.45, fc="#cfd6de", ec=INK, lw=1, zorder=4))  # 18" rim

def car_side(ax):
    # body silhouette (x,z) — stylised open-wheeler
    body = [(0,150),(300,150),(820,250),(1500,330),(1950,470),(2350,560),
            (2750,470),(3700,420),(4350,400),(4700,360),(L,330),(L,70),(300,70),(0,150)]
    ax.add_patch(Polygon(body, closed=True, fc=FILL, ec=INK, lw=1.4, zorder=2))
    # halo / roll hoop over cockpit
    ax.add_patch(Arc((2150,560),760,820,theta1=10,theta2=170,color=INK,lw=2.4,zorder=5))
    ax.plot([2520,2620],[560,920],color=INK,lw=2.4,zorder=5)            # rollhoop strut
    ax.add_patch(Polygon([(2560,560),(2680,560),(2640,930),(2580,930)],closed=True,fc="#2b2f36",ec=INK,zorder=5))
    wheel_side(ax,FAX); wheel_side(ax,RAX)
    ax.add_patch(Rectangle((-40,90),360,70,fc=ACC,ec=INK,lw=1,zorder=6))  # front wing
    ax.add_patch(Rectangle((4500,780),420,40,fc=ACC,ec=INK,lw=1,zorder=6))# rear wing plane
    ax.plot([4720,4720],[400,780],color=INK,lw=1.4,zorder=6)              # rear wing post
    ax.plot([320,4500],[60,60],color=MUT,lw=1.0,ls=(0,(6,3)),zorder=2)    # floor / reference plane
    # dims
    dim(ax,(FAX,0),(RAX,0),"wheelbase 3300", off=-360, fs=8)
    dim(ax,(0,0),(L,0),"overall length 4850", off=-720, fs=8)
    dim(ax,(L,0),(L,H),"max height 950", off=560, vertical=True, fs=8)
    dim(ax,(0,150),(FOH,150),"front OH 900", off=1180, fs=7)
    label(ax,(150,125),"front wing (2026)",(-700,-980))
    label(ax,(4710,820),"rear wing (2026)",(3300,1300))
    label(ax,(2150,930),"halo (2026 safety)",(700,1320))
    label(ax,(2000,60),"ground-effect floor (2026) + plank",(1500,-1180))
    label(ax,(RAX,R),"18\" wheels / 2026 tyres",(4250,-700))
    style(ax,"SIDE")

def car_plan(ax):
    # body plan outline (x, y) symmetric about 0
    half=[(0,40),(350,120),(900,330),(1700,430),(2300,470),(3200,430),(4200,360),(L,150)]
    top=[(x,y) for x,y in half]; bot=[(x,-y) for x,y in half][::-1]
    ax.add_patch(Polygon(top+bot, closed=True, fc=FILL, ec=INK, lw=1.4, zorder=2))
    for ax_x,tr,w in [(FAX,TF,WF),(RAX,TR,WR)]:
        for s in (1,-1):
            cy=s*tr/2
            ax.add_patch(Rectangle((ax_x-R,cy-w/2),2*R,w,fc="#2b2f36",ec=INK,lw=1,zorder=3))
    ax.add_patch(Rectangle((-40,-Wd/2),360,Wd,fc=ACC,ec=INK,lw=1,alpha=.85,zorder=4))   # front wing full width
    ax.add_patch(Rectangle((4500,-500),300,1000,fc=ACC,ec=INK,lw=1,alpha=.85,zorder=4)) # rear wing
    # width + tracks (vertical dims)
    dim(ax,(-250,-Wd/2),(-250,Wd/2),"max width 1800", off=0, vertical=True, fs=8)
    dim(ax,(FAX,-TF/2),(FAX,TF/2),"front track 1520", off=-900, vertical=True, fs=7)
    dim(ax,(RAX,-TR/2),(RAX,TR/2),"rear track 1425", off=900, vertical=True, fs=7)
    style(ax,"PLAN")

def car_front(ax):
    for s in (1,-1):
        cy=s*TF/2
        ax.add_patch(Rectangle((cy-WF/2,0),WF,2*R,fc="#2b2f36",ec=INK,lw=1.2,zorder=3))
        ax.add_patch(Rectangle((cy-WF/2,R-90),WF,180,fc="#cfd6de",ec=INK,lw=1,zorder=4))
    # body cross-section
    ax.add_patch(FancyBboxPatch((-330,120),660,420,boxstyle="round,pad=0,rounding_size=120",
                                fc=FILL,ec=INK,lw=1.4,zorder=2))
    ax.add_patch(Arc((0,540),520,520,theta1=0,theta2=180,color=INK,lw=2.4,zorder=5))   # halo arc
    ax.add_patch(Rectangle((-Wd/2,70),Wd,60,fc=ACC,ec=INK,lw=1,zorder=6))               # front wing span
    dim(ax,(-Wd/2,0),(Wd/2,0),"max width 1800", off=-260)
    dim(ax,(Wd/2,0),(Wd/2,H),"950", off=260, vertical=True, fs=7)
    style(ax,"FRONT")

fig=plt.figure(figsize=(11,8.5)); gs=GridSpec(2,2,figure=fig,height_ratios=[1.05,1],width_ratios=[1.7,1])
axs=fig.add_subplot(gs[0,0]); axp=fig.add_subplot(gs[1,0]); axf=fig.add_subplot(gs[:,1])
car_side(axs); car_plan(axp); car_front(axf)
for a in (axs,axp): a.set_xlim(-900,5050)
axs.set_ylim(-1900,1500); axp.set_ylim(-1200,1200); axf.set_xlim(-1250,1250); axf.set_ylim(-450,1150)
fig.suptitle("FORMULA ZYNERJI — CAR GENERAL ARRANGEMENT  (era-kitbash: 2026 aero/tyres/safety · 2008 dims · 3300 mm WB)",
             fontsize=12, fontweight="bold", color=INK, x=0.02, ha="left")
fig.text(0.02,0.005,"All dimensions in mm. First-pass GA from the dimensional set (design/chassis-integration.md).",
         fontsize=8, color=MUT)
save(fig,"car_ga"); print("saved drawings/car_ga.{svg,png}")
