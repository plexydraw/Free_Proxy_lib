import requests
from bs4 import BeautifulSoup

def lista_free_proxy_list():
 
    url = "https://free-proxy-list.net/"
    HEADERS = {'User-Agent': 'Mozilla/5.0'}  
    r = requests.get(url, headers=HEADERS, timeout=10)
    
    soup = BeautifulSoup(r.text, "html.parser")
    
    filas = soup.find("tbody").find_all("tr")
    proxies = []
    
    for fila in filas:
        campos = fila.find_all("td")
        proxy_ip = campos[0].text
        proxy_puerto = campos[1].text
        proxy_tipo = campos[4].text
        
        if proxy_tipo == "elite proxy":
    
            proxy = f'{proxy_ip}:{proxy_puerto}'
            proxies.append(proxy)
    i = 0
    for proxy in proxies:
        i += 1
        print(f"proxy [ {i} ]")
        print(f"     {proxy}\n")
    
    return {
        "origen": "Free Proxy List",
        "lista": proxies
    }

proxies = lista_free_proxy_list()

