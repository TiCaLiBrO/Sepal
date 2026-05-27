import subprocess

# This will be for SEPAL.

# Simplified color codes.
RED     = "\033[31m"
BLUE    = "\033[34m"
GREEN   = "\033[32m"
CYAN    = "\033[36m"
YELLOW  = "\033[33m"
MAGENTA = "\033[35m"
RESET   = "\033[0m"


subprocess.run(["wsl", "ls"])

# The anchor class will be used for custom anchor creation and management.
class anchor:
    def __init__(self, name, path="root"):
        self.name = name
        self.path = path

# The here anchor will be used to store the path of the `here` SEPAL directory.
here = anchor("here", "root")

# The `there` anchor will be used to store the path of the `there` SEPAL directory.
there = anchor("there", "root")

anchors = [here, there]
current_anchor_index = 0

# lines_of_code is an array of lines of code.
lines_of_code = []

current_step = "print location"
# print location
# get input
# extend input
# execute input

def translate_from_sepal_to_bash(sepal_directory):
    # This will take a SEPAL directory and translate it to a bash directory.
    # SEPAL directories can be relative, which is similar to Bash.
    # Absolute SEPAL directories will start with "root", instead of Bash's "/".
    if sepal_directory.startswith("root"):
        return "/" + sepal_directory[4:]

def translate_from_bash_to_sepal(bash_directory):
    # This will take a Bash directory and translate it to a SEPAL directory.
    # Bash directories can be relative, which is similar to SEPAL.
    # Absolute Bash directories will start with "/", instead of SEPAL's "root".
    if bash_directory.startswith("/"):
        return "root" + bash_directory[1:]




def lex(line_of_code):
    cursor_position = 0
    token_array = []
    action = None
    print("YOLO")
    # can be: None, "/" or "/_"
    while len(line_of_code) > 0:
        if line_of_code[cursor_position] == "/":
            # we're deciding between "/" and "/_"
            if cursor_position + 1 >= len(line_of_code) or line_of_code[cursor_position + 1] == " ":
                action = "/"
                token_array.append(action)
                line_of_code = line_of_code[cursor_position + 1:]
                cursor_position = 0
            else:
                action = "/_"
                token_array.append(action)
                line_of_code = line_of_code[cursor_position + 1:]
                cursor_position = 0
        if cursor_position < len(line_of_code):
            if line_of_code[cursor_position] in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "."]:
                # we're scanning for a directory name.
                directory_name = ""
                while cursor_position < len(line_of_code) and line_of_code[cursor_position] not in [" ", "/", "\\"]:
                    directory_name += line_of_code[cursor_position]
                    cursor_position += 1
                token_array.append(directory_name)
                line_of_code = line_of_code[cursor_position:]
                cursor_position = 0
                directory_name = ""
    print(GREEN + str(token_array) + RESET)
    return token_array

def interpret(line_of_code):
    # This will take a line of code and interpret it, executing the appropriate actions.
    lexer_position = 0
    if line_of_code[lexer_position] == "/_":
        subprocess.run(["wsl", "cd", f"{translate_from_sepal_to_bash(anchors[current_anchor_index].path + '/' + line_of_code[lexer_position + 1])}"])
        print(f"{translate_from_sepal_to_bash(anchors[current_anchor_index].path + line_of_code[lexer_position + 1])}")
        anchors[current_anchor_index].path += "/" + line_of_code[lexer_position + 1]
        line_of_code = line_of_code[lexer_position + 2:]
    if lexer_position < len(line_of_code):
        if line_of_code[lexer_position] == "/":
            subprocess.run(["wsl", "ls", f"{translate_from_sepal_to_bash(anchors[current_anchor_index].path)}"])
            print(f"{translate_from_sepal_to_bash(anchors[current_anchor_index].path)}")
            
            line_of_code = line_of_code[lexer_position + 1:]





def print_location():
    # This will print the current location of the user in the SEPAL system.
    print(GREEN + anchors[current_anchor_index].name + RESET + "@" + BLUE + anchors[current_anchor_index].path + RESET + ": ", end="")    

def get_input():
    # This will get input from the user and store it in the lines_of_code list.
    lines_of_code.append(input())


# This will be the Script Evaluate Print Administration Loop.
while True:
    if current_step == "print location":
        print_location()
        current_step = "get input"
    if current_step == "get input":
        get_input()
        #print("TEST - input: " + str(lines_of_code[0]))
        if lines_of_code[0][0] == "/" or lines_of_code[0][0] == "\\":
            print("TEST - executing input immediately")
            current_step = "execute input"
        else:
            print("TEST - extending input")
            current_step = "extend input"
    if current_step == "extend input":
        print("TEST - extended input is not implemented yet.")
        break # we'll worry about multi-line input later, for now we will just execute single-line input immediately.
    if current_step == "execute input":
        while len(lines_of_code) > 0:
            current_line_of_code = lines_of_code[0]
            # we want to scan the first element of the lines_of_code list and execute it, then remove it from the list.
            lexed_line = lex(current_line_of_code)
            lines_of_code.pop(0)
            interpret(lexed_line)
        print("TEST - finished executing input")
        current_step = "print location"
