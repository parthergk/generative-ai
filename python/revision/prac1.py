num = 7

if num % 2 == 0:
    print("Even")
else:
    print("odd")

nums = [10, 40, 20, 99, 2]
largnu = 0

for i in nums:
    if largnu < i:
        largnu = i
print("Largest number",largnu)

text = "gaurav"
count = 0

for i in text:
    for j in ["a", "e", "i", "o", "u"]:
        if i == j:
            count = count + 1 
print("Vowels", count)


str = "python"
print("Reverse", str[::-1])

nums = [1,2,3,4]
sum:int = 0

for i in nums:
    sum = sum + i

print("Sum Of list", sum)