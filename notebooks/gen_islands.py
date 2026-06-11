"""Generate marimo *islands* HTML for the logistic-map post.

Run with:  uv run --with marimo --with numpy --with matplotlib python notebooks/gen_islands.py

Produces:
  - src/assets/marimo/logistic.body.html   (the interleaved <marimo-island> markup)
  - prints render_head() so we can confirm the exact CDN <head> tags + version.

The prose is authored as markdown cells *between* the interactive cells, so the
rendered result flows as one document rather than a single boxed app.
"""

import asyncio
from pathlib import Path

from marimo import MarimoIslandGenerator

OUT = Path(__file__).resolve().parent.parent / "src" / "assets" / "marimo"


async def main() -> None:
    g = MarimoIslandGenerator()

    # 0. Imports + matplotlib styling that blends into either light/dark theme:
    #    transparent figure background, neutral-gray ink legible on both.
    c_imports = g.add_code(
        "import marimo as mo\n"
        "import numpy as np\n"
        "import matplotlib as mpl\n"
        "import matplotlib.pyplot as plt\n"
        "mpl.rcParams['figure.facecolor'] = 'none'\n"
        "mpl.rcParams['axes.facecolor'] = 'none'\n"
        "mpl.rcParams['savefig.facecolor'] = 'none'\n"
        "mpl.rcParams['text.color'] = '#888888'\n"
        "mpl.rcParams['axes.labelcolor'] = '#888888'\n"
        "mpl.rcParams['axes.edgecolor'] = '#888888'\n"
        "mpl.rcParams['xtick.color'] = '#888888'\n"
        "mpl.rcParams['ytick.color'] = '#888888'",
        display_output=False,
    )

    # 1. Prose.
    c_intro = g.add_code(
        "mo.md(r'''\n"
        "Here is the same logistic map, but woven into the page as **marimo islands** — "
        "individual reactive cells sharing one runtime. Drag the slider and the plot "
        "below it updates live, all inline with this text.\n"
        "''')"
    )

    # 2. The slider (defines `r`, displayed inline).
    c_slider = g.add_code(
        'r = mo.ui.slider(2.5, 4.0, value=3.7, step=0.001, label="growth rate r")\n'
        "r"
    )

    # 3. Prose between widgets.
    c_mid = g.add_code(
        "mo.md(r'''\n"
        "Below ~3.0 the orbit settles to a single value; past ~3.57 it tips into chaos. "
        "The plot is its own island, but it reacts to the slider above:\n"
        "''')"
    )

    # 4. The reactive plot (depends on `r`). Underscore locals stay cell-private.
    c_plot = g.add_code(
        "_xs = np.empty(300)\n"
        "_xs[0] = 0.5\n"
        "for _i in range(1, 300):\n"
        "    _xs[_i] = r.value * _xs[_i - 1] * (1.0 - _xs[_i - 1])\n"
        "_fig, _ax = plt.subplots(figsize=(8, 3.5))\n"
        '_ax.plot(_xs, lw=1.0, color="#b3b3b3")\n'
        '_ax.spines["top"].set_visible(False)\n'
        '_ax.spines["right"].set_visible(False)\n'
        "_ax.set_ylim(0, 1)\n"
        '_ax.set_xlabel("step n")\n'
        '_ax.set_ylabel("x_n")\n'
        '_ax.set_title(f"r = {r.value:.3f}")\n'
        "_fig"
    )

    await g.build()

    OUT.mkdir(parents=True, exist_ok=True)
    body = "\n".join(
        [
            c_imports.render(display_output=False),
            c_intro.render(),
            c_slider.render(),
            c_mid.render(),
            c_plot.render(),
        ]
    )
    (OUT / "logistic.body.html").write_text(body, encoding="utf-8")

    print("=== render_head() ===")
    print(g.render_head())
    print("=== wrote", OUT / "logistic.body.html", "===")


if __name__ == "__main__":
    asyncio.run(main())
