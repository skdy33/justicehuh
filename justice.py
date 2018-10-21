"""
packs
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as BS
import time


"""
params
"""
ID = 'huh324'
pwd = 'adgzcb135'
local_num = '3811'
start_date_x = 5
start_date_y = 2
start_hour = 1
start_minute = 0
end_date_x = 5
end_date_y = 2
end_hour = 2
end_minute = 0 


if __name__=="__main__":
    """
    open
    """
    driver = webdriver.Firefox(executable_path='./geckodriver')
    driver.get("https://krf.korea.ac.kr/modules/ngen/login/NEQU1020E.xrf?menu_pgm_id=NEQU00.NEQU1020E.00")


    id_form = driver.find_element_by_xpath('//*[@id="ipbId_text"]')
    id_form.send_keys(ID)

    pwd_form = driver.find_element_by_xpath('//*[@id="scbPw_secret"]')
    pwd_form.send_keys(pwd)

    time.sleep(1)
    #login_path = driver.find_element_by_xpath('//*[@id="imgLogin_img"]')
    #login_path.click()


    id_form.click()
    pwd_form.click()

    login_path = driver.find_element_by_xpath('//*[@id="imgLogin_img"]')
    login_path.click()


    driver.get('https://krf.korea.ac.kr/main_con.jsp')

    reserve = driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[1]/div/div[2]/table/tbody/tr/td[4]/a')

    reserve.click()

    driver.window_handles

    driver.switch_to_window(driver.window_handles[1])

    while(1):
        try:
            local_num = driver.find_element_by_id('ipbExcesivoNo_text')
            local_num.click()
            local_num.send_keys('3811')
            break
        except:
            pass


    while(1):
        while(1):
            from_d = driver.find_element_by_xpath('//*[@id="dipBillDtFrom_icon"]')
            from_d.click()
            try:
                start_d = driver.find_element_by_xpath("/html/body/div[4]/table/tfoot/tr[%s]/td[%s]/div" % (3+start_date_x, 1+ start_date_y)) 
                start_d.click()
                break
            except:
                pass
        try:
            alert = driver.switch_to_alert()
            alert.accept()
            print("alert accepted")
        except:
            print("done")
            break
    start_d = driver.find_element_by_xpath("/html/body/div[4]/table/tfoot/tr[%s]/td[%s]/div" % (3+start_date_x, 1+ start_date_y)) 
    start_d.click()

    open_start_h = driver.find_element_by_xpath('//*[@id="cbbUseStHh_btn"]')
    open_start_h.click()

    start_h = driver.find_element_by_xpath("/html/body/div[4]/table/tbody/tr[%s]/td/div/table/tbody/tr/td" % (start_hour + 2))
    start_h.click()

    open_start_m = driver.find_element_by_xpath('//*[@id="cbbUseStMm_btn"]')
    open_start_m.click()

    start_m = driver.find_element_by_xpath('/html/body/div[4]/table/tbody/tr[%s]/td/div/table/tbody/tr/td' %(start_minute + 2))
    start_m.click()

    end_d = driver.find_element_by_xpath('//*[@id="dipBillDtTo_icon"]')
    end_d.click()

    end_d = driver.find_element_by_xpath("/html/body/div[4]/table/tfoot/tr[%s]/td[%s]/div" % (3+end_date_x, 1+ end_date_y)) 
    end_d.click()

    open_end_h = driver.find_element_by_xpath('//*[@id="cbbUseEndHh_btn"]')
    open_end_h.click()

    end_h = driver.find_element_by_xpath("/html/body/div[4]/table/tbody/tr[%s]/td/div/table/tbody/tr/td" % (end_hour + 2))
    end_h.click()

    open_end_m = driver.find_element_by_xpath('//*[@id="cbbUseEndMm_btn"]')
    open_end_m.click()

    end_m = driver.find_element_by_xpath('/html/body/div[4]/table/tbody/tr[%s]/td/div/table/tbody/tr/td' %(end_minute + 2))
    end_m.click()

    reserve_button = driver.find_element_by_xpath('//*[@id="btnSave_btn"]')
    reserve_button.click()
