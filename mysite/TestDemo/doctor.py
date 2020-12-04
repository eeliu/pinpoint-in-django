#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from TestDemo.person import Person

from pinpoint.common import PinpointCommonPlugin


class Doctor(Person):

    @PinpointCommonPlugin("Doctor.other")
    def other(self):
        return "Doctor not eating!"
