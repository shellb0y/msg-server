# -*- coding: utf-8 -*-






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