from pyg2plot import Plot

line = Plot("Line")

#运用这个可以生成 html文件,之后打开html文件可以查看线路图

print(years)
line.set_options({
        "data":[
            {"year": "1991", "value": 3 },
            {"year": "1992", "value": 4 },
            {"year": "1993", "value": 3.5 },
            {"year": "1994", "value": 5 },
            {"year": "1995", "value": 4.9 },
            {"year": "1996", "value": 6 },
            {"year": "1997", "value": 7 },
            {"year": "1998", "value": 9 },
            {"year": "1999", "value": 13 },
            {"year": "2000", "value": 14},
            {"year": "2000", "value": 15},
            {"year": "2001", "value": 16}
        ],
    "xField": "year",
    "yField": "value",

})

line.render("plot1.html")

line.render_html()

