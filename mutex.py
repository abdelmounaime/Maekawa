#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Hao Luo

from argparse import ArgumentParser
import sys
from threading import Thread
import time

from maekawa import MaekawaMutex


def create_arg_parser():
    parser = ArgumentParser(
        description='A distributed mutual exclusion program '
        'implemented with Maekawa algorithm',
        )
    parser.add_argument(
        '-cs_int',
        action='store',
        dest='cs_int',
        help='time a node spends in the critical section',
        type=int,
        default=5,
        required=False,
        )
    parser.add_argument(
        '-next_req',
        action='store',
        dest='next_req',
        help='time a node waits after exiting the critical section '
        'before it requests another critical section entrance',
        type=int,
        default=7,
        required=False,
        )
    parser.add_argument(
        '-tot_exec_time',
        action='store',
        dest='tot_exec_time',
        help='total execution time for a node',
        type=int,
        default=7,
        required=False,
        )
    parser.add_argument(
        '-option',
        action='store',
        dest='option',
        help='display message log on screen',
        type=int,
        default=0,
        required=False,
        )
    return parser

def run_mutex(cs_int, next_req, option):
    maekawa_mutex = MaekawaMutex(cs_int, next_req, option)
    maekawa_mutex.run()

if __name__ == '__main__':
    cs_int = 5000
    next_req = 10
    tot_exec_time = 3600
    # parser = create_arg_parser()
    # args = parser.parse_args()
    mutex_thread = Thread(
        target=run_mutex,
        args=(cs_int, next_req,1),
        )
    mutex_thread.daemon = True
    mutex_thread.start()
    time.sleep(tot_exec_time)
