#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from pinpoint.common import PinpointCommonPlugin


class Method(object):

    @staticmethod
    @PinpointCommonPlugin( __name__)
    def static_method(a, b):
        return a + b

    @classmethod
    @PinpointCommonPlugin( __name__)
    def class_method(cls, a, b):
        return cls.__name__ + a + b
