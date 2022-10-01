from pywifi import iface
from secrets import token_hex



class os_get(object):
    def __init__(self) -> None:
        pass
        

    def select_name(self):
        name = ''
        try:
            if iface.platform.platform().split('-')[0] == 'Windows':
                name+='Win-'
            if iface.platform.platform().split('-')[0] == 'Linux':
                name+='Linux-'

            ax = iface.platform.version().split('.')[0]+'-';name+=ax

            ar = iface.platform.uname()[5].split(' ')[0]+'-';name+=ar
    
            name+=token_hex(nbytes=3)
        
            return str(name)

        except Exception or OSError:
            return str('NONE-'+token_hex(nbytes=3))