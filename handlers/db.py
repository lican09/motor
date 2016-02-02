import tornado.web

import tornado_mysql
from tornado_mysql import pools
import datetime

# cursorclass=tornado_mysql.cursors.DictCursor,
pool = tornado_mysql.pools.Pool(
    dict(host='192.168.1.156', port=3306, user='root', passwd='toor', db='xq_mobile_monitor'),
    max_idle_connections=1,
    max_open_connections=10,
    max_recycle_sec=3)

def execute(query, params=None):
    return pool.execute(query, params)
    # conn = yield tornado_mysql.connect(host='192.168.1.133', port=3306, user='xiangqiuser', passwd='234567', db='xq_mobile_monitor')
    # cur = conn.cursor()
    # yield cur.execute(query,params)

    # fut = tornado.concurrent.Future()
    # fut.set_result(conn)

    # # print(cur)
    # # for row in cur:
    # #    print(row)
    # # yield cur.close()
    # # conn.close()

def sp_get_loginserver(p_begin_time = None, p_end_time = None):
    today = datetime.date.today()
    lastday = today - datetime.timedelta(days=7)
    if not p_begin_time:
        p_begin_time = lastday.strftime("%Y-%m-%d 00:00:00")
    if not p_end_time:
        p_end_time = today.strftime("%Y-%m-%d 00:00:00")

    query = """
    SELECT
    A.record_time,
    A.login_obj,
    A.timer_obj,

    B.recv_bytes as client_recv_bytes,
    B.recv_counts as client_recv_counts,
    B.recv_trans_bytes as client_recv_trans_bytes,
    B.send_bytes as client_send_bytes,
    B.send_counts as client_send_counts,
    B.send_trans_bytes as client_send_trans_bytes,
    B.vm_mem_bytes as client_vm_mem_bytes,
    B.session_recovering_ as client_session_recovering_,
    B.session_recover_ok_ as client_session_recover_ok_,
    B.all_session_count_ as client_all_session_count_,
    B.all_session_open_ as client_all_session_open_,
    B.timer_period as client_timer_period,

    C.recv_bytes as game_recv_bytes,
    C.recv_counts as game_recv_counts,
    C.recv_trans_bytes as game_recv_trans_bytes,
    C.send_bytes as game_send_bytes,
    C.send_counts as game_send_counts,
    C.send_trans_bytes as game_send_trans_bytes,
    C.vm_mem_bytes as game_vm_mem_bytes,
    C.session_recovering_ as game_session_recovering_,
    C.session_recover_ok_ as game_session_recover_ok_,
    C.all_session_count_ as game_all_session_count_,
    C.all_session_open_ as game_all_session_open_,
    C.timer_period as game_timer_period
    
    FROM loginserver A INNER JOIN tcp_server_statistics B ON A.net_client_id = B.id
    INNER JOIN tcp_server_statistics C ON A.net_game_id = C.id
    WHERE A.record_time >= %(p_begin_time)s AND A.record_time < %(p_end_time)s;
    """
    return pool.execute(query, {"p_begin_time":p_begin_time, "p_end_time":p_end_time})


def sp_get_frontserver(p_begin_time = None, p_end_time = None):
    today = datetime.date.today()
    lastday = today - datetime.timedelta(days=7)
    if not p_begin_time:
        p_begin_time = lastday.strftime("%Y-%m-%d 00:00:00")
    if not p_end_time:
        p_end_time = today.strftime("%Y-%m-%d 00:00:00")
    
    query = """
    SELECT
    A.record_time,
    A.gs_id,
    A.shadow_player_obj,
    A.shadow_room_obj,
    A.player_obj,
    A.timer_obj,

    B.recv_bytes as client_recv_bytes,
    B.recv_counts as client_recv_counts,
    B.recv_trans_bytes as client_recv_trans_bytes,
    B.send_bytes as client_send_bytes,
    B.send_counts as client_send_counts,
    B.send_trans_bytes as client_send_trans_bytes,
    B.vm_mem_bytes as client_vm_mem_bytes,
    B.session_recovering_ as client_session_recovering_,
    B.session_recover_ok_ as client_session_recover_ok_,
    B.all_session_count_ as client_all_session_count_,
    B.all_session_open_ as client_all_session_open_,
    B.timer_period as client_timer_period,

    C.recv_bytes as game_recv_bytes,
    C.recv_counts as game_recv_counts,
    C.recv_trans_bytes as game_recv_trans_bytes,
    C.send_bytes as game_send_bytes,
    C.send_counts as game_send_counts,
    C.send_trans_bytes as game_send_trans_bytes,
    C.vm_mem_bytes as game_vm_mem_bytes,
    C.session_recovering_ as game_session_recovering_,
    C.session_recover_ok_ as game_session_recover_ok_,
    C.all_session_count_ as game_all_session_count_,
    C.all_session_open_ as game_all_session_open_,
    C.timer_period as game_timer_period
    
    FROM frontserver A INNER JOIN tcp_server_statistics B ON A.net_client_id = B.id
    INNER JOIN tcp_server_statistics C ON A.net_game_id = C.id
    WHERE A.record_time >= %(p_begin_time)s AND A.record_time < %(p_end_time)s;
    """
    return pool.execute(query, {"p_begin_time":p_begin_time, "p_end_time":p_end_time})


