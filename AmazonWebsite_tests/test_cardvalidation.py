from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

PATH = "C:\\Users\\jchoe\\Downloads\\chromedriver_win32 (5)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("http://www.amazon.com")

def searchByTextAndSelectTheFirstItem(text):
    elem = driver.find_element_by_id("twotabsearchtextbox")
    elem.send_keys(text)
    driver.find_element_by_id("nav-search-submit-button").click()
    driver.find_element_by_xpath("//*[@class='a-section aok-relative s-image-square-aspect']/img").click()
    sleep(2)
   
print("Test Case 1 : Search for hats for men and validate price")
searchByTextAndSelectTheFirstItem("hats for men")
driver.find_element_by_class_name("a-dropdown-label").click()
driver.find_element_by_xpath("//*[@class='a-dropdown-item'][2]").click()
driver.find_element_by_id("add-to-cart-button").click()
driver.find_element_by_id("nav-cart").click()
driver.find_element_by_id("sc-subtotal-amount-activecart")

menHatPriceText = driver.find_element_by_xpath("//*[@class='a-spacing-mini']/span").text
subtotalPriceText = driver.find_element_by_xpath("//*[@id='sc-subtotal-amount-activecart']/span").text
menHatPrice = menHatPriceText.replace("$","")
subtotalPrice = subtotalPriceText.replace("$","")

menHatPriceAmount = float(menHatPrice)
actualsubtotalPriceAmount = float(subtotalPrice)  
expectedsubtotalPriceAmount = (menHatPriceAmount + menHatPriceAmount) 
quantity = driver.find_element_by_id("sc-subtotal-label-activecart").text

assert expectedsubtotalPriceAmount == actualsubtotalPriceAmount, "test fail - men hats price is NOT valid"
assert quantity == "Subtotal (2 items):", "test fail - men hats quantity is NOT valid"
print("Test Result : Price and quantity are correct")

print("Test Case 2 : Add hat for women to the card and validate price")
searchByTextAndSelectTheFirstItem("hats for women")
driver.find_element_by_id("add-to-cart-button").click()
driver.find_element_by_id("nav-cart").click()
driver.find_element_by_id("sc-subtotal-amount-activecart")

womenHatPriceText = driver.find_element_by_xpath("//*[@class='a-spacing-mini'][0]/span").text
menHatPriceText = driver.find_element_by_xpath("//*[@class='a-spacing-mini'][1]/span").text
subtotalPriceText = driver.find_element_by_xpath("//*[@id='sc-subtotal-amount-activecart']/span").text

womenHatPrice = womenHatPriceText.replace("$","")
menHatPrice = menHatPriceText.replace("$","")
subtotalPrice = menHatPriceText.replace("$","")

menHatPriceAmount = float(menHatPrice)
womenHatPriceAmount = float(womenHatPrice)
subtotalPriceAmount = float(subtotalPrice)
expectedsubtotalPriceAmount = (womenHatPriceAmount + menHatPriceAmount) 
quanity = driver.find_element_by_id("sc-subtotal-label-activecart").text

assert subtotalPriceAmount  == actualFullPriceText, "test fail - hats price is NOT valid"
assert quanity == "Subtotal (3 items):", "test fail - hats quantity is NOT valid"
print("Test Case 2 Result : Price and quanity are correct")

print("Test Case 3 : Update card items amount")
driver.find_element_by_xpath("//*[@id='a-autoid-2'][1]").click()
sleep(3)
driver.find_element_by_xpath("//*[@class='a-dropdown-item quantity-option'][2]").click()
driver.find_element_by_id("sc-subtotal-amount-activecart")

menHatPriceText = driver.find_element_by_xpath("//*[@class='a-spacing-mini'][0]/span").text
womenHatPriceText = driver.find_element_by_xpath("//*[@class='a-spacing-mini'][1]/span").text
subtotalPriceText = driver.find_element_by_xpath("//*[@id='sc-subtotal-amount-activecart']/span").text

menHatPrice = menHatPriceText.replace("$","")
womenHatPrice = womenHatPriceText.replace("$","")
subtotalPrice = menHatPriceText.replace("$","")

menHatPriceAmount = float(menHatPrice)
womenHatPriceAmount = float(womenHatPrice)
subtotalPriceAmount = float(subtotalPrice)
expectedsubtotalPriceAmount = (womenHatPriceAmount + menHatPriceAmount) 
quanity = driver.find_element_by_id("sc-subtotal-label-activecart").text

assert expectedsubtotalPriceAmount  == subtotalPriceAmount, "test fail - hats price is NOT valid"
assert quanity == "Subtotal (2 items):", "test fail - hats quantity is NOT valid"
print("Test Case 2 Result : Price and quanity are correct")










