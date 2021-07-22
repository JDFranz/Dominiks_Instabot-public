# version 2021-01-28
import datetime as dt
import os
import random
import string
import sys
from time import sleep

import numpy as np
import pandas as pd
from pynput.keyboard import Controller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import selenium
import slow_network_exception

from subprocess import Popen
import sys


desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)

deviation = 1
deltastretch = 1
radnomize = True


def return_login():
    return []



def sleep_random_above(time):
    sleep(int(time * 1.2 * deltastretch) + abs(np.random.randint(0, 100) / 100) * deviation)
    return


def sleep_random_normal(time):
    final_time = time * (0.5 + abs(np.random.normal(1))) * deltastretch
    print(f"sleeping for{final_time}")
    sleep(final_time)


def Convert(string, ):
    li = list(
        str(string).replace("]", "").replace("[", "").replace(" ", "").replace("'", "").replace('"', "").split(","))
    return li


def generate_hashtags(filename: string, size):
    print(f"Method: {sys._getframe().f_code.co_name}")
    text_file = open(filename, "r")
    lines = text_file.readlines()
    lines = [x.strip() for x in lines if x.strip()]
    lines = [x.replace('#', '') for x in lines]
    print(lines)
    return random.sample(lines, size)


class Instabot:

    def __init__(self, username, pw):

        print(f"Method: {sys._getframe().f_code.co_name}")
        self.likedcomments = 0
        self.likedpics = 0
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.instagram.com/")
        sleep_random_above(2)
        self.pw = pw
        self.username = username
        self.keyboard = Controller()
        # accept cookies
        try:
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]').click()
        except:
            self.driver.find_element_by_xpath('/html/body/div[3]/div/div/button[1]').click()

        # fill username , pw, and hit log in#
        sleep_random_above(1)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(self.username)
        sleep_random_above(2)
        self.driver.find_elements_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')[0].send_keys(self.pw)
        sleep_random_above(3)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()
        sleep_random_above(3)

        '''
                button = self.driver.find_elements_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')
                # print(button)
                sleep_random_above(2)
                try:
                    button[0].click()
                except:
                    button.click()#
                    '''  # save login info?

        # save login info?
        try:
            button = self.driver.find_elements_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')
            # print(button)
            button[0].click()
            sleep_random_above(2)
        except:
            pass
        finally:
            sleep_random_above(2)
            # notifications
            button = self.driver.find_elements_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
            sleep_random_above(1.5)
            button[0].click()
            sleep_random_above(1)
            # logged in5

    #  def waitforObj(self,type, string):
    #     return Webdriverwait(self.driver,10 ).until(EC.presence_of _all_elements_located((type,string)))

    # Deleting (Calling destructor)
    def __del__(self):

        print(f"Method: {sys._getframe().f_code.co_name}")
        print('Destructor called, bot deleted.')
        self.driver.close()

    def fake_scroll(self, probability, num_scrolls=2):

        print(f"Method: {sys._getframe().f_code.co_name}")
        if probability < np.random.uniform(0, 1): return

        html_doc = self.driver.find_element_by_tag_name('html')

        for _ in range(np.random.randint(0, num_scrolls)):
            scroll_current = int(np.random.randint(0, 50000))
            self.driver.execute_script(f"window.scrollTo(0, {scroll_current})")
            sleep_random_above(0)

    def type_string_with_delay(self, string):

        print(f"Method: {sys._getframe().f_code.co_name}")
        for character in string:  # Loop over each character in the string
            self.keyboard.type(character)  # Type the character
            delay = np.random.uniform(0, 2) / 10  # Generate a random number between 0 and 10
            sleep(delay)  # Sleep for the amount of seconds generated
        return

    def flexiclick(self, xpath, css_selector, classname):

        print(f"Method: {sys._getframe().f_code.co_name}")
        sleep_random_above(0)
        try:
            button = self.driver.find_elements_by_xpath(xpath)
            button.click()

            print('clicked by xpath')
            return button
        except:
            try:
                button = self.driver.find_elements_by_xpath(xpath)
                button[0].click()

                print('clicked by xpath(array)')
                return button
            except:
                try:
                    button = self.driver.find_element_by_class_name(classname)
                    button.click()

                    print('clicked by classname')
                    return button
                except:
                    try:
                        button = self.driver.find_element_by_class_name(classname)
                        button[0].click()

                        print('clicked by classname(array)')
                        return button
                    except:
                        try:
                            button = self.driver.find_element_by_css_selector(css_selector)
                            button.click()

                            print('clicked by css')
                            return button
                        except:
                            try:
                                button = self.driver.find_element_by_css_selector(css_selector)
                                button[0].click()

                                print('clicked by css(array)')
                                return button
                            except:
                                try:
                                    button = self.driver.find_elements_by_xpath(f"//*[@class='{classname}']")
                                    button.click()

                                    print('clicked by classnamexpath')
                                    return button
                                except:
                                    try:
                                        button = self.driver.find_elements_by_xpath(f"//*[@class='{classname}']")
                                        button[0].click()
                                        print('clicked by classnamexpath(array)')
                                        return button
                                    except:
                                        print('None of the methods worked')
                                        return None

    def flexifind(self, xpath, css_selector, classname):

        print(f"Method: {sys._getframe().f_code.co_name}")
        sleep_random_above(0)
        try:
            button = self.driver.find_elements_by_xpath(xpath)
            print(f"found by xpath")
            return button
        except:
            try:
                button = self.driver.find_element_by_class_name(classname)
                print(f"found by classname")
                return button
            except:

                try:
                    button = self.driver.find_element_by_css_selector(css_selector)
                    print('found by csss')
                    return button
                except:

                    try:
                        button = self.driver.find_elements_by_xpath(f"//*[@class='{classname}']")
                        print('found by classnamexpath')
                        return button
                    except:
                        raise
                        print('None of the methods worked')

    def like_pic(self):

        print(f"Method: {sys._getframe().f_code.co_name}")
        sleep_random_above(2)
        try:
            try:
                like_button = self.driver.find_element_by_xpath(
                    "//article//section//button//*[@aria-label='Gefällt mir]")
                like_button.click()
                self.likedpics += 1
                print(f"liked in session: {self.likedpics}")
                return True

            except:
                print("searching with waitfor")
                like_button = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH,
                                                    "//article//section//button//*[@aria-label='Gefällt mir']")))
            like_button.click()
            self.likedpics += 1
            self.push_read_actions(0, 1)
            return True

        except:
            try:
                like_button = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH,
                                                    "//article//section//button//*[@aria-label='like']")))

                like_button.click()
                self.likedpics += 1
                print(f"liked in session: {self.likedpics}")
                self.push_read_actions(0, 1)
                return True

            except:
                print("did not find like button")
                return False

    def like_comments(self):

        print(f"Method: {sys._getframe().f_code.co_name}")
        sleep_random_above(1)
        try:
            sleep_random_above(0.5)
            like_button = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                'body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > div.EtaWk > ul > ul:nth-child(2) > div > li > div > span > div > button > div > span > svg')))

            like_button.click()
            self.likedcomments += 1
            print(f"liked comment in session: {self.likedcomments}")
        except:
            print("did not find any comment")
        finally:
            return
        pass

    def comment_pic(self, comment):

        print(f"Method: {sys._getframe().f_code.co_name}")
        sleep_random_above(1)
        comment_field = self.driver.find_element_by_css_selector('[aria-label="Kommentar hinzufügen ..."]')
        comment_field.send_keys(comment)
        sleep_random_above(2)
        self.driver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button').click()
        return

    def navigate_to_newest_img(self, username_to_be_liked):

        print(f"Method: {sys._getframe().f_code.co_name}")
        try:
            self.fake_scroll(1)
            self.driver.get(f"https://www.instagram.com/{username_to_be_liked}")
            sleep_random_above(2)
            imgs = self.driver.find_element_by_class_name('eLAPa')
            imgs.click()
            return True
        except:
            return False

    def like_and_comment_newest(self, username_to_be_liked, comment):

        print(f"Method: {sys._getframe().f_code.co_name}")
        self.navigate_to_newest_img(username_to_be_liked)
        self.like_pic()
        self.comment_pic(comment)
        return

    def like_newest(self, username_to_be_liked):

        print(f"Method: {sys._getframe().f_code.co_name}")
        self.navigate_to_newest_img(username_to_be_liked)
        self.like_pic()
        return

    def like_profile_sequential(self, username_to_be_liked):

        print(f"Method: {sys._getframe().f_code.co_name}")
        self.fake_scroll(0.5)
        self.driver.get(f"https://www.instagram.com/{username_to_be_liked}")
        sleep_random_above(2)

        imgs = self.driver.find_elements_by_xpath("//*[@class='eLAPa']")

        imgs[0].click()
        counter = 0

        for img in imgs:
            sleep_random_above(0)
            self.like_pic()
            counter += 1
            try:
                next_button = \
                    self.driver.find_elements_by_xpath("//*[@class=' _65Bje  coreSpriteRightPaginationArrow']")[0]
                sleep_random_above(0)
                self.fake_scroll(0.5)
                next_button.click()
                sleep_random_above(1)
                self.fake_scroll(0.5)
            except:
                print(f"{username_to_be_liked} is liked or something went wrong. Final image counter{counter} ")

    def scroll_box(self):
        sleep_random_above(0.5)
        print(f"Method: {sys._getframe().f_code.co_name}")
        try:
            scrollbox = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]")
            sleep_random_above(0.5)
        except:
            scrollbox = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
            sleep_random_above(0.5)
        # / html / body / div[4] / div / div / div[2]
        # /html/body/div[5]/div/div/div[2]/div
        counter, last_ht, ht = 0, 0, 1
        while True:
            counter += 1
            last_ht = ht
            sleep_random_above(0.3)
            ht = self.driver.execute_script("""arguments[0].scrollTo(0,arguments[0].scrollHeight);
              return arguments[0].scrollHeight;
              """, scrollbox)
            if ht == last_ht:
                sleep_random_above(1.5)
                ht = self.driver.execute_script("""arguments[0].scrollTo(0,arguments[0].scrollHeight);
                              return arguments[0].scrollHeight;
                              """, scrollbox)
            if ht == last_ht: break
        links = self.driver.find_elements_by_xpath(f"//*[@class='FPmhX notranslate  _0imsa ']")
        followers = [title.text for title in links if title != '']
        if followers == []: raise slow_network_exception.Slow_network_exception("Scrollbox",
                                                                                "Elements of scrollbox did not load")
        print(followers)
        print(f"number of elements: {len(followers)}")

        return followers

    def calculate_cleansing_probs(self, todays_specs):
        Follower_count = todays_specs.Follower_count
        Following_count = todays_specs.Following_count

        print({"Followers:": Follower_count, "Following:": Following_count})

        prob = np.max(1 - np.exp(-((Following_count / Follower_count) - 0.4) / 0.2), 0) * 100
        print(f"Probability to Cleanse is: {prob}")
        if (np.random.randint(0, 100) < prob):
            cleansing = True
            print("CLEANSING")
        else:
            cleansing = False
            print("FOLLOWING")
        return cleansing

    def get_save_followers(self, account):

        print(f"Method: {sys._getframe().f_code.co_name} for {account}")

        finallist = []
        for _ in range(1):
            if account != None:
                try:
                    self.driver.get(f"https://www.instagram.com/{account}")
                except selenium.common.exceptions.NoSuchElementException:
                    print(f"Account: {account} seems to be private and not followed")
                    return [f'private_and_no_follow{np.random.randint(0, 10000)}']
            sleep_random_above(1)
            self.driver.find_element_by_xpath(f'//a[contains(@href,"/{account}/followers/")]').click()

            sleep_random_above(1.5)
            # scroll to the bottom until all loaded:
            list = self.scroll_box()
            if (len(finallist) < len(list)):
                finallist = list
        return finallist

    def get_save_followed(self, account):

        print(f"Method: {sys._getframe().f_code.co_name} for {account}")
        finallist = []
        for _ in range(1):
            if account != None:
                self.driver.get(f"https://www.instagram.com/{account}")
            sleep_random_above(1)
            self.driver.find_element_by_xpath(f'//a[contains(@href,"/{account}/following/")]').click()

            sleep_random_above(1.5)
            # scroll to the bottom until all loaded:
            list = self.scroll_box()
            if (len(finallist) < len(list)):
                finallist = list
        return finallist

    def get_followed(self):

        print(f"Method: {sys._getframe().f_code.co_name}")
        self.driver.get(f"https://www.instagram.com/{self.username}")
        sleep_random_above(1)
        self.driver.find_element_by_xpath(f'//a[contains(@href,"/{self.username}/following/")]').click()

        sleep_random_above(1)
        # scroll to the bottom until all loaded:
        return self.scroll_box()

    def get_save_followed(self):

        print(f"Method: {sys._getframe().f_code.co_name}")
        finallist = []
        for _ in range(4):
            self.driver.get(f"https://www.instagram.com/{self.username}")
            sleep_random_above(1)
            self.driver.find_element_by_xpath(f'//a[contains(@href,"/{self.username}/following/")]').click()

            sleep_random_above(1.5)
            # scroll to the bottom until all loaded:
            self.scroll_box()
            list = self.scroll_box()
            if (len(finallist) < len(list)):
                finallist = list
        return finallist

    def push_followers_to_db(self, followerlist):

        print(f"Method: {sys._getframe().f_code.co_name}")
        df = pd.read_excel(f"{self.username}.xlsx")
        new_entry = pd.DataFrame(
            {"date": dt.date, "time": dt.date, "num_follower": len(followerlist), "followerlist": followerlist})
        df = df.concat([df, new_entry])
        df.to_excel(f"{self.username}.xlsx")
        pass

    def get_followers_from_db(self):
        pass

    def push_followed_to_db(self):
        pass

    def get_followed_from_db(self):
        pass

    def follow_account(self, name=None):

        print(f"Method: {sys._getframe().f_code.co_name}")
        if name != None:
            self.driver.get(f"https://www.instagram.com/{name}")
        sleep_random_above(1)
        if self.check_account(100,2500):
            abonnieren = self.flexiclick(
                '//*[@id="react-root"]/section/main/div/header/section/div[2]/div/div/div/div/span/span[1]/button',
                '#react-root > section > main > div > header > section > div.Y2E37 > div > div > div > div > span > span.vBF20._1OSdk > button',
                '_5f5mN       jIbKX  _6VtSN     yZn4P   ')
            self.push_read_actions(1, 0)

            if abonnieren == None: self.flexiclick(
                '//*[@id="react-root"]/section/main/div/header/section/div[2]/div/div/div/button',
                '#react-root > section > main > div > header > section > div.Y2E37 > div > div > div > button',
                'sqdOP  L3NKy   y3zKF     ')
            self.push_read_actions(1, 0)
            if abonnieren == None:
                print(f"---------->{sys._getframe().f_code.co_name} did not click")
                self.push_read_actions(-2, 0)

        sleep_random_above(1)

    def like_feed(self, steps: int):

        print(f"Method: {sys._getframe().f_code.co_name}")
        counter = 0
        self.driver.get("https://www.instagram.com/")
        sleep_random_above(1)
        for _ in range(steps):
            try:

                self.fake_scroll(0.9, 2)
                sleep_random_above(1)

                like_button = self.driver.find_element_by_css_selector('[aria-label="Gefällt mir"]')

                like_button.click()
                self.push_read_actions(0, 1)
                counter += 1

            except:
                print(f"liked {counter}  posts")


            finally:
                sleep_random_above(1)
        pass

    def like_comment_feed(self):

        print(f"Method: {sys._getframe().f_code.co_name}")
        # likes and comments the feed using generic positive comments randomly on a given percentage to likes
        pass

    def like_newest_post_of_Kpercent_random_followers(self, perc_followers):

        print(f"Method: {sys._getframe().f_code.co_name}")
        followers = self.get_followers()
        to_like = random.sample(followers, int(perc_followers / 100 * len(followers)))
        for user in to_like:
            if (self.navigate_to_newest_img(user) == True):
                self.like_pic()
        pass

    def like_newest_unliked_post_of_Kpercent_newest_followers(self, perc_followers):

        print(f"Method: {sys._getframe().f_code.co_name}")
        followers = self.get_followers()
        to_like = followers[0:int(perc_followers / 100 * len(followers))]
        to_like = random.sample(to_like, int(len(to_like)))
        print(f"liking {len(to_like)} followers.")
        print(to_like)

        for user in to_like:
            print(f"currently liking {user}.")
            if (self.navigate_to_newest_img(user) == True):
                while True:
                    sleep_random_above(0)
                    if (self.like_pic()):
                        break

                    try:
                        next_button = \
                            self.driver.find_elements_by_xpath("//*[@class=' _65Bje  coreSpriteRightPaginationArrow']")[
                                0]
                        sleep_random_above(0)
                        self.fake_scroll(0.5)
                        next_button.click()
                        sleep_random_above(1)
                        self.fake_scroll(0.5)
                    except:
                        break
        pass

    def generate_generic_comment(self):
        '''



        '''

    def like_for_Like(self):

        print(f"Method: {sys._getframe().f_code.co_name}")
        # Likes everyone's newest picture who liked the post
        # starting position: a post
        sleep_random_above(0)
        self.flexiclick('/html/body/div[4]/div[2]/div/article/div[3]/section[2]/div/div[2]/button',
                        'body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.EDfFK.ygqzn > div > div.Nm9Fw > button',
                        'sqdOP yWX7d     _8A5w5  ')

        sleep_random_above(1)
        # scroll to the bottom until all loaded:
        links = self.driver.find_elements_by_xpath(f"//*[@class='FPmhX notranslate MBL3Z']")
        names = [title.text for title in links if title != '']
        print(names)
        # das klappt
        for name in names:
            self.like_newest(name)
            print(f"liked {name}")
        pass

    def like_N_posts_hastag(self, hashtag: string, N: int):

        print(f"Method: {sys._getframe().f_code.co_name}")
        self.driver.get(f"https://www.instagram.com/explore/tags/{hashtag}/")
        sleep_random_above(1)
        self.fake_scroll(0.5, 3)
        imgs = self.driver.find_elements_by_xpath("//*[@class='eLAPa']")
        imgs[0].click()
        counter = 0

        condition = [True, True, True]
        for n in range(N):
            sleep_random_above(0)
            if (np.random.randint(0, 100) < 80):
                if self.check_pic(250):
                    counter += 1
                    if n % 3 == 0:
                        condition[0] = self.like_pic()
                    if n % 3 == 1:
                        condition[1] = self.like_pic()
                    if n % 3 == 2:
                        condition[2] = self.like_pic()
                    else:
                        n += -1
                    if (False == condition[0] == condition[1] == condition[2]):
                        print(f"ended liking of hashtag{hashtag} permaturely")
                        return False
            try:

                next_button = \
                    self.driver.find_elements_by_xpath("//*[@class=' _65Bje  coreSpriteRightPaginationArrow']")[0]
                sleep_random_above(0)
                self.fake_scroll(0.5)
                next_button.click()
                sleep_random_above(0)
                self.fake_scroll(0.5)
            except:
                print(f"{hashtag} is liked or something went wrong. Final image counter{counter} ")

        pass

    def like_recent_pics(self):

        print(f"Method: {sys._getframe().f_code.co_name}")
        # starts on a profiles newest img
        sleep_random_above(0.5)
        while True:
            time_passed = self.flexifind('/html/body/div[4]/div[2]/div/article/div[3]/div[2]/a/time',
                                         'body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > div.k_Q0X.NnvRN > a > time',
                                         '_1o9PC Nzb55')
            if "VOR" in str(time_passed[0].get_attribute('text')):
                sleep_random_above(0)
                if (np.random.randint(0, 100) < 90):
                    self.like_pic()
                    self.flexiclick(
                        '/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button/div/span/svg',
                        'body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button > div > span > svg',
                        '_8-yf5')
                    self.push_read_actions(0, 1)
                    try:

                        next_button = \
                            self.driver.find_elements_by_xpath("//*[@class=' _65Bje  coreSpriteRightPaginationArrow']")[
                                0]
                        sleep_random_above(0)
                        self.fake_scroll(0.5)
                        next_button.click()
                        sleep_random_above(0)
                        self.fake_scroll(0.5)
                    except:
                        print(f"nextbutton not found ")
            else:
                break

    def burn_the_heretics(self, iterations, Max_Number_of_heretics, followers_param=None, heretic_param=None):

        print(f"Method: {sys._getframe().f_code.co_name}")

        if followers_param == None:
            for _ in range(iterations):
                followers1 = self.get_followers()
                followers2 = self.get_followers()
                while followers1 != followers2:
                    followers1 = self.get_followers()
                    followers2 = self.get_followers()
                    print("different outputs get_followers")
        else:
            followers1 = followers_param
        if heretic_param == None:
            followed = self.get_followed()

        else:
            followed = heretic_param

        Followed_for_return = followed
        for follower in followers1:
            if follower in followed:
                followed.remove(follower)

        print(f"the heretics are {len(followed)}: {followed}")
        if followed == []:
            return
        #  input("Press Enter to burn the heretics...")

        for heretic in followed[0:Max_Number_of_heretics]:
            self.driver.get(f"https://www.instagram.com/{heretic}")
            sleep_random_above(6)

            links = self.driver.find_elements_by_xpath(f"//*[@class='FPmhX notranslate  _0imsa ']")
            followers = [title.text for title in links if title != '']

            self.flexiclick(
                '//*[@id="react-root"]/section/main/div/header/section/div[2]/div/div/div[2]/div/span/span[1]/button',
                '#react-root > section > main > div > header > section > div.Y2E37 > div > div > div:nth-child(2) > div > span > span.vBF20._1OSdk > button',
                '_5f5mN    -fzfL     _6VtSN     yZn4P   ')
            sleep_random_above(1)
            self.flexiclick('/html/body/div[5]/div/div/div/div[3]/button[1]',
                            'body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.-Cab_',
                            'aOOlW -Cab_   ')
            Followed_for_return.remove(heretic)
            sleep_random_above(5)

        return Followed_for_return

    def follow_hashtag(self, hashtag, num_follows):

        print(f"Method: {sys._getframe().f_code.co_name}")
        self.driver.get(f"https://www.instagram.com/explore/tags/{hashtag}/")
        sleep_random_above(1)
        self.fake_scroll(0.5, 3)
        imgs = self.driver.find_elements_by_xpath("//*[@class='eLAPa']")
        imgs[0].click()
        sleep_random_above(1)

        # this is the click on the the like button
        num_likes = self.flexiclick('/html/body/div[4]/div[2]/div/article/div[3]/section[2]/div/div/button',
                                    'body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.EDfFK.ygqzn > div > div > button',
                                    'sqdOP yWX7d     _8A5w5    ')
        if num_likes == None:
            num_likes = self.flexiclick('/html/body/div[5]/div[2]/div/article/div[3]/section[2]/div/div/a',
                                        'body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.EDfFK.ygqzn > div > div > a',
                                        'zV_Nj')
        if num_likes == None:
            num_likes = self.flexiclick('/html/body/div[5]/div[2]/div/article/div[3]/section[2]/div/div/a/span',
                                        'body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.EDfFK.ygqzn > div > div > a > span',
                                        'zV_Nj')

        sleep_random_above(3)
        links = self.driver.find_elements_by_xpath(f"//*[@class='FPmhX notranslate MBL3Z']")
        accounts = [title.text for title in links if title != '']
        print(accounts[0:num_follows])
        for account in accounts[0:num_follows]:
            sleep_random_above(1)
            self.follow_account(account)

        print(f"followed hashtag: {hashtag}")
        return True

    def like_N_postsandcomments_hashtag(self, hashtag: string, N: int):

        print(f"Method: {sys._getframe().f_code.co_name}")
        self.driver.get(f"https://www.instagram.com/explore/tags/{hashtag}/")
        sleep_random_above(1)
        self.fake_scroll(0.5, 3)
        imgs = self.driver.find_elements_by_xpath("//*[@class='eLAPa']")
        imgs[0].click()
        counter = 0

        for n in range(N):
            sleep_random_above(0)
            if (np.random.randint(0, 100) < 90):
                self.like_pic()

            if (np.random.randint(0, 100) < 90):
                # like comment
                self.like_comments()
            else:
                n += -1

            try:

                next_button = \
                    self.driver.find_elements_by_xpath("//*[@class=' _65Bje  coreSpriteRightPaginationArrow']")[0]
                self.fake_scroll(0.1)
                next_button.click()
                self.fake_scroll(0.1)
                counter += 1
            except:
                print(f"{hashtag} is liked or something went wrong. Final image counter{counter} ")

        pass

    def lpnc_hastags_feed(self, list_hashtags: list, avg_num_likes: int):

        print(f"Method: {sys._getframe().f_code.co_name}")
        # like post and comments
        counter = 0
        for hashtag in list_hashtags:
            counter += 1
            num_likes = int(np.random.normal(avg_num_likes, avg_num_likes / 5))
            print(f"liked {num_likes} in hashtag: {hashtag}")
            self.like_N_postsandcomments_hashtag(hashtag, num_likes)
            self.like_feed(len(list_hashtags) * counter)

    def lpnc_hastags(self, list_hashtags: list, avg_num_likes: int):
        print(f"Method: {sys._getframe().f_code.co_name}")
        # like post and comments
        counter = 0
        for hashtag in list_hashtags:
            counter += 1
            num_likes = int(np.random.normal(avg_num_likes, avg_num_likes / 5))
            print(f"liked {num_likes} in hashtag: {hashtag}")
            self.like_N_postsandcomments_hashtag(hashtag, num_likes)

    def lpnc_hastags(self, list_hashtags: list, avg_num_likes: int):
        # like post and comments
        counter = 0
        for hashtag in list_hashtags:
            counter += 1
            num_likes = int(np.random.normal(avg_num_likes, avg_num_likes / 5))
            self.like_N_postsandcomments_hashtag(hashtag, num_likes)
            print(f"liked {num_likes} in hashtag: {hashtag}")

        return

    def calculate_cleansing_probs(self, todays_specs):
        Follower_count = todays_specs.Follower_count
        Following_count = todays_specs.Following_count

        print({"Followers:": Follower_count, "Following:": Following_count})

        prob = np.max(1 - np.exp(-((Following_count / Follower_count) - 0.4) / 0.2), 0) * 100
        print(f"Probability to Cleanse is: {prob}")
        if (np.random.randint(0, 100) < prob):
            cleansing = True
            print("CLEANSING")
        else:
            cleansing = False
            print("FOLLOWING")
        return cleansing

    def init_specs_today(self):
        print(f"Method: {sys._getframe().f_code.co_name}")
        try:
            df = pd.read_excel(f'{self.username}_specs.xls')
            try:
                todays_specs = df.loc[df['date'] == str(dt.date.today())]
                if not todays_specs.empty:
                    print('-->Specs already exists')
                    return df

            except:
                pass
        except:
            df = pd.DataFrame()

        todays_specs = {
            'date': str(dt.date.today()),
            'Follower_count': -1,
            'Followers_list': 'NaN',
            'Following_count': -1,
            'Following_list': 'NaN',
            'Heretics_count': -1,
            'Heretics_list': 'NaN',
            'liked_today': 0,
            'followed_today': 0
        }

        df = df.append(todays_specs, ignore_index=True)
        print(df)
        df.to_excel(f'{self.username}_specs.xls', index=False)

        return df

    def push_read_actions(self, push_follow=False, push_like=False):
        print(f"Method: {sys._getframe().f_code.co_name}")

        try:
            df = pd.read_excel(f'{self.username}_specs.xls')

            todays_specs = df.loc[df['date'] == str(dt.date.today())]
            if todays_specs.empty:
                print('-->Specs for today dont exists')
                df = self.init_specs_today()
                df.to_excel(f'{self.username}_specs.xls', index=False)

        except:
            print(f'{self.username}_specs.xls does not exist')
            df = self.init_specs_today()
            df.to_excel(f'{self.username}_specs.xls', index=False)


        finally:
            if push_follow:
                print(f"push follow")
                df.loc[df['date'] == str(dt.date.today()), 'followed_today'] += push_follow

            if push_like:
                print(f"push like")
                df.loc[df['date'] == str(dt.date.today()), 'liked_today'] += push_like

            df.to_excel(f'{self.username}_specs.xls', index=False)

        return df

    def check_volume_below(self, follows=50, likes=200):
        try:
            df = pd.read_excel(f'{self.username}_specs.xls')

            todays_specs = df.loc[df['date'] == str(dt.date.today())]
            if todays_specs.empty:
                print('-->Specs dont exists')
                df = self.init_specs_today()

        except:
            print(f'{self.username}_specs.xls does not exist')
            df = self.init_specs_today()


        finally:
            todays_specs = df.loc[df['date'] == str(dt.date.today())]

            if (int(todays_specs['followed_today']) < follows and int(todays_specs['liked_today']) < likes):
                return True

            else:
                print("exceeded Volume for today")
                print(todays_specs)
                return False

    def follow_N_suggested_accounts(self, N):
        print(f"Method: {sys._getframe().f_code.co_name}")

        finallist = []
        try:
            self.driver.get(f"https://www.instagram.com/explore/people/suggested/")

            for i in np.random.randint(0, 25, N):

                sleep_random_above(1)

                try:
                    account=self.driver.find_element_by_class_name( f'FPmhX notranslate MBL3Z')[i].text
                    self.follow_account(account)
                except:
                    account = self.driver.find_element_by_xpath(f'Jv7Aj mArmR MqpiF  ')[i].text
                    self.follow_account(account)



                self.driver.get(f"https://www.instagram.com/explore/people/suggested/")
                if N % 5 == 4: sleep_random_normal(600)



        except:
            print("follow_N_suggested_accounts did not work")

    def push_read_stats(self, push=True):

        print(f"Method: {sys._getframe().f_code.co_name}")

        try:
            df = pd.read_excel(f'{self.username}_specs.xls')
        except:
            df = pd.DataFrame()

        if push:
            followers = self.get_save_followers(account=self.username)
            following = self.get_save_followed(account=self.username)
            heretics = following.copy()

            for follower in followers:
                if follower in heretics:
                    heretics.remove(follower)
            if follower in heretics:
                print("omething went wrong: followers cannot be heretics")

            todays_specs = {
                'date': dt.date.today(),
                'Follower_count': len(followers),
                'Followers_list': followers,
                'Following_count': len(following),
                'Following_list': following,
                'Heretics_count': len(heretics),
                'Heretics_list': heretics
            }

            df = df.append(todays_specs, ignore_index=True)
            print(df)
            df.to_excel(f'{self.username}_specs.xls', index=False)

        return df

    def update_social_network(self, depth):

        print(f"Method: {sys._getframe().f_code.co_name}")
        try:
            df = self.push_read_stats(False)
            todays_specs = df.loc[df['date'] == str(dt.date.today())]
            if todays_specs.empty:
                print('-->no entry for today')
                raise Exception("today's specs empty")

        except:
            df = self.push_read_stats(True)
            df = self.push_read_stats(False)
            todays_specs = df.loc[df['date'] == str(dt.date.today())]

        print(todays_specs)
     


        try:
            network_df = pd.read_excel(f"{self.username}_network.xls")

        except:
            network_df = pd.DataFrame(columns=['Account', 'Followers'])
            network_df.to_excel(f"{self.username}_network.xls", index=False)

        print(f"today's specs: {todays_specs['Followers_list']}")
        print(network_df['Account'])

        counter = 0
        # adding new followers network
        for follower in Convert(todays_specs['Followers_list'].values):
            if counter >= depth: break
            if follower not in network_df['Account'].values:
                counter += 1
                print(f"crawling:{follower} ")
                followers = self.get_save_followers(follower)
                sleep_random_above(20)

                network_df = network_df.append({'Account': follower, 'Followers': followers}, ignore_index=True)
                network_df.to_excel(f"{self.username}_network.xls", index=False)

        # deleting old followers network

        # network_df = network_df[network_df.Account in Convert(todays_specs['Followers_list'].values)]
        network_df.to_excel(f"{self.username}_network.xls", index=False)

        return network_df, todays_specs, f"{self.username}_network.xls"

    def check_pic(self,limit):

        print(f"Method: {sys._getframe().f_code.co_name}")
        sleep_random_above(0.5)

        text=self.driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[2]/div/div/a')
        try:
            text=text.text
        except AttributeError:
            text= text[0].text

        text=str(text).replace('Gefällt','').replace('Mal','').replace('.','').replace(' ','')
        print(text)
        try:
            return  int(text)<limit
        except Exception as inst:
            print(inst)
            return True

    def check_account(self,lower_follower_limit, upper_follower_limit):

        print(f"Method: {sys._getframe().f_code.co_name}")
        sleep_random_above(0.5)

        try:

            text = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]')
            text = text.text
        except AttributeError:

            text = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]')
            text = text[0].text

        text = str(text).replace('Abonnenten', '').replace('m', '000000').replace(',', '').replace('.', '').replace('k', '000').replace('Abonnent', '').replace(' ', '')
        print(text)
        try:
            return lower_follower_limit< int(text) < upper_follower_limit
        except Exception as inst:
            print(inst)
            return True






