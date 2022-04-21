from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

EMAIL = "YOUREMAIL"
PASSWORD = "YOURPASSWORD"


chrome_driver_path = "C:/Users/.../chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
URL= "https://tinder.com"
driver.get(URL)

#Try logging in on Tinder
sleep(2)
login = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a').click()

#Choose log in method ("Facebook")
sleep(2)
fb_login = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button').click()


# Switch to Facebook login window (COOKIE POPUP:  id and xpath changed every time the code was run, generating unique ids and xpaths for the Accept All button element.)
sleep(2)
base_window = driver.window_handles[0]
fb_window = driver.window_handles[1]
driver.switch_to.window(fb_window)

sleep(2)
cookies_accept = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div/div/div[3]/button[2]').click()

#Enter the detils of your login info
sleep(2)

email_entry = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/form/div/div[1]/div/input")
email_entry.send_keys(EMAIL)
password_entry = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/form/div/div[2]/div/input")
password_entry.send_keys(PASSWORD)
log_in = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]").click()

#Switch back to base_ window
driver.switch_to.window(base_window)
print(driver.title)

#Delay by 5 seconds to allow page to load.
sleep(5)

#Allow location
allow_location_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]').click()


#Disallow notifications
notifications_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]').click()


#Allow cookies
cookies = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button').click()


#Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
for n in range(100):

    #Add a 1 second delay between likes.
    sleep(1)

    try:
        print("called")
        like_button = driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)

driver.quit()