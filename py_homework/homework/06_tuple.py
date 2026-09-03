"""
第 06 天：tuple 與多值回傳 —— 你在 C 用指標做的那件事
預估 20 分鐘

=================================================================
【你 pointer_findmaxmin.c 寫過這個】
=================================================================

  C 的函式只能 return 一個值，想回傳兩個就得用指標：

      void find_maxmin(int array[], int *max, int *min)
      {
          *max = array[0];
          *min = array[0];
          ...
      }

      int max_value = 0, min_value = 0;
      find_maxmin(number, &max_value, &min_value);   <- 傳位址進去讓函式填

  Python 直接回傳兩個就好，不需要指標：

      def find_maxmin(nums):
          return max(nums), min(nums)      ← 逗號隔開就是回傳兩個

      big, small = find_maxmin([3, 1, 2])  ← 接的時候也用逗號

  Python 沒有指標。你 C 那套 & 和 * 在這裡全部用不到，也不需要。

-----------------------------------------------------------------
【原理：那個「兩個值」其實是一個 tuple】
-----------------------------------------------------------------

      def f():
          return 1, 2

      x = f()          # x 是 (1, 2)  ← 一個 tuple
      a, b = f()       # 自動拆開，a=1 b=2   （叫做 unpacking）

  你第 02 天寫的 a, b = b, a 也是同一招：
      右邊先打包成 (b, a)，左邊再拆開。所以不用 temp 變數。

-----------------------------------------------------------------
【tuple vs list：差在能不能改】
-----------------------------------------------------------------

      t = (1, 2, 3)     tuple，小括號，不能改
      L = [1, 2, 3]     list，中括號，可以改

      t[0] = 9          ❌ TypeError
      L[0] = 9          ✅

  什麼時候用 tuple？
      這組東西是「一個整體」，不該被拆開改：座標 (x,y)、一筆學生資料
  什麼時候用 list？
      這是會變動的清單：購物車、成績陣列

  你 sort.py 寫的 ("wang","170",50) 就是 tuple，直覺是對的。

=================================================================
【練習】
=================================================================
"""


# --- 第 1 題 ---
# 把 pointer_findmaxmin.c 翻成 Python
# 回傳 (最大值, 最小值)
def find_maxmin(nums):
    return max(nums),min(nums)


# --- 第 2 題 ---
# 傳入秒數，回傳 (時, 分, 秒)
# 3661 -> (1, 1, 1)
# 提示：用 // 和 %
def split_time(seconds):
    
    return seconds//3600,seconds%3600//60,seconds%60


# --- 第 3 題 ---
# 傳入一個 list，回傳 (偶數個數, 奇數個數)
def count_even_odd(nums):
    odd=0
    even=0
    for i in nums:
        if i%2==0:
            even+=1
        else :
            odd+=1
    return even,odd


# --- 第 4 題 ---
# 傳入 (a, b) 兩個數，回傳 (商, 餘數)。除數是 0 就回傳 (None, None)
def divide(a, b):
    if b==0:
        return None,None
    return a//b , a%b 


# =================================================================
print("第1題", "OK" if find_maxmin([35,12,89,4,56]) == (89, 4) else f"錯，給了 {find_maxmin([35,12,89,4,56])}，應該是 (89, 4)")
print("第2題", "OK" if split_time(3661) == (1,1,1) and split_time(59) == (0,0,59) else f"錯，給了 {split_time(3661)}，應該是 (1, 1, 1)")
print("第3題", "OK" if count_even_odd([1,2,3,4,5]) == (2,3) else f"錯，給了 {count_even_odd([1,2,3,4,5])}，應該是 (2, 3)")
print("第4題", "OK" if divide(7,2) == (3,1) and divide(5,0) == (None,None) else f"錯，divide(7,2)給了 {divide(7,2)}，應該是 (3, 1)")
