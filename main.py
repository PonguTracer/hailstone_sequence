def hailstone_sequence(n):
    count = 0
    while n != 1:
        print(n, end='\t')
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
        if count % 10 == 0:
            print()
    print(1)


if __name__ == "__main__":
    n = int(input())
    hailstone_sequence(n)
