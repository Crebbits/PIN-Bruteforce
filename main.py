#!/usr/bin/env python3
import subprocess
import time
import sys

# 3 seconds to alt-tab to correct window after running
time.sleep(3)

for i in range(900,10000):

    pin = str(i).zfill(4)
    # type out the text
    subprocess.call(["C:\\temp\\xdotool.exe", "key", pin])
    # increase or decrease the time below to type slower or faster
    time.sleep(0.40)
