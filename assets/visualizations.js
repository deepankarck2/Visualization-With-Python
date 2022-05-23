window.onload = function() {
    var firstVisualSpec = {
        "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
        "description": "A simple bar chart with embedded data.",
        "data": {
          "url": "https://raw.githubusercontent.com/raynelfss/data-474/main/Data_For_474_Final.csv"
        },
        "vconcat" : [{
          "mark": "rule",
          "encoding": {
            "x": {
              "field": "Year",
              "type": "nominal"
            },
            "xOffset" : {
              "field" : "Area",
              "type": "nominal"
            },
            "y": {
              "field": "Harvest",
              "type": "quantitative"
              },
            "color" : {
                "condition" : {
                  "param": "brush",
                  "title": "Countries",
                  "field": "Area",
                  "type": "nominal"
                },
                "value" : "gray"
            }
          },
          "width": 650,
          "height": 300,
          "params": [{
              "name": "brush",
              "select": {"type": "interval", "encodings": ["x"]}
            },
            {"name": "click",
              "select": {"type": "point", "encodings": ["color"]}
            }],
            "transform": [{"filter": {"param": "click"}}]
        },
        {
          "mark": "circle",
          "encoding": {
            "x": {
              "field": "Temperature Change",
              "type": "quantitative"
            },
            "y": {
              "field": "Harvest",
              "type": "quantitative"
              },
              "size" : {
                "field": "Harvest",
                "type": "quantitative"
              },
            "color" : {
                "condition" : {
                  "param": "brush",
                  "title": "Countries",
                  "field": "Area",
                  "type": "nominal"
                },
                "value" : "gray"
            }
          },
          "width": 650,
          "height": 300,
          "params": [{
              "name": "brush",
              "select": {"type": "interval", "encodings": ["x", "y"]}
            },
            {"name": "click",
              "select": {"type": "point", "encodings": ["color"]}
            }],
            "transform": [{"filter": {"param": "click"}}]
        }
        ],
      };
    vegaEmbed('#vis1', firstVisualSpec);
}