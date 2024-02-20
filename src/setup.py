import cx_Freeze
import sys

base = None
if (sys.platform == "win32"):
    base = "Win32GUI"

executables = [cx_Freeze.Executable("src\main.py", base=base)]

cx_Freeze.setup(
    name="Tetris",
    options={"build_exe": {"packages": ["pygame"]}},
    description="Tetris Game",
    executables=executables
    )