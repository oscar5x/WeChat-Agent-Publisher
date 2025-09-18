import os
import google.generativeai as genai

# 获取你的 API 密钥
# 请将你的API密钥粘贴在下面的双引号内，并确保密钥没有被任何其他人看到。
API_KEY = "AIzaSyBvRe7zzdpUYdA_gW3BKvImURweXG7t5Ms" 

genai.configure(api_key=API_KEY)

def generate_article(title):
    """
    接收一个标题，并使用 Gemini API 生成一篇完整的文章。
    """
    # 编写一个清晰、具体的提示词，来指导AI创作
    prompt = f"""
    请根据以下论文标题，创作一篇适合发布在微信公众号上的文章。
    文章要求：
    1. 标题要吸引人，使用与原标题不同的新标题。
    2. 文章结构清晰，包含引言、正文和结语。
    3. 内容深入浅出，用通俗易懂的语言解释专业知识。
    4. 篇幅适中，大约500-800字。
    5. 语气要生动有趣，能够引发读者对传统文化的兴趣。

    论文标题：
    {title}
    """

    try:
        # 创建一个GenerativeModel实例
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # 使用model.generate_content方法生成内容
        response = model.generate_content(prompt)
        
        # 从响应中提取生成的文章文本
        return response.text
    
    except Exception as e:
        print(f"生成文章时发生错误: {e}")
        return None

if __name__ == '__main__':
    # 示例使用
    test_title = "论敦煌壁画中色彩的艺术美学"
    article = generate_article(test_title)

    if article:
        print("以下是生成的文章：")
        print(article)
    else:
        print("文章生成失败。")