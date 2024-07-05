import plotly.express as px

# Available named colorscales
colorscales = px.colors.named_colorscales()
print("---COLOR SCALES---")
print(colorscales)

# List of available projections
projections = [
    'equirectangular', 'mercator', 'orthographic', 'natural earth', 
    'kavrayskiy7', 'miller', 'robinson', 'eckert4', 
    'azimuthal equal area', 'azimuthal equidistant', 'conic equal area', 
    'conic conformal', 'conic equidistant', 'gnomonic', 
    'stereographic', 'mollweide', 'hammer', 'transverse mercator', 
    'albers usa', 'winkel tripel', 'aitoff', 'sinusoidal'
]
print("\n---PROJECTIONS---")
print(projections)