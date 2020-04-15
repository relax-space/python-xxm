import re

def s18():
    while True:
        value = input("请输入密码,输入exit退出:")
        if value == "exit":
            break
        match = re.search(r"^(?=.*[a-z])(?=.*[0-9])(?=.*[A-Z])(?=.*[$#@])[a-zA-Z0-9$#@]{6,12}$",value)
        if match == None:
            print("密码输入错误")
        else:
            print(match.group(0))

if __name__ == "__main__":
    s18()