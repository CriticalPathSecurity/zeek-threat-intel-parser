#!/usr/local/bin/python3
# _________        .__  __  .__              .__ __________         __  .__
# \_   ___ \_______|__|/  |_|__| ____ _____  |  |\______   \_____ _/  |_|  |__
# /    \  \/\_  __ \  \   __\  |/ ___\\__  \ |  | |     ___/\__  \\   __\  |  \
# \     \____|  | \/  ||  | |  \  \___ / __ \|  |_|    |     / __ \|  | |   Y  \
#  \______  /|__|  |__||__| |__|\___  >____  /____/____|    (____  /__| |___|  /
#        \/                        \/     \/                    \/          \/
#
# @author      Brandon Cummings <brandon.cummings@criticalpathsecurity.com>
# @copyright   2020 Critical Path Security
# @link        https://www.criticalpathsecurity.com/
# @license     MIT License
#
# This script parses line-separated indicators from an input file and exports
# them to an output file in the intelligence data format. You can either run
# the script manually and enter the required parameters when prompted or pass
# it parameters if you want to automate the process.
#
# Please check the README for complete usage instructions.
#/

import sys, os
from os import path

# There are two ways to use this script; by passing arguments or entering the
# required information manually when prompted. If arguments are used, input
# prompts are suppressed.
def main(args, use_input = True):

    # Strip the filename from the args
    args.pop(0)

    # Check to see if arguments are being passed
    if len(args) > 0:
        use_input = False

        # Check to make sure all arguments are present
        if len(args) < 5:
            print('\n')
            print('Only '+str(len(args))+' arguments were present but 5 are required.')
            print('Please check the README for complete usage instructions.', end='\n\n')
            return

    # If input is True, prompt the user for the required information
    if not use_input:
        indicator_type = args[0]
        source = args[1]
        description = args[2]
        input_file = args[3]
        output_file = args[4]

    # Else, set the required data based on the passed arguments
    else:
        print('\n')
        indicator_type = input('Enter the indicator type : ')
        source = input('Enter the source : ')
        description = input('Enter the description : ')
        input_file = input('Enter the absolute path for the input file : ')
        output_file = input('Enter the absolute path for the output file : ')

    # Check to see if the input file exists
    if not path.exists(input_file):
        print('\n')
        print('Can\'t read from the input file.')
        print('Does it exist? Do you have read permission?', end='\n\n')
        return

    # Try to open the input and output files
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:

            # Write the heading line for the intel feed file
            outfile.write('#fields\tindicator\tindicator_type\tmeta.source\tmeta.do_notice\tmeta.desc\n')

            # For each line in the input file, write a tab-delimited line to the
            # output file formatted
            for line in infile:
                outfile.write(line.strip()+'\tIntel::'+str(indicator_type)+'\t'+str(source)+'\tF\t'+str(description)+'\n')

        infile.close()
        outfile.close()

    except IOError:
        print('\n')
        print('Can\'t write to the output file.')
        print('Do you have write permission for the path specified?', end='\n\n')
        return

    finally:
        print('\n')
        print('Finished!')
        print('You can find your output file here:')
        print(output_file, end='\n\n')
        return

# Execute the main function
if __name__ == '__main__' :
    main(sys.argv)
