from pyecharts.charts import Geo
from pyecharts import options as opts
from pyecharts.globals import ChartType, SymbolType

data = [['黄浦区',  24],
        ['徐汇区', 105],
        ['长宁区',  56],
        ['闵行区', 258],
        ['虹口区',   8],
        ['浦东新区',88],
        ['普陀区',  77]]

chart = (
    Geo()
    .add_schema(maptype="上海")
    .add("geo", data, type_=ChartType.HEATMAP)                 # 热力图形式
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(),
        title_opts=opts.TitleOpts(title="Geo_Shanghai_Heatmap"),
    )
)

chart.render('geo2.html')
