import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import time

# 設定搜尋的關鍵字
keywords = ["Roots品牌", "加拿大休閒品牌"]

# Google 搜尋 URL
search_url = "https://www.google.com/search"

# 設定 headers 模擬瀏覽器行為
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    )
}

# 用來儲存搜尋結果的資料
search_results = []

# 抓取 Google 搜尋自然排名的資料
def fetch_google_search_results(keyword, pages=20):
    global search_results
    for page in range(pages):
        print(f"正在抓取關鍵字: {keyword} 第 {page + 1} 頁...")
        params = {"q": keyword, "start": page * 10}
        response = requests.get(search_url, headers=headers, params=params)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            search_elements = soup.find_all("div", class_="tF2Cxc")  # 自然排名容器
            
            for element in search_elements:
                title = element.find("h3")  # 標題
                description = element.find("div", class_="VwiC3b")  # 描述
                url_tag = element.find("a", href=True)  # 超連結

                # 確保資料完整
                if title and description and url_tag:
                    search_results.append({
                        "標題": title.get_text(),
                        "描述": description.get_text(),
                        "超連結": url_tag["href"],
                        "抓取時間": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    })
        else:
            print(f"第 {page + 1} 頁請求失敗，狀態碼: {response.status_code}")

        # 延遲請求以避免被封鎖
        time.sleep(5)

# 儲存資料到 Excel
def save_to_excel(data, filename):
    if not data:
        print("沒有資料可以儲存！")
    else:
        df = pd.DataFrame(data, columns=["標題", "描述", "超連結", "抓取時間"])
        df.to_excel(filename, index=False)
        print(f"資料已儲存為 {filename}")

# 主程式
if __name__ == "__main__":
    for keyword in keywords:
        fetch_google_search_results(keyword)

    # 儲存到 Excel
    filename = "11211242_關鍵字_google自然排名結果.xlsx"  # 使用你的學號命名
    save_to_excel(search_results, filename)
