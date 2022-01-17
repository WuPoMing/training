# 抓取 Medium 的文章資料
import urllib.request as req
url="https://medium.com/_/graphql"
# 建立一個 Request 物件，附加 Requeest 的資訊
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8") # 根據觀察，取得資料是 JSON 格式

# 解析 JSON 格式的資料，取得每篇文章的標題
import json
data=data.replace("[","")
data=json.loads(data) # 把原始的 json 資料解析成字典/列表的表示形式
# 取的 JSON 資料中的文章標題
post=data["payload"]["references"]["Post"]
for key in post:
    post=post[key]
    print(post["title"])