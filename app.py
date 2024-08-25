import solara
import plotly.express as px
import numpy as np

@solara.component
def Page():
    # Reactive states for slider values
    mean, set_mean = solara.use_state(0.0)
    std, set_std = solara.use_state(1.0)

    with solara.Column():
        with solara.Sidebar():
            solara.Markdown("# This is the Sidebar")
            solara.Markdown("#### Slider Controls")
            # Slider that controls the mean of the data
            solara.Sliderfloat(label="Mean", value = mean, min=10.0, max = 10.0, step = 0.1, on_value = set_mean)
            # Slider that controls the std of the data
            solara.Sliderfloat(label="Standard Deviation", value = std, min=0.1, max=10.0, step=0.1, on_value=set_std)

            # Main Content Below

            # Create and display a histogram based on the mean and std
            data = np.random.normal(loc=mean, scale = std, size = 1000)
            fig_hist = px.histogram(data, nbins=30, title="Histogram")
            fig_hist.update_layout(xaxis_title="Value", yaxis_title="Frequency", width=600) #Set the width here

            solara.Markdown(" # This is the main content area")
            solara.FigurePlotly(fig_hist)