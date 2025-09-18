import os

def check_chromedriver_exists():
    """
    检查当前目录下是否存在 chromedriver.exe 文件。
    """
    driver_name = "chromedriver.exe"
    if os.path.exists(driver_name):
        print(f"✅ 找到 {driver_name} 文件！它位于当前目录下。")
        return True
    else:
        print(f"❌ 未找到 {driver_name} 文件。")
        print("请将 chromedriver.exe 移动到与你的 Python 脚本相同的文件夹中。")
        return False

# 运行检查函数
if __name__ == "__main__":
    check_chromedriver_exists()