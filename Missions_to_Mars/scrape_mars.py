import requests
from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd
import warnings
warnings.simplefilter("ignore")


def scrape():
    

    url="https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')


    print(soup.prettify())


    news_title=soup.find('div', class_="content_title").text

    print(news_title)


    news_p= soup.find('div', class_="rollover_description_inner").text


    print(news_p)


    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)


    url_jpl = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_jpl)


    html = browser.html
    soup_jpl = bs(html, 'html.parser')
    print(soup_jpl.prettify)


    featured_image=soup_jpl.find('a', class_='button fancybox')['data-fancybox-href']


    featured_image_url='https://www.jpl.nasa.gov'+featured_image


    url="https://twitter.com/marswxreport?lang=en"
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')


    print(soup.prettify)


    mars_weather=soup.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text


    print(mars_weather)



    url="https://space-facts.com/mars/"
    response=requests.get(url)
    soup=bs(response.text,"html.parser")


    mars_fact=soup.find("table",id="tablepress-p-mars-no-2")


    print(mars_fact)


    table_rows = mars_fact.find_all('tr')


    data=[]
    for tr in table_rows:
        td = tr.find_all('td')
        row = [i.text for i in td]
        data.append(row)
    data


    mars_table=pd.DataFrame(data,columns=("fact","measurement"))



    hemisphere_image_urls = [
        {"title": "Cerberus Hemisphere Enhanced", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
        {"title": "Schiaparelli Hemisphere Enhanced", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
        {"title": "Syrtis Major Hemisphere Enhanced", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
        {"title": "Valles Marineris Hemisphere Enhanced", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg"},
    ]

    alldata={
        "news_title":news_title,
        "new_p":news_p,
        "featured_image_url": featured_image_url,
        "mars_weather":mars_weather,
        "mars_fact":mars_table,
        "hemisphere":hemisphere_image_urls
        }

    return alldata
 

