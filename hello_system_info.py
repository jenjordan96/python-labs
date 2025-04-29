# hello_system_info.py

import platform
import sys

print("Hello, World!")
print(f"Operating System: {platform.system()} {platform.release()}")
print(f"Python Version: {sys.version}")

