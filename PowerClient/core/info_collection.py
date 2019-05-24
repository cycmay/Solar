import sys
import platform


class InfoCollection(object):

    def collect(self):
        # 收集信息
        try:
            info_data = InfoCollection.sun_power()
            formatted_data = self.build_report_data(info_data)
            return formatted_data
        except AttributeError:
            sys.exit("不支持当前操作系统： [%s]! " % platform.system())

    @staticmethod
    def sun_power():
        from plugins.collect_sunPower import collect
        return collect()

    @staticmethod
    def build_report_data(data):
        # 留下一个接口，方便以后增加功能或者过滤数据
        pass
        return data


