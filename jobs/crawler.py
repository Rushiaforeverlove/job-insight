import requests
from bs4 import BeautifulSoup
from .models import Job

def run():

    url = "https://www.cakeresume.com/jobs"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    # 抓所有 job title
    titles = soup.select('a[class*="jobTitle"]')

    # 抓所有 company name
    companies = soup.select('a[class*="companyName"]')

    # 配對（避免 index 錯亂）
    for i in range(min(len(titles), len(companies))):

        title = titles[i].get_text(strip=True)
        company = companies[i].get_text(strip=True)

        Job.objects.get_or_create(
            title=title,
            company=company,
            defaults={
                "salary": 0,
                "location": "Unknown",
                "skill": "N/A",
                "source": "cakeresume"
            }
        )

    print("CakeResume 爬蟲完成")