def sp_get_gameserver(p_begin_time = None, p_end_time = None):
    today = datetime.date.today()
    lastday = today - datetime.timedelta(days=7)
    if not p_begin_time:
        p_begin_time = lastday.strftime("%Y-%m-%d 00:00:00")
    if not p_end_time:
        p_end_time = today.strftime("%Y-%m-%d 00:00:00")
    
    query = """
    SELECT
    A.record_time,
    A.gs_id,
    A.player_obj,
    A.room_obj,
    A.timer_obj,
    A.storage_obj,

    B.recv_bytes as front_recv_bytes,
    B.recv_counts as front_recv_counts,
    B.recv_trans_bytes as front_recv_trans_bytes,
    B.send_bytes as front_send_bytes,
    B.send_counts as front_send_counts,
    B.send_trans_bytes as front_send_trans_bytes,
    B.vm_mem_bytes as front_vm_mem_bytes,
    B.session_recovering_ as front_session_recovering_,
    B.session_recover_ok_ as front_session_recover_ok_,
    B.all_session_count_ as front_all_session_count_,
    B.all_session_open_ as front_all_session_open_,
    B.timer_period as front_timer_period,

    C.recv_bytes as login_recv_bytes,
    C.recv_counts as login_recv_counts,
    C.recv_trans_bytes as login_recv_trans_bytes,
    C.send_bytes as login_send_bytes,
    C.send_counts as login_send_counts,
    C.send_trans_bytes as login_send_trans_bytes,
    C.vm_mem_bytes as login_vm_mem_bytes,
    C.connect_failed as login_connect_failed,
    C.connect_recovering as login_connect_recovering,
    C.connect_recover_ok as login_connect_recover_ok,
    C.all_connect_count as login_all_connect_count,
    C.all_connect_open as login_all_connect_open,
    C.timer_period as login_timer_period
    
    FROM gameserver A INNER JOIN tcp_server_statistics B ON A.net_front_id = B.id
    INNER JOIN tcp_client_statistics C ON A.net_login_id = C.id
    WHERE A.record_time >= %(p_begin_time)s AND A.record_time < %(p_end_time)s;
    """
    return pool.execute(query, {"p_begin_time":p_begin_time, "p_end_time":p_end_time})


def sp_get_transferserver(p_begin_time = None, p_end_time = None):
    today = datetime.date.today()
    lastday = today - datetime.timedelta(days=7)
    if not p_begin_time:
        p_begin_time = lastday.strftime("%Y-%m-%d 00:00:00")
    if not p_end_time:
        p_end_time = today.strftime("%Y-%m-%d 00:00:00")
    
    query = """
    SELECT
    A.record_time,
    A.timer_obj,

    B.recv_bytes as game_recv_bytes,
    B.recv_counts as game_recv_counts,
    B.recv_trans_bytes as game_recv_trans_bytes,
    B.send_bytes as game_send_bytes,
    B.send_counts as game_send_counts,
    B.send_trans_bytes as game_send_trans_bytes,
    B.vm_mem_bytes as game_vm_mem_bytes,
    B.session_recovering_ as game_session_recovering_,
    B.session_recover_ok_ as game_session_recover_ok_,
    B.all_session_count_ as game_all_session_count_,
    B.all_session_open_ as game_all_session_open_,
    B.timer_period as game_timer_period
    
    FROM transferserver A INNER JOIN tcp_server_statistics B ON A.net_game_id = B.id
    WHERE A.record_time >= %(p_begin_time)s AND A.record_time < %(p_end_time)s;
    """
    return pool.execute(query, {"p_begin_time":p_begin_time, "p_end_time":p_end_time})