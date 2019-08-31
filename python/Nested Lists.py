if __name__ == '__main__':
    n=int(input())
    names = []
    for i in range(2*n):
        names.append(input().split())
    grades = {}
    for j in range(0, len(names), 2):
        grades[names[j][0]] = float(names[j + 1][0])
    second_lowest = []
    sorted_list = sorted(set(grades.values()))[1]
    for students in grades.keys():
        if grades[students] == sorted_list:
            second_lowest.append(students)
    for result in sorted(second_lowest):
        print(result)
