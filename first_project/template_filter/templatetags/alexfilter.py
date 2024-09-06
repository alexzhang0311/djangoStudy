#过滤器最多只能有两个参数并且第一个参数永远是需要被过滤的那个对象
from django import template
from datetime import datetime

register = template.Library()

def greet(value,word):
    return value+word

#过滤器注册到django,参数一：过滤器名字，参数二：过滤器函数
register.filter("greet",greet)

#过滤器所在的app必须注册在项目的settings文件当中

#html文件中加载过滤器
@register.filter
def time_since(value):
    if isinstance(value,datetime):
        now = datetime(year=2024,month=9,day=17,hour=0,minute=0,second=0)
        time_diff = abs((value - now).total_seconds())
        
        days = int(time_diff // (24*3600))
        remain_seconds = time_diff % (24*3600)

        hours = int(remain_seconds // 3600)
        remain_seconds %= 3600

        mints =  int(remain_seconds // 60)
        remain_seconds %= 60

        seconds = int(remain_seconds)
        return f"距离中秋节还有:{days}天，{hours}小时，{mints}分钟，{seconds}秒"
        
    else:
        return value