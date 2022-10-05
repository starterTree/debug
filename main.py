#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Plugin import Plugin
from pyfx import Controller
from pyfx.model import DataSourceType
import logging
from rich.pretty import pprint

dataYaml = """
debug:
  view_config:
    debug : "view config"
  readDict:
    readDict: "read_dict"
"""



def runInMenu(args):
# data is the JSON data to be rendered in the TUI
# only supports dict, list and primitive variable
    #cmd = args["objet"]["cmd"]
    for key in args:
        print(key)
    if args["objet"]["debug"] == "view config":
        Controller().run(DataSourceType.VARIABLE, args["self"])

def register(args):
    #logging.basicConfig(filename='/tmp/st.log', level=logging.DEBUG, filemode='w')
    #logging.debug("loadData(configFile="+str(configFile)+", data="+str(starterTreeDATA))
    #pprint(starterTreeDATA["menu_completion"])
    #logging.debug("execMainPromptSession(data=" + str(starterTreeDATA) + ", promptTitle=" + str(promptTitle))
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")


Plugin(namePlugin="debug", titleName="DEBUG", afterRegister=register, runInMenu=runInMenu, dataYaml=dataYaml)
Plugin(namePlugin="debugSettings", titleName="", customRegister=register, runInMenu=None)

