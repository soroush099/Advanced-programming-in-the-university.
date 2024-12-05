# practice 3
# soroush yousefi

# برنامه ای بنویسید که یک رشته را از ورودی بخواند و تعداد تکرار هر کلمه را نمایش دهد.

ch = input("Enter a string: ")

# اینجا کلمات رو اول به حروف کوچیک تبدیل کردم تا دقت کار بره بالا
ch = ch.lower().split()

# ببخشید استاد واقعا نمیدونم که دیکشنری رو خوندیم یا نه ولی از بچه های دانشگاه پرسیدم گفتن خوندیم منم استفاده کردم
shomaresh = {}

for i in ch:
    if i in shomaresh:
        shomaresh[i] += 1
    else:
        shomaresh[i] = 1

for i in shomaresh:
    print(f"{i}: {shomaresh[i]}")

