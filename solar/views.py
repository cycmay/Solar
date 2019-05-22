from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from django.db.models import Count
# Create your views here.
import json

from solar import models
from solar import solar_handlers
from .json_api import JsonResponse, JsonError

from django.shortcuts import get_object_or_404


ATYPE = "09"    # 传输数据为数据报格式


def index(request):
    """
    总表视图
    :param request:
    :return:
    """
    solars = []
    # 检索数据库灯杆号
    numb = []
    for queryset in models.Solar.objects.values("number").annotate(Count=Count('number')).order_by():
        numb.append(queryset["number"])
    for num in numb:
        solar = models.Solar.objects.filter(number=num).order_by("-c_time")[0]
        solars.append(solar)
    return render(request, 'solar/index.html', locals())


def dashboard(request):
    return render(request, 'solar/dashboard.html')


class ReturnSolar(APIView):

    def get(self, request, *args, **kwargs):
        solars = []
        # 检索数据库灯杆号
        numb = []
        for queryset in models.Solar.objects.values("number").annotate(Count=Count('number')).order_by():
            numb.append(queryset["number"])
        for num in numb:
            solar = models.Solar.objects.filter(number=num).order_by("-c_time")[0]
            solars.append(solar)
        return JsonResponse(solars)


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