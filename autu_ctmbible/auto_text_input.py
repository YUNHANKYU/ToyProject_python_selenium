# -*- coding: utf-8 -*- 

### 사용법
###
### 0.
### 한글 주석 사용을 위해 1번 줄에 "# -*- coding: utf-8 -*- " 추가 필요
###
### 1. 
### chrome을 실행하게 도와주는 드라이버 연결. 드라이버 설치 후 경로 설정 필요.
### 크롬 드라이버 설치링크 : https://sites.google.com/a/chromium.org/chromedriver/
### ex) browser = webdriver.Chrome("/Users/yunhangyu/Documents/toyproject/chromedriver")
###
### 2.
### 크롬 개발자도구로 진입하여 제어하기 원하는 부분의 selector id 혹은 xPath 를 가져와야함
### 방법 : 원하는 부분 코드 우클릭 > COPY > Copy Selector(or xPath) 클릭 후 아래 붙여넣기
### - click() : 버튼 클릭
###   ex) browser.find_element_by_css_selector("body > div > div.content > form > div > div > a.subtn").click()
### - send_keys() : 파라미터로 입력하기 원하는 내용 보내기. 키보드 클릭도 가능.
###   ex) iiid = browser.find_element_by_css_selector("#identifierId").send_keys("newjane6793")
###   - from selenium.webdriver.common.keys import Keys : Keys.RETURN 등 다양한 키보드 입력 사용 가능
###     ex) send_keys(Keys.RETURN)
 
from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("/Users/yunhangyu/Documents/toyproject/chromedriver")

### 해당 링크로 크롬 창 여는 기능 
browser.get("https://user.ctm.kr/mem/login_outlogin.asp?prepage=https://bible.ctm.kr/default_in.asp?k=hev")

#   로그인 시작
##
###
############################################################################################################

### 아이디 입력
# iiid = browser.find_element_by_css_selector('#inputID').send_keys('newjane6793')
iiid = browser.find_element_by_css_selector('#inputID').send_keys('soi101')

### 패스워드 입력
# pwwwd = browser.find_element_by_css_selector('#inputPWD').send_keys("hong598900@")
pwwwd = browser.find_element_by_css_selector('#inputPWD').send_keys("ri4608sv")

### 로그인 버튼 클릭
browser.find_element_by_css_selector("body > div > div.content > form > div > div > a.subtn").click()

time.sleep(1)
############################################################################################################
###
##
#   로그인 완료


for index in range(2, 4):

    # body > center > table > tbody > tr > td > table > tbody > tr > td:nth-child(3) > center > table > tbody > tr > td > table > tbody > tr > td > form > table > tbody > tr:nth-child(6) > td:nth-child(1)
    # body > center > table > tbody > tr > td > table > tbody > tr > td:nth-child(3) > center > table > tbody > tr > td > table > tbody > tr > td > form > table > tbody > tr:nth-child(6) > td:nth-child(2)
    # body > center > table > tbody > tr > td > table > tbody > tr > td:nth-child(3) > center > table > tbody > tr > td > table > tbody > tr > td > form > table > tbody > tr:nth-child(6) > td:nth-child(4)
    # body > center > table > tbody > tr > td > table > tbody > tr > td:nth-child(3) > center > table > tbody > tr > td > table > tbody > tr > td > form > table > tbody > tr:nth-child(13) > td:nth-child(3)
    ### 성경 book 종류 선택 요엘 ~ 하박국
    browser.find_element_by_css_selector("body > center > table > tbody > tr > td > table > tbody > tr > td:nth-child(3) > center > table > tbody > tr > td > table > tbody > tr > td > form > table > tbody > tr:nth-child(13) > td:nth-child({0})".format(index+1)).click()
    time.sleep(3)

    ### 해당 book 총 장 수 가져오는 로직
    cn = browser.find_element_by_xpath('/html/body/center/form/table[2]/tbody/tr[1]/td/table/tbody/tr/td[3]/font')
    print(cn.text)
    print(cn.text.replace(' ', '').split('총')[1].split('장')[0])
    chapterNum = int(cn.text.replace(' ', '').split('총')[1].split('장')[0])

    ###################################################################################################################
    #                                                                                                                 #
    #                                                                                                                 #
    #                                                    iframe in                                                    #
    #                                                                                                                 #
    #                                                                                                                 #
    ###################################################################################################################

    ### 총 장 수만큼 반복
    for j in range(chapterNum):

        ### 구절 입력하는 곳이 iframe 안쪽이기 때문에 browser를 iframe으로 변경
        iframe = browser.find_element_by_xpath('/html/body/center/form/table[2]/tbody/tr[2]/td/iframe')
        browser.switch_to_frame(iframe)

        ### 총 몇 번의 텍스트 필드를 거쳐야 하는지 확인
        ### name = "tcnt" /html/body/form[2]/input[7]
        fn = browser.find_element_by_css_selector('body > form:nth-child(2) > input[type=HIDDEN]:nth-child(7)')
        print('필드 토탈 넘 = {0}'.format(fn.get_attribute('value')))
        fieldNum = int(fn.get_attribute('value'))

        ### 필드 수만큼 반복하면서 구절 문자열을 필드에 채워주고 ENTER 입력
        for i in range(fieldNum+1):
            print(i)
            ww = browser.find_element_by_id('sp{0}'.format(i))
            print(ww.text)
            first = browser.find_element_by_name('bscript146419{0}'.format(i))
            first.send_keys(ww.text)
            first.send_keys(Keys.RETURN)
            time.sleep(2)

        time.sleep(5)
        print('')

    ###################################################################################################################
    #                                                                                                                 #
    #                                                                                                                 #
    #                                                    iframe out                                                   #
    #                                                                                                                 #
    #                                                                                                                 #
    ###################################################################################################################
    # /html/body/center/table/tbody/tr[6]/td
    browser.find_element_by_xpath('/html/body/center/table/tbody/tr[6]/td').click()
    time.sleep(5)
    # browser.switch_to_default_content()
    
    ### 구절 입력하는 곳이 iframe 안쪽이기 때문에 browser를 iframe으로 변경
    iframe = browser.find_element_by_xpath('/html/frameset/frame[2]')
    browser.switch_to_frame(iframe)
    browser.find_element_by_css_selector("body > center > table > tbody > tr > td > table > tbody > tr > td:nth-child(3) > center > table > tbody > tr > td > table > tbody > tr > td > form > table > tbody > tr:nth-child(7) > td:nth-child({0})".format(index+1))
# browser.find_element_by_xpath('/html/body/center/form/table[2]/tbody/tr[5]/td/a/img').click()

time.sleep(10)