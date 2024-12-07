import dash
from dash import dcc, html, Input, Output
import plotly.graph_objs as go
import pandas as pd
import geopandas as gpd
import numpy as np
import json

app = dash.Dash(__name__)

# #ffdb4d yellow
# #d1b33d darker yellow
# #ffb836 orange
# #404040 gray
# #e4e1dc light gray
# #ffffff white

# Paleta de Colores para Cambios Rapidos
color_palette = {
    "main_background":"#ffffff",
    "main_text":"#404040",
    "banner_background":"#ffdb4d",
    "banner_text":"#404040",
    "global_selector_background":"#e4e1dc",
    "global_selector_text":"#ffb836",
    "global_selector_label_text":"#404040",
    "legend_text":"#404040",
    "indicator_text":"#ffb836",
    "indicator_text2":"#404040",
}

df_1_baches_clim = pd.read_csv(r"1_baches_clim.csv")
df_1_baches_clim["date"] = pd.to_datetime(df_1_baches_clim["date"])
#dates = df_1_baches_clim.resample("D", on="date").count()

histogram_data = pd.DataFrame({
    'Date': df_1_baches_clim["date"],
    'Description': df_1_baches_clim["description"],
    'Sentiment': df_1_baches_clim["sentimiento"]
})

time_series_data = pd.DataFrame({
    'Date': df_1_baches_clim["date"],
    'Id': df_1_baches_clim["id"],
    'Temp': df_1_baches_clim["temp_c"],
    'Rain': df_1_baches_clim["rain_mm"]
})

scatter_data = pd.DataFrame({
    'Latitude': df_1_baches_clim["latitude"],
    'Longitude': df_1_baches_clim["longitude"],
    'Date': df_1_baches_clim["date"],
    'Atendido': df_1_baches_clim["atendido"]
})

df_2_1_geo_urb_ageb = gpd.read_file(r"2_geo_se.shp")
#print(df_2_1_geo_urb_ageb.info())

df_2_1_geo_urb_ageb = df_2_1_geo_urb_ageb.to_crs(epsg=4326)
geojson = json.loads(df_2_1_geo_urb_ageb.to_json())

choropleth_data = pd.DataFrame({
    'Marginacion': df_2_1_geo_urb_ageb["GM_2020_NU"],
    'PoblacionTotal': df_2_1_geo_urb_ageb["POB_TOT"]
})

