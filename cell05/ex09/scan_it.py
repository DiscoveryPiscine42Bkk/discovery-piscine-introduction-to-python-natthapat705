#!/usr/bin/env python3
import sys

# ไม่รวมชื่อโปรแกรมตัวแรก
args = sys.argv[1:]

if len(args) < 2:
    print("none")
else:
    for arg in reversed(args):
        print(arg)