from infi.systray import SysTrayIcon
from configs import openConfig
import os
import sys

def resource_path(relative_path):
  if hasattr(sys, '_MEIPASS'):
     return os.path.join(sys._MEIPASS, relative_path)
  return os.path.join(os.path.abspath("."), relative_path)

def createTray():
  def clickConfig(systray):
    openConfig()
  def close(systray):
    os._exit(1)
  menu_options = (("Configurações", None, clickConfig),)
  systray = SysTrayIcon(resource_path('icon.ico'), "Go Exit 1.0", menu_options, on_quit=close)
  systray.start()