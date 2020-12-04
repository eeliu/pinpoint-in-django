#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from pinpoint.common import PinpointCommonPlugin


class Private(object):
    @PinpointCommonPlugin( __name__)
    def __private_func(self, arg):
        return "Private called by " + arg

    @PinpointCommonPlugin( __name__)
    def common_func(self, name):
        r = self.__private_func(name)
        return r
