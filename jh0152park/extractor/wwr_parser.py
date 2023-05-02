import requests
from bs4 import BeautifulSoup


def get_wwr_job_list(job="python"):
    ret = []
    url = "https://weworkremotely.com/remote-jobs/search?term="

    res = requests.get(url+job)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    companies = soup.find_all("li", attrs={"class": "feature"})

    for company in companies:
        link = company.find_all("a")[1]["href"]
        link = "/".join(url.split("/")[:3]) + "/" + link
        office, work_type, locate = company.find_all("span", attrs={"class": "company"})
        office, work_type, locate = office.text, work_type.text, locate.text
        title = company.find("span", attrs={"class": "title"}).text

        ret.append({
            "company": office,
            "link": link,
            "title": title,
            "type": work_type,
            "locate": locate
        })

    return ret
