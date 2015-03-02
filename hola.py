#!/usr/bin/python
# -*- coding: utf-8 -*-


class hola:
    def parse(self, request, rest):
        return None

    def process(self, parsedRequest):
        return("200 ok", "<html><body><h1>Hola!!</h1>")


class adios:
    def parse(self, request, rest):
        return None

    def process(self, parsedRequest):
        return("200 ok", "<html><body><h1>Adios!!</h1>")
