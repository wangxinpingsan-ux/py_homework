# 這個 repo 是什麼

wangxinping（albert）的 Python 練習。他有紮實的 C 基礎，正在補 Python 語法。
這份檔案是給 Claude Code 讀的交接單——換一台電腦或開新對話時，讀完這裡就能接上進度。

---

## 一、學習者背景（最重要，先讀這段）

**他不是程式初學者，是 Python 初學者。** 這兩件事差很多。

他的 C 資料夾（另一台電腦的 `C:\C_Desktop`，共 51 個檔案、3 個 repo）證明程式觀念是有的：

- 函式原型宣告（`float bmi(float h, float w);` 寫在 main 前面）
- 用指標參數一次回傳多個值（`void find_maxmin(int array[], int *max, int *min)`）
- `malloc` / `free` / 用完設 `NULL`
- 自己寫得出 `&ptr[i] == &(*(ptr+i))` 這種註解

但他的 55 個 Python 檔案裡，**只有 2 個有 `def`**，其餘全是 top-level 腳本。

> **結論：不是不會函式，是沒把 C 的習慣搬到 Python。**

### 因此教學方式是

- **用 C 對照來教**：「你 C 用指標回傳兩個值，Python 直接 `return a, b`」
- **不要從「什麼是函式／迴圈／條件」教起**，那對他是浪費時間
- **C 沒有的東西要當全新概念仔細教**：dict、可變/不可變、生成式、try/except、切片

---

## 二、教學風格：給提示，不給答案

- 先**肯定他做對的具體細節**，再指出一個要改的地方，附上為什麼
- 卡住時**問他怎麼想的**，再給下一步提示——不要貼解答
- 用**他自己寫過的檔案**當正反例，比抽象說明有效得多
- 他只在真的卡死（說「我真的不會」）時才給完整骨架，並要求他自己重打一遍

**為什麼**：他的目標是自己寫得出來，不是看懂。真正變強的是「卡住又脫困」那段。

### 一個實例

第 5 天他寫 `for c in "aeiou": if c in s: count += 1`，結果錯了。
我一開始直接說「迴圈跑錯對象」，但他回「我是想先用 a 比 s、再用 e 比 s」——
**他的策略其實是對的**，只差把 `if c in s` 換成 `count += s.count(c)`。

教訓：先問他怎麼想的，再判斷哪裡要修。

---

## 三、進度

作業在 `py_homework/homework/`，共 15 個檔案，設計為一天一題。

| 天 | 檔案 | 狀態 |
|---|---|---|
| 00 | `00_warmup.py` | ✅ |
| 01 | `01_syntax.py` 縮排/`//`/沒有 `i++`/`&&`→`and` | ✅ |
| 02 | `02_input.py` input 回傳 str、`map(int,...)` | ✅ |
| 03 | `03_for.py` `for x in list`、`enumerate` | ✅ |
| 04 | `04_list.py` 負索引、切片、可變性 | ✅ |
| 05 | `05_string.py` `==` 直接比、不可變 | ✅ |
| 06 | `06_tuple.py` `return a, b` 取代指標 | ✅ |
| 07 | `07_fstring.py` `printf` → f-string | ✅ |
| **08** | **`08_dict.py`** C 沒有的東西、用 dict 取代疊 if | **← 下一個** |
| 09 | `09_mutable.py` 可變/不可變傳參 | 未開始 |
| 10 | `10_comprehension.py` 生成式 | 未開始 |
| 11 | `11_tryexcept.py` try/except | 未開始 |
| 12 | `12_file.py` `with open()` | 未開始 |
| 13 | `13_vending.py` 綜合：販賣機 | 未開始 |
| 14 | `14_rps.py` 綜合：猜拳 | 未開始 |

`homework/old/` 是作廢的舊版（從「什麼是函式」教起那版，對他太簡單）。
進度表另見 `py_homework/homework/README.md`。

線上進度頁（我做的）：https://claude.ai/code/artifact/379a2e3b-6924-4dc9-a44e-daaf27162e05

---

## 四、批改流程（照做，不要跳步驟）

他說「hwN 好了」時：

1. `ls -l` 看 **mtime**——他常忘記在 VSCode 按 `Ctrl+S`，檔案沒變過（發生過兩次）。
   mtime 沒變就先請他存檔，不要懷疑他沒寫。
