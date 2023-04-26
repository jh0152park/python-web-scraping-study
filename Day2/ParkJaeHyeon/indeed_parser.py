import requests
from bs4 import BeautifulSoup

"""
 * Currently do not accept website scraping by indeed web site side.
 * And also could not found the way to solve 403 error. of course could not found other solution video too.
"""

# URL = "https://kr.indeed.com/jobs?q="
# TERM = "python"
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
#     "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"
# }
#
# res = requests.get(URL+TERM, headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")
