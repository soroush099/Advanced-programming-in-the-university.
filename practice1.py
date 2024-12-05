# practice1
# soroush yousefi
# برنامه ای بنویسید که یک عدد را از ورودی خوانده و تمام اعداد اول قبل از آن را تعیین و خروجی دهد.

def is_aval(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def adad_aval_kamtar(n):
    aval = []
    for i in range(2, n):
        if is_aval(i):
            aval.append(i)
    return aval


number = int(input("Enter a number: "))
primes = adad_aval_kamtar(number)

# نمایش اعداد اول، مثلا یکم خوشکلش کردم استاد لطفا ایراد نگیرید
print(f"اعداد اول کمتر از {number} عبارتند از: {primes}")
