import pandas as pd

# 建立一個簡單的資料表
data = {
    '姓名': ['小明', '小華', '小紅'],
    '分數': [90, 85, 95]
}
df = pd.DataFrame(data)

# 印出結果
print("Pandas 測試成功！資料如下：")
print(df)
