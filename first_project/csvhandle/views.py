from django.shortcuts import render,loader
from django.http import HttpResponse,HttpRequest,StreamingHttpResponse
import csv
# Create your views here.

def index(request):
    response = HttpResponse(content_type='text/csv;charset=utf-8')
    response["Content-Disposition"] = "attachement;filename=abc.csv"
    writer = csv.writer(response)

    for row in range(0,1000000):
        writer.writerow(['Row {}'.format(row),'{}'.format(row)])
    # writer.writerow(['username','age'])
    # writer.writerow(['张弛','18'])
    return response

    # context = {
    #     'rows':[
    #         ['username','age'],
    #         ['张弛','18']
    #     ]
    # }
    # template = loader.get_template('csv.html')
    # csv_template = template.render(context)
    # response.content = csv_template
    # return response


def stream_csv(request):
    response = StreamingHttpResponse(content_type='text/csv;charset=utf-8')
    response["Content-Disposition"] = "attachement;filename=large.csv"
    # response.streaming_content = ("username,age\n","alexzhang,18\n")
    rows = ("Row {},{}\n".format(row,row) for row in range(0,1000000))
    response.streaming_content = rows
    return response