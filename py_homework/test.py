def pascal_a(n):
    # 改名 tri：原本叫 all 會蓋掉 Python 內建的 all() 函式
    # range(n) 就好：原本 range(1, n+1, 1) 只是要跑 n 次，變數也沒用到
    tri = [[0] * (2 * n + 1) for _ in range(n)]
    tri[0][n] = 1  # 頂點放正中央

    for i in range(n - 1):
        for j in range(2 * n - 1):
            # 下一列第 j+1 格 = 這一列的左上(j) + 右上(j+2)
            tri[i + 1][j + 1] = tri[i][j] + tri[i][j + 2]

    for row in tri:
        # 0 印成空白，三角形才看得出形狀（原版印 0 會變成一整塊數字牆）
       answer= [str(v) if v else " " for v in row]

print(answer)