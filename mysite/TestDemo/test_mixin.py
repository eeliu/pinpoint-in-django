#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from pinpoint.common import PinpointCommonPlugin


class Animal(object):
    @PinpointCommonPlugin( __name__)
    def animal_func(self):
        return " and I am an animal"


class ThinkMixIn(object):
    @PinpointCommonPlugin( __name__)
    def think_func(self):
        return " and I can think"


class Human(Animal, ThinkMixIn):
    @PinpointCommonPlugin( __name__)
    def human_func(self):
        return "I am a human"