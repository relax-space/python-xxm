import requests
from bs4 import BeautifulSoup
import urllib 

"""
下载京东商品

python.exe .\second_step\s4.py

参考：https://www.jianshu.com/p/b2d288e67fa3

"""

class JdDownloader:
    def __init__(self):
        pass
    
    def download(self,keyword):
        url = f"https://search.jd.com/Search?keyword={keyword}&enc=utf-8"
        html = self.fetchHtml(url)
        datas = self.parseHtml(html)
        return datas
    
    def fetchHtml(self,url):
        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
            }
        html = requests.get(url,headers=headers)
        html.encoding = html.apparent_encoding #为了避免乱码
        return html.text

    
    def parseHtml(self,html):
        bf = BeautifulSoup(html,"lxml")
        titles = bf.find_all(class_="p-name p-name-type-2")
        prices = bf.find_all(class_="p-price")
        #common 需要从另外的链接获取，由于只是练习，就不获取了
        #https://item.jd.com/4311178.html#comment
        comments = bf.find_all(class_="p-commit") 
        shops = bf.find_all(class_="curr-shop hd-shopname")
        # imgs = bf.select('div.p-img > a > img')
        imgs = bf.find_all(class_="p-img")
        datas =[]
        for title,price,comment,shop,img in zip(titles,prices,comments,shops,imgs):
            datas.append({
                "title":title.text.strip(),
                "price":price.text.strip(),
                "comments":comment.text.strip(),
                "shop":shop.text.strip(),
                "link":title.find_all("a")[0].get("href"),
                "img":img.find_all("a")[0].find("img").get("source-data-lazy-img"),
            })
        return datas
    

if  __name__ == "__main__":
    value = input("请输入要搜索的内容：")
    d = JdDownloader()
    d.download(value)

