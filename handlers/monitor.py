# -*- coding: utf-8 -*-
#监控
import tornado.web
import db
import api
import tornado.gen

class MonitorLogin(tornado.web.RequestHandler):

    @tornado.web.authenticated
    def get(self):
        self.render("monitor/login.html", user=self.current_user)

    @tornado.web.authenticated
    @tornado.gen.coroutine
    def post(self):
        cur = yield db.sp_get_loginserver()

        header = []
        for description in cur.description:
            header.append(description[0])
            print cur.description

        data = {"header":header, "table":cur.fetchall()}
        response = api.response(True, data)
        self.write(response)


class MonitorFront(tornado.web.RequestHandler):
    @tornado.web.authenticated
    def get(self):
        self.render("monitor/front.html", user=self.current_user)

    @tornado.web.authenticated
    @tornado.gen.coroutine
    def post(self):
        cur = yield db.sp_get_frontserver()

        header = []
        for description in cur.description:
            header.append(description[0])

        data = {"header":header, "table":cur.fetchall()}
        response = api.response(True, data)
        self.write(response)


class MonitorGame(tornado.web.RequestHandler):
    @tornado.web.authenticated
    def get(self):
        self.render("monitor/game.html", user=self.current_user)

    @tornado.web.authenticated
    @tornado.gen.coroutine
    def post(self):
        cur = yield db.sp_get_gameserver()

        header = []
        for description in cur.description:
            header.append(description[0])

        data = {"header":header, "table":cur.fetchall()}
        response = api.response(True, data)
        self.write(response)


class MonitorTransfer(tornado.web.RequestHandler):
    @tornado.web.authenticated
    def get(self):
        self.render("monitor/transfer.html", user=self.current_user)

    @tornado.web.authenticated
    @tornado.gen.coroutine
    def post(self):
        cur = yield db.sp_get_transferserver()

        header = []
        for description in cur.description:
            header.append(description[0])

        data = {"header":header, "table":cur.fetchall()}
        response = api.response(True, data)
        self.write(response)

