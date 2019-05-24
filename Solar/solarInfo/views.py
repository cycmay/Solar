from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from django.db.models import Count
# Create your views here.
import json

from solarInfo import models
from solarInfo import solar_handlers
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
    return render(request, 'solarInfo/index.html', locals())


def detail(request):
    """
    日志视图
    :param request:
    :return:
    """
    solars = models.Solar.objects.all()[:200]
    return render(request, 'solarInfo/detail.html', locals())



def dashboard(request, number):
    solar = models.Solar.objects.filter(number=number).order_by("-c_time")[0]
    context = {
        "solar": solar,
    }
    return render(request, 'solarInfo/dashboard.html', context=context)


class ReturnSolar(APIView):

    def get(self, request, *args, **kwargs):
        """
        get api:
            在request对象中
            request.query_params 中可以获取?param1=32&param2=23形式的参数.
            request.query_params 返回的数据类型为QueryDict
            QueryDict转为普通python字典. query_params.dict()即可.

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        # 检索数据库灯杆号
        data = request.query_params.dict()
        if not data:
            return JsonError("nothing got.")
        number = data.get("number")
        solar = models.Solar.objects.filter(number=number).order_by("-c_time")[0]
        return JsonResponse(solar)


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