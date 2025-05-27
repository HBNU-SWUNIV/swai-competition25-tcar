import requests

url = "http://localhost:8000/evaluate-site"

payload = {
    "url": "https://www.naver.com",
    "html": """
    <html lang="ko">
      <head>
        <meta charset="utf-8">
        <meta name="description" content="네이버 메인에서 다양한 정보와 검색을 만나보세요.">
        <title>NAVER</title>
      </head>
      <body>
        <h1>네이버에 오신 것을 환영합니다</h1>
        <p>뉴스, 쇼핑, 블로그 등 다양한 서비스를 제공합니다.</p>
      </body>
    </html>
    """,
    "meta": """
    <meta charset="utf-8">
    <meta name="description" content="네이버 메인에서 다양한 정보와 검색을 만나보세요.">
    <meta name="keywords" content="뉴스, 쇼핑, 검색, 메일">
    """
}

response = requests.post(url, json=payload)

print("🔎 상태 코드:", response.status_code)
print("📦 응답 결과:", response.json())
