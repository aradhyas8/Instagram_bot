from selenium import webdriver
import time
from secrets import pw
import selenium.webdriver.common.keys import Keys
import random import randint



class Bot():
    links = []

    comments = ['Looks Good','Great','Good stuff','Amazing','Nice post','Nice click']
    def __init__(self):
       self.login('aradhyas8')
       self.like_comment_by_hashtag('comics')

    def login(self,username ):
        self.driver = webdriver.Chrome()
        self.driver.get('https://instagram.com/')
        time.sleep(6)
        username_input = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_input.click()
        username_input.clear()
        username_input.send_keys(username)
        password_input = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(pw)
        submit_button = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]')
        submit_button.click()
        not_now_button = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_now_button.click()
    def like_comment_by_hashtag(self, hastag):
        search_box = self.driver.find_element(By.XPATH,"//input[@placeholder='Search']")
        search_box.send_keys('#'+hashtag)
        sleep(10)
        self.driver.find_element(By.XPATH,'//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/ul/div[1]/a').send_keys(Keys.ENTER)
        sleep(10)

        links = self.driver.find_elements(By.TAG_NAME,'a')
        def condition(link):
            return '.com/p/' in link.get_attribute('href')
        valid_links = list(filter(condition, links))

        for i in range(5):
            link = valid_links[i].get_attribute('href')
            if link not in self.links:
                self.links.append(link)
        for link in self.links:
            self.driver.get(link)
            sleep(5)
            #Likes the image
            self.driver.find_element(By.XPATH,'/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button')
            sleep(5)
            self.driver.find_element(By.CLASS_NAME,'RxpZH').click()
            sleep(5)
            self.driver.find_element(By.XPATH,"//textarea[@placeholder='Add a comment…']").send_keys(self.comments[randint(0,5)])
            sleep(3)
            self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
            sleep(3)






def main():
    obj = Bot()
    # print(obj.geek)
if __name__ == '__main__':
    main()
