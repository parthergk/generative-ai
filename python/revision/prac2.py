nameStr = "madam";

if nameStr == nameStr[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

nums = [1,1,2,2,3,4,4]

print("Remove dublicat", set(nums))

text = "banana"
count = {}

for i in text:
    count[i] = count.get(i, 0) + 1
print("Frequency Count", count)

nums = [1,2,3,4,5,6]

print("first 3 elements",nums[0:3])
print("last 2 elements",nums[4:])
print("reverse list",nums[::-1])