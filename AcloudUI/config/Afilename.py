from datetime import datetime

def filenamechange(kzm):
    dn = datetime.now()
    oldname = dn.strftime('%Y%m%d%H%M%S%f')
    return oldname+kzm