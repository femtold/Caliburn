#
#
#

from __future__ import print_function
import sys


class Logger(object):
    NONE     = 0
    ERROR    = 1
    WARNING  = 2
    INFO     = 3
    TRACE    = 4
    ALL      = 5
    
    _level   = INFO
    levelStr = {
                ALL :    "all",
                TRACE:   "trace",
                INFO:    "info",
                WARNING: "warning",
                ERROR:   "error",
                NONE:    "none"
                }
    
    
    def __init__(self, dest=None):
        self._dest = dest
        
        
    def _print(self, text, end="\n", file=sys.stdout):
        print(text, end=end, file=file)
        
    
    def log(self, level, item):
        if level <= Logger._level:
            if self._dest:
                output = self._dest
            else:
                output = sys.stdout if level>Logger.WARNING else sys.stderr
                
            