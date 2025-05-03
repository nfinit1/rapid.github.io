import marimo

__generated_with = "0.13.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    ui_slide = mo.ui.slider(1, 10); ui_slide
    return (ui_slide,)


@app.cell
def _(ui_slide):
    ui_slide.value
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
