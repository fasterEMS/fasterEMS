# Generate image for the Parallel-Plate Capacitor and Waveguide Example
#
# Don't delete, otherwise one won't be able to modify the images in
# case the tutorial changes.

import sys
import plotly.graph_objects as go

def plot_axes(fig, x_range, y_range):
    """Plot the X and Y axis and grid of the Cartesian coordinate system"""
    fig.update_xaxes(
        range=x_range,
        tickmode='linear', showticklabels=False,
        side='top',
        gridcolor='rgb(224,224,224)'
    )
    fig.update_yaxes(
        range=y_range,
        tickmode='linear', showticklabels=False,
        side='right',
        gridcolor='rgb(224,224,224)'
    )

    fig.add_vline(x=0, line_width=3)
    fig.add_hline(y=0, line_width=3)


def plot_annotated_point(fig, xy_coords, logical_coords):
    fig.add_traces(
        go.Scatter(
            x=(xy_coords[0],), y=(xy_coords[1],),
            mode='markers+text', text="(%.1f, %.1f)" % logical_coords,
            textposition='top center', showlegend=False
        ),
    )


fig = go.Figure()

plot_axes(fig, x_range=(-8, 8), y_range=(-4, 4))

fig.add_shape(type='line', x0=-5, x1=5, y0=0.8, y1=0.8)
plot_annotated_point(fig, (-5, 0.8), (-50, 8))
plot_annotated_point(fig, (5, 0.8), (50, 8))

fig.add_shape(type='line', x0=-5, x1=5, y0=-0.8, y1=-0.8)
plot_annotated_point(fig, (-5, -0.8), (-50, -8))
plot_annotated_point(fig, (5, -0.8), (50, -8))

fig.update_layout(
    plot_bgcolor='rgb(255,255,255)',
    height=400, width=400,
    margin=dict(l=0, r=0, t=0, b=0),
    font=dict(size=22)
)
#fig.show()

fig.write_image("%s.svg" % sys.argv[0])
