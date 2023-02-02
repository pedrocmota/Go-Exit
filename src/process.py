import win32gui, win32process, psutil
import time
from configs import readConfigs

def getActiveProcess():
  try:
    pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())
    name = psutil.Process(pid[-1]).name()
    configs = readConfigs()
    excludes = configs["exclude"]
    if name in excludes:
      return None
    return {
      "pid": pid[-1],
      "name": psutil.Process(pid[-1]).name()
    }
  except:
    return None

def killProcess(pid):
  try:
    process = psutil.Process(pid)
    process.kill()
  except:
    pass

def isRunning():
  processes = list(p.name() for p in psutil.process_iter())
  count = processes.count("Go Exit.exe")
  return count > 2