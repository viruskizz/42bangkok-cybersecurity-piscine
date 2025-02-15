
### Client
client on listening `netcat` on port 4242
```bash
nc -l -p 4242
```

### Server
server send message to client on `netcat` port 4242
```bash
nc client 4242
```


<!-- Link -->
[arp-poisoning]: https://www.thehacker.recipes/ad/movement/mitm-and-coerced-authentications/arp-poisoning

https://medium.com/@ravisinghmnnit12/how-to-do-man-in-the-middle-attack-mitm-with-arp-spoofing-using-python-and-scapy-441ee577ba1b