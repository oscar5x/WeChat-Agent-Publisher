import requests
from bs4 import BeautifulSoup

def get_baidu_hot_topics():
    """
    爬取百度热搜榜并返回热点话题列表。
    """
    url = "http://www.baidu.com"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 如果请求不成功，会抛出异常
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 寻找热搜榜的 HTML 元素，这通常需要根据网站结构进行调整
        # 这里以一个常见的例子作为参考，实际可能需要检查百度页面的最新结构
        topic_elements = soup.select('.s-top-list-content-op a') 
        
        topics = [element.get_text().strip() for element in topic_elements]
        return topics
        
    except requests.RequestException as e:
        print(f"请求失败: {e}")
        return []

if __name__ == '__main__':
    print("正在获取百度热搜榜...")
    topics = get_baidu_hot_topics()
    if topics:
        print("以下是获取到的热点话题：")
        for i, topic in enumerate(topics, 1):
            print(f"{i}. {topic}")
    else:
        print("未能获取到热点话题。")
