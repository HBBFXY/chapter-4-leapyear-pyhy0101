# 闰年判断程序
# 规则：能被4整除但不能被100整除，或者能被400整除的年份是闰年
try:
    # 获取用户输入的年份
    year = int(input("请输入一个年份: "))
    # 判断是否为闰年
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year}年是闰年")
    else:
        print(f"{year}年不是闰年")
except ValueError:
    print("请输入有效的数字年份")
