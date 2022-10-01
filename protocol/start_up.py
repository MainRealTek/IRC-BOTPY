from os import system

class up_start(object):
    def __init__(self,name_reg,cmd)->None:
        self.name_reg = name_reg
        self.cmd = cmd
        try:
            self.add_startup(self.name_reg,self.cmd)
            return None
        except Exception:
            pass

    def add_startup(name_reg,cmd):
        try:
            system('powershell.exe New-ItemProperty -Path HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run -Name '+name_reg+' -PropertyType String -Value '+cmd+' -Force')
        except:
            pass

