# -*- coding: utf-8 -*-
import newkuka_api
import service
import re
import time

PHONESETS = 'server:1'
index = 0
regex = {'1': u'^您正在橙e网注册，验证码为(\\d{6})，有效期120秒。【平安银行】$',
         '2': u'.*您正在注册广发银行E\+盈电子账户,动态验证码为：(\\d{6})。【广发银行】$'}

while 1:
    coms_status = service.get_coms_status()
    # print coms_status
    for c in coms_status:
        if coms_status[c]['phonum'] and coms_status[c]['state'] == 0:
            if ++index == 1 and not service.r.sismember(PHONESETS, coms_status[c]['phonum']):
                service.r.delete(PHONESETS)
            service.r.sadd(PHONESETS, coms_status[c]['phonum'])

        while 1:
            sms = service.get_sms(c)
            if sms:
                print c, coms_status[c]['phonum'], sms
                for r in regex:
                    pattern = re.compile(regex[r])
                    match = pattern.match(sms['content'])
                    if match:
                        print match.group(1)
                        redis_key = coms_status[c]['phonum'] + ':' + r
                        service.r.hmset(redis_key, {'code': match.group(1), 'time': sms['time']})
                        service.r.expire(redis_key, 30 * 60)

            else:
                time.sleep(1)
                break
        # print c, coms_status[c]['phonum'], service.get_sms(c)
        index = 0
    time.sleep(3)
# newkuka_api.close()


# import win32com.client
#
# conn = win32com.client.Dispatch(r'ADODB.Connection')
# DSN = 'PROVIDER=Microsoft.Jet.OLEDB.4.0;DATA SOURCE=E:/PycharmProjects/MessageServer/MMSCRM.mdb;'
# conn.Open(DSN)
# rs = win32com.client.Dispatch(r'ADODB.Recordset')
# rs.Cursorlocation = 3
# rs_name = 'card'  # 表名
# rs.Open('[' + rs_name + ']', conn, 1, 3)
# rs.MoveFirst()
# for x in range(rs.RecordCount):
#     if rs.EOF:
#         break
#     else:
#         print rs.Fields.Item(0).Value, rs.Fields.Item(1).Value, rs.Fields.Item(2).Value
#         rs.MoveNext()
# rs.Close()
# conn.Close()

# import pypyodbc
# if __name__=="__main__":
#     str = 'Driver={Microsoft Access Driver (*.mdb,*.accdb)};DBQ=E:\\PycharmProjects\\msg-server\\MMSCRM.mdb;'
#     conn = pypyodbc.win_connect_mdb(str)
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM phrase")
#     for row in cur.fetchall():
#         for field in row:
#             print field,
#         print ''
#     conn.commit()
#     cur.close()
#     conn.close()
