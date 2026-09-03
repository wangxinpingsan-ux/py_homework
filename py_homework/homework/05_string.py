"""
第 05 天：字串 —— C 最痛苦、Python 最爽的部分
預估 25 分鐘

=================================================================
【C 的字串是 char 陣列，Python 的字串是「一個東西」】
=================================================================

  要做的事              C                          Python
  --------------------  -------------------------  ------------------
  比較兩個字串相等      strcmp(a, b) == 0          a == b
  接起來                strcat(a, b)  (要先夠大!)  a + b
  長度                  strlen(a)                  len(a)
  複製                  strcpy(dst, src)           b = a
  重複 3 次             寫迴圈                     a * 3
  找子字串              strstr(a, "abc")           "abc" in a
  轉大寫                寫迴圈 + toupper           a.upper()

  在 C 你要煩惱 '\0'、緩衝區長度、會不會溢位。Python 全都不用。

-----------------------------------------------------------------
【坑：字串「不可變」】
-----------------------------------------------------------------

  C:       s[0] = 'X';        合法，直接改記憶體

  Python:  s[0] = "X"         ❌ TypeError！字串改不動

  要改就做一個新的：
           s = "X" + s[1:]

  所以 s.upper() 不會改 s，它「回傳一個新字串」：
           s = "abc"
           s.upper()          # 回傳 "ABC"，但 s 還是 "abc"
           s = s.upper()      # ✅ 要接回去

  ⚠️ 注意這跟 list 不一樣：list 有 a.sort()（改自己）也有 sorted(a)（回傳新的），
     兩種都給你。字串只有「回傳新的」這一種，因為它根本改不動。

-----------------------------------------------------------------
【切片（你筆記有記）】
-----------------------------------------------------------------

      s = "ABCDEF"
      s[0:3]   -> "ABC"
      s[2:]    -> "CDEF"
      s[::-1]  -> "FEDCBA"      ← C 要寫一整個反轉迴圈

-----------------------------------------------------------------
【常用方法（你筆記記過，這裡練到會）】
-----------------------------------------------------------------

      s.split()        切成 list（遇空白切）
      s.strip()        去頭尾空白
      s.replace(a, b)  取代
      s.count("A")     算 A 出現幾次
      s.find("B")      找位置，找不到回傳 -1
      "-".join(串列)   把 list 黏成字串，中間夾 "-"   ← join 是 split 的反向

=================================================================
【練習】
=================================================================
"""


# --- 第 1 題 ---
# 判斷是不是回文（正著讀反著讀一樣）。"aba" -> True
# 提示：用切片，一行就好
def is_palindrome(s):
    return s==s[::-1]


# --- 第 2 題 ---
# 算字串裡有幾個母音 aeiou（只考慮小寫）
# 提示：for c in s: 可以一個字一個字拿；用 c in "aeiou" 判斷
def count_vowels(s):
    count=0
    
    for c in s:
         if c in "aeiou":
            count+=1
    return count
            


# --- 第 3 題 ---
# 把 "  hello world  " 變成 "HELLO-WORLD"
# 步驟：去頭尾空白 -> 切成 list -> 轉大寫 -> 用 "-" 黏起來
def format_name(s):
    
    
    
    return s.strip().upper().replace(" ", "-")


# --- 第 4 題 ---
# 把字串裡的數字全部挑出來，回傳成一個「整數」
# "a1b2c3" -> 123
# 提示：c.isdigit() 判斷是不是數字字元；先黏成字串再 int()
def extract_number(s):
    
    
    text = "".join([c for c in s if c.isdigit()])                 # 用什麼黏？中間不加東西
    return int(text)                     # 轉哪個變數？

    





# =================================================================
print("第1題", "OK" if is_palindrome("aba") and not is_palindrome("abc") else f"錯，is_palindrome('abc')給了 {is_palindrome('abc')}，應該是 False")
print("第2題", "OK" if count_vowels("hello") == 2 and count_vowels("xyz") == 0 else f"錯，給了 {count_vowels('hello')}，應該是 2")
print("第3題", "OK" if format_name("  hello world  ") == "HELLO-WORLD" else f"錯，給了 {format_name('  hello world  ')}，應該是 HELLO-WORLD")
print("第4題", "OK" if extract_number("a1b2c3") == 123 else f"錯，給了 {extract_number('a1b2c3')}，應該是 123")
