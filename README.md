# SolarS

## 一款数据展示平台

- 网站框架使用的是Django

- 数据来源Client 仿真数据软件，使用socket 套接字进行数据通信

- 网站主要完成的功能有：api接口封装、仿真数据解析、动态折线图生成以及其他web常用功能

- 辅助工具：

  ​	PowerClient——单独的进程，用于对socket数据解析和report

  ​	Dss-serializer—— 需单独安装，api接口风格格式化工具

---

## 注意事项：

1. 安装步骤

   (1) 环境搭建

   ​	本项目使用到的django==2.0

   > $ pip install requirements

   (2) 数据库迁移

   > $ cd Solar  //进入web工程 
   >
   > $python manager.py migrate

   (3) 创建超级用户

   > $ python manager.py createsuperuser

   (4) 启动项目

   > $ python manager.py runserver

   (5) 仿真数据源

   > $ cd PowerClient/bin
   >
   > $ python main.py report_data

2. 使用方法

   浏览器输入  http://127.0.0.1:8000/soalr/

3.  展示图

   ![index](https://github.com/cycmay/SolarS/blob/master/tools/images/541ALR8HN.png "index")



