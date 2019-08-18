import sys
if len(sys.argv)!=3:
    print "Usage: tcpPing <IP>\n eg: tcpPing 192.168.1.1 80"
    sys.exit(1)

from scapy.all import sr,IP,TCP
ans,unans=sr(IP(dst=sys.argv[1])/TCP(dport=int(sys.argv[2]),flags="S"))
print ans
for snd,rcv in ans:
    print rcv.sprintf("%IP.src% is alive")