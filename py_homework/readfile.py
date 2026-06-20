readfile="d:\\Users\\lucas\\Desktop\\程式\\py_readfile.txt"
try:
 with open (readfile) as file:
    print(file.read())
except FileNotFoundError:
  print("檔案不存在")