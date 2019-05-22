#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socket
import sys

# client 端参数
host = "127.0.0.1"
port = 60000

address = (host, port)

# test_str ="7b09003d33333530303130313030326833500101002001220109cf021809b70100d60978010079072a020a22024909d00100fd097c01011e046622167b"
# test_str.encode().hex()
# print(test_str)


def collect():
    """

    :return: Hex e.g.
        7b09003d33333530303130313030326833500101002001220109cf021809b70100d60978010079072a020a22024909d00100fd097c01011e046622167b
    """
    # 使用连接函数 connect 连接到该 IP 的特定的端口
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created.")
    try:
        server_socket.bind(address)
        print("Socket Bind complete.")
    except socket.error as msg:
        print("Bind faild. Error Code: " + str(msg[0]) + "Message: " + msg[1])
        sys.exit()
    server_socket.listen(5)
    print("socket listening now!")


    # wait to accept a connection - blocking call
    conn, addr = server_socket.accept()
    print("Connected with " + addr[0] + ":" + str(addr[1]))
    while True:
        # receive data
        data = conn.recv(1024)
        if not data:
            break
        # bytes对象的hex()方法可以输出直接十六进制形式的
        data = data.hex()
        # 格式化
        data = format_data(data)
        print(data)
        yield data
    conn.close()
    server_socket.close()
    return

# 数据报格式化
def format_data(info):
    """

    :param info: 数据包 16进制数 字符串
    :return:
    """

    # "sourceip": info[22:30],    # IP
    # "sourceport": info[30:34],  # Port
    # "ender": info[34:36]        # 结束
    # 数据包的解析

    # 头部信息
    header = {
        "starter": info[0:2],    # 起始符
        "type": info[2:4],       # DTU注册类型码/数据类型码 09
        "length": int(info[4:8], 16),     # 长度
        "identity": info[8:30],  # 身份码
    }

    # 数据详细信息
    body = {
        "starter": info[30:32],     # 0x68（首部）
        "gatewayid": info[32:44],   # 网关 ID
        "order": info[44:46],       # 命令码
        "length": info[46:48],      # 载荷长度
        "data": {                   # 载荷
            "data1": {
                "number": info[48:50],  # n号灯杆数据
                "s_voltage": float(int(info[50:54], 16) / 100.0),   # 太阳能板电压~，采用二进制编码，每个电压占2字节，高位在前、低位在后，
                                                                    # 且电压放大100倍的整数，如 09 D0 表示电压25.12V
                "s_current": float(int(info[54:58], 16) / 100.0),   # 电流 A格式同上
                "b_voltage": float(int(info[58:62], 16) / 100.0),   # 蓄电池电压 格式同上 V
                "charging_status": int(info[62:64], 16),                     # 充电工作状态
                "load_current": float(int(info[64:68], 16) / 100.0),  # 负载电流 V
                "load_voltage": float(int(info[68:72], 16) / 100.0),  # 负载电压 A
                "lamp_status": int(info[72:74], 16),                    # 开灯状态
                "work_time": int(info[74:78], 16),                      # 工作时间 min
                "cumulative_power": float(int(info[78:82], 16) / 100.0),  # 累计电量 kWh
            },
            "data2": {
                "number": info[82:84],  # n号灯杆数据
                "s_voltage": float(int(info[84:88], 16) / 100.0),   # 太阳能板电压~，采用二进制编码，每个电压占2字节，高位在前、低位在后，
                                                                    # 且电压放大100倍的整数，如 09 D0 表示电压25.12V
                "s_current": float(int(info[88:92], 16) / 100.0),   # 电流 A格式同上
                "b_voltage": float(int(info[92:96], 16) / 100.0),   # 蓄电池电压 格式同上 V
                "charging_status": int(info[96:98], 16),                     # 充电工作状态
                "load_current": float(int(info[98:102], 16) / 100.0),    # 负载电流 V
                "load_voltage": float(int(info[102:106], 16) / 100.0),    # 负载电压 A
                "lamp_status": int(info[106:108], 16),                    # 开灯状态
                "work_time": int(info[108:112], 16),                      # 工作时间 min
                "cumulative_power": float(int(info[112:116], 16) / 100.0),  # 累计电量 kWh
            },
        },
        "checksum": info[-4:-2]       # 校验和 16
    }

    data = {
        "header": header,
        "body": body,
    }

    return data

if __name__ == "__main__":
    pass
    # 收集信息功能测试
    # data = collect()
    # print(data)
    collect()
    # 解析数据报功能测试
    # data = format_data(test_str)
    # print(data)