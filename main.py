
# importing required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# set params for webdriver instance
options = webdriver.ChromeOptions()
# set location of browser
options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
# set location of chromedriver executable
browser = webdriver.Chrome(chrome_options=options, executable_path="/Users/.../chromedriver")
# set url holding the table
url = 'https://records.nhl.com/history/attendance'

def scrape_webpage():
    # open webpage
    browser.get(url)
    browser.maximize_window()
    browser.implicitly_wait(220)  # set max load time

    # scroll down to load entire page
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight,)")
    time.sleep(5)

    # define the lists for each column
    seasons_list = []
    reg_season_gms_list = []
    reg_season_att_list = []
    playoff_gms_list = []
    playoff_att_list = []

    # xpath for html element that holds all the rows
    html_element_1 = "/html/body/div/div/div/main/div/div[2]/div[2]/div[2]/div/div/div[2]/div"

    # find the number of rows
    list_length = len(browser.find_elements(By.XPATH, html_element_1))
    # print(list_length)

    # loop through each row
    for x in range(0, list_length, 1):
        # time.sleep(1)
        browser.execute_script("window.scrollTo({top:75, behavior:'smooth',})")

        # find first element that you want to store
        season = browser.find_element(By.XPATH,
                                      f'/html/body/div/div/div/main/div/div[2]/div[2]/div[2]/div/div/div[2]/div[{x + 1}]/div/div[1]').get_attribute(
            "innerHTML").splitlines()[0]
        # print(f'{x}- ', season)
        seasons_list.append(season)
        # repeat this step for how many elements you want to store per row

        # 2nd element
        reg_season_gms = browser.find_element(By.XPATH,
                                              f'/html/body/div/div/div/main/div/div[2]/div[2]/div[2]/div/div/div[2]/div[{x + 1}]/div/div[2]').get_attribute(
            "innerHTML").splitlines()[0]
        # print(f'{x}- ', reg_season_gms)
        reg_season_gms_list.append(reg_season_gms)

        # 3rd element
        reg_season_att = browser.find_element(By.XPATH,
                                              f'/html/body/div/div/div/main/div/div[2]/div[2]/div[2]/div/div/div[2]/div[{x + 1}]/div/div[3]').get_attribute(
            "innerHTML").splitlines()[0]
        # print(f'{x}- ', reg_season_att)
        reg_season_att_list.append(reg_season_att)

        # 4th element
        playoff_gms = browser.find_element(By.XPATH,
                                           f'/html/body/div/div/div/main/div/div[2]/div[2]/div[2]/div/div/div[2]/div[{x + 1}]/div/div[4]').get_attribute(
            "innerHTML").splitlines()[0]
        # print(f'{x}- ', playoff_gms)
        playoff_gms_list.append(playoff_gms)

        # 5th element
        playoff_att = browser.find_element(By.XPATH,
                                           f'/html/body/div/div/div/main/div/div[2]/div[2]/div[2]/div/div/div[2]/div[{x + 1}]/div/div[5]').get_attribute(
            "innerHTML").splitlines()[0]
        # print(f'{x}- ', playoff_att)
        playoff_att_list.append(playoff_att)

    time.sleep(5)
    browser.close()

    # print(seasons_list)
    # print(reg_season_gms_list)
    # print(reg_season_att_list)
    # print(playoff_gms_list)
    # print(playoff_att_list)

    # put stored lists into dataframe
    df = pd.DataFrame({'Season': seasons_list,
                       'Regular Season Games': reg_season_gms_list,
                       'Regular Season Attendance': reg_season_att_list,
                       'Playoff Games': playoff_gms_list,
                       'Playoff Attendance': playoff_att_list
                       })
    # export as csv file
    df.to_csv('nhl_attendance.csv')


# if called directly, run script
if __name__ == '__main__':
    scrape_webpage()


