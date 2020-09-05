from selenium import webdriver
from time import sleep
import credentials

class InstaBot():
    def __init__(self):
        mobile_emulation = { "deviceName": "Nexus 5" } 
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        self.driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options=chrome_options)
        
    def login(self):
        self.driver.get("https://instagram.com")

        sleep(2)
        
        log_in_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div/div/div/div[2]/button')      
        log_in_btn.click()

        sleep(2)

        usr_input= self.driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[3]/div/label/input')
        usr_input.send_keys(credentials.username)

        pass_input= self.driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[4]/div/label/input')
        pass_input.send_keys(credentials.password)

        sleep(2)

        enter_btn = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[6]')
        enter_btn.click()

        sleep(10)
        skip_btn = bot.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/button')
        skip_btn.click()
        
        sleep(5)

        cancel_btn = bot.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        cancel_btn.click()

    def post_it(self):
        ps_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav[2]/div/div/div[2]/div/div/div[3]')
        ps_btn.click()
        
        sleep(20)

        next_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div[1]/header/div/div[2]/button')
        next_btn.click()

        sleep(1)

        caption_text=input("Enter a caption for your post without hashtags.... :)\n")

        sleep(1)

        caption = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div[2]/section[1]/div[1]/textarea')
        caption.send_keys(caption_text)
        caption.send_keys("\n\n")
        hashtags= "1"
        while (hashtags != "0"):
            hashtags=""
            hashtags=input("Enter hashtags you. Press 0 when done\n")
            if(hashtags != "0"):
                txt_box="#"+hashtags+' '
                caption.send_keys(txt_box)

        sleep(2)
        
        share_btn= self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div[1]/header/div/div[2]/button')
        share_choice=input("Do you wish to post this? Yes/No\n")
        share_choice.lower()
        if (share_choice=="yes"):
            share_btn.click()

        else:
            print("Terminatiog Operation")
            self.driver.get("https://www.youtube.com/watch?v=Xhh3_-JRnDc")

    def end_this_the_cool_way(self):
        not_now_btn = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        not_now_btn.click()

        sleep(1)

        cool_way=input("Do you wish to end this the cool way? Yes/No\n")
        cool_way.lower()
        if(cool_way == "yes"):
            like_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[2]/div[1]/div/article[1]/div[3]/section/span[1]/button')
            like_btn.click()
            print("I liked your post for you")
            sleep(3)
            self.driver.get("https://www.youtube.com/watch?v=Xhh3_-JRnDc")
        else:
            print("Ok bye")
            self.driver.get("https://www.youtube.com/watch?v=Xhh3_-JRnDc")


bot = InstaBot()
bot.login()
bot.post_it()
sleep(5)
bot.end_this_the_cool_way()
