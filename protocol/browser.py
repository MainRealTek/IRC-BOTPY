from os import system

class open_page(object):
    def __init__(self,web_page):
        self.web_page = web_page
        try:
            if self.run_page_main(self.web_page) == True:
                return None
        except Exception:
            pass

    def main_firefox(self,url):
        try:
            system("powershell.exe cd 'C:\Program Files\Mozilla Firefox\';start firefox.exe "+url)
        except OSError or Exception:
            pass


    def main_edge(self,url):
        try:
            system("powershell.exe  cd 'C:\Program Files (x86)\Microsoft\Edge\Application\';start msedge.exe "+url)
        except OSError or Exception:
            pass



    def main_chrome(self,url):
        try:
            system("powershell.exe cd 'C:\Program Files\Google\Chrome\Application\';start chrome.exe "+url)
        except OSError or Exception:
            pass

    def search_chrome(self,url):
        try:
            self.main_chrome(url)
            return True
        except:
            return False



    def search_edge(self,url):
        try:
            self.main_edge(url)
            return True
        except OSError or Exception:
            return False

    def search_firefox(self,url):
        try:
            self.main_firefox(url)
            return True
        except OSError or Exception:
            return False


    def run_page_main(self,url):
        while True:
            if self.search_edge(url) == True:
                break
            if self.search_edge(url) == False:
                pass
            if self.search_chrome(url) == True:
                break
            if self.search_chrome(url) == False:
                pass
            if self.search_firefox(url) == True:
                break
            if self.search_firefox(url) == False:
                pass

            break
        return True


ii = open_page('gg')