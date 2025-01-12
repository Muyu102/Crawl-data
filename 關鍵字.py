import requests
import pandas as pd
from datetime import datetime

# Google API 配置
API_KEY = ""
CX = ""

# 搜尋的關鍵字
keywords = ["Roots品牌", "加拿大休閒品牌"]

# 收集的資料
ad_data = []

# 定義函式來抓取廣告資料
def fetch_ads_data(keyword, num_results=50):
    results = []
    start_index = 1  # API 的搜尋結果起始索引
    while len(results) < num_results:
        # 構建 API URL
        url = "https://www.googleapis.com/customsearch/v1"
        params = {
            "key": API_KEY,
            "cx": CX,
            "q": keyword,
            "start": start_index,
        }

        # 發送請求
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
        except requests.RequestException as e:
            print(f"請求失敗: {e}")
            break

        # 提取廣告結果
        for item in data.get("items", []):
            title = item.get("title", "無標題")
            snippet = item.get("snippet", "無描述")
            link = item.get("link", "無連結")
            results.append({
                "標題": title,
                "描述": snippet,
                "超連結": link,
                "抓取時間": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            })

        # 更新起始索引
        start_index += 10

        # 如果沒有更多結果，提前退出
        if "nextPage" not in data.get("queries", {}):
            break

    return results[:num_results]

# 主程式
if __name__ == "__main__":
    for keyword in keywords:
        print(f"正在抓取關鍵字: {keyword}")
        ads = fetch_ads_data(keyword, num_results=200)
        ad_data.extend(ads)
        print(f"完成關鍵字 {keyword} 的抓取，共獲得 {len(ads)} 筆資料。")

    # 儲存結果到 Excel
    if ad_data:
        filename = "11211242_關鍵字_google廣告結果.xlsx"
        df = pd.DataFrame(ad_data, columns=["標題", "描述", "超連結", "抓取時間"])
        df.to_excel(filename, index=False)
        print(f"資料已儲存為 {filename}")
    else:
        print("沒有資料可儲存！")