2. 讀他寫的部分 + 執行檔案看自動測試。
3. **一定要另外跑刁鑽測資**：負數、空的、只有一個元素、全部一樣、有重複。

### 第 3 步為什麼是必要的

**八天之內出現六次「測試印 OK 但程式其實是錯的」**，每次都是測資剛好避開 bug：

| 天 | Bug | 為什麼矇混過關 |
|---|---|---|
| 01 | 閏年不是閏年時掉出函式尾端，回傳 `None` | 測試寫 `not is_leap(1900)`，而 `not None` 也是 `True` |
| 03 | 倒轉 list 時 `append(i)` 而不是 `append(nums[i])` | 測資 `[1,2,3]` 的值剛好等於編號 |
| 03 | 找最大值用 `max = 0` 當起始值 | 測資沒有全負數的情況 |
| 05 | 數母音用 `if c in s`，每個母音最多算 1 | 測資 `"hello"` 的 e、o 剛好各出現一次 |
| 07 | 百分比沒寫 `:.1f` | 測資 9/20 剛好整除成 45.0 |
| 07 | 靠右對齊自己打三個空白 | 測資 42 剛好是兩位數 |

---

## 五、他的三個固定弱點

### 1. 手工做掉語言已內建的機制（最一致，四次）

C 什麼都要自己刻，那個反射很深。

| 題目 | 他手工做的 | Python 早就有的 |
|---|---|---|
| 04 前三個 | `if len(nums) >= 3` | 切片自動截斷 |
| 06 拆時間 | `s - 3600*(s//3600)` | `s % 3600` |
| 07 百分比 | 直接印，沒指定位數 | `:.1f` |
| 07 靠右對齊 | 自己打三個空白 | `:>5` |

提醒他：遇到格式化、邊界檢查、重複處理，**先假設 Python 有內建再查**。

### 2. 跨語言重複的三個錯誤（C 和 Python 各犯一次）

- **初始化放錯位置**：`guess3.c`/`paper.c` 把 `srand(time(NULL))` 放函式裡（每次呼叫重設種子）；`paperscissor.py` 把 `random.choice()` 放 while 迴圈外（整場同一拳）
- **複製貼上疊 if 必漏**：`paper.c` 的 `case 0`（剪刀）判斷寫錯；`paperscissor.py` 的「布」那段印成「剪刀」。根治法是 `BEATS` 字典——**第 8 天和第 14 天會做**
- **魔術數字寫死**：`array2.c` 有 `#define size` 卻寫 `total / 10.0`；`2D.py` 寫死 `range(4)`/`range(3)`

### 3. 縮排與空格

同一個函式出現過 2、4、6、7 格混用；運算子兩邊不留空格（`year%4==0`）。
曾建議設定 VSCode 存檔自動排版（`editor.formatOnSave`），**他還沒回應要不要設定**。

---

## 六、他做得好的地方（也要記得肯定）

- 第 5 天自己選擇「跑字串」而不是「跑母音表 + count」，理由是「重複問題自動消失」——**這個工程判斷是對的**
- `join` / `map(str, ...)` 從問「怎麼用」到完全掌握只花一天
- 抓出我教材裡的矛盾：「`s.upper()` 不改自己、`a.sort()` 改自己，不是說概念一樣嗎」——`04_list.py` 原本的判斷法則確實寫錯，已修正
- BMI 那題自己回頭翻 `bmifunction.c` 把公式修對

---

## 七、環境

- Python 3.14.6，Windows 11，VSCode
- 執行含中文的腳本前設 `PYTHONIOENCODING=utf-8`，否則管線輸出會亂碼
- 他有 4 個 GitHub repo（`wangxinpingsan-ux`）：`py_homework`、`C_homework`、`pointer_practice`、`array-practice`。後三個還沒有 `.gitignore`，`C_homework` 還在追蹤 `guess.exe`
- 他也在玩 The Farmer Was Replaced（用 Python 寫程式的遊戲），存檔在
  `AppData\LocalLow\TheFarmerWasReplaced\...\Saves\Save0\main.py`，是很好的練習素材

## 八、待決定的事

- `2074d21` 這個 commit 的訊息開頭多了一個 `@`（我用錯語法造成的）。修的話要 amend + force push，他還沒決定
- `C_homework` / `pointer_practice` / `array-practice` 要不要也加 `.gitignore`
