from flask import Flask
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def homepage():
    try:
        # 抓取 travelweekly 首頁內容
        url = "https://www.travelweekly.com/"
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; MyBot/1.0; +http://example.com/bot)"
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        # 使用 BeautifulSoup 解析 HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # 簡單抓出首頁的前幾個標題（以 h3 為例）
        headlines = soup.find_all("h3", limit=5)
        items = [h.get_text(strip=True) for h in headlines if h.get_text(strip=True)]

        # 組合成 HTML 回應
        result = "<h1>TravelWeekly Headlines</h1><ul>"
        for item in items:
            result += f"<li>{item}</li>"
        result += "</ul>"

        return result

    except Exception as e:
        return f"<p>Error fetching data: {str(e)}</p>"

if __name__ == "__main__":
    app.run()