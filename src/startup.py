import os
import sys
import inspect
from os import path

tempXMLFile = path.expandvars(r'%APPDATA%\goexit\temp.xml')

def prepareXML():
  if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(os.path.realpath(sys.executable))
  elif __file__:
    application_path = os.path.dirname(__file__)
  xml = inspect.cleandoc(f'''
    <?xml version="1.0" encoding="UTF-16"?>
    <Task version="1.4"
      xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
      <Triggers>
        <LogonTrigger>
          <Enabled>true</Enabled>
        </LogonTrigger>
      </Triggers>
      <Principals>
        <Principal id="Author">
          <LogonType>InteractiveToken</LogonType>
          <RunLevel>HighestAvailable</RunLevel>
        </Principal>
      </Principals>
      <Settings>
        <MultipleInstancesPolicy>IgnoreNew</MultipleInstancesPolicy>
        <DisallowStartIfOnBatteries>true</DisallowStartIfOnBatteries>
        <StopIfGoingOnBatteries>true</StopIfGoingOnBatteries>
        <AllowHardTerminate>true</AllowHardTerminate>
        <StartWhenAvailable>false</StartWhenAvailable>
        <RunOnlyIfNetworkAvailable>false</RunOnlyIfNetworkAvailable>
        <IdleSettings>
          <StopOnIdleEnd>true</StopOnIdleEnd>
          <RestartOnIdle>false</RestartOnIdle>
        </IdleSettings>
        <AllowStartOnDemand>false</AllowStartOnDemand>
        <Enabled>true</Enabled>
        <Hidden>false</Hidden>
        <RunOnlyIfIdle>false</RunOnlyIfIdle>
        <DisallowStartOnRemoteAppSession>false</DisallowStartOnRemoteAppSession>
        <UseUnifiedSchedulingEngine>true</UseUnifiedSchedulingEngine>
        <WakeToRun>false</WakeToRun>
        <ExecutionTimeLimit>PT0S</ExecutionTimeLimit>
        <Priority>7</Priority>
      </Settings>
      <Actions Context="Author">
        <Exec>
          <Command>"{application_path}\Go Exit.exe"</Command>
        </Exec>
      </Actions>
    </Task>
    '''
  )
  if not os.path.exists(tempXMLFile):
    with open(tempXMLFile, "w") as f:
      f.write(xml)
  os.system('schtasks.exe /Create /XML ' + tempXMLFile + ' /tn "Go Exit"')
  #os.remove(tempXMLFile)