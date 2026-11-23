import requests
from bs4 import BeautifulSoup
def search_web(query,max_results=4):
    try:
        r=requests.get("https://html.duckduckgo.com/html/",params={"q":query},headers={"User-Agent":"Mozilla/5.0"},timeout=15);r.raise_for_status()
        soup=BeautifulSoup(r.text,"html.parser");out=[]
        for item in soup.select(".result")[:max_results]:
            a=item.select_one(".result__a");s=item.select_one(".result__snippet")
            if a:out.append({"title":a.get_text(" ",strip=True),"url":a.get("href",""),"snippet":s.get_text(" ",strip=True) if s else ""})
        return out
    except Exception:return []
