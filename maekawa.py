#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Hao Luo

import config
from node import Node


class MaekawaMutex(object):
    """Class that implements and runs Maekawa mutual exclusion algorithm"""
    def __init__(self, cs_int, next_req, option):
        Node.CS_INT = cs_int
        Node.NEXT_REQ = next_req
        Node.OPTION = option
        self._nodes = [Node(i) for i in xrange(config.NUM_NODE)]

    def _build_connection(self):
        for node in self._nodes:
            node.build_connection(config.NUM_NODE)

    def run(self):
        self._build_connection()
        for node in self._nodes:
            node.run()
