import sys

n=len(sys.argv)
print("total arguments passed:")

print("\nname of python script:")


print("\narguments passed:", end)
for i in range(1,n):
    print(sys.argv[i], end = " ")

sum = 0

for i in range(1,n):
    sum += int(sys.argv[i])

    print("\n\nResult", sum)
