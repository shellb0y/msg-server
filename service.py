# -*- coding: utf-8 -*-
import newkuka_api
import json


# +SMS:402,{"port":69,"time":"2017-02-23 11:33:28","number":"10086","content":"尊敬的15983741984客户，至02月23日11时，您的账户余额为2.90元。欠费停机将影响您的通信畅通，建议您及时充值。话费查询请拨1008611。您可通过提高网龄和消费、减少停机次数、补充认证资料来获得信用星级。【四川移动掌上营业厅】便捷充话费，随时随地办业务，首次使用即送200M流量，还有50M流量红包天天抢，下载点击： http://dx.10086.cn/schfcd 中国移动"}
def get_sms(com):
    data = newkuka_api.get_sms(com)
    return json.loads('{' + data.split(',{')[1])


# AP$PORTS=8,"67,69,73,77,80,81,82,83"
def get_coms():
    data = newkuka_api.get_coms()
    return data


# ['AP$PINFO=84,67,{"state":0,"phonum":"15281582796","imsi":"460022815834607","imei":"863725035157757"}', 'AP$PINFO=84,69,{"state":0,"phonum":"18227453458","imsi":"460000484943115","imei":"863725035143427"}', 'AP$PINFO=84,73,{"state":0,"phonum":"18283628394","imsi":"460000484967019","imei":"863725034987204"}', 'AP$PINFO=84,77,{"state":0,"phonum":"18227463913","imsi":"460000484943331","imei":"863725035146115"}', 'AP$PINFO=84,80,{"state":0,"phonum":"13568699148","imsi":"460000484960639","imei":"863725035004033"}', 'AP$PINFO=84,81,{"state":0,"phonum":"15808362108","imsi":"460022815835241","imei":"863725035157880"}', 'AP$PINFO=84,82,{"state":0,"phonum":"15183618254","imsi":"460000484963174","imei":"863725034996999"}', 'AP$PINFO=84,83,{"state":0,"phonum":"15183616580","imsi":"460022815834725","imei":"863725035149614"}']
def get_coms_status():
    status = newkuka_api.get_coms_status()
    data = {}
    for s in status:
        _t = s.split(',{')
        # if _t:
        #     print _t[0][_t[0].index(',')+1:]
        data[_t[0][_t[0].index(',') + 1:]] =  json.loads('{' + _t[1])
    return data

