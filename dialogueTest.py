import string
def divide_blocks(file):
    all_blocks = {}
    current_block = "!!NONE!!"
    for line in file:
        if "#" in line and current_block == "!!NONE!!":
            blockname = line.split("#")[1]
            all_blocks[blockname] = []
            current_block = blockname
        elif line == "\n" and current_block != "!!NONE!!":
            current_block = "!!NONE!!"
        else:
            all_blocks[current_block].append(line)
    return all_blocks

def normal_text(line):
    b = input(line)

def choice_dict(list_lines, level):
    options = [x for x in list_lines if "->" in x and get_level(x) == level]
    choice = {}
    index = 0
    for i in range(len(options)):
        choice[i + 1] = (options[i].strip(),[])
        for line in list_lines[list_lines.index(options[i]):]:
            if i != len(options) - 1:
                if line == options[i + 1]:
                    break
            if get_level(line) > level:
                choice[i + 1][1].append(line)
        index += 1
    return choice

def eval_choice(choice_dict_):
    valid_options = []
    for (x, y) in choice_dict_.items():
        output_text = str(x) + ": " + y[0]
        print(output_text)
        valid_options.append(x)
    #print(valid_options)
    while True:
        user_input = int(input("Input a valid int:"))
        if user_input in valid_options:
            #print(choice_dict_[user_input][1])
            eval_lines(choice_dict_[user_input][1])
            break
        else:
            print("Invalid input.")


def get_level(line):
    i = 0
    for char in [x for x in line if x == "\t"]:
        i += 1
    return i

def eval_command(string):
    string_list = string.split(":")
    #print(string_list)
    command = string_list[0].strip()
    target = string_list[1].strip()
    if command == "goto":
        queue_.append(target)
    elif command == "new":
        vars[target] = 0
    elif command in vars.keys():
        vars[command] = target

def eval_lines(lines):
    for line in lines:
        if "->" in line:
            eval_choice(choice_dict(lines, get_level(line)))
            break
        if ("[" in line and "]" in line):
            cmd_ = line.replace("[","").replace("]","")
            eval_command(cmd_)
        else:
            line = line.strip().split("-@")
            output_string = ""
            for segment in line:
                if segment in vars:
                    segment = vars[segment]
                output_string += segment
            print(output_string)

def eval_block(block_key):
    blocktext = blocks[block_key]
    queue_.remove(block_key)
    eval_lines(blocktext)

with open("TextFiles/new.txt") as file:
    blocks = divide_blocks(file)
    queue_ = []
    queue_.append("START")
    vars = {}
    while len(queue_) > 0:
        eval_block(queue_[0])

