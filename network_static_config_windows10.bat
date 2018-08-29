REM Script must be run as administrator
REM enter interface name in quote
set IFACE_NAME="Wi-Fi"
REM add assigned IP
set IP_ASSIGNED=
set GATEWAY=
set PRIMARY_DNS=
set ALTERNATE_DNS=4.2.2.2
set SUBNET_MASK=
REM set ip, dns and gateway
netsh interface ip set address name=%IFACE_NAME% static %IP_ASSIGNED% %SUBNET_MASK% %GATEWAY%
REM set primary dns
netsh interface ip add dnsservers %IFACE_NAME% %PRIMARY_DNS%
REM set aternative dns
netsh interface ip add dnsservers %IFACE_NAME% %ALTERNATE_DNS% index=2
echo
REM pause until key pressed from user.
pause