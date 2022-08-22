import sims4
import ctypes
import sys
    
def allocconsole():
    ctypes.windll.kernel32.AllocConsole()
    sys.stdout = open("CONOUT$","w")
    sys.stderr = open("CONOUT$","w")

allocconsole()
