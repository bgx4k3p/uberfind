Uberfind
==============
Uberfind is a search tool for finding hardcoded usernames/passwords, encryption keys and other sensitive information inside multiple files. It performs a recursive search for all files within a given path, it can filter files based on the extension and it generates a results file with a number of characters before and after the search string. Parsing trough thousands of files in seconds. 


Arguments
--------------

    $ python uberfind.py -h

    usage: uberfind.py [-h] [-v] [-p PATH] [-k KEYWORDS] [-e EXTENSIONS]
                       [-r RESULTS] [-n CHARS] [-a]
    
    optional arguments:
      -h, --help     show this help message and exit
      -v, --verbose  Enable verbosity
      -p PATH        Specify path to search in
      -k KEYWORDS    Specify keywords to search for
      -e EXTENSIONS  Specify file types to search in
      -r RESULTS     Specify results output file, default 'results.txt'
      -n CHARS       Number of characters to return before and after a keyword
      -a             Search ALL files, no filter


Usage Examples
--------------

Default settings with no arguments - Search recursively in the current folder for keywords 'username' and 'password'. Look inside .dll, .xml, .db, .conf, .ini, .txt, .dat, .vbs, .bat files, then return 50 characters before/after the keyword from any line that contains it with the line number and the name of the file. Results go in 'results.txt' inside the current folder.

    python uberfind.py

Search inside .dll files in c:\Windows folder for keyword 'password' verbosely:

    python uberfind.py -p c:\Windows -e .dll -k password -v

