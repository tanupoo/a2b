#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
import struct

re_def = re.compile("^([\s0-9a-fx,:\.\-]+)$", flags=re.IGNORECASE)
re_hd = re.compile("^[0-9a-f]{5,8}\s([\s0-9a-f]+).*", flags=re.IGNORECASE)
re_tcpdumpx = re.compile("^[^:]+:\s+([\s0-9a-f]+).*", flags=re.IGNORECASE)
re_gdb = re.compile("^\s*0x[a-f0-9]+:\s+([\s0-9a-fx]+).*", flags=re.IGNORECASE)

def usage():
    print('''\
Usage: a2b [-h] [-p]
    it guesses what the text is from either hexdump, tcpdump, gdb, or other.
    e.g. echo "0x74 0x65 0x73 0x74 0x0A" | a2b
    -p: python bytes type.
''')
    exit(0)

f_str = False
if len(sys.argv) == 2:
    if sys.argv[1] == "-h":
        usage()
    elif sys.argv[1] == "-p":
        f_str = True

all_data = bytes()
for line in sys.stdin:
    v = None
    for recom in [re_hd, re_tcpdumpx, re_gdb]:
        r = recom.match(line)
        if r:
            v = r.group(1)
            break
    #
    if v == None:
        r = re_def.match(line)
        if r:
            v = r.group(1)
            if "." in v:
                if True:
                    # "a4.9.0.19"
                    u = 16
                else:
                    # "164.9.0.19"
                    u = 10
                v = "".join(["%02x"%int(i,u) for i in v.split(".")])
    #
    if v:
        v = re.sub(r"[,:\-\.\s\n]", "", v)
        v = v.replace("0x","")
        if len(v)%2 == 0:
            if f_str:
                for i in range(0,len(v),2):
                    all_data += struct.pack("B", int(v[i:i+2],16))
            else:
                for i in range(0,len(v),2):
                    s = struct.pack("B", int(v[i:i+2],16))
                    sys.stdout.buffer.write(s)
# flush all_data
if f_str:
    print(all_data)
