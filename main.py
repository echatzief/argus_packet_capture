import sys

for line in sys.stdin:
  if "Dur" not in line:
    print(line)
