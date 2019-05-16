from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
import json
from solar import models
from solar import solar_handlers

from django.shortcuts import get_object_or_404


ATYPE = "09"    # 传输数据为数据报格式

def index(request):
    """
    总表视图
    :param request:
    :return:
    """
    solars = models.Solar.objects.order_by("-c_time")[:2]
    return render(request, 'solar/index.html', locals())

@csrf_exempt
def report(request):
    if request.method == 'POST':
        asset_data = request.POST.get('client_data')
        data = json.loads(asset_data)
        # print(data)
        if not data:
            return HttpResponse('没有数据！')
        if not issubclass(dict, type(data)):
            return HttpResponse('数据必须为字典格式！')

        # 你的检测代码
        # 若传输过来的数据为数据信息包
        if data.get("header").get("type") == ATYPE:
            body = data.get("body")
            collect = body.get("data")
            for solar in collect:
                obj = solar_handlers.NewSolar(request, collect.get(solar))
                response = obj.create_record()
                print(response)
            return HttpResponse("OK!")
    return HttpResponse('200 ok')