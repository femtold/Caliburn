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
        
        
    def _print(self, text, end="\n", file_=sys.stdout):
        print(text, end=end, file=file_)
        
    
    def log(self, level, item):
        if level <= Logger._level:
            if self._dest:
                output = self._dest
            else:
                output = sys.stdout if level>Logger.WARNING else sys.stderr
                
            self._print("--- {0:<7} - ".format(self.levelStr[level].upper()), end="", file_=output)
            self._print(str(item).strip("\r\n"), file_=output)
            
    def trace(self, *args):
        self.log(Logger.TRACE, *args)
    
    def info(self, *args):
        self.log(Logger.INFO, *args)
    
    def warning(self, *args):
        self.log(Logger.WARNING, *args)
    
    def error(self, *args):
        self.log(Logger.ERROR, *args)
    
    def getLevel(self):
        return Logger._level
    
    def setLevel(self, level):
        Logger._level = level
        
        
class ANSIColors(object):
    purple    = "\033[35m"
    blue      = "\033[34m"
    yellow    = "\033[35m"
    green     = "\033[32m"
    red       = "\033[31m"
    color_off = "\033[0m"
    
    
class ColorLogger(Logger):
    colormap = {Logger.TRACE   : ANSIColors.purple,
                Logger.INFO    : ANSIColors.blue,
                Logger.WARNING : ANSIColors.yellow,
                Logger.ERROR   : ANSIColors.red
                }
    
    def log(self, level, item):
        if level <= Logger._level:
            output = level > Logger.WARNING and sys.stdout or sys.stderr
            self._print("--- {0}{1:<7}{2} -".format(self.colormap[level], Logger.levelStr[level].upper(), ANSIColors.color_off), end="", file_=output)
            self._print(str(item).strip('\r\n'), file=output)
            
            