# Layout General del Aplicativo (Dashboard)
app.layout = html.Div(
    style={'fontFamily': 'helvetica, sans-serif', 'color': color_palette["main_text"],
           'backgroundColor': color_palette["main_background"], 'margin': '0', 'padding': '0',
           'height': '100vh'},
    children=[
        # Banner de Titulo
        html.Div(
            style={
                'backgroundColor': color_palette["banner_background"],
                'padding': '15px',
                'color': color_palette["banner_text"],
                'fontFamily': 'georgia, serif',
                'fontSize': '24px',
                'fontWeight': 'bold',
                #'borderBottom': '2px solid #ffb836',
            },
            children=[
                html.Div(
                    children=[html.Label("Baches en Hermosillo - Efectividad del Mecanismo de Reporte",
                                         style={'fontSize': '24px'})],
                    style={'textAlign': 'left'}
                ),
                # html.Div(
                #     children=[html.Img(src='assets/mcd_dark.png', height=80)],
                #     style={'textAlign': 'right'}
                # ),
            ]
        ),

        # Layout principal (separado en dos columnas al 60 y 40)
        html.Div(
            style={'display': 'flex', 'flexDirection': 'row', 'width': '100%',
                   #'border':'5px solid #404040',
                   'margin': '0', 'padding': '0'},
            children=[
                # Columna Izquierda: Mapa y Selectores Globales
                html.Div(
                    style={'width': '60%', 'padding': '20px'},
                    children=[
                        # Seccion para acomodo de Selectores Globales
                        html.Div(
                            style={'display': 'flex', 'justifyContent': 'space-between',
                                   'marginBottom': '10px', 'width':'100%'},
                            children=[
                                # Selector para Coloracion de Tiles de Choropleth
                                html.Div(
                                    children=[
                                        html.Label("Indicadores Socioeconomicos",
                                                   style={'fontSize': '14px', 'flex':'1',
                                                          'color':color_palette["global_selector_label_text"]}),
                                        dcc.Dropdown(
                                            id='choropleth-dropdown',
                                            options=[
                                                # {'label': 'MB', 'value': "Muy Bajo"},
                                                # {'label': 'B', 'value': "Bajo"},
                                                # {'label': 'M', 'value': "Medio"},
                                                # {'label': 'A', 'value': "Alto"},
                                                # {'label': 'MA', 'value': "Muy Alto"}
                                                {'label': 'Grado de Marginacion', 'value': "Marginacion"},
                                                {'label': 'Poblacion Total', 'value': "PoblacionTotal"}
                                            ],
                                            #value=["Muy Bajo", "Bajo", "Medio", "Alto", "Muy Alto"],
                                            value="PoblacionTotal",
                                            multi=False,
                                            style={'backgroundColor': color_palette["global_selector_background"],
                                                   'color': color_palette["global_selector_text"], 'flex':'1'}
                                        )
                                    ]
                                ),
                                # Selector para Periodo de Tiempo
                                html.Div(
                                    children=[
                                        html.Label("Periodo (Año)",
                                                   style={'fontSize': '14px',
                                                          'color':color_palette["global_selector_label_text"]}),
                                        dcc.Dropdown(
                                            id='scatter-period-dropdown',
                                            options=[
                                                {'label': '2021', 'value': 2021},
                                                {'label': '2022', 'value': 2022},
                                                {'label': '2023', 'value': 2023},
                                                {'label': '2024', 'value': 2024}
                                            ],
                                            value=[2021, 2022, 2023, 2024],
                                            multi=True,
                                            style={'backgroundColor': color_palette["global_selector_background"],
                                                   'color': color_palette["global_selector_text"]}
                                        )
                                    ]
                                ),
                                # Selector para Colonia o AGEB
                                # html.Div(
                                #     children=[
                                #         html.Label("Colonia(s)",
                                #                    style={'fontSize': '14px',
                                #                           'color':color_palette["global_selector_label_text"]}),
                                #         dcc.Dropdown(
                                #             id='scatter-value-dropdown',
                                #             options=[
                                #                 {'label': 'balderrama', 'value': 'balderrama'},
                                #                 {'label': 'centenario', 'value': 'centenario'},
                                #                 {'label': 'san benito', 'value': 'san benito'},
                                #                 {'label': 'nuevo hermosillo', 'value': 'nuevo hermosillo'}
                                #             ],
                                #             value='centenario',
                                #             multi=False,
                                #             style={'backgroundColor': color_palette["global_selector_background"],
                                #                    'color': color_palette["global_selector_text"],
                                #                    'font-color': color_palette["global_selector_text"]}
                                #         )
                                #     ]
                                # ),
                            ]
                        ),
                        # Espacio para graficar el Choropleth + Scatter
                        dcc.Graph(
                            id='choropleth-map',
                            config={'displayModeBar': False},
                            style={'height': '625px'}
                        )
                    ]
                ),
                # Columna Derecha: Leyenda, Indicadores, Barra Horizontal, Espacio Dinamico (Series Tiempo/Histograma)
                html.Div(
                    style={'width': '40%', 'padding': '20px', 'display': 'flex',
                           'flexDirection': 'column', 'gap': '20px'},
                    children=[
                        # Leyenda e Indicadores
                        html.Div(
                            style={'display': 'flex', 'flexDirection': 'row', 'gap': '20px', 'textAlign': 'center', 'color': color_palette["indicator_text"]},
                            children=[
                                html.Div(
                                    style={'display': 'flex', 'flexDirection': 'column',
                                           'alignItems': 'center', 'textAlign': 'center',
                                           'marginTop':'0','marginBottom':'0','marginLeft':'50px'},
                                    children=[
                                        html.Div(id='indicator-1', style={'fontSize': '38px','margin':'10px'}),
                                        html.Label("Baches Reportados", style={'fontSize': '14px','marginBottom':'50px'}),
                                        html.Div(id='indicator-3', style={'fontSize': '38px','margin':'10px'}),
                                        html.Label("del Total Historico", style={'fontSize': '14px','marginBottom':'0'})
                                    ]
                                ),
                                html.Div(
                                    style={'display': 'flex', 'flexDirection': 'column',
                                           'alignItems': 'center', 'textAlign': 'center',
                                           'marginTop':'0','marginBottom':'0','marginLeft':'50px'},
                                    children=[
                                        html.Div(id='indicator-2', style={'fontSize': '38px','margin':'10px'}),
                                        html.Label("Baches Atendidos", style={'fontSize': '14px','marginBottom':'50px'}),
                                        html.Div(id='indicator-4', style={'fontSize': '38px','margin':'10px'}),
                                        html.Label("del Total Reportado en el Periodo", style={'fontSize': '14px',
                                                                                               'marginBottom':'0'})
                                    ]
                                ),
                            ]
                        ),
                        # Barra Horizontal (Stacked)
                        dcc.Graph(
                            id='horizontal-barplot',
                            config={'displayModeBar': False},
                            style={'height': '100px'}
                        ),

                        # Selector para Espacio Dinamico (Series Tiempo o Histograma)
                        html.Div(
                            style={'display': 'flex', 'justifyContent': 'space-between', 'marginBottom': '0'},
                            children=[
                                html.Div(
                                    style={'marginBottom': '0', 'display': 'inline'},
                                    children=[
                                        html.Label("Reportes de Baches ante:", style={'fontSize': '12px'}),
                                        dcc.RadioItems(
                                            id='plot-selector',
                                            options=[
                                                {'label': 'Tiempo y Clima', 'value': 'time_series_1'},
                                                {'label': 'Sentimiento Ciudadania', 'value': 'histogram'}
                                            ],
                                            inline=True,
                                            value='time_series_1',
                                            style={'margin':'5px', 'fontSize': '10px',
                                                   'color': color_palette["global_selector_label_text"]}
                                        )
                                    ]
                                ),
                                # Selector para agregacion por Dia o por Mes para los sub-graficos
                                html.Div(
                                    children=[
                                        html.Label("Agregacion en Tiempo", style={'fontSize': '14px'}),
                                        dcc.Dropdown(
                                            id='time-aggregation-dropdown',
                                            options=[
                                                {'label': 'Dia', 'value': 'D'},
                                                {'label': 'Mes', 'value': 'M'}
                                            ],
                                            value='M',
                                            style={'backgroundColor': color_palette["global_selector_background"],
                                                   'color': color_palette["global_selector_text"]}
                                        )
                                    ]
                                ),
                            ]
                        ),
                        # Espacio Dinamico (Alterna entre Series de Tiempo e Histograma)
                        dcc.Graph(
                            id='dynamic-plot',
                            config={'displayModeBar': False},
                            style={'height': '300px'}
                        )
                    ]
                )
            ]
        ),
    ]
)


