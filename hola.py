#!/usr/bin/python
# -*- coding: utf-8 -*-

import webapp
import aleat
import suma

class hola(webapp.app):
    def parse(self, request, rest):
        return None

    def process(self, parsedRequest):
        return("200 ok", "<html><body><h1>Hola!!</h1>")


class adios(webapp.app):
    def parse(self, request, rest):
        return None

    def process(self, parsedRequest):
        return("200 ok", "<html><body><h1>Adios!!</h1>")

if _name_ == "__main__":
    hola = hola()
    adios = adios()
    aleat = aleat.aleat()
    suma = suma.suma()
    classapps = {"/hola": hola, "/resta": suma, "/adios": adios, "/aleat": aleat, "/suma": suma}
    try:
        testWebApp = webapp.webApp("localhost", 1234, classapps)
    except KeyboardInterrupt:
        print "Key board interrupt"
