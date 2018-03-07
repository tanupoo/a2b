
test()
{
    echo "check $2"
    ret=`echo "$2" | $cmd`
    if [ ${ret} = "$1" ] ; then
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

test "test" "74 65 73 74"
test "test" "74657374"
test "test" "7465 7374 "
test "test" "74,65,73,74"
test "test" "74.65.73.74"
test "test" "74:65:73:74"
test "test" "74-65-73-74"
test "test" "0x7465,0x7374"
test "test" "0x74-0x65-0x73-0x74"
test "test" "0x74 0x65 0x73 0x74"

#test "60 0a 97 3e"

