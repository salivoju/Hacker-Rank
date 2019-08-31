if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        name = input().split()
        student_marks[name[0]] = [float(a) for a in name[1:]]
    query_name = input()
    print("%.2f" %(sum(student_marks[query_name])/len(student_marks[query_name])))

