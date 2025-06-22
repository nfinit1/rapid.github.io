import marimo

__generated_with = "0.13.4"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
async def _():
    from datetime import time, datetime
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


@app.cell
def _():
    style = {
        "color": "blue"
    }
    return (style,)


@app.cell
def _(mo, style):
    date_picker_start = mo.ui.date(
        label="Choose Start Date"
    )
    styled_date_picker_start = date_picker_start.style(style)
    date_picker_end = mo.ui.date(
        label="Choose End Date"
    )
    styled_date_picker_end = date_picker_end.style(style)

    time_picker_start = mo.ui.dropdown(
        label="Choose Start Time",
        options = [
            "0001Z", "0201Z", "0301Z", "0401Z", "0501Z", "0601Z", 
            "0701Z", "0801Z", "0901Z", "1001Z", "1101Z", "1201Z", 
            "1301Z", "1401Z", "1501Z", "1601Z", "1701Z", "1801Z", 
            "1901Z", "2001Z", "2101Z", "2201Z", "2301Z", "2401Z"
        ], 
        value="1601Z",
    )
    styled_time_picker_start = time_picker_start.style(style)
    time_picker_end = mo.ui.dropdown(
        label="Choose End Time", 
        options = [
            "0000Z", "0200Z", "0300Z", "0400Z", "0500Z", "0600Z", 
            "0700Z", "0800Z", "0900Z", "1000Z", "1100Z", "1200Z", 
            "1300Z", "1400Z", "1500Z", "1600Z", "1700Z", "1800Z", 
            "1900Z", "2000Z", "2100Z", "2200Z", "2300Z", "2400Z"
        ], 
        value="1600Z"
    )
    styled_time_picker_end = time_picker_end.style(style)
    return (
        styled_date_picker_end,
        styled_date_picker_start,
        styled_time_picker_end,
        styled_time_picker_start,
    )


@app.cell
def _(
    mo,
    styled_date_picker_end,
    styled_date_picker_start,
    styled_time_picker_end,
    styled_time_picker_start,
):
    mo.hstack([
        mo.vstack([styled_date_picker_start, styled_time_picker_start]),
        mo.vstack([styled_date_picker_end, styled_time_picker_end])
    ])
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
