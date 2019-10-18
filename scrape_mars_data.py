from bs4 import BeautifulSoup
import pandas as pd


def init_browser():
	return Browser("chrome",headless=false)
	
def scrape():
	browser = init_browser
	url = "https://mars.nasa.gov.news"
	browser.visit(url)
	
	bs_version = BeautifulSoup(browser.html, 'html.parser' )
	content_titles = bs_version.find_all(class_="content_title")
	paragraphs = bs_version.find_all(class_="article_teaser_body")
	featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'
	mars_image = browser.visit(featured_image_url)
	
	news_url = "https://twitter.com/marswxreport?lang=en"
	mars_news = browser.visit(news_url)
	bs_news = BeautifulSoup(browser.html, 'html.parser' )
	
	facts_url = "https://space-facts.com/mars/"
	facts_tables = pd.read(facts_url)
	
	#falling asleep, will continue tommorow on Fri 10/18/2019
	
	hemisphere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
	hemisphere_info = browser.visit(hemisphere_url)
	bs_hemisphere = BeautifulSoup(browser.html, 'html.parser' )
	
	#watched Astros kick the Yankees ass in their own stadium last night

	hemisphere_items = hemisphere_url.find_all("div",class_="item")
	item_list = "[]"
	for item in item_list:
		anchor_tag = item_find("a")
		href_attribute = anchor_tag["href"]
		item_list.append({"", "anchor_tag":hemisphere_url + href_attribute})
		
	return item_list