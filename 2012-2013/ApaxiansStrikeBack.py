
if __name__ == "__main__":
    name = input()
    first_char = name[0]
    count = 0
    for i in range(len(name)):
        if name[i] == first_char:
            count+=1
    print(count)