# Callback to update choropleth and scatter map
@app.callback(
    Output('choropleth-map', 'figure'),
    Input('choropleth-dropdown', 'value'),
    Input('scatter-period-dropdown', 'value')
)
def update_choropleth(selected_feature, selected_period):

    # filtered_scatter = scatter_data[
    #     (scatter_data['Size'] >= size_range[0]) & (scatter_data['Size'] <= size_range[1]) &
    #     (scatter_data['Value'] >= value_range[0]) & (scatter_data['Value'] <= value_range[1])
    # ]

    filtered_scatter = scatter_data[scatter_data['Date'].dt.year.isin(selected_period)]

    choroplethmap = go.Choroplethmap(geojson=geojson,
                                    locations=df_2_1_geo_urb_ageb.index,
                                    z=choropleth_data[selected_feature],
                                    colorscale="Greys",
                                    marker_opacity=0.75,
                                    marker_line_width=0,
                                    colorbar=dict(
                                                    orientation='h',
                                                    title=selected_feature,
                                                    len=0.5,
                                                    x=0.3,
                                                    xanchor='center',
                                                    y=0.01,
                                                    yanchor='bottom'
                                                ),
                                    )

    scattermap = go.Scattermap(
        lat=filtered_scatter["Latitude"],
        lon=filtered_scatter["Longitude"],
        mode="markers",
        marker=go.scattermap.Marker(size=2),
        name="Baches",
    )
    return {
        'data': [choroplethmap, scattermap],
        'layout': go.Layout(
            geo=dict(
                projection_type='mercator',
                showland=True,
                landcolor='black',
                subunitcolor='white'
            ),
            title='Mapa de Hermosillo, Sonora - AGEBs y Reportes de Baches',
            paper_bgcolor=color_palette["main_background"],
            plot_bgcolor=color_palette["main_background"],
            font=dict(color=color_palette["main_text"], size=10),
            margin={'r': 0, 't': 40, 'l': 0, 'b': 0},
            map_style="carto-positron",
            map_zoom=10.8,
            map_center = {"lat": 29.0838, "lon": -110.9529}
        )
    }

