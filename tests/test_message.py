# -*- coding: utf-8 -*-
import unittest
import access_helper

class test_message(unittest.TestCase):
    def test_send(self):
        (conn,cur) = access_helper.get_connection_cursor()
        cur.execute("""INSERT INTO MSG_Outbox(receiver,MsgTitle,CommPort,MsgType) VALUES ('15974253250','fdafdafdafdafa',4,0)""")
        access_helper.clear(conn,cur)

    def test_recevie(self):
        (conn,cur) = access_helper.get_connection_cursor()
        cur.execute("SELECT * FROM MSG_Inbox")
        for row in cur.fetchall():
            for field in row:
                print field,
            print ''
        access_helper.clear(conn, cur)

    def test_devices(self):
        (conn,cur) = access_helper.get_connection_cursor()
        cur.execute("SELECT * FROM Devices")
        for row in cur.fetchall():
            for field in row:
                print field,
            print ''
        access_helper.clear(conn, cur)