from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Solar(models.Model):
    status = (
        (0, '在线'),
        (1, '下线'),
    )
    number = models.SmallIntegerField(default=0, verbose_name='灯杆号')
    s_voltage = models.FloatField(default=0.0, verbose_name="太阳能板电压(V)")
    s_current = models.FloatField(default=0.0, verbose_name="太阳能板电流(A)")
    b_voltage = models.FloatField(default=0.0, verbose_name="蓄电池电压(V)")
    charging_status = models.SmallIntegerField(default=0, verbose_name="充电工作状态")
    load_current = models.FloatField(default=0.0, verbose_name="负载电流（A）")
    load_voltage = models.FloatField(default=0.0, verbose_name="负载电压(V)")
    lamp_status = models.SmallIntegerField(default=0, verbose_name="开灯状态")
    work_time = models.FloatField(default=0.0, verbose_name="工作时间(Min)")
    cumulative_power = models.FloatField(default=0.0, verbose_name="累计电量(Kwh)")
    c_time = models.DateTimeField(auto_now=True, verbose_name='添加日期')

    class Meta:
        verbose_name = 'solar'
        verbose_name_plural = "solar"
        ordering = ['-c_time']
