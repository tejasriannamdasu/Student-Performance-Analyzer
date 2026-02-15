reg_no = input("enter registration number:")
D = int(reg_no[len(reg_no) - 1])
print("Register Digit(D):", D)
n = int(input("enter number of activity scores:"))
scores = [0] * n
for i in range(n):
    scores[i] = int(input("enter score:"))
low_risk = [0] * n
medium_risk = [0] * n
high_risk = [0] * n
critical_risk = [0] * n
l = 0
m = 0
h = 0
c = 0
valid_entries = 0
ignored_entries = 0
for i in range(n):
    score = scores[i]
    if score < 0:
        ignored_entries = ignored_entries + 1
    else:
        valid_entries = valid_entries + 1
        if score <= 30:
            low_risk[l] = score
            l = l + 1
        elif score <= 60:
            medium_risk[m] = score
            m = m + 1
        elif score <= 100:
            high_risk[h] = score
            h = h + 1
        else:
            critical_risk[c] = score
            c = c + 1
print("before personalization Filtering:")
print("low_risk :", low_risk[:l])
print("medium_risk :", medium_risk[:m])
print("high_risk :", high_risk[:h])
print("critical_risk :", critical_risk[:c])
removed_count = 0
if D % 2 == 0:
    print("personalization : normal security mode activated for even digit")
    removed_count =c
    c = 0
else:
    print("personalization : strict security mode activated for odd digit")
    removed_count =l
    l = 0
print("after personalization Filtering:")
print("Low Risk :", low_risk[:l])
print("Medium Risk :", medium_risk[:m])
print("High Risk :", high_risk[:h])
print("Critical Risk :", critical_risk[:c])
print("Total Valid Entries:", valid_entries)
print("Total Ignored Entries:", ignored_entries)
print("Removed Due to Personalization:", removed_count)
