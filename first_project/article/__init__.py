from django.urls import register_converter

class CategoryConverter(object):
    regex = r"\w+|(\w+\+\w+)+"

    def to_python(self, value):
        text = value.split('+')
        return text

    def to_url(self, value):
        # return value
        if isinstance(value,list):
            text = "+".join(value)
            return text
        else:
            raise RuntimeError("转换URL的时候，分类参数必须为列表")

register_converter(CategoryConverter,'cate')
