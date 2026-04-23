TEMPLATE_FILE = "modifiedcode.asm"
OUTPUT_FILE   = "shellcode.asm"
XOR_KEY = 0x41


def prepare_command(cmd: str):
    cmd_bytes = cmd.encode("ascii")

    if b"\x00" in cmd_bytes:
        raise ValueError("Command darf keine Nullbytes enthalten")

    patched = cmd_bytes[:-1] + bytes([cmd_bytes[-1] ^ XOR_KEY])
    xor_offset = len(cmd_bytes) - 1

    db_string = '"' + patched.decode("latin1") + '"'

    return xor_offset, db_string


def main(command: str):
    with open(TEMPLATE_FILE, "r") as f:
        asm = f.read()

    xor_offset, db_string = prepare_command(command)

    asm = asm.replace("{{XOR_OFFSET}}", str(xor_offset))
    asm = asm.replace("{{COMMAND_BYTES}}", db_string)

    with open(OUTPUT_FILE, "w") as f:
        f.write(asm)

    print(f"[+] Command       : {command}")
    print(f"[+] XOR offset    : {xor_offset}")
    print(f"[+] Output written: {OUTPUT_FILE}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} \"<command>\"")
        sys.exit(1)

    main(sys.argv[1])