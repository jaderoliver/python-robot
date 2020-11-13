#!/usr/bin/env python
# -*- coding: cp1252 -*-
"""
### =============================================
###  PROJECT: Fasenra
###  MODULE: classes
###  DESCRIPTION: Fasenra project classes definition
###  VERSION: 1.0.1
###  DEVELOPER: Bruno Calado
###  TEAM: AVV
###  DATE: 23-01-2019
###  PRE-REQ:
###  Copyright 2017 Altran
### =============================================
"""
 
############################
### --- IMPORTATIONS --- ###
############################

#########################
### --- VARIABLES --- ###
#########################

#############################
### --- ELEMENT CLASS --- ###
#############################

class Element:
    def __init__(self, name, type, locator=None, text=None):
        self.name    = name
        self.id      = locator
        self.txt     = text
        self.type    = type


##########################
### --- PAGE CLASS --- ###
### Contains: Element  ###
##########################

class Page:
    def __init__(self, name):
        self.name   = name
        self.isopen = None
        self.isself = None

    def add(self, name, type, locator, text=None, isopen=False, isself=False):
        if type.lower()=='page':
            element = locator
        else:
            element = Element(name=name, type=type.lower(), locator=locator, text=text)
            if isopen :  self.isopen = element
            if isself :  self.isself = element
        cmd = "self.%s = element" % name
        exec(cmd)
    
        
