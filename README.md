# [truthTables](https://rayelg.github.io/truthTables/)
Python & Brython implementations of a boolean expression intepreter.

truthtable.py in master branch is the project adapted for python commandline.

truthTableHtml (And the gh-pages branch) uses brython to implement this program for web use.

![truthTableHtml](https://i.imgur.com/I0G5Qwc.png)

Boolean expressions can contain:
* Alphabetic characters (Boolean variables)
* The following operators: (In order of precedence)
  AND
  OR
  NAND
  NOR
  XOR
  XNOR
* Round brackets (Expressions within brackets are evaluated first)

An expression might look like A XOR (B AND NOT C)
