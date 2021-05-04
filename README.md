# RCShell
A reverse Shell Implementation in Python using websockets, RCShell stands for Remote Clean Shell

OpenSSL is used to create the certificates/private key for the TLS sockets

This command can make those quickly

```openssl req -x509 -sha256 -nodes -newkey rsa:2048 -keyout key.pem -out cert.pem```

all the options are usually left on default except for the Common Name ("localhost" for local testing)
