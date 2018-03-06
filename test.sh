
test()
{
    echo "check $1"
    ret=`echo "$1" | $cmd`
    if [ ${ret} = "test" ] ; then
        echo OK
    else
        echo NG
    fi
}

if [ -z "$1" ] ; then
    cmd=./a2b.py
else
    cmd=$1
fi

test "74 65 73 74"
test "74657374"
test "7465 7374 "
test "74,65,73,74"
test "74.65.73.74"
test "74:65:73:74"
test "74-65-73-74"
test "0x7465,0x7374"
test "0x74-0x65-0x73-0x74"
test "0x74 0x65 0x73 0x74"

