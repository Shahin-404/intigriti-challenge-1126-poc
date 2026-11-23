Intigriti Challenge 1126 PoC package

Files:
- help_fixed.bin: original uploaded bundle used as input.
- create_bundle.py: regenerates help_flag_duplicate.bin.
- help_flag_duplicate.bin: generated modified bundle.
- exploit.py: sends the bundle to the challenge endpoint.

Run from this directory:
  python3 create_bundle.py
  python3 exploit.py
