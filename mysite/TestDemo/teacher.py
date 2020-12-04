#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from TestDemo.person import Person

from pinpoint.common import PinpointCommonPlugin


class Teacher(Person):

    @PinpointCommonPlugin("Teacher.eat")
    def eat(self):
        return super().eat()+"Teacher eating too!"