# Callback to update the indicators
@app.callback(
    [
        Output('indicator-1', 'children'),
        Output('indicator-2', 'children'),
        Output('indicator-3', 'children'),
        Output('indicator-4', 'children'),
    ],
    Input('scatter-period-dropdown', 'value')
)
def update_indicators(selected_period):

    total_historico = scatter_data.shape[0]

    filtered_scatter = scatter_data[scatter_data['Date'].dt.year.isin(selected_period)]
    bool_counts = filtered_scatter['Atendido'].value_counts()

    baches_reportados = bool_counts.sum()
    baches_atendidos = bool_counts[True]

    porcentaje_historico = (baches_reportados/total_historico)*100
    porcentaje_atendido = (baches_atendidos/baches_reportados)*100

    return (
        f'{baches_reportados}',
        f'{baches_atendidos}',
        f'{porcentaje_historico:.2f}%',
        f'{porcentaje_atendido:.2f}%'
    )

# Actualizacion de Barras Horizontales
@app.callback(
    Output('horizontal-barplot', 'figure'),
    Input('scatter-period-dropdown', 'value')
)
def update_horizontal_barplot(selected_period):

    filtered_scatter = scatter_data[scatter_data['Date'].dt.year.isin(selected_period)]
    bool_counts = filtered_scatter['Atendido'].value_counts()

    categories = ['Atendidos', 'No Atendidos']
    atendidos = [bool_counts[True]]
    no_atendidos = [bool_counts[False]]

    bar_data = [
        go.Bar(
            y=categories,
            x=atendidos,
            name='Atendidos',
            orientation='h',
            marker=dict(color='rgb(50, 205, 50)'),
        ),
        go.Bar(
            y=categories,
            x=no_atendidos,
            name='No Atendidos',
            orientation='h',
            marker=dict(color='rgb(255, 99, 71)'),
        )
    ]

    return {
        'data': bar_data,
        'layout': go.Layout(
            title="Proporcion de Reportes Atendidos",
            barmode='stack',
            paper_bgcolor=color_palette["main_background"],
            plot_bgcolor=color_palette["main_background"],
            font=dict(color=color_palette["main_text"], size=8),
            margin={'r': 10, 't': 40, 'l': 0, 'b': 20},
            height= 100,
        )
    }


