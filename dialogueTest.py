import string
def makeNewFile():
    with open("TextFiles/new.txt", 'w') as file:
        file.write("a")

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

def get_level(line):
    i = 0
    for char in [x for x in line if x == "\t"]:
        i += 1
    return i

def evaluateBlock(block_key):
    blocktext = blocks[block_key]
    queue_.remove(block_key)
    index = 0
    currentLevel = 0
    while index < len(blocktext):
        if "->" in blocktext[index]:
            choices = [x for x in blocktext if ("->" in x)]
            n = 1
            for i in choices:
                strOutput = str(choices.index(i) + 1)+ ": "+ i[2:].strip()
                print(strOutput)
            choice_int = int(input("Put in an int"))
            index = blocktext.index(choices[choice_int - 1]) + 1
        elif blocktext[index][0:2] == "\t#":
            queue_.append(blocktext[index].split("#")[1])
            break
        else:
            b = input(blocktext[index].strip())
            index += 1

with open("TextFiles/new.txt") as file:
    blocks = divide_blocks(file)
    queue_ = []
    queue_.append("START")
    while len(queue_) > 0:
        evaluateBlock(queue_[0])
