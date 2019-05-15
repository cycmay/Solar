import json
from solar import models


class NewSolar(object):
    def __init__(self, request, data):
        self.request = request
        self.data = data

    def create_record(self):
        """
        添加新的记录
        :return:
        """

        solar = models.Solar.objects.create(number=self.data.get('number'),
                                            s_voltage=self.data.get('s_voltage'),
                                            s_current=self.data.get('s_current'),
                                            b_voltage=self.data.get('b_voltage'),
                                            charging_status=self.data.get('charging_status'),
                                            load_current=self.data.get('load_current'),
                                            load_voltage=self.data.get('load_voltage'),
                                            lamp_status=self.data.get('lamp_status'),
                                            work_time=self.data.get('work_time'),
                                            cumulative_power=self.data.get('cumulative_power'),
                                            c_time=self.data.get('c_time'),
                                            )
        return solar