"""
第 14 天：綜合實作 —— 猜拳（修掉你在 C 和 Python 都犯過的 bug）
預估 50 分鐘   這題沒有自動測試，自己執行測

=================================================================
【你這題寫過兩次，兩次都有 bug。先看懂為什麼】
=================================================================

--- bug 1：初始化放錯位置（C 和 Python 各犯一次，方向相反）---

  paper.c / guess3.c：
      int guessnumber(void) {
          srand(time(NULL));     ❌ 每次呼叫都重設種子
          return rand() % 3;     time() 是「秒」，同一秒連玩會拿到同一個答案
      }
      正解：srand() 一輩子只在 main 開頭呼叫一次

  paperscissor.py：
      answer = random.choice(computer)   ❌ 在 while 迴圈「外面」
      while run == True:                 電腦整場出同一拳
      正解：抽拳要放進迴圈裡，每輪重抽

  Python 的 random.choice() 不用 srand，import random 就能直接用。

--- bug 2 & 3：複製貼上疊 if，必漏 ---

  paper.c（剪刀=0 石頭=1 布=2）：
      case 0:  if (guess_number == 1) win;    ❌ 剪刀對石頭是輸！應該是 ==2
      case 1:  if (guess_number == 0) win;    ✅
      case 2:  if (guess_number == 1) win;    ✅

  paperscissor.py：
      elif player == "布":
          if answer == "石頭":  print("剪刀")   ❌ 該印 win
          if answer == "石頭":  print("win")    ❌ 同一個條件寫兩次，永遠到不了

  同一題、不同語言、不同時間，各漏一種組合。
  這不是粗心 —— 是「用複製貼上處理 9 種組合」這個方法本身有問題。

=================================================================
【根治法：把規則放進 dict（第 08 天練過）】
=================================================================

      BEATS = {"剪刀": "布", "石頭": "剪刀", "布": "石頭"}
      #         ↑ key 打敗 value

      if player == computer:            平手
      elif BEATS[player] == computer:   玩家贏
      else:                             玩家輸

      9 種組合、0 次複製貼上、不可能漏。規則只寫一次。

      小技巧：list(BEATS) 直接拿到 ["剪刀","石頭","布"]
              random.choice(list(BEATS)) 就能抽拳，不用另開一個 list
              player not in BEATS 就能檢查輸入合不合法

=================================================================
【規格】
=================================================================

  judge(player, computer)
      回傳 "draw" / "win" / "lose"（win = 玩家贏）
      ⚠️ 裡面【不准 print】，if 最多 3 個
      （這題你第 08 天已經寫過了，直接搬過來）

  play_round()
      1. random.choice 抽電腦的拳 ← 每輪都要重抽！
      2. 印出雙方出拳
      3. 呼叫 judge，印中文結果
      4. return 結果字串

  main()
      wins = loses = draws = 0
      while 迴圈：
        - 輸入 q -> break
        - 不在 BEATS 裡 -> 印提示，continue（這局不算）
        - 呼叫 play_round，依回傳值計分
      結束印統計：「X勝 Y敗 Z平，勝率 NN.N%」
      ⚠️ 一局沒玩就按 q，算勝率會 ZeroDivisionError -> 先判斷（第 11 天）

【自我檢查】
  [ ] 連玩 5 局，電腦出拳不是每次都一樣（bug 1）
  [ ] 布 vs 石頭 -> 你贏（Python 版 bug 2）
  [ ] 剪刀 vs 石頭 -> 你輸（C 版 bug）
  [ ] judge 裡沒有 print，if 不超過 3 個
  [ ] 一局沒玩直接 q，不會紅字當掉
"""

import random

BEATS = {"剪刀": "布", "石頭": "剪刀", "布": "石頭"}


def judge(player, computer):
    pass


def play_round():
    pass


def main():
    pass


main()
