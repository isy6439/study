import sys

string = sys.stdin.readline().strip()

index_d2 = string.find("D2")
index_d2_lower = string.find("d2")

if index_d2 != -1 or index_d2_lower != -1:
    print("D2")
else:
    print("unrated")