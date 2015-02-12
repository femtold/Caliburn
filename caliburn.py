#
#
#

import argparse
import ConfigParser
import msvcrt
import sys

def print_banner():
    pass

def main():
    
    ###########################
    ##  Add argument parser  ##
    ###########################
    parser = argparse.ArgumentParser(description="Caliburn is an application for performing interaction between PC and a remote embedded system via the RS232 protocol.",
                                     epilog="Please raise any bugs when you encounter and give any suggestion when you need a new feature.")
    
    parser.add_argument("-p", "--port", dest="port", action="store", description="Specify the name of the serial port to use.")
    parser.add_argument("-b", "--baud", dest="baudrate", action="store", type=int, description="Specify the value of the baudrate for the serial port used.")
    parser.add_argument("-f", "--file", dest="config", required=True, action="store", description="Specify the name of the configuration file.")
    parser.add_argument("-o", "--outfile", dest="outfile", action="store")
    parser.add_argument("-v", "--verbose", dest="verbose", action="count")
    parser.add_argument("--echo", dest="echo", action="store_true")
    
    args = parser.parse_args()
    print_banner()
    
    ####################################
    ##  Parse the configuration file  ##
    ####################################
    config = ConfigParser.RawConfigParser()
    try:
        if (not config.read([args.config])):
            print("=== The configuration file is invalid.")
            print("... ... Press any key to exit ... ...")
            msvcrt.getch()
            sys.exit(1)
    except ConfigParser.MissingSectionHeaderError:
        print("=== The contents in the configuration file is invalid.")
        print("--- Press any key to exit ---")
        msvcrt.getch()
        sys.exit(1)

if __name__ == "__main__":
    main()