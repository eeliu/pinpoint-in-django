#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from TestDemo.person import Person

from pinpoint.common import PinpointCommonPlugin


class Student(Person):
    @PinpointCommonPlugin("Student.eat")
    def eat(self):
        return "Student eating"
