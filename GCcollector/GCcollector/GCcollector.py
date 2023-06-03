import requests
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
    links.drop_duplicates(keep='first')
    return links


def get_id():
    f = pandas.read_csv('Data/Complete.csv', encoding='utf-8')
    id = len(f['Id'])

    print(id)
    return id

def addDisciplines(id, grades):
    f = open('Data/Disciplines.csv','a',encoding='utf-8', newline='')
    writer = csv.writer(f)
    for grade in grades:
        writer.writerow([id,grade])

    f.close()
def main():
    links = getLinks()
    id = get_id()

    for link in links['Links']:
        parsed = link.split('/')
        companyIndex = 5
        jobTypeIndex = 6
        jobTitleIndex = 8
        company = parsed[companyIndex]
        jobType = parsed[jobTypeIndex]
        jobTitle = parsed[jobTitleIndex]

        opts = Options()
        opts.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        browser = Firefox(options=opts)
        browser.get(link)
        browser.implicitly_wait(1)  # gives an implicit wait for 1 second
        # search_form = browser.find_element(By.CSS_SELECTOR, "li.mb20:nth-child(3) > span:nth-child(2)")
        search_form = browser.find_element(By.XPATH, "/html/body/div[4]/div/div[5]/div/div[2]/div/ul[1]")

        a = search_form.text.split('\n')
        id = id +1
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
                    if(  day[1] in {'0','1','2','3','4','5','6','7','8','9'}):
                        #valid date
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
        addDisciplines(id,disciplines)

        try:

            applicationLink = browser.find_element(By.XPATH, '/html/body/div[4]/div/div[5]/div/div[1]/div/div[5]/div[2]/div[1]/div/a')
            applicationLink = applicationLink.get_attribute("href")
        except:
            print('cant find link')
            applicationLink = link
        print(applicationLink)
        browser.close()
        f = open('Data/Complete.csv', 'a', newline='',encoding='utf-8')
        writer = csv.writer(f)

        row = [id, jobTitle, industry, jobType, company, salary,grade, deadLine, daysLeft, email, recruiterName, stage,
               interviewDate, starting, 'no', applicationLink,locations,score]
        writer.writerow(row)
        f.close()


main()
