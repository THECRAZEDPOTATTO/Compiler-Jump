import pymem
from pymem import Pymem 
import ctypes
import os
import subprocess
os.startfile("notepad")
pm = pymem.Pymem('notepad.exe')
pm.inject_python_interpreter()
shellcode = '''
import os
import pymem
from pymem import Pymem 
os.startfile("calc")
pm = pymem.Pymem('calc')
pm.inject_python_interpreter()
shellcode = """
import os
import pymem
from pymem import Pymem 
os.startfile("cmd")
pm = pymem.Pymem('cmd')
pm.inject_python_interpreter()
shellcode = """
import os
import pymem
from pymem import Pymem 
os.startfile("cmd")
pm = pymem.Pymem('cmd')
pm.inject_python_interpreter()
shellcode = """
import os
import os
import pymem
from pymem import Pymem 
os.startfile("cmd")
pm = pymem.Pymem('cmd')
pm.inject_python_interpreter()
shellcode = """
import os
import os
import pymem
from pymem import Pymem 
os.startfile("cmd")
pm = pymem.Pymem('cmd')
pm.inject_python_interpreter()
shellcode = """
#FINAL CODE HERE & pkgs
"""
pm.inject_python_shellcode(shellcode)
"""
pm.inject_python_shellcode(shellcode)
"""
pm.inject_python_shellcode(shellcode)
"""
pm.inject_python_shellcode(shellcode)
"""
pm.inject_python_shellcode(shellcode)
'''
pm.inject_python_shellcode(shellcode)
