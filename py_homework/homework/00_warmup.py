"""
熱身題（5 分鐘）：修 bug
你的 map2.py 裡有一個標反了的地方：

    num = 721
    str3 = str(num)
    print(f"個位={str3[2]}")     # <- str3[0] 是 '7'，那是百位不是個位！
    print(f"十位={str3[1]}")
    print(f"百位={str3[0]}")

【任務】
寫一個函式 split_digits(num)，回傳 (個位, 十位, 百位) 的 tuple，
而且要用「數學」做，不要用字串索引 —— 這樣 num 幾位數都不會出錯：
    提示：個位 = num % 10 ，十位 = num // 10 % 10 ，百位 = ?

    split_digits(721)  ->  (1, 2, 7)
    split_digits(5)    ->  (5, 0, 0)
"""


def split_digits(num):
    return (num % 10, num // 10 % 10, num // 100 % 10)


print(split_digits(721))  # 應該印 (1, 2, 7)
print(split_digits(5))  # 應該印 (5, 0, 0)
