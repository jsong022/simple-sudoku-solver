# Simple Sudoku Solver
Author: Jay Song

Date: 12/10/17

### Description
A sudoku solver using a simple brute force DFS with no heuristics used at all.
Written using Python 3.6.3

### Instructions
- ./simple-sudoku.py
	- No arguments to input puzzle manually 1 row at a time
	- Each row is a 9 character stringfdfd
	- Use '0', '.', '-'. '\_', or ' ' for unknown squares
- ./simple-sudoku.py ARG1 ARG2 ...
	- Can take 1 or more 81-character Strings as arguments

##### Sample Output
>\>\>./simple-sudoku.py 000260701680070090190004500820100040004602900050003028009300074040050036703018000
>solving....
>\-------------
>|...|26.|7.1|
>|68.|.7.|.9.|
>|19.|..4|5..|
>\-------------
>|82.|1..|.4.|
>|..4|6.2|9..|
>|.5.|..3|.28|
>\-------------
>|..9|3..|.74|
>|.4.|.5.|.36|
>|7.3|.18|...|
>\-------------
>Solution found:
>\-------------
>|435|269|781|
>|682|571|493|
>|197|834|562|
>\-------------
>|826|195|347|
>|374|682|915|
>|951|743|628|
>\-------------
>|519|326|874|
>|248|957|136|
>|763|418|259|
>\-------------
--- 0.031223297119140625 seconds ---