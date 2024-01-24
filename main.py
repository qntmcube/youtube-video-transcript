def timestamp(str):
    split = str.split(":")
    if len(split) == 2:
        print(split)
        if len(split[1]) == 2 and split[0].isnumeric() and split[1].isnumeric():
            print("true")
            return True
    return False


file1 = open('input.txt', 'r')
lines = file1.readlines()
for i in lines:
    if timestamp(i[:-1]):
        lines.remove(i)
out = open('output.txt', 'w')
out.writelines(lines)