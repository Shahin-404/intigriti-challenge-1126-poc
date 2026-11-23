import struct
from pathlib import Path

SOURCE_FILE = Path("help_fixed.bin")
OUTPUT_FILE = Path("help_flag_duplicate.bin")
SIGN_OFFSET = 0x346
PROGRAM_SIZE = 424

original = SOURCE_FILE.read_bytes()

program = b">" * 256 + b".>" * 80 + b"."
if len(program) > PROGRAM_SIZE:
    raise ValueError("Brainfuck program exceeds expected DATA size")
program += b"\x00" * (PROGRAM_SIZE - len(program))

duplicate_data = b"w" + struct.pack("<I", len(program)) + b"DATA" + program
modified = original[:SIGN_OFFSET] + duplicate_data + original[SIGN_OFFSET:]
OUTPUT_FILE.write_bytes(modified)

print("Original bundle size:", len(original))
print("Program length:", len(program))
print("Duplicate DATA length:", len(duplicate_data))
print("Modified bundle size:", len(modified))
print("SHA256:", __import__("hashlib").sha256(modified).hexdigest())
print("Output:", OUTPUT_FILE)
