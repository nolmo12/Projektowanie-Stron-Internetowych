import requests
import json
from matplotlib import pyplot as plt
from bs4 import BeautifulSoup
import numpy as np

#zad 1
def check_url(url:str) -> bool:
    response = requests.get(url)
    if response.status_code > 199 and response.status_code < 300:
        return True
    return False

#zad2
def get_weather_data(city:str) -> None:
    response = requests.get("https://www.meteoprog.pl/pl/weather/"+city)
    temp_list = []
    if check_url(response.url):
        soup = BeautifulSoup(response.content, features="html.parser")
        ul = soup.find("div", class_="current-temperature").findAll("ul", class_ = "today-hourly-weather hide-scroll")
        for li in ul:
            temp = li.findAll("span", class_="today-hourly-weather__temp")
            for x in temp:
                temp_list.append(x.text.strip())

    new_temp_list = []

    for y in temp_list:
        zm = filter(lambda x : x.isdigit(), y)
        value = ''.join(list(zm))
        new_temp_list.append(value)

    plt.plot(new_temp_list)
    plt.title(city)
    plt.ylabel("Temperatura")
    plt.xlabel("Czas")
    plt.show()


print(check_url("https://powietrze.gios.gov.pl/pjp/content/api"))

get_weather_data("Warszawa")
