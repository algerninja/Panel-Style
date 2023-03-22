import panel as pn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pn.extension()


csv_file = "https://raw.githubusercontent.com/holoviz/panel/main/examples/assets/occupancy.csv"
data = pd.read_csv(csv_file, parse_dates=["date"], index_col="date")


df_pane = pn.pane.DataFrame(data, width=1500)

layout = pn.Column(df_pane)

layout.servable()
