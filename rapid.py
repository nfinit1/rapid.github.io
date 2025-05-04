import marimo

__generated_with = "0.13.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
async def _():
    try:
        import types
        import sys
        from pyodide.http import pyfetch

        resp = await pyfetch("public/utils.py")
        code = await resp.string()
        utils = types.ModuleType("utils")
        exec(code, utils.__dict__)
        sys.modules["utils"] = utils
        from utils import multiply
    except ImportError:
        from utils import multiply
    return (multiply,)


@app.cell
def _():
    import pandas as pd
    return (pd,)


@app.cell
def _(mo):
    ui_slide = mo.ui.slider(1, 10); ui_slide
    return (ui_slide,)


@app.cell
def _(multiply, ui_slide):
    multiply(ui_slide.value)
    return


@app.cell
def _(multiply, pd):
    df = pd.DataFrame({"name": ["Rick", "Sarah", "Scarlett", "Aubrey"],
                       "age":  ["40", "38", "8", "6"],
                       "birthday": ["January 20, 1985", "February 5, 1987", "May 21 2018", "June 30 2016"]})
    df.age = df.age.apply(multiply)
    return (df,)


@app.cell
def _(df, mo):
    ui_table = mo.ui.table(df); ui_table
    return (ui_table,)


@app.cell
def _(ui_table):
    ui_table.value
    return


if __name__ == "__main__":
    app.run()
