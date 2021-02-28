from pyecharts.charts import Bar
from pyecharts import options as opts

# 图片主题
from pyecharts.globals import ThemeType

#bar = Bar()
bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT)) # 在初始化选项中设置图片主题

bar.add_xaxis(["a", "b", "c", "d", "e", "f"])
bar.add_yaxis("X", [5, 20, 36, 10, 75, 90])
bar.add_yaxis("Y", [10, 18, 29, 20, 65, 80])
bar.set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))

bar.render("bar.html")
