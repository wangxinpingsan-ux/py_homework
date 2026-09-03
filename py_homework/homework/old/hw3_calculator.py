"""
作業 3：防呆計算機
難度 ★★☆☆☆   預估 40 分鐘
前置：hw1, hw2

=================================================================
【你原本的 calculator.py 有兩個「一定會當掉」的地方】
=================================================================

    num1 = float(input("enter first number"))
        使用者打 abc  ->  ValueError: could not convert string to float
        程式直接紅字結束

    print(num1 / num2)
        num2 是 0  ->  ZeroDivisionError
        程式直接紅字結束

真實的程式不能因為使用者亂打就死掉。這題就是練這個。

-----------------------------------------------------------------
【新東西：try / except】
-----------------------------------------------------------------

    try:
        n = float(input("輸入數字："))    # 試著做這件事
    except ValueError:                    # 如果爆的是 ValueError
        print("那不是數字")               # 就做這個，程式不會死

    你在 readfile.py 已經用過 try 了，只是那次抓的是 FileNotFoundError。
    這次抓的是 ValueError（轉型失敗）跟 ZeroDivisionError（除以零）。

-----------------------------------------------------------------
【招式：try + while = 問到對為止】
-----------------------------------------------------------------

    def get_number(prompt):
        while True:                  # 一直繞
            try:
                return float(input(prompt))   # 成功就 return，return 會直接跳出迴圈
            except ValueError:
                print("那不是數字，請重新輸入")   # 失敗就繞回去再問一次

    這是很常見的寫法，值得背下來。
    關鍵：return 在 while 裡面 —— 一旦成功回傳，迴圈自然結束。

=================================================================
【規格】
=================================================================

  get_number(prompt)
      顯示 prompt 問使用者要一個數字，輸入不合法就重問，直到拿到為止。
      return 那個 float。

  get_operator()
      問使用者要 + - * / 其中一個。
      不是這四個就重問（用 while + if，不需要 try）。
      return 那個符號。

  calculate(a, b, op)
      用 if / elif 算出結果並 return。
      如果 op 是 "/" 而且 b == 0，回傳字串 "不能除以零" 就好。
      （這個函式裡不要 print）

  main()
      問數字 -> 問符號 -> 問數字 -> 印結果
      然後問「還要算嗎？(y/n)」，n 就結束。

【自我檢查】
  [ ] 輸入 abc 不會當掉，會叫你重打
  [ ] 10 / 0 印出「不能除以零」而不是紅字 traceback
  [ ] calculate 裡面沒有 print，只有 return
  [ ] 縮排 4 格（你原本的 calculator.py 只縮 1 格）

【加分題（想挑戰再做）】
  你的 lambda.py 練過 lambda。試著用 dict 取代 calculate 裡的 if/elif：
      OPS = {"+": lambda a, b: a + b,
             "-": lambda a, b: a - b, ...}
      OPS["+"](3, 5)  ->  8
  好處：以後要加 "**" 只要多一行 dict，不用動任何 if。
"""


def get_number(prompt):
    # TODO
    pass


def get_operator():
    # TODO
    pass


def calculate(a, b, op):
    # TODO
    pass


def main():
    # TODO
    pass


main()
