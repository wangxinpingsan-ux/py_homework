email=(str(input("enter your email ")))
index=email.index("@")
hint=email.find("@")
print(f"@ is in {hint+1}")
print(f"{email[0:index]}")
print(f"{email[index+1:]}")

print(f"{email.replace("@",""" \

""")}")