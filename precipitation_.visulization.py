from re import template
from traceback import print_tb
from turtle import title
import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output  

style_sheeet = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets= style_sheeet)

df = pd.read_csv("https://raw.githubusercontent.com/deepankarck2/Final-Project-474/main/rainfall_trend_in_flood_risky_countries.csv")

#Initial Choloropleth Map
dff_map = df.loc[df['Year'] == '2010']
fig_map = go.Figure(data = go.Choropleth(locations=dff_map['Country'],
                                        z = (dff_map['Affect']),
                                        locationmode = 'country names',
                                        colorscale = 'thermal'))
fig_map.update_layout(margin=dict(l=20, r=30, t=80, b=60))
fig_map.update_layout(template="plotly_white", title="Surprise Map of Coutries being affected by Rainfall", 
                        legend_title="hh",
                        font=dict(
                        family="Courier New, monospace",
                        size=15,
                        color="RebeccaPurple"
    ),
    annotations= [dict(
            x=1.01,
            y=1.05,
            align="right",
            valign="top",
            showarrow=False,
            xref="paper",
            yref="paper",
            xanchor="center",
            yanchor="top",
            text='Surprise Value')])


#Heap Map for China's Provience
df_heat = pd.read_csv("https://raw.githubusercontent.com/deepankarck2/Final-Project-474/main/china_flood_data2.csv")
df_heat= df_heat.pivot("Town", "Crop", "Affected")

fig_heat_map = px.imshow(df_heat, template="plotly_dark",width=800, height=400, title="Effect of Flood on Agriculture no different regions in China")
fig_heat_map.update_layout(margin=dict(l=10, r=20, t=50, b=50), annotations= [dict(
            x=1.01,
            y=1.05,
            align="right",
            valign="top",
            showarrow=False,
            xref="paper",
            yref="paper",
            xanchor="center",
            yanchor="top",
            text='Percent Drop in Production')])

colors = {
    'background': '#111111',
    'text': '#14EB2F',
    'text2': '#0000FF'
}

app.layout = html.Div([
   

    html.H2("Showing Rainfall information", style={'text-align': 'center', 'color': colors['text2']}),

        html.Div([
         
            dcc.Graph(id='map_rain_fall_country', figure=fig_map, clickData=None, className='six columns'),

            dcc.Graph(id='line_each_country', figure={}, 
            config={
                'scrollZoom': True,
                'showTips': True,
                'displayModeBar': True,
            },
            className = 'six columns',
            )
        ]),

        

        html.Div([
            html.Br(), html.Br(),

            html.H2(children='Heat Map',
            style={
            'color': colors['text2']
            }
            ),

         html.Div(children='''
            Showing The Effects of Flood in Differnt Crops after a dangerous flood in 2019.
        ''',
            style={
            #
            'background-color':'black',
            'color': colors['text']
            }),

            html.Br(),
            
            html.Div([
                dcc.Graph(id='heat_map', figure=fig_heat_map, clickData=None),
        ],style={'width': '50%','padding-left':'25%', 'padding-right':'25%'}
        )
        ])
])


@app.callback(
    Output(component_id='line_each_country', component_property='figure'),
    Input(component_id='map_rain_fall_country', component_property='clickData'),
)
def update_line_graph(country_choosen):
    if country_choosen is None:
        dff = df.loc[df['Country'] == 'Niger']
        fig = px.line(dff, x="Year", y=['Annual Mean', '5-yr smooth'], template="plotly_dark")
        print(dff) 
        fig.update_traces(mode='lines')

        fig.update_layout(title= "Rain Line Chart for Niger",
                   xaxis_title= 'Year Information',
                   yaxis_title= 'Avergage Rainfall in mm')
        fig.update_layout(legend=dict(
                            orientation="h",
                            yanchor="bottom",
                            y=1.02,
                            xanchor="right",
                            x=1
                        ))
        fig.update_layout(autotypenumbers='convert types')

        return fig

    else: 
        print(country_choosen)
        country_name = country_choosen['points'][0]['location']

        dff = df.loc[df['Country'] == country_name]
        fig = px.line(dff, x="Year", y=['Annual Mean', '5-yr smooth'], template ="plotly_dark")

        fig.update_traces(mode='lines')
        
        fig.update_layout(title= f"Rain Line Chart for {country_name}",
                   xaxis_title= 'Year Information',
                   yaxis_title= 'Avergage Rainfall in mm')

        fig.update_layout(legend=dict(
                            orientation="h",
                            yanchor="bottom",
                            y=1.02,
                            xanchor="right",
                            x=1
                        ))
        fig.update_layout(autotypenumbers='convert types')

        return fig


if __name__ == '__main__':
    app.run_server(debug=True)
