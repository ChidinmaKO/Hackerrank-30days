name_list = {}
numberOfStudents = len(name_list)
score_list = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_list[name] = score

    for value in name_list.values():
        score_list.append(value)

    score_list = list(dict.fromkeys(score_list))
    score_list.sort()

    for i in sorted(name_list):
        if (score_list[1]) == name_list[i]:
            print (i)
