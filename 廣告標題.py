import pandas as pd
from collections import Counter

# 讀取 Excel 檔案
df = pd.read_excel(r"C:\Users\Xuan\Downloads\11211242_關鍵字_google廣告結果.xlsx")

# 合併所有描述
all_descriptions = " ".join(df["描述"].dropna())

# 計算詞頻
description_word_counts = Counter(all_descriptions.split())

# 輸出前10大字詞
print("廣告描述中最常出現的前10大字詞:")
print(description_word_counts.most_common(10))
