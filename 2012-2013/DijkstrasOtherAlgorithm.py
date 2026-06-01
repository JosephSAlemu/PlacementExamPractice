def gcd(a: int, b: int) -> int:
    if a == b:
        return a
    elif a > b:
        return gcd(a-b, b)
    else:
        return gcd(a, b-a)


if __name__ == "__main__":
    arg = input()
    arg = arg.split(" ")
    a, b = int(arg[0]), int(arg[1])
    answer = gcd(a, b)
    print(answer)
