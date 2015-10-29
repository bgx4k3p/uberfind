Uberfind
==============
Uberfind is a search tool for finding hardcoded usernames/passwords, encryption keys and other sensitive information inside multiple files within a given path. It can parse all files recursively, or search based on file extensions. The output text file contains file names, line numbers and a specified number of characters before and after all instances of the searched keywords. Added support for accepting comma separated keywords and file extensions as arguments. The parsing is via case-insensitive regex, which allows for catching variations of the keywords. 


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

Default settings, no arguments: Search recursively in the current folder for keywords 'username' and 'password'. Look inside .dll, .xml, .db, .conf, .ini, .txt, .dat, .vbs, .bat, .yml files, then return 25 characters before/after each instance of the keyword from any line that contains it with the line number and the name of the file. Results go in 'results.txt' inside the current folder.

    $ python uberfind.py

Search inside **.dll** files in **c:\Windows** folder for keyword **'password'** verbosely:

    $ python uberfind.py -p c:\Windows -e .dll -k password -v

Sample Output
--------------
Search inside **.yml**, **.db** and **.conf** files for the keywords **'user'** and **'password'** in the given path **/usr/local/share/metasploit-framework/**

    $ python uberfind.py -p /usr/local/share/metasploit-framework/ -k password,user -e yml,db,conf -v
        
    $$\   $$\ $$\                           $$$$$$$$\ $$\                 $$\
    $$ |  $$ |$$ |                          $$  _____|\__|                $$ |
    $$ |  $$ |$$$$$$$\   $$$$$$\   $$$$$$\  $$ |      $$\ $$$$$$$\   $$$$$$$ |
    $$ |  $$ |$$  __$$\ $$  __$$\ $$  __$$\ $$$$$\    $$ |$$  __$$\ $$  __$$ |
    $$ |  $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|$$  __|   $$ |$$ |  $$ |$$ /  $$ |
    $$ |  $$ |$$ |  $$ |$$   ____|$$ |      $$ |      $$ |$$ |  $$ |$$ |  $$ |
    \$$$$$$  |$$$$$$$  |\$$$$$$$\ $$ |      $$ |      $$ |$$ |  $$ |\$$$$$$$ |
     \______/ \_______/  \_______|\__|      \__|      \__|\__|  \__| \_______|
    
    
    Search path: /usr/local/share/metasploit-framework/
    Keywords: password, user
    File extensions: yml, db, conf
    Return 25 characters before and after a keyword.
    
    /usr/local/share/metasploit-framework/config/database.yml
    /usr/local/share/metasploit-framework/data/john/confs/john.conf
    /usr/local/share/metasploit-framework/data/lab/test_lab.yml
    /usr/local/share/metasploit-framework/data/lab/test_targets.yml
    Searched through 12 files.
    Found keyword in 4 files.
    For more details, check the results file: /Users/Temp/uberfind/results.txt

**results.txt**

    === FILE ===>   /usr/local/share/metasploit-framework/config/database.yml
    --> Found "user": Line 4
      username: msf4
    
    --> Found "password": Line 5
      password: msf4
