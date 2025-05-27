import requests
from bs4 import BeautifulSoup
# 設定目標網址格式
base_url = "https://www.tradingview.com/news-flow/"
# base_url = "https://news.cnyes.com/news/cat/all"
# 定義分類
categories = [
    "activitiesCategory/theme-Luxury",
    "activitiesCategory/theme-Naturalwonders",
    "activitiesCategory/theme5",
    "activitiesCategory/theme-ART",
    "activitiesCategory/theme-Seasonallimitededit hiion",
    "activitiesCategory/theme-Zuwaigani",
    "activitiesCategory/China-theme",
    "activitiesCategory/Theme-OneEncounter-OneChance",
    "activitiesCategory/theme-Festival",
    "activitiesCategory/theme-Hygge" ]
    # 設定請求標頭，避免被網站封鎖
headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36" }
# 遍歷分類
for category in categories:
    url=base_url # .format(category)  # 生成對應的網址
    print(f"\n========= START WAR {category} =========\n")
    try:
      response=requests.get(url,headers=headers,timeout=10)
      response.raise_for_status() # 檢查請求是否成功
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Fail ...", e)
        continue# 跳過當前分類，進入下一個分類
     # 解析 HTML
    soup = BeautifulSoup(response.text,"html.parser")
     # 找
    search_results = soup.find_all(string=lambda text: "%" in text if text else False)
# 輸出結果
    if search_results:
        for result in search_results:
          print(f"[{category}] 找到: {result.strip()}")
    else:
        print(f"[{category}] ❌ Still Fail ...")
    print("=" * 95)  # 分隔線
