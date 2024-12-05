# practice 4
# soroush yousefi

# برنامه ای بنویسید که یک لیست را خوانده و اعداد مثبت آن را فیلتر کند و نمایش دهد.
"""
    فکر کنم سورت سوال یعنی فقط اعداد مثبت رو نمایش بدیم
اگر برعکسش هم باشه فقط کافیه شرط بزرگ تر از صفر رو کوچیکتر از صفر کنیم
"""


shart_tekrar = True
numbers = []
while shart_tekrar:
    number = input("Enter a number: ")
    if number == "":
        shart_tekrar = False
    else:
        number = int(number)
        if number >= 0:
            numbers.append(number)

print(numbers)
