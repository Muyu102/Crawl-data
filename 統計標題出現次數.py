import pandas as pd

# 載入資料
file_path = r"C:\Users\Xuan\Downloads\11211242_關鍵字_google廣告結果.xlsx"
df = pd.read_excel(file_path)

# 計算每個廣告標題的出現次數
most_frequent_ad = df["標題"].value_counts().idxmax()  # 出現次數最多的標題

# 篩選最常出現的廣告資料
frequent_ad_data = df[df["標題"] == most_frequent_ad]

# 轉換 "抓取時間" 為 datetime 格式
frequent_ad_data["抓取時間"] = pd.to_datetime(frequent_ad_data["抓取時間"])

# 提取小時範圍
frequent_ad_data["小時"] = frequent_ad_data["抓取時間"].dt.hour

# 分析時段分佈
hour_distribution = frequent_ad_data["小時"].value_counts().sort_index()

# 輸出結果
print(f"最常出現的廣告標題是：{most_frequent_ad}")
print("該廣告的播放時段分佈:")
print(hour_distribution)
