#!/usr/bin/env perl

sub usage
{
    print <<EOD;
Usage: a2b [-hd|-tcpdump|-gdb]

e.g. echo "0x74 0x65 0x73 0x74 0x0A" | a2b
EOD
    exit 0
}

while (<STDIN>) {
    chomp;
    if ($ARGV[0] eq '-h') {
        &usage();
    } elsif ($ARGV[0] eq '-hd') {
        next if (!s/^[0-9a-f]{8}([0-9a-f\s]+).*/$1/);
    } elsif ($ARGV[0] eq '-tcpdump') {
        next if (!/^\s/);
    } elsif ($ARGV[0] eq '-gdb') {
        s/^0x[0-9a-f]+://;
        s/0x//g;
    } else {
        s/0x//g;
        s/[-.:,]//g;
        s/^\s*//;
    }
    @x = split(/ */);
    while (@x) {
            printf "%c", hex(shift(@x) . shift(@x));
    }
}
