from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.flipkart.com/home-kitchen/home-appliances/refrigerators/double-door~type/pr?sid=j9e%2Cabm%2Chzg&otracker=nmenu_sub_TVs%20and%20Appliances_0_Double%20Door'

uClient2 = uReq(my_url)
page_html = uClient2.read()
uClient2.close()

page_soup = soup(page_html, "html.parser")

containers11 = page_soup.findAll("div",{"class":"_3O0U0u"}) 

filename = "Refrigerators.csv"
f = open(filename, "w", encoding='utf-8-sig')
headers = "Product, Price\n"
f.write(headers)

for container in containers11:
	title_container = container.findAll("div",{"class":"_3wU53n"})
	product_name = title_container[0].text

	price_con = container.findAll("div",{"class":"_1vC4OE _2rQ-NK"})
	try:
		price = price_con[0].text
	except:
		price = 'No Data'
	
	print("Product: " + product_name)
	print("Price: " + price)

	f.write(product_name + "," + price.replace(",", "|") + "\n")

f.close()