def concise_procedure():
    while True:
        hashtags = []
        hashtags.append(generate_hashtags('rap&Hiphop hashtags', 10))
        hashtags.append(generate_hashtags('EDM hashtags', 10))
        hashtags.append(generate_hashtags('Rockmusic hashtags', 10))

        print(hashtags)

        while abs(dt.datetime.today().hour - 15) >= 2.5:
            print(f" it is {dt.datetime.today().hour}.")
            sleep_random_normal(2000)

        try:
            print("###############################################Login and setup")
            bot = Instabot(return_login()[0], return_login()[1])
            network_df, todays_specs, network_path = bot.update_social_network(0)

            followers = Convert(todays_specs['Followers_list'].values)
            followed = Convert(todays_specs['Following_list'].values)

            cleansing = bot.calculate_cleansing_probs(todays_specs)
        except:
            print("SETUP WENT WRONG")

        for hashtaglist in hashtags:
            for i in range(5):
                try:
                    print(f"###############################################Block:{i}")
                    if (np.random.randint(0, 100) > 80):

                        if cleansing:
                            remainders = bot.burn_the_heretics(1, 7, followers_param=followers,
                                                               heretic_param=remainders)
                        else:
                            bot.follow_hashtag(hashtaglist[i], 7)
                        bot.lpnc_hastags_feed(hashtaglist, 15)
                        if cleansing:
                            remainders = bot.burn_the_heretics(1, 7, followers_param=followers,
                                                               heretic_param=remainders)
                            sleep_random_normal(500)
                        else:
                            if (np.random.randint(0, 100) > 80):
                                bot.lpnc_hastags_feed(hashtaglist, 15)
                                bot.follow_hashtag(hashtaglist[i], 7)
                        sleep_random_normal(500)
                except:
                    print(f"###############################################Block:{i}")
                    print("something went wrong mid-rpocedure")
                    bot.__del__()
                    sleep_random_normal(500)
                    bot = Instabot(return_login()[0], return_login()[1])

