import requests
from bs4 import BeautifulSoup

URL = "https://weworkremotely.com/remote-jobs/search?term="
TERM = "react"

res = requests.get(URL+TERM)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

companies = soup.find_all("li", attrs={"class": "feature"})

for company in companies:
    link = company.find_all("a")[1]["href"]
    link = "/".join(URL.split("/")[:3]) + "/" + link
    office, work_type, region = company.find_all("span", attrs={"class": "company"})
    office, work_type, region = office.text, work_type.text, region.text
    title = company.find("span", attrs={"class": "title"}).text
    featured = company.find("span", attrs={"class": "featured"})
    featured = featured.text if featured else company.find("span", attrs={"class": "date"}).text

    print(f"Office: {office}")
    print(f"Title: {title} / {featured}")
    print(f"Working Type: {work_type} / {region}")
    print(link + "\n")


