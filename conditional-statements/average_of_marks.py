# Calculating the average marks of five subjects and printing the corresponding grade.

sub1 = int(input())
sub2 = int(input())
sub3 = int(input())
sub4 = int(input())
sub5 = int(input())

avg = (sub1 + sub2 + sub3 + sub4 + sub5) / 5

if avg >= 90:
    print("Distinction")
elif avg >= 75 and avg < 90:
    print("First Class")
elif avg >= 60 and avg < 75:
    print("Second Class")
else:
    print("Fail")