# -*- coding: utf-8 -*-
import tornado.web
import tornado.gen
import db

#验证用户是否登录
def get_current_user(self):
    return self.get_secure_cookie('user')
tornado.web.RequestHandler.get_current_user = get_current_user

#登录处理
class Login(tornado.web.RequestHandler):
    def get(self):
        self.render("login.html")

    @tornado.gen.coroutine
    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")

        query = "SELECT * FROM user WHERE username=%(username)s AND password=%(password)s"
        cur = yield db.execute(query, {"username":username, "password":password})
        if cur.fetchone():
            self.set_secure_cookie("user", username, expires_days=None)
        self.redirect(self.get_argument("next", "/"))

#登出，清空cookie跳转到首页
class Logout(tornado.web.RequestHandler):
    @tornado.web.authenticated
    def get(self):
        self.clear_all_cookies()
        self.redirect("/")