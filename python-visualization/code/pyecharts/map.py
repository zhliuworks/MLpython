from pyecharts.charts import Map
from pyecharts import options as opts

data = [['China',  24],
        ['Canada',  56],
        ['Brazil',  56],
        ['United States', 119],
        ['Russia',  79],
        ['Japan',  23],
        ['Australia',  97]]

chart = (
        Map()
        .add("value", data, "world")
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="Map_World"),
            visualmap_opts=opts.VisualMapOpts(max_=200),
        )
    )

chart.render('map.html')
