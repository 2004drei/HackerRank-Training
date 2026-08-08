

def split_and_join(line):
    split_ed = line.split(" ")
    return "-".join(split_ed)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)