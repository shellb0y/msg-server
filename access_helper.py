# -*- coding: utf-8 -*-
import pypyodbc


def get_connection_cursor():
    # str = 'Driver={Microsoft Access Driver (*.mdb,*.accdb)};DBQ=E:\\PycharmProjects\\MessageServer\\MMSCRM.mdb;'
    str = u'Driver={Microsoft Access Driver (*.mdb,*.accdb)};DBQ=e:\\kuka\\MMSCRM.mdb;'
    conn = pypyodbc.win_connect_mdb(str)
    cur = conn.cursor()
    return conn, cur


def clear(conn, cur):
    conn.commit()
    cur.close()
    conn.close()
