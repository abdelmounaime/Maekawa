#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Hao Luo

"""This module implements message passing functionality.

classes:
    MessageEncoder: encode a Message object to json
    MessageDecoder: decode a Message object from json_string
    Message: media of nodes communication

"""
import json

from enum_type import MSG_TYPE


class MessageEncoder(json.JSONEncoder):
    def encode(self, obj):
        obj_dict = dict()
        obj_dict['msg_type'] = int(obj.msg_type)
        obj_dict['src'] = obj.src
        obj_dict['dest'] = obj.dest
        obj_dict['ts'] = obj.ts
        obj_dict['data'] = obj.data
        return super(MessageEncoder, self).encode(obj_dict)


class MessageDecoder(json.JSONDecoder):
    def decode(self, json_string):
        parsed_dict = super(MessageDecoder, self).decode(json_string)
        return Message(MSG_TYPE(parsed_dict['msg_type']),
                       parsed_dict['src'], 
                       parsed_dict['dest'],
                       parsed_dict['ts'],
                       parsed_dict['data'])


class Message(object):
    """Class that implements the media of nodes communication.

    Attributes:
        msg_type (MSG_TYPE): type of message
        src (int): source of message
        dest (int): destination of message
        ts (int): Lamport timestamp of message
        data (str): other information of message

    """
    def __init__(self,
            msg_type=None,
            src=None,
            dest=None,
            ts=None,
            data=None,
            ):
        self.msg_type = msg_type
        self.src = src
        self.dest = dest
        self.ts = ts
        self.data = data

    def __json__(self):
        return dict(msg_type=self.msg_type, 
            src=self.src,
            dest=self.dest, 
            ts=self.ts, 
            data=self.data)

    def __cmp__(self, other):
        if self.ts != other.ts:
            return cmp(self.ts, other.ts)
        else:
            return cmp(self.src, other.src)

    def set_type(self, msg_type):
        self.msg_type = msg_type

    def set_src(self, src):
        self.src = src

    def set_dest(self, dest):
        self.dest = dest

    def set_ts(self, ts):
        self.ts = ts

    def set_data(self, data):
        self.data = data

    def to_json(self):
        return json.dumps(self, cls=MessageEncoder)

    @staticmethod
    def to_message(json_str):
        return json.loads(json_str, cls=MessageDecoder)
