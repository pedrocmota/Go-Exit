import json
from os import path
import os
import ctypes
from tkinter import messagebox

defaultConfigs = {
  "shortcut": "<cmd_l>+<alt>+c",
  "exclude": [
    "explorer.exe"
  ]
}

configFileLocation = path.expandvars(r'%APPDATA%\goexit\configs.json')
shortcutFileLocation = path.expandvars(r'%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup')

def firstRun():
  return not path.exists(configFileLocation)

def writeDefaultConfigs():
  os.makedirs(os.path.dirname(configFileLocation), exist_ok=True)
  with open(configFileLocation, "w") as f:
    json.dump(defaultConfigs, f)

def readConfigs():
  try:
    with open(configFileLocation, "r") as f:
      return json.load(f)
  except:
    writeDefaultConfigs()
    return defaultConfigs

def openConfig():
  os.startfile(configFileLocation)

def isAdmin():
  try:
    is_admin = (os.getuid() == 0)
  except AttributeError:
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
  return is_admin