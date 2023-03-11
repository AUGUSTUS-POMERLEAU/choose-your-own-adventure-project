Project for a choose-your-own-adventure generator. Reads .txt files as dialogue trees.

Current syntax:

Dialogues are divided into "blocks". Blocks begin with their titles, between #'s, and end with a blank line, like this:

#new_block#
words
words

#other_new_block#
...

A choice is made with a -> arrow, with the relevant dialogue indented underneath, like this:

#new_block#
words
-> option1
  words
  words
-> option2
  different words
  ...

Commands do things inside the program. The current commands are:

[new:. . .] Creates a new variable, and sets its value to 0
[. . . (variable name):. . . (variable value] Putting in the name of a variable and a value on the left sets the variable to that value
[goto:. . . (block name)] This command starts running a new block. 
