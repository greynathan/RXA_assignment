import pandas as pd
import plotly.express as px
import dash 
from dash import dcc
from dash import dash_table
from dash import html
from dash.dependencies import Input, Output
from ML import prediction

# Instantiation of the app and supression of startup exceptions
# This is done to account for my multiple app.callbacks on each page
app = dash.Dash(__name__, suppress_callback_exceptions=True)

# I open the data frames for the map, table and 2020 predictions 
df = pd.read_parquet('df_map.parquet.gzip')
df_table = df[['zip_code', '2011_MHI', '2012_MHI', '2013_MHI', '2014_MHI', '2015_MHI', '2016_MHI', '2017_MHI', '2018_MHI', '2019_MHI']].copy()
df_2020 = pd.read_parquet('df_2020.parquet.gzip')

# This is the first layer of HTML elements, where I have the tabs
app.layout = html.Div(children=[
    html.H1(children='RXA Assignment', style={'text-align': 'center'}),

    dcc.Tabs(id="tabs-styled-with-props", value='tab-1', children=[
        dcc.Tab(label='Median Household Income by Zip Code Map', value='tab-1'),
        dcc.Tab(label='Median Household Income by Zip Code Table', value='tab-2'),
        dcc.Tab(label='Zip Code Median Household Income Predcitor', value='tab-3'),
        
    ], colors={
        "border": "gray",
        "primary": "gray",
        "background": "gray"
    }),
    html.Div(id='tabs-content-props'),        
])

# This callback takes in which tab is in us and the function returns the page with the appropriate information 
@app.callback(Output('tabs-content-props', 'children'),
              Input('tabs-styled-with-props', 'value'))
def render_content(tab):
    # tab 1 handles the map
    if tab == 'tab-1':
        return html.Div([
            html.Label(['Median Household Income by Zip Code'],style={'font-weight': 'bold'}),
            html.Br(), html.Br(),
            html.Label(['Choose year:'],style={'font-weight': 'bold'}),
            dcc.Dropdown(
                id='dropdown',
                options=[
                    {'label': '2011', 'value': '2011_MHI'},
                    {'label': '2012', 'value': '2012_MHI'},
                    {'label': '2013', 'value': '2013_MHI'},
                    {'label': '2014', 'value': '2014_MHI'},
                    {'label': '2015', 'value': '2015_MHI'},
                    {'label': '2016', 'value': '2016_MHI'},
                    {'label': '2017', 'value': '2017_MHI'},
                    {'label': '2018', 'value': '2018_MHI'},
                    {'label': '2019', 'value': '2019_MHI'},
                    {'label': '2020 Prediction', 'value': '2020_pred'},
                        ],
                value='2011_MHI',
                style={"width": "60%"}),
            
            html.Div(dcc.Graph(id='map')),        
            ])
    # tab 2 handles the table
    elif tab == 'tab-2':
        return html.Div([
            html.Label(['Median Household Income by Zip Code'],style={'font-weight': 'bold'}),
            html.Br(), html.Br(),
            dash_table.DataTable(df_table.to_dict('records'), [{"name": i, "id": i} for i in df_table.columns])        
            ])
    # tab 3 handles the prediction calulator
    elif tab == 'tab-3':
        return html.Div([
            html.Label(['Zipcode Median Household Income Prediction Calculator'],style={'font-weight': 'bold'}),
            html.Br(), html.Br(),
            html.Label(['Past 8 years income: '],style={'font-weight': 'bold'}),
            html.Br(), html.Br(),
            dcc.Input(id="year1", type="text", placeholder="year 1", debounce=True),
            dcc.Input(id="year2", type="text", placeholder="year 2", debounce=True),
            html.Br(), html.Br(),
            dcc.Input(id="year3", type="text", placeholder="year 3", debounce=True),
            dcc.Input(id="year4", type="text", placeholder="year 4", debounce=True),
            html.Br(), html.Br(),
            dcc.Input(id="year5", type="text", placeholder="year 5", debounce=True),
            dcc.Input(id="year6", type="text", placeholder="year 6", debounce=True),
            html.Br(), html.Br(),
            dcc.Input(id="year7", type="text", placeholder="year 7", debounce=True),
            dcc.Input(id="year8", type="text", placeholder="year 8", debounce=True),
            html.Br(), html.Br(),
            html.Button('Submit', id='button'),
            html.Br(), html.Br(),
            html.Label(['Prediction:'],style={'font-weight': 'bold'}),
            html.Div(html.Label(id='out')),
        ])

# This callback and function is used to select the cooresponding data to 
# be displayed on the map
@app.callback(
    Output('map', 'figure'),
    [Input(component_id='dropdown', component_property='value')],
)
def select_graph(value):
    if value == "2020_pred":
        fig = px.scatter_mapbox(df_2020, lat="LAT", lon="LNG", hover_name="zip_code", hover_data=["zip_code", value],
                            color= value, color_continuous_scale="turbo",
                            range_color=(0, 100000), zoom=3, height=300)
        fig.update_layout(
            mapbox_style="white-bg",
            mapbox_layers=[
                {
                    "below": 'traces',
                    "sourcetype": "raster",
                    "sourceattribution": "United States Geological Survey",
                    "source": [
                        "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
                    ]
                }
            ])
        fig.update_layout(
                    autosize=True,
                    margin = dict(
                            l=0,
                            r=0,
                            b=0,
                            t=0,
                            pad=4,
                            autoexpand=True
                        ),
                    height = 600,
                )
        return fig
    else:
        fig = px.scatter_mapbox(df, lat="LAT", lon="LNG", hover_name="zip_code", hover_data=["zip_code", value],
                                color= value, color_continuous_scale="turbo",
                                range_color=(0, 100000), zoom=3, height=300)
        fig.update_layout(
            mapbox_style="white-bg",
            mapbox_layers=[
                {
                    "below": 'traces',
                    "sourcetype": "raster",
                    "sourceattribution": "United States Geological Survey",
                    "source": [
                        "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
                    ]
                }
            ])
        fig.update_layout(
                    autosize=True,
                    margin = dict(
                            l=0,
                            r=0,
                            b=0,
                            t=0,
                            pad=4,
                            autoexpand=True
                        ),
                    height = 600,
                )
        return fig

# This callback and fucntion is used to take in the prediction data, run it through
# the prediction function and return the prediction
@app.callback(
    Output("out", "children"),
    Input("year1", "value"),
    Input("year2", "value"),
    Input("year3", "value"),
    Input("year4", "value"),
    Input("year5", "value"),
    Input("year6", "value"),
    Input("year7", "value"),
    Input("year8", "value"),
    Input('button', 'n_clicks')
)
def pred_calc(year1, year2, year3, year4, year5, year6, year7, year8, n):
    #Making sure the function only runs when the button is pressed 
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if ('button' in changed_id) and (year1 and year2 and year3 and year4 and year5 and year6 and year7 and year8) != None:
        list = [[year1, year2, year3, year4, year5, year6, year7, year8]]
        df_pred = pd.DataFrame(list, columns=['2011_MHI', '2012_MHI', '2013_MHI', '2014_MHI', '2015_MHI', '2016_MHI', '2017_MHI', '2018_MHI'])
        return prediction(df_pred)[0]
    else:
        return ''
# This sets the server ip and port. As well as enables debugging
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port = '8050', debug=True)