@app.callback(
    Output('dynamic-plot', 'figure'),
    [
        Input('plot-selector', 'value'),
        Input('time-aggregation-dropdown', 'value'),
        Input('scatter-period-dropdown', 'value')
    ]
)
def update_dynamic_plot(plot_type, time_aggregation, selected_period):

    filtered_time_series_data = time_series_data[time_series_data['Date'].dt.year.isin(selected_period)]

    filtered_histogram_data = histogram_data[histogram_data['Date'].dt.year.isin(selected_period)]
    print(filtered_histogram_data.shape)
    filtered_histogram_data = filtered_histogram_data[~filtered_histogram_data['Description'].str.contains('Bacheo en', na=False)]
    print(filtered_histogram_data.shape)

    if time_aggregation == 'D':
        report_count_aggregated_data = filtered_time_series_data.resample('D', on='Date').sum()
        weather_aggregated_data = filtered_time_series_data.resample('D', on='Date').mean()
    elif time_aggregation == 'M':
        report_count_aggregated_data = filtered_time_series_data.resample('M', on='Date').sum()
        weather_aggregated_data = filtered_time_series_data.resample('M', on='Date').mean()


    if plot_type == 'time_series_1':
        plot_1 = go.Scatter(
            x=report_count_aggregated_data.index,
            y=report_count_aggregated_data['Id'],
            mode='lines',
            name='Cant. Reportes',
            line=dict(color='#4d4c47', width=1),
            yaxis='y1'
        )

        plot_2 = go.Scatter(
            x=weather_aggregated_data.index,
            y=weather_aggregated_data['Rain'],
            mode='lines',
            name='Lluvia (mm)',
            line=dict(color='#729c8d', width=1),
            yaxis='y2'
        )

        plot_3 = go.Scatter(
            x=weather_aggregated_data.index,
            y=weather_aggregated_data['Temp'],
            mode='lines',
            name='Temperatura (C°)',
            line=dict(color='#eaa616', width=1),
            yaxis='y3'
        )

        return {
            'data': [plot_1, plot_2, plot_3],
            'layout': go.Layout(
                title=f'Reportes de Baches y Condiciones Climatologicas vs. Tiempo ({time_aggregation})',
                paper_bgcolor=color_palette["main_background"],
                plot_bgcolor=color_palette["main_background"],
                font=dict(color=color_palette["main_text"], size=8),
                margin={'r': 10, 't': 40, 'l': 50, 'b': 40},
                yaxis=dict(
                    title='Cant. Reportes',
                    titlefont=dict(color='orange'),
                    tickfont=dict(color='orange'),
                    showgrid=True
                ),
                yaxis2=dict(
                    title='Lluvia (mm)',
                    titlefont=dict(color='blue'),
                    tickfont=dict(color='blue'),
                    overlaying='y',
                    side='right',
                    showgrid=False
                ),
                yaxis3=dict(
                    title='Temperatura (C°)',
                    titlefont=dict(color='green'),
                    tickfont=dict(color='green'),
                    overlaying='y',
                    side='right',
                    position=1,
                    showgrid=False
                ),
            )
        }

    elif plot_type == 'histogram':

        plot_histogram = go.Histogram(
            x=filtered_histogram_data['Sentiment'],
            nbinsx=6,
            marker=dict(color='orange', line=dict(color='black', width=1))
        )
        return {
            'data': [plot_histogram],
            'layout': go.Layout(
                title=f'Sentimiento de Ciudadania al Reportar ({time_aggregation})',
                paper_bgcolor=color_palette["main_background"],
                plot_bgcolor=color_palette["main_background"],
                font=dict(color=color_palette["main_text"]),
                margin={'r': 10, 't': 40, 'l': 10, 'b': 40}
            )
        }

if __name__ == '__main__':
    app.run_server(debug=True)
