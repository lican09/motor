# -*- coding: utf-8 -*-
import tornado.web, tornado.ioloop
import motor
from tornado import gen

class monitor_frontserver(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        """Display all messages."""
        self.write('''<html><head><meta http-equiv="refresh" content="2">
        </head><body><a href="/">返回</a><br>
        ''')
        self.write('<ul>')
        db = self.settings['db']
        db.monitor_frontserver.find().sort([('_id', -1)]).limit(1).each(self._got_message)

    def _got_message(self, message, error):

        if error:
            raise tornado.web.HTTPError(500, error)
        elif message:
            self.write('<h1>monitor_frontserver:</h1><br>')
            # self.write('<p> %s</p><br>' % message)

            # net_statistics_client
            self.write('<h2>net_statistics_client</h2><br>')
            self.write('<p>会话<br>数量:%s 打开:%s恢复:%s %s <br></p>' %( message[u'net_statistics_client'][u'all_session_count'],message[u'net_statistics_client'][u'all_session_open'],message[u'net_statistics_client'][u'cur_session_recovering'],message[u'net_statistics_client'][u'cur_session_recover_ok']))
            self.write('<p>接收<br>实际:%s/s 线路:%s/s 吞吐:%s io/s <br></p>' % (message[u'net_statistics_client'][u'recv_bytes'],message[u'net_statistics_client'][u'recv_trans_bytes'],message[u'net_statistics_client'][u'recv_counts']))
            self.write('<p>发送<br>实际:%s/s线路:%s/s吞吐:%s io/s<br></p>' % (message[u'net_statistics_client'][u'send_bytes'],message[u'net_statistics_client'][u'send_trans_bytes'],message[u'net_statistics_client'][u'send_counts']))
            self.write('<p>内存<br>内核:%s timer_period:%s <br></p>' % (message[u'net_statistics_client'][u'vm_mem_bytes'],message[u'net_statistics_client'][u'all_session_open']))

            # net_statistics_game
            self.write('<h2>net_statistics_client</h2><br>')
            self.write('<p>会话<br>数量:%s 打开:%s恢复:%s %s <br></p>' %(message[u'net_statistics_game'][u'all_connect_count'],message[u'net_statistics_game'][u'all_connect_open'],message[u'net_statistics_game'][u'cur_connect_recovering'],message[u'net_statistics_game'][u'cur_connect_recover_ok']))
            self.write('<p>接收<br>实际:%s/s 线路:%s/s 吞吐:%s io/s <br></p>' % (message[u'net_statistics_game'][u'recv_bytes'],message[u'net_statistics_game'][u'recv_trans_bytes'],message[u'net_statistics_game'][u'recv_counts']))
            self.write('<p>发送<br>实际:%s/s线路:%s/s吞吐:%s io/s<br></p>' % (message[u'net_statistics_game'][u'send_bytes'],message[u'net_statistics_game'][u'send_trans_bytes'],message[u'net_statistics_game'][u'send_counts']))
            self.write('<p>内存<br>内核:%s timer_period:%s <br></p>' % (message[u'net_statistics_game'][u'vm_mem_bytes'],message[u'net_statistics_game'][u'timer_period']))




            # self.write('<li>gs_id:  %s byte/s</li>' % message)
            self.write('<br><br><li>shadow_room_obj:  %s /s</li>' % message[u"shadow_room_obj"])
            self.write('<li>shadow_player_obj: %s<br></li>' % message[u'shadow_player_obj'])
            self.write('<br><br><li>timer_obj:  %s /s</li>' % message[u"timer_obj"])
            # addr
            # _id
            self.write('<li>时间: %s<br></li>' % message[u'ts_flag'])
            self.write('''</ul></body></html> ''')
        else:
            # Iteration complete
            # self.write('</ul>')
            self.finish()
class monitor_loginserver(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @gen.coroutine
    def get(self):
        """Display all messages."""
        self.write('''<html><head><meta http-equiv="refresh" content="3">
        </head><body><a href="/">返回</a><br>
        ''')
        self.write('<ul>')
        db = self.settings['db']
        cursor = db.monitor_loginserver.find().sort([('_id', 1)]).limit(1)
        while (yield cursor.fetch_next):
            message = cursor.next_object()
            # self.write('<li>%s</li>' % message['msg'])
            self.write('<li>%s</li>' % message)
        # Iteration complete
        self.write('</ul>')
        self.write('''</ul></body></html> ''')
        self.finish()

class MessagesHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @gen.coroutine
    def get(self):
        """Display all messages."""
        self.write('<ul>')
        self.write('<a href="/frontserver">frontserver</a><br>')
        self.write('<a href="/loginserver">loginserver</a><br>')
        self.write('<a href="/transferserver">transferserver</a><br>')
        self.write('<a href="/gameserver">gameserver</a><br>')

        # db = self.settings['db']
        # cursor = db.messages.find().sort([('_id', -1)])
        # while (yield cursor.fetch_next):
        #     message = cursor.next_object()
        #     self.write('<li>%s</li>' % message['msg'])

        # Iteration complete
        self.write('</ul>')
        self.finish()



db = motor.motor_tornado.MotorClient("192.168.1.107",27017).xiangqi_mobile_log

application = tornado.web.Application(
    [
        (r'/', MessagesHandler),
        (r'/frontserver', monitor_frontserver),
        # (r'/gameserver', monitor_gameserver),
        (r'/loginserver', monitor_loginserver),
        # (r'/transferserver', monitor_transferserver)
    ],
    db=db
)

print('Listening on http://localhost:8888')
application.listen(8888)
tornado.ioloop.IOLoop.instance().start()