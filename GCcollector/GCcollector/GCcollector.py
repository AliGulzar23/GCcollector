import requests
from selenium.common import InvalidArgumentException
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

import pandas
import csv


def month_to_int(month):
    months = {"January": 1,
              "February": 2,
              "March": 3,
              "April": 4,
              "May": 5,
              "June": 6,
              "July": 7,
              "August": 8,
              "September": 9,
              "October": 10,
              "November": 11,
              "December": 12
              }

    return str(months.get(month))


def getLinks():
    links = pandas.read_csv('Data/Links.csv')
    return links['Links']


def get_id():
    f = pandas.read_csv('Data/Complete.csv', encoding='utf-8')
    id = len(f['Id'])

    print(id)
    return id


def addDisciplines(id, grades):
    f = open('Data/Disciplines.csv', 'a', encoding='utf-8', newline='')
    writer = csv.writer(f)
    for grade in grades:
        writer.writerow([id, grade])

    f.close()


def main():
    # links = getLinks()
    id = get_id()
    f = open('Data/Complete.csv', 'a', newline='', encoding='utf-8')
    writer = csv.writer(f)
    links = getLinks()
    #links = ['https://www.linkedin.com/jobs/view/3619639236/?eBP=CwEAAAGIklSbQNHUvxVYLuGkvgWO_dLOOmS7-95DOvH56e8o1Zm9NNpBjdlpuEt-sYRc20Q8nVah53b97i78gJ2XsuchBfGQUXkVc8qXsGNebY-CcfaMngCQ1TLArgmpxSyqbetJpLOYUfQJVCvjnIMKcck-OWBu9NvjoybMePCepbyhu6f8-fwcJAvHAJwcXc5NgN1w5Dg2QP0sMt4yGFBhhn7lMDp8MwfPrj1bIl9qEQ5PcBO4q-aFj6YSzQyvW4RySo4eG_jWqakIhLlKbN1NBAi6ZIzJF_6e87eFGphUb7BuSsGmCCq5l0PtgqWafChqs32c3uf5UW36mF3SrTVEYTyPSry4&recommendedFlavor=SCHOOL_RECRUIT&refId=BMDQYAla2kPs6B4SNGgpTQ%3D%3D&trackingId=1zi3uqDutDTL91FPf7Mhwg%3D%3D&trk=flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3BaSdNbRhCRvGCanqwHU9CBA%3D%3D&lici=1zi3uqDutDTL91FPf7Mhwg%3D%3D']
    for link in links:
        id = id + 1
        if 'gradcracker' in link:
            print('gradcracker')
            gradcracker(id,link,writer)
        if 'aston' in link.lower():
            print('Aston')
            Aston_Futures(id, link, writer)
        if 'linkedin' in link.lower() :
            linkedin(id,link,writer)

    f.close()

def linkedin(id,link,writer):
    opts = Options()
    opts.binary_location = r'/usr/lib/firefox/firefox'
    browser = Firefox(options=opts)
    browser.get(link)
    try:
        title = browser.find_element(By.XPATH,'/html/body/main/section[1]/div/section[2]/div/div[1]/div/h1').text
        industry = browser.find_element(By.XPATH, '/html/body/main/section[1]/div/div/section[1]/div/ul/li[4]/span').text
        jobType = ' '
        company = browser.find_element(By.XPATH,'/html/body/main/section[1]/div/section[2]/div/div[1]/div/h4/div[1]/span[1]/a').text
        salary = ' '
        grade = ' '
        deadline = ' '
        daysLeft = ' '
        email = ' '
        recruiterName = ' '
        stage = ' '
        interviewDate = ' '
        startingDate = ' '
        applied = 'no'
        applicationLink = browser.find_element(By.XPATH,'/html/body/main/section[1]/div/section[2]/div/div[1]/div/div/button[1]').get_attribute('href')
        location = browser.find_element(By.XPATH,"/html/body/main/section[1]/div/section[2]/div/div[1]/div/h4/div[1]/span[2]").text
        score = ' '
        row = [id,title,industry,company,salary,grade,deadline,daysLeft,email,recruiterName,stage,interviewDate,startingDate,applied,applicationLink,location,score]
        print(row)
        writer.writerow(row)
    except Exception as e:
        print('stupid linked in moment')
        print(e)


    browser.close()



