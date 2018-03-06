#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re

re_def = re.compile("^([\s0-9a-fx,:\.\-]+)$", flags=re.IGNORECASE)
re_hd = re.compile("^[0-9a-f]{3,8}\s([\s0-9a-f]+).*", flags=re.IGNORECASE)
re_tcpdump = re.compile("^\s+([\s0-9a-f]+).*", flags=re.IGNORECASE)
re_gdb = re.compile("^0x[a-f0-9]+:\s+([\s0-9a-fx]+).*", flags=re.IGNORECASE)

def usage():
    print('''\
Usage: a2b [-h]
    it guesses what the text is from either hexdump, tcpdump, gdb, or other.
    e.g. echo "0x74 0x65 0x73 0x74 0x0A" | a2b
''')
    exit(0)

if len(sys.argv) == 2 and sys.argv[1] == "-h":
    usage()

for line in sys.stdin:
    v = None
    for recom in [re_hd, re_tcpdump, re_gdb]:
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
        v = re.sub(r"([,:\-\.\s\n]|0x)", "", v)
        if len(v)%2 == 0:
            for i in range(0,len(v),2):
                print(chr(int(v[i:i+2],16)), end="")
