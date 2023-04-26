import requests
from bs4 import BeautifulSoup

URL = "https://weworkremotely.com/remote-jobs/search?term="
TERM = "python"

res = requests.get(URL+TERM)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

companies = soup.find_all("li", attrs={"class": "feature"})

for company in companies:
    tmp = company.find_all("span", attrs={"class": "company"})
    office = tmp[0].text
    work_type = tmp[1].text
    title = company.find("span", attrs={"class": "title"}).text
    featured = company.find("span", attrs={"class": "featured"})
    featured = featured.text if featured else company.find("span", attrs={"class": "date"}).text
    region = company.find("span", attrs={"class": "region company"}).text

    print(f"Office: {office}")
    print(f"Title: {title} / {featured}")
    print(f"Working Type: {work_type} / {region}\n")


