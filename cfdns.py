## CFBypass DNS Method v2.BETA
# Coded 6/10/19
# Inspired by CloudSearch.cf
# Author = SmallDoink
# Date = 6/10/19
# Version = v2.BETA
# Updated: Added DNS Method
# Imports
import os
import socket
import dns.resolver
# End Imports
# Start Setup
os.system('clear')
cfdns = dns.resolver.Resolver()
os.system('clear')
class c:
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
        white='\033[0m'
        
i = raw_input(c.orange + "Wesbite> " + c.white)
meth = raw_input(c.orange + "Method> " + c.white)
if meth == "1":
    site = "i"
    bpip = cfdns.query(i, "A")
    for rdata in bpip:
        print"IP Behind CloudFlare"
        print rdata

elif meth == "2":
    site = "i"
    ip = socket.gethostbyname('ssh.'+i)
    print"IP Behind Cloudflare - "+ip
else:
    print"[!] Error | Please use a listed method"

