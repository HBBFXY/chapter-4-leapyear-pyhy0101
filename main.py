while True:
    try:
        # 获取用户输入并转换为整数
        year = int(input("请输入一个年份（输入0退出）："))
        
        # 检查是否退出程序
        if year == 0:
            print("程序已退出。")
            break
        
        # 判断是否为闰年
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f"{year}年是闰年")
        else:
            print(f"{year}年不是闰年")
            
    except ValueError:
        # 处理非数字输入的情况
        print("请输入有效的数字年份")
