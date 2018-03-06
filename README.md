a2b
===

a hex string to binary converter in perl and python.

## usage

    a2b [-hd|-tcpdump|-gdb|-h]

for example,

    % echo "74 65 73 74 0A" | ./a2b
    test

## string format

any combination of 1-byte hex string.
the following delimiters are acceptable.

    . (priod)
    , (comma)
    - (hyphen)
    : (colon)

e.g. the followings are going to be all same output.

    74 65 73 74 0A
    746573740A
    7465 7374 0A
    74.65.73.74.0A
    74:65:73:74:0A
    74-65-73-74-0A
    0x7465,0x7374,0x0A
    0x74-0x65-0x73-0x74-0x0A

## hexdump output

the -hd option specify the input is the output of hexdump(1)
like below:

    % hexdump -C test.txt
    00000000  30 30 30 31 30 32 30 33  30 34 30 35 30 36 30 37  |0001020304050607|
    00000010  30 38 30 39 30 61 30 62  30 63 30 64 30 65 30 66  |08090a0b0c0d0e0f|
    00000020  31 30 31 31 31 32 31 33  31 34 31 35 31 36 31 37  |1011121314151617|
    00000030  31 38 31 39 31 61 31 62  31 63 31 64 31 65 31 66  |18191a1b1c1d1e1f|
    00000040  32 30 32 31 32 32 32 33  32 34 32 35 32 36 32 37  |2021222324252627|

## tcpdump output

the -hd option specify the input is the output of tcpdump(1)
like below:

    % tcpdump -sx 1500 -nqti lnc0
    92.168.246.128.4158 > 203.178.141.195.110: tcp 0 (DF)
                            4500 003c 7474 4000 4006 b5a8 c0a8 f680
                            cbb2 8dc3 103e 006e e8c8 6f7c 0000 0000
                            a002 e000 5204 0000 0204 05b4 0103 0300
                            0101 080a 05ee 9984 0000 0000

## dgb output

the -gdb option specify the input is the output of the command x of gdb(1)
like below:

    (gdb) x/128b &ac
    0xbfbff328:     0x01    0x00    0x00    0x00    0x70    0xf3    0xbf    0xbf
    0xbfbff330:     0x78    0xf3    0xbf    0xbf    0x68    0xf3    0xbf    0xbf
    0xbfbff338:     0x82    0xa7    0x04    0x08    0xd3    0xb3    0x04    0x08
    0xbfbff340:     0x2c    0x3f    0x08    0x08    0x00    0x00    0x00    0x00
    0xbfbff348:     0x00    0x00    0x00    0x00    0x00    0x00    0x00    0x00
    0xbfbff350:     0x64    0xf3    0xbf    0xbf    0x00    0x00    0x00    0x00
