# practice3
# soroush yousefi

# برنامه ای بنویسید که رشته ای را خوانده و کاراکتر های با اندیس فرد آن را نمایش دهد.

# ____________________________________________________________
print("_"*40)
# ____________________________________________________________

# حل با حلقه فور که به نظر من ساده تر است.
ch1 = input("Enter a string: ")

for i in range(len(ch1)):
    if i % 2 != 0:
        print(ch1[i])

# ____________________________________________________________
print("_"*40)
# ____________________________________________________________

# حل با حلقه وایل.
ch2 = input("Enter a string: ")

i2 = 0
while i2 < len(ch2):
    if i2 % 2 != 0:
        print(ch2[i2])
    i2 += 1

# ____________________________________________________________
print("_"*40)
# ____________________________________________________________
