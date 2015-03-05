#!/usr/bin/python
# -*- coding: utf-8 -*-


import random, webapp


class aleat(webapp.app):
    def parse(self, request, rest):
        return None

    def process(self, parsedRequest):
        return("200 ok", ("<html><body>Hola."
                          "<a href=" + "/aleat/" +
                          str(random.randint(0, 10000000)) +
                          ">Dame Otra!!" +
                          "</p>" +
                          "</body></html>" +
                          "\r\n"))
