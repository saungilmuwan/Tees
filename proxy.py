import requests
import os
import sys

try:
    while True:
        s = requests.get("https://public.freeproxyapi.com/api/Proxy/Mini")
        if s.status_code == 200:
            res = s.json()
            MODE = 'a' if os.path.isfile(res['type']+"_"+res['proxyLevel']+'.txt') else 'w'

            with open(str(res['type'])+"_"+str(res['proxyLevel'])+'.txt',MODE,encoding='utf-8') as output:
                output.write(str(res['host'])+":"+str(res['port'])+"\n")

            print("Got: "+str(res['host'])+":"+str(res['port']))
        else:
            break
except KeyboardInterrupt:
    quit()
    sys.exit()
