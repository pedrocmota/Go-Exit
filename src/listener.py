from pynput import keyboard
from configs import readConfigs
from process import getActiveProcess, killProcess

def listener():
  configs = readConfigs()
  with keyboard.GlobalHotKeys({
    configs["shortcut"]: onAction
  }) as h:
    h.join()

def onAction():
  process = getActiveProcess()
  if process != None:
    killProcess(process["pid"])