import os

if os.name == 'nt':
    os.add_dll_directory("C:/cygwin64/usr/x86_64-w64-mingw32/sys-root/mingw/bin")
    
from .libHelloWorld import *

del os
del libHelloWorld