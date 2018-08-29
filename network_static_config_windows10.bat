REM Script must be run as administrator
REM enter interface name in quote
set IFACE_NAME="Wi-Fi"
REM add assigned IP instead of 192.168.0.2
set IP_ASSIGNED=192.168.0.2
REM enter gateway here instead of 192.168.0.2
set GATEWAY=192.168.0.1
REM Enter subnet mask instead of 255.255.255.0
set SUBNET_MASK=255.255.255.0
REM enter/change primary dns instead of 8.8.8.8 if require
set PRIMARY_DNS=8.8.8.8
set ALTERNATE_DNS=4.2.2.2
REM set ip, dns and gateway
netsh interface ip set address name=%IFACE_NAME% static %IP_ASSIGNED% %SUBNET_MASK% %GATEWAY%
REM set primary dns
netsh interface ip add dnsservers %IFACE_NAME% %PRIMARY_DNS%
REM set aternative dns
netsh interface ip add dnsservers %IFACE_NAME% %ALTERNATE_DNS% index=2
echo
REM pause until key pressed from user.
pause