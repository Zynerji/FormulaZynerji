"""Shared drawing helpers for Formula Zynerji whitepaper figures (matplotlib, vector out)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import os

OUT = os.path.dirname(os.path.abspath(__file__))
INK = "#1b2430"; ACC = "#b3122b"; MUT = "#7a8694"; FILL = "#e9edf2"

def style(ax, title=None):
    ax.set_aspect("equal"); ax.axis("off")
    if title:
        ax.set_title(title, fontsize=11, fontweight="bold", color=INK, loc="left")

def dim(ax, p0, p1, text, off=0.0, vertical=False, fs=8):
    """Dimension line with arrowheads + label. p0,p1 in data coords; off shifts perpendicular."""
    (x0, y0), (x1, y1) = p0, p1
    if vertical:
        x = x0 + off
        ax.plot([x0, x], [y0, y0], color=MUT, lw=.6); ax.plot([x1, x], [y1, y1], color=MUT, lw=.6)
        ax.annotate("", (x, y0), (x, y1), arrowprops=dict(arrowstyle="<->", color=INK, lw=.9))
        ax.text(x, (y0+y1)/2, text, rotation=90, ha="right", va="center", fontsize=fs, color=INK,
                backgroundcolor="white")
    else:
        y = y0 + off
        ax.plot([x0, x0], [y0, y], color=MUT, lw=.6); ax.plot([x1, x1], [y1, y], color=MUT, lw=.6)
        ax.annotate("", (x0, y), (x1, y), arrowprops=dict(arrowstyle="<->", color=INK, lw=.9))
        ax.text((x0+x1)/2, y, text, ha="center", va="bottom", fontsize=fs, color=INK,
                backgroundcolor="white")

def label(ax, xy, text, xytext, fs=8, color=INK):
    ax.annotate(text, xy=xy, xytext=xytext, fontsize=fs, color=color,
                arrowprops=dict(arrowstyle="-", color=MUT, lw=.7), ha="left", va="center")

def box(ax, xy, w, h, text, fc=FILL, ec=INK, fs=9, tc=INK, lw=1.3, bold=False):
    from matplotlib.patches import FancyBboxPatch
    x, y = xy
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=1.2",
                                fc=fc, ec=ec, lw=lw, zorder=2))
    ax.text(x+w/2, y+h/2, text, ha="center", va="center", fontsize=fs, color=tc, zorder=3,
            fontweight="bold" if bold else "normal")
    return (x+w/2, y+h/2)

def arrow(ax, p0, p1, color=INK, lw=1.7, text=None, fs=8, st="-|>"):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle=st, mutation_scale=14, color=color, lw=lw, zorder=4))
    if text:
        ax.text((p0[0]+p1[0])/2, (p0[1]+p1[1])/2, text, ha="center", va="center",
                fontsize=fs, color=color, backgroundcolor="white", zorder=5)

def save(fig, name):
    fig.savefig(os.path.join(OUT, name+".pdf"), bbox_inches="tight")   # vector, for LaTeX \includegraphics
    fig.savefig(os.path.join(OUT, name+".svg"), bbox_inches="tight")
    fig.savefig(os.path.join(OUT, name+".png"), dpi=150, bbox_inches="tight")  # for quick view
    plt.close(fig)
    return name
