from selenium import webdriver

browser = webdriver.Chrome(executable_path="/home/faizan/Documents/python/pythonOOPS/chromedriver")
browser.get('https://www.apartmentguide.com/apartments/Maryland/Laurel/Briarwood-Place-Apartment-Homes/48001/')



print "Finding Buttons"
try:
	while browser.find_element_by_css_selector('a._1i1ia') is not None:
		button = browser.find_element_by_css_selector('a._1i1ia')
		print("Button Found")
		button.click()
		print("Button Clicked")
except Exception:
	pass

print("No more buttons to search")