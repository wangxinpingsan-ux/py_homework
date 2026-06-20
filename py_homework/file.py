import os


str = "d:\\Users\\lucas\\Desktop\\meet\\1.PNg"
print(str)

if os.path.exists(str):
    print("存在")
    if os.path.isfile(str):
        print ("是檔案")
    elif os.path.isdir(str):
        print("是目錄")
else:
    print("不存在")

