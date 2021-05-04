# RCShell
A reverse Shell Implementation in Python using websockets, RCShell stands for Remote Clean Shell

OpenSSL is used to create the certificates/private key for the TLS sockets

This command can make those quickly

```openssl req -x509 -sha256 -nodes -newkey rsa:2048 -keyout key.pem -out cert.pem```

all the options are usually left on default except for the Common Name ("localhost" for local testing)

in order to remotelly control computers you need to setup the server
on a command and controll computer with ports open/forwarded on it's public IP 

The following illustration shows the default setup of the system

![alt text](https://github.com/Trojanzaro/RCShell/blob/main/network_setup.png?raw=true)

PLEASE USE RESPONSIBLY, I AIN'T RESPONSIBLE IF YOU GET YOUR ASS KICKED =)
