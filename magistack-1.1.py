# MagiStack Interpreter v1.1
# Created by Connor Scialdone
#
# Values are pushed/popped from the stack as a, b, etc.
#   in alphabetical order (a first, then b, and so on)
#
# Commands:
#   0-9: Push value
#   +: Pop a and b, push a+b
#   -: Pop a and b, push b-a
#   *: Pop a and b, push a*b
#   /: Pop a and b, push b/a (floored)
#   %: Pop a and b, push b%a
#   !: Pop a, push boolean !a>0
#   `: Pop a and b, push boolean b>a
#   :: Pop a, push two instances of a
#   \: Pop a and b, push a and b (swap)
#   $: Pop a and discard
#   .: Pop a, output as integer
#   ,: Pop a, output as ASCII character
#   =: Pop a and b, skip next command if a!=b
#   #: Skip to next #, |, or end of program
#   @: Skip to last @, |, or start of program
#   ]: Unconditionally terminate skipping forward
#   [: Unconditionally terminate skipping backward
#   |: Unconditionally terminate skipping either direction
#   ?: Push stack size to stack (i.e. [5,4,3,2,1] -> [5,4,3,2,1,5])
#   ^: Wait for input, then push as integer (pushes 0 if not integer, allows signed)
#   &: Wait for input, then push as ASCII value (only takes first character!)
#   _: Exit program   
#
# Comments can easily be simulated by wrapping text in #.
# Any non-command characters (newlines, letters, etc.) will
#   be ignored automatically.
#
# A filepath to execute (preferably .mgst) can by given by
#   command line; if not given, the program will prompt for
#   a path.

import sys,math,re

stack = [] # The stack

# Main method (called with the string to process)
def main(prog):
    global stack
    prog = re.sub("\s","",prog)
    
    p = -1 # Counter variable for position in string
    while p < len(prog)-1:
        p,c = p+1,prog[p+1] # Update position and get character

        # Command Handling
        if   c.isdigit(): stack.append(int(c)) # Digits
        elif c == "+": # Addition
            checkStackSize(2,p)
            a = stack.pop()
            b = stack.pop()
            stack.append(a+b)
        elif c == "-": # Subtraction
            checkStackSize(2,p)
            a = stack.pop()
            b = stack.pop()
            stack.append(b-a)
        elif c == "*": # Multiplication
            checkStackSize(2,p)
            a = stack.pop()
            b = stack.pop()
            stack.append(a*b)
        elif c == "/": # Division
            checkStackSize(2,p)
            a = stack.pop()
            b = stack.pop()
            stack.append(math.floor(b/a))
        elif c == "%": # Modulus
            checkStackSize(2,p)
            a = stack.pop()
            b = stack.pop()
            stack.append(b%a)
        elif c == "!": # Boolean inverter
            checkStackSize(1,p)
            a = stack.pop()
            stack.append(0 if a == 1 else 1)
        elif c == "`": # Greater than
            checkStackSize(2,p)
            a = stack.pop()
            b = stack.pop()
            stack.append(1 if b>a else 0)
        elif c == ":": # Duplicator
            checkStackSize(1,p)
            a = stack.pop()
            stack.append(a)
            stack.append(a)
        elif c == "\\": # Swapper
            checkStackSize(2,p)
            a = stack.pop()
            b = stack.pop()
            stack.append(a)
            stack.append(b)
        elif c == "$": # Popper
            checkStackSize(1,p)
            a = stack.pop()
        elif c == ".": # Integer output
            checkStackSize(1,p)
            a = stack.pop()
            print(a,end="")
        elif c == ",": # ASCII output
            checkStackSize(1,p)
            a = stack.pop()
            print(chr(a),end="")
        elif c == "=": # Comparison
            checkStackSize(2,p)
            a = stack.pop()
            b = stack.pop()
            if a != b: p += 1
        elif c == "#": # Skip forward
            p += 1
            while p < len(prog) and prog[p] not in ["#","|","]"]: p += 1
        elif c == "@": # Skip backward
            p -= 1
            while p > -1 and prog[p] not in ["@","|","["]: p -= 1
        elif c == "?": #Push stack size
            stack.append(len(stack))
        elif c == "^": #Push integer input
            i = input("")
            if re.match("[+\-]?[0-9]+$",i) != None: stack.append(int(i))
            else: stack.append(0)
        elif c == "&": #Push ASCII input
            for i in input(""): stack.append(ord(i))
        elif c == "_": #Exit program
            exit()
        else: continue # Unknown

    stack = [] # Reset stack after program end

# Throws an error if the stack contains fewer values than the given "expected" parameter
def checkStackSize(expected,pos):
    if len(stack) < expected:
        print("\n[P:"+str(pos+1)+"] StackError: Expected at least "+str(expected)+" values in stack, got "+str(len(stack)))
        exit()

# Testing entry point; enter a program into prog to execute
prog = """"""
#main(prog)

# Main entry point; gets the command line argument or prompts for a path, then runs.
main("91+,"+(open(sys.argv[1]).read() if len(sys.argv) > 1 else open(input("Please enter a path:\n> "),"r").read()))
