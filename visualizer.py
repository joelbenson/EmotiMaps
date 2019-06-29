import plotly
import plotly.graph_objs as go
from data import StateData

class Visualizer():
    def visualizeData(database, emotionList, locationList):

        COLORSCALE = [[0.0, 'rgb(255, 255, 255)'], [1.0, 'rgb(102, 0, 0)']]

        for emotion in emotionList:
            data = dict (
                type = 'choropleth',
                locations = locationList,
                locationmode = 'USA-states',
                colorscale = COLORSCALE,
                z = StateData.getEmotionData(database, emotion),
                marker = go.choropleth.Marker(
                    line = go.choropleth.marker.Line(
                    color = 'rgb(255,255,255)',
                    width = 2))
            )

            layout = go.Layout(
                title = go.layout.Title(
                    text = emotion.capitalize()
                ),
                geo = go.layout.Geo(
                    scope = 'usa',
                    projection = go.layout.geo.Projection(type = 'albers usa'),
                    showlakes = False,
                    lakecolor = 'rgb(255, 255, 255)'),
                )
            plotly.offline.plot(go.Figure(data=[data], layout = layout), filename= (emotion + ".html"))
