marks = []
Name=input("enter your name: ")
x=len(Name)
N = int(input("enter no of students: "))
for i in range(N):
    s = int(input("enter your  marks: "))
    marks.append(s)
    if marks[i]%10==x:
        if marks[i]>98:
            marks[i]=100
        else:
           marks[i]=marks[i]+2
valid_count = 0
fail_count = 0
for mark in marks:
    if mark < 0 or mark > 100:
        print(mark, "→ Invalid")
    else:
        valid_count = valid_count + 1
        if mark >= 90:
            print(mark, "→ Excellent")
        elif mark >= 75:
            print(mark, "→ Very Good")
        elif mark >= 60:
            print(mark, "→ Good")
        elif mark >= 40:
            print(mark, "→ Average")
        else:
            print(mark, "→ Fail")
            fail_count = fail_count + 1
print("Total Valid Students:", valid_count)
print("Total Failed Students:", fail_count)


