from configs import readConfigs, isAdmin, firstRun
from tray import createTray
from listener import listener
from sys import exit
from startup import prepareXML
from process import isRunning
from tkinter import messagebox

def init():
  createTray()
  listener()

if __name__ == "__main__":
  if(isRunning()):
    exit()
  if not isAdmin():
    messagebox.showerror('Go Exit - Erro', 'Go Exit deve ser executado como administrador!')
  else:
    if(firstRun()):
      res = messagebox.askyesno('Go Exit', 'Deseja iniciar o Go Exit automaticamente ao iniciar o Windows?')
      if res:
        readConfigs()
        prepareXML()
    init()