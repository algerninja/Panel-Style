import panel as pn

pn.extension("bootstrap")

card = pn.widgets.Button(name="Click me", css_classes=["btn", "btn-primary"])
select = pn.Card(style={"width": "3000px"})
content2 = pn.Column(card, select, sizing_mode="stretch_width")


app = pn.template.BootstrapTemplate(title="Mi sitio web", main=content2)

app.servable()
