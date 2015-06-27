from selenium import webdriver
from lxml import html, etree
from pyvirtualdisplay import Display

display = Display(visible=0, size=(1024, 768))
display.start()

def rutenAPI(url):

	# browser = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true --ssl-protocol=any'])
	browser = webdriver.Firefox()
	browser.get(url)

	html = etree.HTML(browser.page_source)

	def ship_iter():
		# methods = html.xpath("//li[@class='ship']/ul/li/text()")
		cost = html.xpath("//li[@class='ship']/ul/li/span[@class='cost']/text()")
		ship = html.xpath("//li[@class='ship']/ul/li/span[@class='ship-type']/text()")
		method_counts = int(html.xpath("count(//li[@class='ship']/ul/li)"))
		result = [ship[a-2] + "/" + cost [a-2] for a in range(0, method_counts)]
		return(result)
0
	title = html.xpath(u"//h2/text()")
	init_price = html.xpath(u"//li[@class='initiation']/span/text()")
	buyout_price = html.xpath(u"//li[@class='price']/span/span[@class='dollar']/text()")
	pay_methods = html.xpath(u"//li[@class='pay']/ul/li/text()")
	ship_methods = ship_iter()
	remain = html.xpath(u"//ul[@class='quantity']/li[@class='remain-count']/span/span[@class='number']/text()")
	sold = html.xpath(u"//ul[@class='quantity']/li[@class='sold-count']/span/span[@class='number']/text()")
	# [0] is remaining stock and [1] is sold

	print("Title:", title)
	print("Buyout Price:", buyout_price)
	print("Initial Price:", init_price)
	print("Stock / Total Sold: ", remain, "/", sold)
	print("Payment Methods:", pay_methods)
	print("Shipping Methods / Cost", ship_iter())

	browser.close()

rutenAPI("http://goods.ruten.com.tw/item/show?21452063121287")