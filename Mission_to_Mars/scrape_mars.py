import pandas as pd
#dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs 

# def init_browser():
#     executable_path = {'executable_path': 'C:/Users/Tomas Faria/Desktop/chromedriver.exe'}
#     return Browser('chrome', **executable_path, headless=False)

def scrape():

    results = {}
    
    executable_path = {'executable_path': 'C:/Users/Tomas Faria/Desktop/chromedriver.exe'}

    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    browser.is_element_present_by_css('ul.item_list li.slide', wait_time=2)
    soup = bs(browser.html)
    title = soup.find('div', 'content_title').get_text()
    news_p = soup.find('div', 'article_teaser_body').get_text()
    results['news_title'] = title
    results['news_paragraph'] = news_p

    #2
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    full_image_btn = browser.find_by_id('full_image')
    full_image_btn.click()
    browser.is_element_present_by_text('more info', wait_time=1)
    more_info_btn = browser.find_link_by_partial_text('more info')
    more_info_btn.click()
    soup = bs(browser.html)
    image_url_rel = soup.select_one('figure.lede a img').get('src')
    image_url = f'https://www.jpl.nasa.gov{image_url_rel}'
    results['featured_image'] = image_url

    #3
    df = pd.read_html('https://space-facts.com/mars/')[0]
    df.columns = ['decription', 'value']
    df.set_index['description', inplace = True]
    results['facts'] = df.to_html(classes = 'table table-stripped')

    #4
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    hemispheres = []
    links = browser.find_by_css('a.product-item h3')

    for i in range(len(links)):
        hemi = {}
        browser.find_by_css('a.product-item h3')[i].click()
        sample_elm = browser.find_link_by_text('Sample').first()
        image_url = sample_elm['href']
        title = browser.find_by_css('h2.title').text
        hemi['title'] = title
        hemi['image_url'] = image_url
        hemispheres.append(hemi)
        browser.back()
    results['hemispheres'] = hemispheres


    return (results)

# print(scrape)


