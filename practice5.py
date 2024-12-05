# practice 5
# soroush yousefi

# برنامه ای بنویسید که لیستی از لغات را دریافت کند و لغتی که بیشترین طول را دارد را نمایش دهد

shart_tekrar = True
long_word = ""
words = []
while shart_tekrar:
    word = input("Enter a string: ")
    if word == "":
        shart_tekrar = False

    elif len(word) > len(long_word):
        words.append(word)
        long_word = word

print(f"long word: {long_word}\nlen: {len(long_word)}")
print(f"words: {words}")

