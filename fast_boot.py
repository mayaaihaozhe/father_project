import requests
from bs4 import BeautifulSoup

def get_movies():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537',
        'Host': 'movie.douban.com'
    }
    movie_list = []
    for i in range(0,1):
        link = 'https://movie.douban.com/top250?start=' + str(i * 10)
        r = requests.get(link, headers=headers, timeout=10)
        print(str(i+1), "页响应状态码:", r.status_code)
        
        soup = BeautifulSoup(r.text, "html.parser")
        div_list = soup.find_all('div', class_='hd')
        for each in div_list:
            movie = each.a.span.text.strip()
            movie_list.append(movie)
    return movie_list[:10]

movies = get_movies()
print("豆瓣电影排行前十：")
for i in range(len(movies)):
    print(f"第{i+1}名：{movies[i]}")
