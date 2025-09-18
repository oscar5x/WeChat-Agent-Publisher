import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

def search_cnki_with_selenium(keyword):
    """
    使用Selenium模拟浏览器行为在知网搜索论文，并返回标题列表。
    """
    driver = None
    try:
        # 创建一个 Service 对象，指定 ChromeDriver 的路径
        # 确保 chromedriver.exe 文件与你的脚本在同一目录下
        service = Service(executable_path='./chromedriver.exe')
        
        # 启动 Chrome 浏览器
        driver = webdriver.Chrome(service=service)
        driver.get("https://kns.cnki.net/kns8/defaultresult/index")
        
        print(f"浏览器已打开，正在搜索关于“{keyword}”的论文...")

        # 找到搜索框并输入关键词
        search_box = driver.find_element(By.ID, 'txt_search')
        search_box.send_keys(keyword)
        search_box.send_keys(Keys.RETURN)

        # 等待页面加载，这里设置较长时间以确保数据加载完毕
        time.sleep(10)
        
        # 使用我们通过开发者工具找到的更精确的 CSS 选择器
        # 找到所有论文标题元素
        title_elements = driver.find_elements(By.CSS_SELECTOR, 'div.module-wrap-aside a')
        
        titles = [element.text.strip() for element in title_elements]
        
        return titles
        
    except Exception as e:
        print(f"发生错误: {e}")
        print("未能获取到论文标题，请检查网络连接或代码中的选择器。")
        return []
    finally:
        if driver:
            driver.quit()  # 无论是否成功，最后都关闭浏览器，释放资源

if __name__ == '__main__':
    search_keyword = "传统壁画"
    paper_titles = search_cnki_with_selenium(search_keyword)
    
    if paper_titles:
        print("以下是获取到的部分论文标题：")
        for i, title in enumerate(paper_titles, 1):
            print(f"{i}. {title}")
    else:
        print("未能获取到论文标题。")