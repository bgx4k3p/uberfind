#!/usr/bin/python
import os
import argparse
import re

__description__ = 'Quick script to parse trough files/folders recursively and search for a keyword.'
__author__ = 'bgx4k3p'
__version__ = '1.3'
__date__ = '2015/10/29'

""" SETTINGS
path - Path to search in recursively, default is the current directory
keywords - Strings to search for
file_ext - Specify file extensions to look in
results - Output file
chars - Number of characters to return before and after a keyword is found in a file
all_files - Look trough all files, no extensions filter
verbose - Enable verbosity
"""


# Function to search for a list of keywords in an input file and write the results to an output file, using Regex
def searcherRegex(outfile, infile, lookup, n, v):

    writepath = True
    counter = 0

    with open(infile, 'r') as temp:
        for num, line in enumerate(temp, 1):

            # Strip whitespace characters at the end of the line
            line = line.rstrip()

            # Check each string on the lookup list
            for string in lookup:

                # Regex search with Ignorecase
                searchObj = re.finditer(string, line, re.M | re.I)

                if searchObj:
                    for match in searchObj:

                        # Find the start index of the keyword
                        start = match.span()[0]

                        # Find the end index of the keyword
                        end = match.span()[1]

                        # Truncate line to get only 'n' characters before and after the keyword
                        if match.span()[0] - n < 0:
                            tmp = line[0:end + n] + '\n'
                        else:
                            tmp = line[start - n:end + n] + '\n'

                        # Write the file path once
                        if writepath:

                            # Verbose
                            if v:
                                print (os.path.realpath(infile))

                            # Write the filename in the results file
                            outfile.write('=== FILE ===>   ' + os.path.realpath(infile) + '\n')
                            writepath = False
                            counter += 1

                        # Write the information and line number to output file
                        outfile.write('--> Found \"' + string + '\": Line ' + str(num) + '\n' + tmp + '\n')

    if counter == 1:
        outfile.write('\n\n')

    return counter


# MAIN
def main():

    # DEFAULT VALUES
    default_keywords = ['password', 'username']
    default_file_ext = ['.dll', '.xml', '.db', '.conf', '.ini', '.txt', '.dat', '.vbs', '.bat', '.yml']

    # Handle arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", action='store', help="Specify path to search in", dest="path", default=os.getcwd())
    parser.add_argument("-k", nargs="*", action='store', help="Specify keywords to search for", dest="keywords", default=default_keywords)
    parser.add_argument("-e", nargs="*", action='store', help="Specify file types to search in", dest="extensions", default=default_file_ext)
    parser.add_argument("-r", action='store', help="Specify results output file, default 'results.txt'", dest="results", default="results.txt")
    parser.add_argument("-n", action='store', help="Number of characters to return before and after a keyword",
                        dest="chars", default=25)
    parser.add_argument("-a", action='store_true', help="Search ALL files, no filter", dest="all_files", default=False)
    parser.add_argument("-v", "--verbose", default=False, action='store_true', help="Enable verbosity", dest="verbose")
    args = parser.parse_args()

    if args.all_files:
        print "Searching ALL files!"

    # Ensure all extensions have a . at the beginning (this removes the . if it's there, then adds it back)
    args.extensions = [".{}".format(ext.replace('.', '')) for ext in args.extensions]

    args.path = os.path.abspath(args.path)

    # Processing
    with open(args.results, 'w') as r:

        print '\n'
        print '$$\   $$\ $$\                           $$$$$$$$\ $$\                 $$\ '
        print '$$ |  $$ |$$ |                          $$  _____|\__|                $$ |'
        print '$$ |  $$ |$$$$$$$\   $$$$$$\   $$$$$$\  $$ |      $$\ $$$$$$$\   $$$$$$$ |'
        print '$$ |  $$ |$$  __$$\ $$  __$$\ $$  __$$\ $$$$$\    $$ |$$  __$$\ $$  __$$ |'
        print '$$ |  $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|$$  __|   $$ |$$ |  $$ |$$ /  $$ |'
        print '$$ |  $$ |$$ |  $$ |$$   ____|$$ |      $$ |      $$ |$$ |  $$ |$$ |  $$ |'
        print '\$$$$$$  |$$$$$$$  |\$$$$$$$\ $$ |      $$ |      $$ |$$ |  $$ |\$$$$$$$ |'
        print ' \______/ \_______/  \_______|\__|      \__|      \__|\__|  \__| \_______|'
        print '\n'
        print "Search path:", args.path
        print "Keywords:", ', '.join(str(keyword) for keyword in args.keywords)
        print "File extensions:", ', '.join(str(ext).replace('.', '') for ext in args.extensions)
        print "Return", args.chars, "characters before and after a keyword.\n"

        # Counter for the number of files containing a keyword
        count = 0

        matched_files = 0

        for root, dirs, files in os.walk(args.path):
            for filename in files:
                fname, ext = os.path.splitext(filename)
                if ext not in args.extensions:
                    continue

                matched_files += 1

                f = os.path.join(root, filename)

                # Perform search
                # for f in files_to_search:
                count += searcherRegex(r, f, args.keywords, args.chars, args.verbose)

        print "Searched through {} files.".format(matched_files)
        print "Found keyword in", count, 'files.'
        print "For more details, check the results file:", os.path.realpath(args.results) + "\n"

if __name__ == '__main__':
    main()