def Aston_Futures(id, link, writer):
    opts = Options()
    opts.binary_location = r'/usr/lib/firefox/firefox'
    browser = Firefox(options=opts)

    browser.get(link)

    username = '180058062'
    password = 'Dot2rand603'
    wait = True
    while wait:
        try:
            browser.find_element(By.XPATH,  '/html/body/tc-ui-app-root/tc-ui-shared-romeo/div/main/ng-component/section/div/div/div/div/tc-ui-unauth-login-options/div[1]/div/div[2]/a[1]/span[1]').click()
            wait = False
        except Exception as e :
            print('page is still waiting')
            print(e)

    wait = True
    while wait:
        try:
            browser.find_element(By.XPATH,
                                 '/html/body/tc-ui-app-root/tc-ui-shared-romeo/div/main/ng-component/section/div/div/div/div/tc-ui-unauth-login/tc-ui-unauth-login-redirect/div/div/form/div/button').click()
            wait = False
        except Exception as e:
            print('page is still waiting')
            print(e)
    wait = True
    while wait:
        try:
            UN = browser.find_element(By.XPATH, '//*[@id="userNameInput"]')
            UN.send_keys(username)
            PW = browser.find_element(By.XPATH, '//*[@id="passwordInput"]')
            PW.send_keys(password)
            signIN = browser.find_element(By.XPATH, '//*[@id="submitButton"]')
            signIN.click()
            wait = False
        except Exception as e:
            print('page still waiting')
            print(e)
    wait = True
    while wait:
        try:
            deadLine = browser.find_element(By.XPATH, '//*[@id="jobClosingDate"]').text
            wait = False
        except Exception as e:
            print('page is still waiting ')
            print(e)
    application_link = browser.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[5]/div[2]/div[2]/div[1]/div/div/div/a').get_attribute("href")
    title = browser.find_element(By.XPATH, '//*[@id="job-title"]').text
    type = browser.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[5]/div[2]/div[3]/div/div[4]/div/div/div').text
    salary = browser.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[2]/div[5]/div[2]/div[3]/div/div[6]/div/div/div').text
    starting = browser.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[2]/div[5]/div[2]/div[2]/div[2]/div/div/div').text
    grade = ' '
    industry = browser.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[2]/div[5]/div[2]/div[3]/div/div[5]/div/div/div').text
    company = browser.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[2]/div[5]/div[2]/div[3]/div/div[2]/div/div/div/a').text
    email = ' '
    recruiterName = ' '
    stage = ' '
    daysLeft = ' '
    interviewDate = ' '
    applied = 'no'
    locations = browser.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[2]/div[5]/div[2]/div[3]/div/div[8]/div/div/div').text
    score = ' '
    row = [id,title,industry,type,company,salary,grade,deadLine,daysLeft,email,recruiterName,stage,interviewDate,starting,applied,link,locations,score]
    print(row)
    browser.close()
    writer.writerow(row)

def gradcracker(id, link, writer):
    parsed = link.split('/')
    companyIndex = 5
    jobTypeIndex = 6
    jobTitleIndex = 8
    company = parsed[companyIndex]
    jobType = parsed[jobTypeIndex]
    jobTitle = parsed[jobTitleIndex]

    opts = Options()
    opts.binary_location = r'/usr/lib/firefox/firefox'
    browser = Firefox(options=opts)
    browser.get(link)
    browser.implicitly_wait(1)  # gives an implicit wait for 1 second
    # search_form = browser.find_element(By.CSS_SELECTOR, "li.mb20:nth-child(3) > span:nth-child(2)")
    search_form = browser.find_element(By.XPATH, "/html/body/div[4]/div/div[5]/div/div[2]/div/ul[1]")

    a = search_form.text.split('\n')
    deadLine = ' '
    starting = ' '
    salary = ' '
    grade = ' '
    industry = ' '
    email = ' '
    recruiterName = ' '
    stage = ' '
    interviewDate = ' '
    daysLeft = ' '

    score = 0
    locations = ''
    disciplines = browser.find_element(By.XPATH, '/html/body/div[4]/div/div[5]/div/div[2]/div/ul[2]').text.split(
        '\n')
    index = 0
    for i in a:
        if ("(Show map)" in i):
            # implies that there exists locations
            locations = a[index - 1]

        if ("Deadline:" in i):
            if ("Ongoing" in i):
                deadLine = "Ongoing"
            else:
                date = i.split(':')[1][1:]
                month = month_to_int(date.split(' ')[0])
                day = date.split(' ')[1]
                if (day[1] in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}):
                    # valid date
                    day = day[:2]
                else:
                    day = day[0]
                year = date.split(' ')[2]
                dateStr = day + "-" + month + "-" + year
                print(dateStr)
                deadLine = dateStr

        if ("Starting" in i):
            if ("Salary" in i):
                salary = i.split(':')[1][1:]
            else:
                date = i.split(':')[1][1:]
                month = month_to_int(date.split(' ')[0])
                year = date.split(' ')[1]
                starting = month + "-" + year
        else:
            starting = 'TBC'
        if ("grades" in i):
            grade = 'all grades'
        elif ("and above" in i):
            grade = i.split(' ')[0]
        index = index + 1
    addDisciplines(id, disciplines)

    try:

        applicationLink = browser.find_element(By.XPATH,
                                               '/html/body/div[4]/div/div[5]/div/div[1]/div/div[5]/div[2]/div[1]/div/a')
        applicationLink = applicationLink.get_attribute("href")
    except:
        print('cant find link')
        applicationLink = link
    print(applicationLink)
    browser.close()

    row = [id, jobTitle, industry, jobType, company, salary, grade, deadLine, daysLeft, email, recruiterName, stage,
           interviewDate, starting, 'no', applicationLink, locations, score]
    writer.writerow(row)


main()
