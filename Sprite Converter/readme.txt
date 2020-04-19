This is the sprite converter. It turns 12-color bmp files into importable C code.

== HOW TO RUN ==
1) Have Python 3 installed. You can download here: https://www.python.org/downloads/
2) Place all 12-color (also known as 4bit colored) bmp image files into the "sprites" folder.
3) Run the spriteConverter.py file. It will automatically detect any files that are NOT proper format, so don't worry.
4) Provide the C code to the source code. (as of writing, the organization of this program hasn't been planned out. Will update where to put this later!)

== WHAT AM I LOOKING AT? ==
In order to increase portability, I've opted against importing file reading libraries. As such, all graphics data will be placed in the source code directly in its own file. This means the C code must be RE-COMPILED with every update to the sprite set. Be aware, you should NOT just copy/paste without viewing the C code provided. Any and all files which are not of the proper format will be printed with an ERROR line. 

== HOW CAN I ASK QUESTIONS/COMPLAIN? ==
My email is drewrooks@gmail.com