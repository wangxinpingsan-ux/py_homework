"""
第 03 天：for 迴圈 —— C 和 Python 差最多的地方
預估 25 分鐘

=================================================================
【C 的 for 是「數數字」，Python 的 for 是「拿東西」】
=================================================================

  C:       for (int i = 0; i < 5; i++)
                    ↑起點  ↑條件  ↑增量     三段式，你自己控制 i

  Python:  for i in range(5):
                    ↑ 直接說「跑 5 次」，i 依序是 0,1,2,3,4

  range 三種用法（跟 C 的三段式對應）：
      range(5)          ->  0 1 2 3 4
      range(1, 5)       ->  1 2 3 4          （含頭不含尾，跟 C 一樣）
      range(1, 10, 2)   ->  1 3 5 7 9        （第三個是步長 = i += 2）
      range(5, 0, -1)   ->  5 4 3 2 1        （倒著跑 = i--）

-----------------------------------------------------------------
【重點：大多數時候你根本不需要 i】
-----------------------------------------------------------------

  C 要拿陣列元素，一定要透過 index：
      for (int i = 0; i < size; i++) {
          printf("%d\n", arr[i]);       <- 只能用 arr[i]
      }

  Python 可以直接把「元素」拿出來：
      for x in arr:
          print(x)                       <- x 就是元素本身，不用 arr[i]

  這是最大的思維差異。你 array2.c 是這樣寫的：

      for (int a = 0; a < size; a++) { total = total + grade[a]; }

  翻成 Python 不要寫成 for a in range(len(grade))，直接：

      for score in grade:
          total = total + score

-----------------------------------------------------------------
【真的需要 index 的時候：enumerate】
-----------------------------------------------------------------

  你筆記寫過 enumerate，它一次給你「編號 + 元素」兩個東西：

      for i, x in enumerate(["a", "b", "c"]):
          print(i, x)        # 0 a / 1 b / 2 c

  等於 C 的 for(i=0;...;i++) 加上 arr[i]，但兩個都幫你準備好了。

-----------------------------------------------------------------
【小提醒：Python 沒有 do-while】
-----------------------------------------------------------------

  C:       do { ... } while (cond);
  Python:  while True:
               ...
               if not cond:
                   break

=================================================================
【練習】規定：不准用內建的 sum() max()，這幾題就是要練 for
=================================================================
"""


# --- 第 1 題 ---
# 算 list 的總和。用「直接拿元素」的寫法，不要用 range(len(...))
def total(nums):
    total=0
    for i in nums:
        total=total+i
    return total


# --- 第 2 題 ---
# 回傳 1 到 n 的平方和：1*1 + 2*2 + ... + n*n
# 提示：range(1, n+1)
def square_sum(n):
    total=0
    for i in range(1,n+1):
        total=total+i**2
    return total

# --- 第 3 題 ---
# 回傳「最大值在第幾個位置」（index）。有並列就回傳第一個。
# 提示：用 enumerate 同時拿到 index 和值
def index_of_max(nums):##[3, 9, 2]
    biggest=nums[0]
    address=0
    for i ,x in enumerate(nums):
        if x>biggest:
            biggest=x
            address=i

    return address
        


# --- 第 4 題 ---
# 把 list 倒過來回傳一個「新的」list（不要改到原本的，不准用 reverse/[::-1]）
# 提示：range(len(nums)-1, -1, -1) 可以倒著跑 index
def reversed_list(nums):
    answer=[]
    for i in range(len(nums)-1, -1, -1):
        answer.append(nums[i])
    return answer


# =================================================================
_original = [1, 2, 3]
_result = reversed_list(_original)
print("第1題", "OK" if total([1, 2, 3, 4]) == 10 and total([]) == 0 else f"錯，給了 {total([1,2,3,4])}，應該是 10")
print("第2題", "OK" if square_sum(3) == 14 else f"錯，給了 {square_sum(3)}，應該是 14 (1+4+9)")
print("第3題", "OK" if index_of_max([3, 9, 2]) == 1 and index_of_max([5, 1]) == 0 else f"錯，給了 {index_of_max([3,9,2])}，應該是 1")
print("第4題", "OK" if _result == [3, 2, 1] and _original == [1, 2, 3] else f"錯，給了 {_result}（原本的list現在是 {_original}，不該被改）")
