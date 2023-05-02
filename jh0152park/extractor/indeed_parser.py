from bs4 import BeautifulSoup
from selenium import webdriver

JOB = {}

OPTIONS = webdriver.ChromeOptions()
OPTIONS.headless = True
OPTIONS.add_argument("window-size=1920x1080")
OPTIONS.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")


def get_indeed_job_list(job="python"):
    ret = []
    url = "https://kr.indeed.com/jobs?q="

    driver = webdriver.Chrome(options=OPTIONS)
    driver.get(url+job)

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
            locate = job.find("div", attrs={"class": "companyLocation"}).text
            type_ = "N/A" if job.find("div", attrs={"class": "metadata"}) is None else\
                    job.find("div", attrs={"class": "metadata"}).text

            ret.append({
                "company": company,
                "link": "https://kr.indeed.com" + link,
                "title": title,
                "type": type_,
                "locate": locate
            })
    return ret
