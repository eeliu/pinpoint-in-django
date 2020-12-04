#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from pinpoint.common import PinpointCommonPlugin


class Person(object):
    @PinpointCommonPlugin("Person")
    def eat(self):
        return "father eating!"
