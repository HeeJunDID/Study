import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=2&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}
res = requests.get(url, headers = headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
# print(res.text)
items = soup.find_all("li", attrs={"class" : re.compile("^search-product")})
# print(items[0].find("div", attrs = {"class":"name"}).get_text())
for item in items:

    # 광고 제품은 제외
    ad_badge = item.find("span", attrs = {"class" : "ad-badge-text"})
    if ad_badge:
        print("<광고는 제외>")
        continue
    name = item.find("div", attrs = {"class":"name"}).get_text() # 제품명

    # 애플 제품 제외
    if "Apple" in name:
        print("apple 제품 제외")
        continue
    price = item.find("strong", attrs = {"class" : "price-value"}).get_text() # 가격
    price = item.find("img", attrs = {"class" : "search-product-wrap-img"}).get_text() # 가격
    
    rating = item.find("em", attrs = {"class" : "rating"}) # 평점
    if rating:
        rating = rating.get_text()
    else:
        print("<평점 없는 상품 제외합니다>")
        continue
    
    total_rating = item.find("span", attrs = {"class" : "rating-total-count"}) # 평점수
    if total_rating:
        total_rating = total_rating.get_text()
        total_rating = total_rating[1:-1]
    else:
        print("<평점 수 없는 제품 제외>")
        continue
    if float(rating) >= 4.5 and int(total_rating) >= 1000:

        print("제품명:", name)
        print("가격:", price)
        print("평점:", rating)
        print('평점수:', total_rating)
        print("------------")