def safe_sceleton():
    try:
        try:# Setup
            print("###############################################Login and setup")
            bot = Instabot(return_login()[0], return_login()[1])
        except Exception as inst:
            print('=========================>>> BAD SETUP')
            print(inst)
            raise Exception("Bot setup went wrong")


    except:
        try:
            bot.__del__()
        except:
            pass

    finally:
        print("========================>>>RESTART")
        os.system("instabot.py")

def stupid_mode():
    try:
        while True:
            deviation = 3
            deltastretch = 3
            hashtags = []
            if(np.random.randint(0, 100) < 50):
                hashtags.append(generate_hashtags('Rockmusic hashtags', 10))
                hashtags.append(generate_hashtags('local hashtags', 10))
                hashtags.append(generate_hashtags('EDM hashtags', 10))
            else:
                hashtags.append(generate_hashtags('local hashtags', 10))
                hashtags.append(generate_hashtags('music hashtags', 10))
                hashtags.append(generate_hashtags('rap&Hiphop hashtags', 10))

            print(hashtags)

           # while abs(dt.datetime.today().hour -15
            #          ) >= 2:
            #    print(f" it is {dt.datetime.today().hour}.")
            #    sleep_random_normal(2000)

            try:
                print("###############################################Login and setup")
                bot = Instabot(return_login()[0], return_login()[1])
                bot.follow_account('jandomif')
                bot.like_profile_sequential('jandomif')

                cleansing = 0
                if cleansing:
                    network_df, todays_specs, network_path = bot.update_social_network(0)
                    followers = Convert(todays_specs['Followers_list'].values)
                    followed = Convert(todays_specs['Following_list'].values)

            except Exception as inst:
                print(inst)
                print("SETUP WENT WRONG")
                sleep_random_normal(500)
                pass

            for hashtaglist in hashtags:

                for i in range(5):
                    print(bot.push_read_actions(0, 0))
                    if (bot.check_volume_below(np.random.randint(50, 70), np.random.randint(250, 400))):

                        try:
                            print(f"###############################################Block:{i}")
                            if (np.random.randint(0, 100) < 80):

                                if cleansing:
                                    remainders = bot.burn_the_heretics(1, 7, followers_param=followers,
                                                                       heretic_param=remainders)
                                else:
                                    bot.follow_hashtag(hashtaglist[i][0], 7)
                                    bot.follow_hashtag(hashtaglist[i][1], 7)
                                    bot.follow_hashtag(hashtaglist[i][2], 7)
                                    bot.follow_N_suggested_accounts(8)
                                bot.lpnc_hastags_feed(hashtaglist, 15)

                                if cleansing:
                                    remainders = bot.burn_the_heretics(1, 7, followers_param=followers,
                                                                       heretic_param=remainders)
                                    sleep_random_normal(500)
                                else:
                                    if (np.random.randint(0, 100) < 80):
                                        bot.lpnc_hastags_feed(hashtaglist, 15)
                                        bot.follow_hashtag(hashtaglist[i][5], 7)
                                        bot.follow_N_suggested_accounts(5)
                                        bot.follow_hashtag(hashtaglist[i][3], 7)
                                        bot.follow_hashtag(hashtaglist[i][4], 7)
                        except Exception as inst:
                            print(f"###############################################Block:{i}")
                            print("something went wrong mid-rpocedure")
                            print(type(inst))
                            print(inst.args)
                            print(inst)
                            bot.__del__()
                            bot = Instabot(return_login()[0], return_login()[1])
                        finally:
                            try:
                                print("Systems nominal")
                                bot.__del__()

                            except:
                                pass
                    else:

                        print(bot.push_read_actions(0, 0))
                        break

    except:
        print("RESTART")
        os.system("instabot.py")
    #<class 'selenium.common.exceptions.InvalidSessionIdException'>
    #selenium.common.exceptions.InvalidSessionIdException: Message: invalid session id
    #selenium.common.exceptions.InvalidSessionIdException: Message: invalid session id
    #<class 'selenium.common.exceptions.NoSuchElementException'>


def only_liking():
    try:
        hashtags = []
        hashtags.append(generate_hashtags('calisthenics_hashtags', 10))
        hashtags.append(generate_hashtags('motivational', 10))
        hashtags.append(generate_hashtags('most_liked_hashtags.txt', 10))
        hashtags.append(generate_hashtags('hashtags', 10))


        try:# Setup
            print("###############################################Login and setup")
            bot = Instabot(return_login()[0], return_login()[1])
        except Exception as inst:
            print('=========================>>> BAD SETUP')
            print(inst)
            raise Exception("Bot setup went wrong")





        for hashtaglist in hashtags:

            for i in range(5):
                if not (bot.check_volume_below(np.random.randint(50, 70), np.random.randint(175, 225))): quit()

                if (np.random.randint(0, 100) < 80):
                    bot.lpnc_hastags(hashtaglist, np.random.randint(5,20))

                else:
                    bot.lpnc_hastags_feed(hashtaglist, np.random.randint(5, 20))
                    sleep_random_normal(500)

    except Exception as inst:
        print(inst)
        try:
            bot.__del__()
        except:
            pass

    finally:
        print("========================>>>RESTART")
        os.system("instabot.py")





if __name__ == "__main__":

    only_liking()