import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import panel as pn

import panel as pn
import numpy as np
import holoviews as hv


csv_file = "EDO_PORTUGUESA_COMPLETE.csv"
data = pd.read_csv(csv_file)

ACCENT_COLOR = "#665566"

pn.extension()


bootstrap = pn.template.BootstrapTemplate(title="Bootstrap Template", accent_base_color=ACCENT_COLOR, header_background=ACCENT_COLOR)

# bootstrap = pn.template.BootstrapTemplate(title="Bootstrap Template")

xs = np.linspace(0, np.pi)
freq = pn.widgets.FloatSlider(name="Frequency", start=0, end=10, value=2)
phase = pn.widgets.FloatSlider(name="Phase", start=0, end=np.pi)


@pn.depends(freq=freq, phase=phase)
def sine(freq, phase):
    return hv.Curve((xs, np.sin(xs * freq + phase))).opts(responsive=True, min_height=400)


@pn.depends(freq=freq, phase=phase)
def cosine(freq, phase):
    return hv.Curve((xs, np.cos(xs * freq + phase))).opts(responsive=True, min_height=400)


bootstrap.sidebar.append(freq)
bootstrap.sidebar.append(phase)

bootstrap.main.append(pn.Row(pn.Card(hv.DynamicMap(sine), title="Sine"), pn.Card(hv.DynamicMap(cosine), title="Cosine")))


bootstrap.servable()
