from bs4 import BeautifulSoup
from selenium import webdriver

JOB = {}

URL = "https://kr.indeed.com/jobs?q="
TERM = "python"

driver = webdriver.Chrome()
driver.get(URL+TERM)

soup = BeautifulSoup(driver.page_source, "lxml")
pages = soup.find_all("nav", attrs={"role": "navigation"})[0].find_all("div", attrs={"class": "css-tvvxwd ecydgvn1"})
pages = 5 if len(pages) > 5 else len(pages) if len(pages) > 0 else 1

for page in range(pages):
    url = f"https://kr.indeed.com/jobs?q=python&start={page*10}"
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "lxml")
    jobs = soup.find_all("td", attrs={"class": "resultContent"})

    for job in jobs:
        link = job.select("h2 a")[0]["href"]
        title = job.select("h2 a span")[0].text
        company = job.find("span", attrs={"class": "companyName"}).text
        type_ = "N/A" if job.find("div", attrs={"class": "metadata"}) is None else\
                job.find("div", attrs={"class": "metadata"}).text

        if company not in JOB:
            JOB[company] = {
                "link": "https://kr.indeed.com" + link,
                "title": title,
                "type": type_
            }

for company, condition in JOB.items():
    print(f"{company}\n{condition}\n")

while True:
    pass

