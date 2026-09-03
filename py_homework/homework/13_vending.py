"""
第 13 天：綜合實作 —— 販賣機（把前 12 天全用上）
預估 50 分鐘   這題沒有自動測試，自己執行測

用到的東西：dict(08) / f-string(07) / try-except(11) / 函式回傳值

=================================================================
【你原本 vendingmachine.py 的 3 個問題】
=================================================================

  menu = {"漢堡":"100"}            價格是字串，每次用都要 int() 轉
  cart.append(int(menu.get(food))) cart 只存價格，結帳印不出買了什麼
  food = input(...).lower()        中文用 .lower() 完全沒作用

  第 2 點特別重要：品名可以查回價格 menu["漢堡"] -> 100，
  但價格 100 查不回品名。**存資訊多的那個。**

=================================================================
【規格】
=================================================================

  print_menu(menu)
      印出「品名：價格」對齊的菜單。用 f-string 的寬度對齊（第 07 天）

  checkout(cart, menu)
      算總金額並 return。
      ⚠️ 這個函式裡【一個 print 都不准有】，它只負責算。

  show_cart(cart, menu)
      印出購物車每一項的品名 + 價格，最後印總金額
      （總金額呼叫 checkout 拿，不要重算一次）

  main()
      1. print_menu
      2. while 迴圈：
         - 輸入 q     -> break
         - 輸入 list  -> show_cart
         - 在菜單裡   -> cart.append(品名)，印「已加入 漢堡（100元）」
         - 不在菜單裡 -> 印「商品不存在」，不可以當掉
      3. 迴圈結束後印最後明細

【自我檢查】
  [ ] menu 的價格是 100 不是 "100"
  [ ] 用 if food in menu 檢查，不是 .get() is None
  [ ] checkout 裡面沒有 print，只有 return
  [ ] 買兩個漢堡，總金額 200
  [ ] 亂打「牛排」不會崩潰
  [ ] 縮排全部 4 格（你原本的 else 底下只縮 1 格）

【加分題】
  1. 加一個 remove 指令，可以從購物車拿掉東西（提示：cart.remove）
  2. 結帳時統計「漢堡 x2  200」而不是列兩行（提示：第 08 天第 1 題的 count_items）
"""

menu = {"漢堡": 100, "薯條": 30, "雞腿": 60, "雞塊": 40, "可樂": 30, "紅茶": 15}


def print_menu(menu):
    pass


def checkout(cart, menu):
    pass


def show_cart(cart, menu):
    pass


def main():
    cart = []
    print_menu(menu)
    # TODO


main()
