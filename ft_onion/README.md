# FT_Onion
Create own dark web under onion network

## How to
### Server side
1. Run tor docker server
```bash
make
```
** wait docker startup done **
2. Copy `ONION_SITE` to clipboard

### Client side
1. prepare your host, install revelant package
**Install torify cli**
```bash
apt install -y tor
```

**Download tor browser**
```bash
# https://www.torproject.org/download/
wget https://www.torproject.org/dist/torbrowser/14.0.6/tor-browser-linux-x86_64-14.0.6.tar.xz
```

References:
- [Onion Setup]
- [Onion Client Authorization]
- [Tor Authentication v3]
- [SSH Hardening]

<!-- Link -->
[Onion Setup]: https://community.torproject.org/onion-services/setup/
[Onion Client Authorization]: https://community.torproject.org/onion-services/advanced/client-auth/
[Tor Authentication v3]: https://objsal.medium.com/tor-v3-authentication-1f3fd7192fea
[SSH Hardening]: https://www.cyberciti.biz/faq/how-to-disable-ssh-password-login-on-linux/
