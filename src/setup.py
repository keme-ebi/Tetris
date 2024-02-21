"""setup module to create an executable game file"""

import cx_Freeze
import sys

# set base to None to avoid console opening in the background
base = None
if (sys.platform == "win32"):
    base = "Win32GUI"

# the file to execute
executables = [cx_Freeze.Executable("src\main.py", base=base)]

# setup
cx_Freeze.setup(
    name="Tetris",
    options={"build_exe": {"packages": ["pygame"]}},
    description="Tetris Game",
    executables=executables
    )