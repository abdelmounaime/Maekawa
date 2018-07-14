#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Hao Luo

"""This module contains some utility functions."""
import socket

def datetime_to_str(time):
    """convert python datetime object to a 
    {hour}:{min}:{second}:{millisecond} string format

    """
    return '{hour}:{min}:{second}:{millisecond}'.format(
        hour=time.hour,
        min=time.minute, 
        second=time.second,
        millisecond=str(int(round(time.microsecond / 1000.0))),
        )

def create_server_socket(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', port))
    s.listen(5)
    return s

def create_client_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    return s
