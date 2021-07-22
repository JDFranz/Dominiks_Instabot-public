# Version: 20210131

# TODO da muss überall noch funk name rein


import datetime as dt
import sys
from time import sleep
import slow_network_exception
import xlsx_handler
import numpy as np
import pandas as pd
from pynput.keyboard import Controller
from selenium import webdriver
import selenium
import xlrd
import collections
import matplotlib.image as image
import matplotlib.cbook as cbook
from PIL import Image


def Convert(string, ):
    li = list(
        str(string).replace("]", "").replace("[", "").replace(" ", "").replace("'", "").replace('"', "").split(","))
    return li


desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)


def return_login():
    return ['deinusername', 'deinpasswort']

def sleep_random_above(time):
    sleep(int(time*1.2) + abs(np.random.randint(0, 100) / 100))
    return


def sleep_random_normal(time):
    final_time = time * (0.5+abs(np.random.normal(1)))
    print(f"sleeping for{final_time}")
    sleep(final_time)




class Instabot:

    def __init__(self, username, pw, offline=False):

        print(f"Method: {sys._getframe().f_code.co_name}")
        self.driver = webdriver.Chrome()
        self.pw = pw
        self.username = username
        self.keyboard = Controller()
        self.likedcomments = 0
        self.likedpics = 0

        try:
            actions_df = pd.read_excel(f"{self.username}_network.xls")

        except:
            actions_df = pd.DataFrame(columns=['date', 'to_follow', 'to_like'])
            actions_df.to_excel(f"{self.username}_network.xls", index=False)

        if offline:
            print(f"FIRING UP OFFLINE")
            return

        self.driver.get("https://www.instagram.com/")
        sleep_random_above(2)

        # accept cookies
        try: self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]').click()
        except: self.driver.find_element_by_xpath('/html/body/div[2]/div/div/button[1]').click()
        # fill username , pw, and hit log in#
        sleep_random_above(4)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(self.username)
        sleep_random_above(2)
        self.driver.find_elements_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')[0].send_keys(self.pw)
        sleep_random_above(1)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()
        sleep_random_above(4)

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
            sleep_random_above(1)
            # notifications
            button = self.driver.find_elements_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
            sleep_random_above(1.5)
            button[0].click()
            sleep_random_above(1)
            # logged in

    #  def waitforObj(self,type, string):
    #     return Webdriverwait(self.driver,10 ).until(EC.presence_of _all_elements_located((type,string)))

    # Deleting (Calling destructor)
    def __del__(self):
        print('Destructor called, bot deleted.')
        self.driver.close()

    def flexiclick(self, xpath, css_selector, classname):
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

    def flexifind(self, xpath, css_selector, classname):
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

    def get_save_followers(self, account): #Works

        print(f"Method: {sys._getframe().f_code.co_name} for {account}")

        finallist = []
        for _ in range(1):
            if account != None:
                try:
                    self.driver.get(f"https://www.instagram.com/{account}")
                    sleep_random_above(1)
                    self.driver.find_element_by_xpath(f'//a[contains(@href,"/{account}/followers/")]').click()
                except selenium.common.exceptions.NoSuchElementException:
                    print(f"Account: {account} seems to be private and not followed")
                    return [f'private_and_no_follow{np.random.randint(0, 10000)}']

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

    def follow_account(self, name):

        print(f"Method: {sys._getframe().f_code.co_name}")

        self.driver.get(f"https://www.instagram.com/{name}")
        sleep_random_above(1)
        self.flexiclick(
            '//*[@id="react-root"]/section/main/div/header/section/div[2]/div/div/div/div/span/span[1]/button',
            '#react-root > section > main > div > header > section > div.Y2E37 > div > div > div > div > span > span.vBF20._1OSdk > button',
            '_5f5mN       jIbKX  _6VtSN     yZn4P   ')

        sleep_random_above(1)

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
                return False

    def follow_N_suggested_accounts(self, N):
        print(f"Method: {sys._getframe().f_code.co_name}")

        finallist = []
        try:
            self.driver.get(f"https://www.instagram.com/explore/people/suggested/")

            for i in np.random.randint(0, 25 ,N):

                sleep_random_above(1)
                self.driver.find_element_by_xpath(f'//*[@id="react-root"]/section/main/div/div[2]/div/div/div[{i}]/div[3]/button').click()
                self.push_read_actions(1,0)
                if N% 5==0: sleep_random_normal(600)

        except: print("follow_N_suggested_accounts did not work")

    def check_pic(self):
        pass

    def fake_scroll(self, probability, num_scrolls=2):

        print(f"Method: {sys._getframe().f_code.co_name}")
        if probability < np.random.uniform(0, 1): return

        html_doc = self.driver.find_element_by_tag_name('html')

        for _ in range(np.random.randint(0, num_scrolls)):
            scroll_current = int(np.random.randint(0, 50000))
            self.driver.execute_script(f"window.scrollTo(0, {scroll_current})")
            sleep_random_above(0)

    def ld_db(self,username):
        cols = ["#followers", "followers", "#followed", "followed", "#notfollowbacks", "notfollowbacks", "#likes",
                "#follows", "#unfollows"]
        db_handler = xlsx_handler.date_time_xlsx_handler(f"{username}_specs", cols)
        return db_handler

    def entry_todays_specs(self, username,db_handler=None):

        if db_handler==None:
            cols = ["#followers", "followers", "#followed", "followed", "#notfollowbacks", "notfollowbacks","post_dates","engagement", "#likes",
                    "#follows", "#unfollows"]
            db_handler = xlsx_handler.date_time_xlsx_handler(f"{username}_specs", cols)


        if db_handler.exists_today() :
            print(f" Datapoint for date: {dt.date.today()} (today) exists--> NOT ADDED")
            return db_handler


        eng_dict = self.get_engagement(username)
        followers=self.get_save_followers(username)
        followed = self.get_save_followed(username)

        post_dates= eng_dict.keys()
        eng=eng_dict.values()
        num_followers=len(followers)
        num_followed=len(followed)

        op_d = followed.copy()
        op_r= followers.copy()
        op_b=[]
        for follower in op_r:
            if follower in op_d:
                op_d.remove(follower)
                op_b.append(follower)



        data = {
                "#followers": num_followers,
                "followers":str(", ".join(followers)),
                "#followed":num_followed,
                "followed":str(", ".join(followed)),
                "#followbacks": str(len(op_b)),
                "followbacks": str(", ".join(op_b)),
                "#notfollowbacks": len(op_d),
                "notfollowbacks":str(", ".join(op_d)),
                "post_dates":str(", ".join(post_dates)),
                "engagement":str(", ".join(eng)),
                "#likes":-1,
                "#follows":-1,
                "#unfollows":-1
                }

        today=db_handler.add_today_smart(data)
        return db_handler

    def get_engagement(self, account, num_posts='all'):


        print(f"Method: {sys._getframe().f_code.co_name}")
        self.fake_scroll(0.5)
        self.driver.get(f"https://www.instagram.com/{account}")
        sleep_random_above(2)

        for i in range(10):
            scroll_current = i*10000
            self.driver.execute_script(f"window.scrollTo(0, {scroll_current})")
            sleep_random_above(0.5)

        self.driver.execute_script(f"window.scrollTo(0, 0)")
        sleep_random_above(0.5)


        imgs = self.driver.find_elements_by_xpath("//*[@class='eLAPa']")
        imgs[0].click()
        counter = 0
        stats = {}

        for img in imgs:
            sleep_random_above(0)

            date_el = self.flexifind('/html/body/div[5]/div[2]/div/article/div[3]/div[2]/a/time',
                                     'body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > div.k_Q0X.I0_K8.NnvRN > a > time',
                                     '_1o9PC Nzb55')

            try:
                date = date_el[0].get_attribute('datetime')[0:10]
            except:
                date = date_el.get_attribute('datetime')[0:10]

            try:
                num_likes_el = self.flexifind('', '', 'vcOH2')
                num_likes = num_likes_el.text

            except:
                num_likes_el = self.flexifind('', '', 'zV_Nj')
                num_likes = num_likes_el.text

            if num_likes=='':
                print(f" bad value")
                num_likes_el = self.flexifind('/html/body/div[5]/div[2]/div/article/div[3]/section[2]/div/div[2]/a/span', '', '')

                num_likes = num_likes_el[0].text


            stats[str(date)] = num_likes
            counter += 1
            print(stats)
            try:
                next_button = \
                    self.driver.find_elements_by_xpath("//*[@class=' _65Bje  coreSpriteRightPaginationArrow']")[0]
                sleep_random_above(0)
                self.fake_scroll(0.5)
                next_button.click()
                sleep_random_above(1)
                self.fake_scroll(0.5)
            except:
                print(f"{account} something went wrong. Final image counter{counter} ")

        return stats

    def report_today(self, handler):
        print(f"Method: {sys._getframe().f_code.co_name} ")

        if not handler.exists_today():
            return
        try:
            pd.read_excel(f"{handler.path.replace('xls', '')}_{str(dt.date.today())}.xls")
            print("A report for today already exists")
            return f"{handler.path.replace('xls', '')}_{str(dt.date.today())}.xls"
        except:
            pass

        today = handler.check_today()
        cols=today.columns

        keys=['followers','followed','followbacks','notfollowbacks','post_dates','engagement']

        data=[]
        for col in keys:
            if ", " in str(today[col][0]):
                data.append({col:str(today[col][0]).split(", ")})



        print(data)
        output=pd.DataFrame()
        for col in data:
            output=pd.concat([output,pd.DataFrame(col)],ignore_index=True,axis=1)

        output.columns=keys
        print(output)




        output.to_excel(f"{handler.path.replace('xls', '')}_{str(dt.date.today())}.xls")
        return f"{handler.path.replace('xls', '')}_{str(dt.date.today())}.xls"

    def visualize_report_today(self, todays_specs_xls, account):

        todays_specs_df= pd.read_excel(todays_specs_xls)
        print(todays_specs_df)
        data= [len(todays_specs_df['followers'].dropna()),
               len(todays_specs_df['followed'].dropna()),
               len(todays_specs_df['followbacks'].dropna()),
               len(todays_specs_df['notfollowbacks'].dropna())
               ]

        dates=todays_specs_df['post_dates'].dropna()
        engangement=todays_specs_df['engagement'].dropna()
        eng_data=[]
        for s in engangement:
            eng_data.append(int(str(s).replace('Gefällt ','').replace(' Mal','').replace(' Aufrufe','').replace('.','')))

        print(eng_data)
        print("plotting follow stats")
        fig, (ax, ax2) = plt.subplots(nrows=2, sharex=True, gridspec_kw={'height_ratios': [1, 6]})

        labels=['followers','followed','followbacks','notfollowbacks']
        bars=ax.barh(labels,data , color=['darkred','skyblue','skyblue','skyblue'])



        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.xaxis.grid(True)

        for i in ax.patches:
            ax.text(i.get_width() , i.get_y(),
                     str(round((i.get_width()), 2)),
                     fontsize=7,
                     color='grey')



        plt.xlabel("#accounts")


        img = Image.open('wegrow.png')
        img = img.convert("RGBA")

        pixdata = img.load()

        width, height = img.size
        for y in range(height):
            for x in range(width):
                if sum(list(pixdata[x, y])) >950:
                    pixdata[x, y] = (255, 255, 255, 0)

                else:
                    pixdata[x, y] = (0, 0, 0, 50)






        img.save('wegrow2.png')
        im = image.imread('wegrow2.png')

        ax2.barh(dates,eng_data,height= 0.5 )
        for i in ax2.patches:
            ax2.text(i.get_width() , i.get_y(),
                     str(round((i.get_width()), 2)),
                     fontsize=7,
                     color='grey')

        fig.figimage(im, 0, 0, zorder=3, alpha=.5, origin='upper')
        ax2.tick_params(axis='y', labelsize= 7)

        fig.tight_layout()
        plt.show()
        fig.savefig(f"{account}.png")

















if __name__ == '__main__':

    try:

        #wenn man
        bot.follow_account('jandomif')
        bot.like_profile_sequential('jandomif')
        bot = Instabot(return_login()[0], return_login()[1],0 )
        handler=bot.entry_todays_specs("jan_vs_ripley")
        xls=bot.report_today(handler)
        bot.visualize_report_today(xls,"jan_vs_ripley")
        bot.__del__()


    except slow_network_exception.Slow_network_exception:
        bot.__del__()
        sleep_random_above(200)


names=['']
