if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    remove_dup = set(arr)
    Runner= sorted(list(remove_dup))
    print(Runner[-2])
