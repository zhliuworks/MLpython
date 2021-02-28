from pyecharts.charts import Geo
from pyecharts import options as opts

data = [['广东',  24],
        ['北京',  56],
        ['上海',  56],
        ['江西', 119],
        ['湖南',  79],
        ['浙江',  23],
        ['江苏',  97]]

# 采用链式调用
chart = (
    Geo()

    # 控制地图类型、视角中心点等
    .add_schema(maptype="china")
    
     # 添加图表名称、传入数据集、选择geo图类型、调整图例等
    .add("geo", data)

    # 系列配置项 series_options
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))

    # 全局配置项 global_options
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(),
        title_opts=opts.TitleOpts(title="Geo_China"),
    )
)

chart.render('geo1.html')
