#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Hao Luo

from datetime import datetime
from threading import Lock

import utils

global inc
inc = 0
lock = Lock()

def log_receive_message(msg, ts):
    global inc
    lock.acquire()
    file = open('front-end/output/'+str(inc)+'.txt', 'w')
    inc = inc +1
    lock.release()
    file.write('{'+'"h":"{timestamp}", "id":"{thread_id}", "s":"{src}", "t":"{msg_type}, "tl":"{localtime}"'.format(
        timestamp=msg.ts,
        thread_id=msg.dest,
        src=msg.src,
        msg_type=msg.msg_type.to_str(),
        localtime=ts,
    )+'}')
    file.close()

def log_enter_cs(ts, node_id, node_list):
    global inc
    lock.acquire()
    file = open('front-end/output/' + str(inc) + '.txt', 'w')
    inc = inc + 1
    lock.release()
    # file.write('{time} {thread_id} {node_list}\n'.format(
    #     time=utils.datetime_to_str(ts),
    #     thread_id=node_id,
    #     node_list=node_list,
    # ))
    file.write('{' + '"h":"{timestamp}", "id":"{thread_id}", "s":"{src}", "t":"{msg_type}, "tl":"{localtime}"'.format(
        timestamp='1000',
        thread_id='5',
        src='4',
        msg_type='INSC',
        localtime='500',
    ) + '}')
    file.close()

def log_receive_message_debug(msg, ts):
    global inc
    lock.acquire()
    file = open('front-end/output/' + str(inc) + '.txt', 'w')
    inc = inc + 1
    lock.release()
    file.write("{dest} {src} {msg_type} {msg_ts} {self_ts}\n".format(
        dest=msg.dest,
        src=msg.src,
        msg_type=msg.msg_type.to_str(),
        msg_ts=msg.ts,
        self_ts=ts,
    ))
    file.close()