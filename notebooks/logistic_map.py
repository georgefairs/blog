import marimo

__generated_with = "0.11.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt

    return mo, np, plt


@app.cell
def _(mo):
    mo.md(
        r"""
        # The logistic map

        A one-line model of constrained growth — and a doorway into chaos:

        $$x_{n+1} = r\,x_n\,(1 - x_n)$$

        Drag the growth rate **r** past ~3.57 and watch a stable orbit dissolve
        into chaos. This whole notebook runs in your browser via WebAssembly —
        no server, no Python install.
        """
    )
    return


@app.cell
def _(mo):
    r = mo.ui.slider(2.5, 4.0, value=3.7, step=0.001, label="growth rate r")
    x0 = mo.ui.slider(0.01, 0.99, value=0.5, step=0.01, label="initial x₀")
    n = mo.ui.slider(50, 600, value=200, step=10, label="iterations")
    mo.vstack([r, x0, n])
    return n, r, x0


@app.cell
def _(n, np, plt, r, x0):
    xs = np.empty(n.value)
    xs[0] = x0.value
    for i in range(1, n.value):
        xs[i] = r.value * xs[i - 1] * (1.0 - xs[i - 1])

    fig, ax = plt.subplots(figsize=(8, 3.5))
    ax.plot(xs, lw=0.9, color="#111827")
    ax.set_title(f"Trajectory at r = {r.value:.3f}")
    ax.set_xlabel("step n")
    ax.set_ylabel("xₙ")
    ax.set_ylim(0, 1)
    fig
    return


if __name__ == "__main__":
    app.run()
